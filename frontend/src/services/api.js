import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000', // The address of the FastAPI backend
});

export const fetchCategories = async () => {
  try {
    const response = await apiClient.get('/categories');
    return response.data;
  } catch (error) {
    console.error("Error fetching categories:", error);
    throw error;
  }
};

export const fetchTutorialsByCategory = async (categoryId) => {
  try {
    const response = await apiClient.get(`/categories/${categoryId}/tutorials`);
    return response.data;
  } catch (error) {
    console.error(`Error fetching tutorials for category ${categoryId}:`, error);
    throw error;
  }
};

export const fetchTutorialById = async (id) => {
  try {
    const response = await apiClient.get(`/tutorials/${id}`);
    return response.data;
  } catch (error) {
    console.error(`Error fetching tutorial ${id}:`, error);
    throw error;
  }
};
