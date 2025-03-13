import React, { useState, useEffect } from "react";
import { fetchUrgentOrgan } from "../api/api";
import "./UrgentOrgan.css"; // Import the CSS file

const UrgentOrgan = () => {
    const [organ, setOrgan] = useState(null);

    useEffect(() => {
        async function getOrgan() {
            const data = await fetchUrgentOrgan();
            setOrgan(data);
        }
        getOrgan();
    }, []);

    return (
        <div className="urgent-organ-container">
            <h2 className="urgent-organ-heading">Urgent Organ</h2>
            {organ ? (
                <ul className="organ-details">
                    <li><strong>Organ:</strong> <span className="organ-value">{organ.organ}</span></li>
                    <li><strong>Condition:</strong> <span className="organ-value">{organ.organ_condition}</span></li>
                    <li><strong>Transplant Time:</strong><span className={`organ-value ${organ.transplant_time && typeof organ.transplant_time === 'string' && organ.transplant_time.toLowerCase().includes('urgent') ? 'transplant-urgent' : ''}`}>{organ.transplant_time}</span></li>
                </ul>
            ) : (
                <p className="loading-message">Loading...</p>
            )}
        </div>
    );
};

export default UrgentOrgan;