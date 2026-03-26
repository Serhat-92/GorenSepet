export const colors = {
    primary: '#2563EB', // Modern Royal Blue
    primaryDark: '#1E40AF',
    primaryLight: '#60A5FA',
    secondary: '#10B981', // Emerald Green for success
    background: '#F3F4F6', // Light Gray for background (easier on eyes)
    surface: '#FFFFFF', // White for cards
    text: '#1F2937', // Dark Gray for text (softer than pure black)
    textLight: '#6B7280', // Gray for secondary text
    error: '#EF4444',
    warning: '#F59E0B',
    border: '#E5E7EB',
    // Accessibility specific
    highContrastText: '#FFFFFF',
    focusRing: '#3B82F6',
};

export const spacing = {
    tiny: 4,
    small: 8,
    medium: 16,
    large: 24,
    xlarge: 32,
    xxlarge: 48,
};

export const shadows = {
    small: {
        shadowColor: "#000",
        shadowOffset: { width: 0, height: 1 },
        shadowOpacity: 0.18,
        shadowRadius: 1.00,
        elevation: 1,
    },
    medium: {
        shadowColor: "#000",
        shadowOffset: { width: 0, height: 2 },
        shadowOpacity: 0.25,
        shadowRadius: 3.84,
        elevation: 5,
    },
    large: {
        shadowColor: "#000",
        shadowOffset: { width: 0, height: 5 },
        shadowOpacity: 0.34,
        shadowRadius: 6.27,
        elevation: 10,
    }
};

export const typography = {
    header: {
        fontSize: 32,
        fontWeight: 'bold',
        color: colors.text,
        letterSpacing: 0.5,
    },
    subheader: {
        fontSize: 24,
        fontWeight: '600',
        color: colors.text,
    },
    body: {
        fontSize: 18,
        color: colors.text,
        lineHeight: 28,
    },
    caption: {
        fontSize: 14,
        color: colors.textLight,
    },
    button: {
        fontSize: 18,
        fontWeight: '600',
        color: '#FFFFFF',
    }
};

export const layout = {
    borderRadius: 12,
    inputHeight: 56,
};
