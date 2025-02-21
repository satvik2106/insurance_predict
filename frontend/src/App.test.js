import { render, screen } from '@testing-library/react';
import App from './App';

test('renders Register page initially', () => {
  render(<App />);
  expect(screen.getByText(/Register/i)).toBeInTheDocument();
});
