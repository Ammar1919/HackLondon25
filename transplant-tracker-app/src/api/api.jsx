import axios from "axios"

const API_BASE_URL = "http://localhost:5000/api/patients"; // Flask backend URL
const API_BASE_URL_2 = "http://localhost:5000/api/get_organ_id";
const API_BASE_URL_3 = "http://localhost:5000/api/urgency/patient";
const API_BASE_URL_4 = "http://localhost:5000/api/urgency/organ";

// Fetch all patients
export const fetchAllPatients = async () => {
    try {
        const response = await axios.get(`${API_BASE_URL}/`);
        return response.data;
    } catch (error) {
        console.error("Error fetching patients:", error);
        return [];
    }
}; 

// Fetch a single patient by ID
export const fetchPatientById = async (userId) => {
    try {
        const response = await axios.get(`${API_BASE_URL}/${userId}`);
        return response.data;
    } catch (error) {
        console.error("Error fetching patient:", error);
        return { error: "User not found" };
    }
};

// Function to get organ_id
export const fetchOrganId = async (organId) => {
    try {
        const response = await axios.post(`${API_BASE_URL_2}/`, {
            organ_id: organId
        });
        return response.data; // { "organ_id": 5 }
    } catch (error) {
        console.error("Error fetching organ_id:", error);
        return { error: "Could not retrieve organ_id" };
    }
};

// Fetch urgent patient data
export const fetchUrgentPatient = async () => {
    try {
        const response = await axios.get(`${API_BASE_URL_3}/`);
        return response.data;
    } catch (error) {
        console.error("Error fetching urgent patient:", error);
        return { error: "Could not retrieve patient data" };
    }
};

// Fetch urgent organ data
export const fetchUrgentOrgan = async () => {
    try {
        const response = await axios.get(`${API_BASE_URL_4}/`);
        return response.data;
    } catch (error) {
        console.error("Error fetching urgent organ:", error);
        return { error: "Could not retrieve organ data" };
    }
};