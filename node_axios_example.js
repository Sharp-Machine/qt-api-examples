// Example script for hitting the QT Engine using Node.js
// Run with: node node_axios_example.js

const axios = require('axios');

const BASE_URL = 'http://localhost:8000';

async function generateTrajectory() {
    console.log("1. Loading Model...");
    const path = require('path');
    const modelPath = path.resolve(__dirname, '..', 'temp_models', 'droid_v1.pkl');
    await axios.post(`${BASE_URL}/models/nonlinear/load?path=${encodeURIComponent(modelPath)}`);

    console.log("2. Initiating Generation Request...");
    
    try {
        const payload = {
            type: "robotics_7dof",
            model_id: "nonlinear",
            n_samples: 5,
            prefix: null
        };
        
        const initRes = await axios.post(`${BASE_URL}/generate`, payload);
        const opId = initRes.data.operation_id;
        console.log(`-> Received Operation ID: ${opId}`);
        
        console.log("\n2. Polling for results...");
        
        let isDone = false;
        while (!isDone) {
            // Wait 500ms between polls
            await new Promise(resolve => setTimeout(resolve, 500));
            
            const pollRes = await axios.get(`${BASE_URL}/operations/${opId}`);
            const data = pollRes.data;
            
            if (data.done) {
                if (data.status === 'FAILED') {
                    console.error("Generation failed:", data.error);
                    return;
                }
                
                console.log(`-> Generation Complete in ${data.response.inference_latency_ms.toFixed(2)}ms!`);
                console.log(`-> Unpacked ${data.response.samples.length} trajectory paths.`);
                isDone = true;
            } else {
                console.log("   Status: IN_PROGRESS... waiting 500ms");
            }
        }
        
    } catch (error) {
        console.error("API Error:", error.message);
    }
}

generateTrajectory();
