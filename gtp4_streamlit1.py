import streamlit as st
from streamlit_echarts import st_echarts

# Data for the Nightingale/Rose chart
data = [
    {"value": 40, "name": "rose 1"},
    {"value": 33, "name": "rose 2"},
    {"value": 28, "name": "rose 3"},
    {"value": 22, "name": "rose 4"},
    {"value": 20, "name": "rose 5"},
    {"value": 15, "name": "rose 6"},
    {"value": 12, "name": "rose 7"},
    {"value": 10, "name": "rose 8"}
]

# Color scheme from the image
colors = [
    "#5b8ff9",  # blue
    "#5ad8a6",  # green
    "#5d7092",  # indigo
    "#f6bd16",  # yellow
    "#e86452",  # red
    "#6dc8ec",  # cyan
    "#945fb9",  # purple
    "#ff9845"   # orange
]

# Toggle states for each section of the chart
toggle_states = {f"rose {i+1}": st.sidebar.checkbox(f"rose {i+1}", True) for i in range(len(data))}

# Filter data based on toggle states
filtered_data = [d for d in data if toggle_states[d["name"]]]

# ECharts options
options = {
    "tooltip": {
        "trigger": "item",
        "formatter": "{a} <br/>{b}: {c} ({d}%)"
    },
    "legend": {
        "bottom": "0",
        "left": "center",
        "data": [d["name"] for d in filtered_data]
    },
    "color": colors,
    "series": [
        {
            "name": "Roses",
            "type": "pie",
            "radius": ["30%", "70%"],
            "center": ["50%", "50%"],
            "roseType": "radius",
            "itemStyle": {
                "borderRadius": 5
            },
            "label": {
                "show": True
            },
            "emphasis": {
                "label": {
                    "show": True
                }
            },
            "data": filtered_data
        }
    ]
}

# Render the chart with the options
st_echarts(options=options, height="600px")