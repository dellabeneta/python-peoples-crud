import { IconButton, useTheme } from '@mui/material';
import Brightness4Icon from '@mui/icons-material/Brightness4';
import Brightness7Icon from '@mui/icons-material/Brightness7';

const ThemeToggle = ({ toggleTheme }) => {
  const theme = useTheme();
  
  return (
    <IconButton
      sx={{ 
        position: 'fixed',
        right: 20,
        top: 20,
        backgroundColor: theme.palette.background.default,
        borderRadius: '50%',
        padding: '8px',
        boxShadow: '0 2px 4px rgba(0,0,0,0.1)',
        '&:hover': {
          backgroundColor: theme.palette.action.hover,
        }
      }}
      onClick={toggleTheme}
      color="inherit"
      aria-label="toggle theme"
    >
      {theme.palette.mode === 'dark' ? <Brightness7Icon /> : <Brightness4Icon />}
    </IconButton>
  );
};

export default ThemeToggle;
