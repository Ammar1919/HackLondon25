import React, { useState, useEffect } from "react";
import { fetchUrgentPatient } from "../api/api";
import "./UrgentPatient.css"; // Import the CSS file

const UrgentPatient = () => {
    const [patient, setPatient] = useState(null);

    useEffect(() => {
        async function getPatient() {
            const data = await fetchUrgentPatient();
            setPatient(data);
        }
        getPatient();
    }, []);

    return (
        <div className="urgent-patient-container">
            <h2 className="urgent-patient-heading">Urgent Patient</h2>
            {patient ? (
                <ul className="patient-details">
                    <li><strong>Name:</strong> <span className="patient-value">{patient.name}</span></li>
                    <li><strong>Condition:</strong> <span className="patient-value">{patient.health_condition}</span></li>
                    <li><strong>Hospital:</strong> <span className="patient-value">{patient.hospital_location}</span></li>
                </ul>
            ) : (
                <p className="loading-message">Loading...</p>
            )}
        </div>
    );
};

export default UrgentPatient;