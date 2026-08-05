graph TD
    subgraph "Input & UI Layer"
        A[Video Source / Live Feed] --> B[PyWebView GUI]
        B --> C[Manual ROI Calibration]
    end

    subgraph "AI Inference Engine"
        C --> D[Frame Pre-processing]
        D --> E{IISc-AIM UVH-26 Model}
        E -->|YOLOv11-S| F[Indian Vehicle Detection]
        F --> G[Filtering: Cars, Bikes, Autos, Trucks]
    end

    subgraph "Decision Logic"
        G --> H[Observation Window: 10s Avg]
        H --> I[Flow-Ratio Calculation]
        I --> J[Adaptive Green-Time Optimization]
    end

    subgraph "Output & Analytics"
        J --> K[Signal State Update: G/Y/R]
        K --> L[Real-time Metrics Dashboard]
        L --> M[Export to traffic_results.csv]
        M --> N[Matplotlib Visual Analytics]
    end

    style E fill:#f9f,stroke:#333,stroke-width:2px
    style J fill:#bbf,stroke:#333,stroke-width:2px
    style K fill:#dfd,stroke:#333,stroke-width:2px