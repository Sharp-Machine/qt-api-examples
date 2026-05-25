/**
 * Demonstrates how to use the QT API to predict Continuous Quantile trajectories 
 * for Robotics configurations using Node.js and an asynchronous polling loop.
 */

// Replace with your actual API key
const API_KEY = "AIzaSyDAVGM-E3WIjd4PAJnErxSDzb-sXYIZdE8";

// The public Gateway URL
const BASE_URL = "https://qt-paas-gateway-ane34s9g.uc.gateway.dev";

async function generateRoboticsFutures() {
    console.log("Initiating Robotics Future Generation via QT API...");

    // 1. Define the payload for the Robotics Modality
    const payload = {
        type: "robotics_7dof",
        model_id: "nonlinear", // Must match a model loaded in the backend memory
        n_samples: 100      // How many distinct probability paths to generate
    };

    const headers = {
        'Content-Type': 'application/json',
        'X-QT-Api-Key': 'qt_demo_123' // Required header for this specific demo backend
    };

    try {
        // 2. Fire the initial POST request to the Gateway
        const initResponse = await fetch(`${BASE_URL}/generate?key=${API_KEY}`, {
            method: 'POST',
            headers: headers,
            body: JSON.stringify(payload)
        });

        if (!initResponse.ok) {
            throw new Error(`HTTP error! status: ${initResponse.status}`);
        }

        const initData = await initResponse.json();
        const operationId = initData.operation_id;
        
        console.log(`Success! Generation accepted. Operation ID: ${operationId}`);
        console.log("Polling for results (this usually takes 1-3 seconds)...");

        // 3. Poll the server until the generative inference is complete
        let isDone = false;
        let resultData = null;

        while (!isDone) {
            // Wait 1 second before polling again
            await new Promise(resolve => setTimeout(resolve, 1000));
            
            const pollResponse = await fetch(`${BASE_URL}/operations/${operationId}?key=${API_KEY}`, {
                headers: headers
            });

            if (!pollResponse.ok) {
                // If it's a 404, it might still be initializing in the queue. Otherwise throw.
                if (pollResponse.status !== 404) {
                     throw new Error(`HTTP polling error! status: ${pollResponse.status}`);
                }
                process.stdout.write(".");
                continue;
            }

            const pollData = await pollResponse.json();
            
            if (pollData.done) {
                if (pollData.status === "FAILED") {
                    throw new Error(`Server returned generation error: ${pollData.error}`);
                }
                isDone = true;
                resultData = pollData.response;
                console.log("\n[SUCCESS] Generation Complete!");
            } else {
                process.stdout.write(".");
            }
        }

        // 4. Process the returned distributions
        const samples = resultData.samples;
        const latency = resultData.inference_latency_ms;
        
        console.log(`\nReceived ${samples.length} distinct future paths.`);
        console.log(`Each path contains ${samples[0].length} continuous dimensional states.`);
        console.log(`Server-side Inference Latency: ${latency.toFixed(2)} ms`);
        
        // Example: Print the first 3 predicted steps of the first sample
        console.log("\nSample 1 (First 3 steps):");
        console.log(samples[0].slice(0, 3));

    } catch (error) {
        console.error("\nFailed during generation process:", error);
    }
}

// Run the script
generateRoboticsFutures();
