# app.py
import streamlit as st
import sys
import os

# 设置页面配置
st.set_page_config(
    page_title="Surgical Risk Prediction",
    page_icon="🏥",
    layout="wide"
)

# 检查核心依赖
try:
    import pandas as pd
    import numpy as np
    st.success("✅ pandas and numpy loaded")
except ImportError:
    st.error("❌ Essential libraries not found. Please check requirements.txt")
    st.stop()

# 特别处理 joblib 导入
try:
    # 尝试从 scikit-learn 导入
    from sklearn.externals import joblib
    st.success("✅ Using sklearn's joblib")
except ImportError:
    try:
        # 尝试直接导入
        import joblib
        st.success("✅ Using standalone joblib")
    except ImportError:
        st.error("""
        ❌ joblib not found. This is a critical error.
        
        Please ensure your requirements.txt contains:
        joblib==1.4.2
        
        If deploying on Streamlit Cloud:
        1. Go to 'Manage app'
        2. Click 'Clear cache'
        3. Redeploy the application
        """)
        st.stop()

# 加载模型
try:
    model = joblib.load("model.joblib")
    st.success("✅ Model loaded successfully")
except Exception as e:
    st.error(f"❌ Failed to load model: {str(e)}")
    st.error("Please ensure 'model.joblib' exists in the root directory")
    st.stop()

# 变量配置（保持原有内容）
VARIABLE_CONFIG = {
    "Sex": {
        "min": 0, 
        "max": 1,
        "description": "Patient gender (0=Female, 1=Male)",
        "value": 0
    },
    # ... 其他变量配置不变 ...
}

# 应用界面（保持原有内容）
st.title("Unplanned Reoperation Risk Prediction System")
st.markdown("---")

# ... 输入表单和预测逻辑保持不变 ...

# 诊断信息
with st.expander("Environment Diagnostics"):
    st.write("**Python Version:**", sys.version)
    st.write("**System Path:**", sys.path)
    
    try:
        import pkg_resources
        installed_packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}
        st.write("**Installed Packages:**")
        st.json(installed_packages)
    except ImportError:
        st.warning("Could not retrieve installed packages list")
    
    st.write("**Current Directory Contents:**")
    try:
        files = os.listdir('.')
        st.write(files)
    except Exception as e:
        st.error(f"Error listing files: {str(e)}")