import { useState } from "react";
import { fetchOrganId } from "../api/api";
import "./OrganIDFetcher.css"; // Import the CSS file

const OrganIdFetcher = () => {
    const [inputId, setInputId] = useState("");
    const [organId, setOrganId] = useState(null);
    const [error, setError] = useState("");

    const handleFetchOrganId = async () => {
        if (!inputId) {
            setError("Please enter an organ ID.");
            return;
        }
        setError("");
        
        const data = await fetchOrganId(inputId);
        if (data.error) {
            setError(data.error);
        } else {
            setOrganId(data.organ_id);
        }
    };

    return (
        <div className="organ-fetcher-container">
            <h2 className="organ-fetcher-heading">Fetch Organ ID</h2>
            <div className="organ-fetcher-form">
                <input
                    type="number"
                    className="organ-fetcher-input"
                    placeholder="Enter Organ ID"
                    value={inputId}
                    onChange={(e) => setInputId(e.target.value)}
                />
                <button 
                    className="organ-fetcher-button" 
                    onClick={handleFetchOrganId}
                >
                    Get Organ ID
                </button>
            </div>

            {organId && (
                <div className="organ-fetcher-result">
                    <strong>Organ ID:</strong> {organId}
                </div>
            )}
            {error && <div className="organ-fetcher-error">{error}</div>}
        </div>
    );
};

export default OrganIdFetcher;