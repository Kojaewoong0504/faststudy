import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000', // The address of the FastAPI backend
});

export const fetchCategories = async () => {
  try {
    const response = await apiClient.get('/api/v1/categories');
    return response.data;
  } catch (error) {
    console.error("Error fetching categories:", error);
    throw error;
  }
};

export const fetchTutorialById = async (id) => {
  try {
    const response = await apiClient.get(`/api/v1/tutorials/${id}`);
    return response.data;
  } catch (error) {
    console.error(`Error fetching tutorial ${id}:`, error);
    throw error;
  }
};