flowchart TD

%% =========================
%% INPUT LAYER
%% =========================
subgraph INPUT["📥 Input Layer"]
    A[Traffic Video / Live Camera]
    B[PyWebView Desktop GUI]
    C[Manual ROI Selection]
    A --> B
    B --> C
end

%% =========================
%% AI ENGINE
%% =========================
subgraph AI["🤖 AI Inference Engine"]
    D[Frame Preprocessing]
    E["YOLOv11-S (IISc-AIM UVH-26)"]
    F[Vehicle Detection]
    G[Vehicle Classification]
    C --> D
    D --> E
    E --> F
    F --> G
end

%% =========================
%% CONTROL ENGINE
%% =========================
subgraph CONTROL["🚦 Adaptive Signal Controller"]
    H[10-Second Observation Window]
    I[Traffic Density Estimation]
    J[Flow Ratio Calculation]
    K[Adaptive Green Time Computation]
    G --> H
    H --> I
    I --> J
    J --> K
end

%% =========================
%% OUTPUT
%% =========================
subgraph OUTPUT["📊 Output & Analytics"]
    L[Traffic Signal Update]
    M[CSV Performance Logging]
    N[Performance Visualization]
    K --> L
    L --> M
    M --> N
end

%% =========================
%% STYLING
%% =========================
style E fill:#E8F0FE,stroke:#1A73E8,stroke-width:2px
style K fill:#FFF4E5,stroke:#FB8C00,stroke-width:2px
style L fill:#E8F5E9,stroke:#43A047,stroke-width:2px