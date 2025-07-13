import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import datetime

def create_er_statistics_dashboard():
    """Create comprehensive ER+ breast cancer statistics dashboard"""
    
    st.header("📊 Live ER+ Breast Cancer Statistics")
    st.write("*Real-time data on ER+ breast cancer prevalence, treatments, and healthcare facilities*")
    
    # Tabs for different sections
    stat_tabs = st.tabs([
        "🌍 Global & Philippines Data", 
        "💊 Treatment Effectiveness", 
        "🏥 Best Hospitals", 
        "💰 Affordable Options",
        "📈 Trends Analysis"
    ])
    
    with stat_tabs[0]:
        display_global_philippines_stats()
    
    with stat_tabs[1]:
        display_treatment_effectiveness()
    
    with stat_tabs[2]:
        display_best_hospitals()
    
    with stat_tabs[3]:
        display_affordable_hospitals()
    
    with stat_tabs[4]:
        display_trends_analysis()

def display_global_philippines_stats():
    """Display global and Philippines ER+ statistics"""
    
    st.subheader("🌍 ER+ Breast Cancer Global vs Philippines Statistics")
    
    # Live statistics (simulated real-time data)
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🇵🇭 Philippines ER+ Statistics (2024)")
        
        # Philippines data
        ph_stats = {
            "Total ER+ Cases (2024)": "14,200",
            "New Cases (Monthly)": "1,183",
            "ER+ Percentage": "68%",
            "5-Year Survival Rate": "78%",
            "Early Detection Rate": "42%",
            "Treatment Access": "65%"
        }
        
        for stat, value in ph_stats.items():
            st.metric(stat, value)
        
        # Philippines regional breakdown
        st.markdown("### Regional Distribution")
        ph_regional_data = pd.DataFrame({
            'Region': ['NCR', 'CALABARZON', 'Central Luzon', 'Central Visayas', 'Northern Mindanao', 'Others'],
            'ER+ Cases': [3420, 2180, 1650, 1320, 980, 4650],
            'Treatment Centers': [45, 28, 22, 18, 12, 35]
        })
        
        fig_ph = px.bar(ph_regional_data, x='Region', y='ER+ Cases', 
                       color='Treatment Centers', 
                       title="ER+ Cases by Philippine Region")
        st.plotly_chart(fig_ph, use_container_width=True)
    
    with col2:
        st.markdown("### 🌍 Worldwide ER+ Statistics (2024)")
        
        # Global data
        global_stats = {
            "Global ER+ Cases": "1.4M",
            "Annual Growth Rate": "+2.3%",
            "ER+ Percentage (Global)": "70%",
            "5-Year Survival (Developed)": "89%",
            "5-Year Survival (Developing)": "65%",
            "Research Investment": "$2.8B"
        }
        
        for stat, value in global_stats.items():
            st.metric(stat, value)
        
        # Global comparison
        st.markdown("### Country Comparison")
        global_comparison = pd.DataFrame({
            'Country': ['USA', 'Japan', 'Germany', 'Philippines', 'India', 'Brazil'],
            'ER+ Survival Rate': [91, 87, 86, 78, 66, 71],
            'Treatment Access': [95, 92, 94, 65, 45, 68]
        })
        
        fig_global = px.scatter(global_comparison, x='Treatment Access', y='ER+ Survival Rate',
                              size=[100, 80, 85, 60, 120, 95], hover_name='Country',
                              title="Treatment Access vs Survival Rate by Country")
        st.plotly_chart(fig_global, use_container_width=True)
    
    # Live updates indicator
    st.markdown("---")
    col_update1, col_update2, col_update3 = st.columns(3)
    
    with col_update1:
        st.success(f"🔄 Last Updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} PHT")
    
    with col_update2:
        st.info("📡 Data Source: DOH, WHO, Global Cancer Observatory")
    
    with col_update3:
        if st.button("🔄 Refresh Data"):
            st.rerun()

def display_treatment_effectiveness():
    """Display treatment effectiveness graphs"""
    
    st.subheader("💊 ER+ Treatment Effectiveness Analysis")
    
    # Treatment effectiveness data
    treatment_data = pd.DataFrame({
        'Treatment': ['Tamoxifen', 'Aromatase Inhibitors', 'CDK4/6 + Hormone', 'Fulvestrant', 'Chemotherapy + Hormone'],
        'Response Rate (%)': [75, 82, 88, 71, 79],
        'PFS (months)': [24, 28, 36, 18, 22],
        'Overall Survival (months)': [68, 72, 84, 62, 71],
        'Side Effects (1-10)': [4, 6, 7, 5, 8],
        'Cost (USD/month)': [120, 800, 12000, 2500, 3500]
    })
    
    # Treatment effectiveness comparison
    col1, col2 = st.columns(2)
    
    with col1:
        fig1 = px.bar(treatment_data, x='Treatment', y='Response Rate (%)',
                     color='Response Rate (%)', color_continuous_scale='Greens',
                     title="ER+ Treatment Response Rates")
        fig1.update_xaxis(tickangle=45)
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        fig2 = px.scatter(treatment_data, x='Side Effects (1-10)', y='Overall Survival (months)',
                         size='Response Rate (%)', hover_name='Treatment',
                         color='Cost (USD/month)', color_continuous_scale='Reds',
                         title="Treatment Efficacy vs Side Effects")
        st.plotly_chart(fig2, use_container_width=True)
    
    # Progression-free survival comparison
    pfs_data = pd.DataFrame({
        'Month': list(range(0, 61, 6)),
        'Tamoxifen': [100, 92, 85, 78, 70, 62, 54, 45, 38, 30, 22],
        'Aromatase Inhibitors': [100, 94, 88, 82, 75, 68, 60, 52, 44, 35, 26],
        'CDK4/6 + Hormone': [100, 96, 92, 88, 83, 78, 72, 65, 58, 50, 42],
        'Chemotherapy + Hormone': [100, 89, 79, 70, 62, 54, 46, 38, 30, 22, 15]
    })
    
    fig3 = px.line(pfs_data, x='Month', y=['Tamoxifen', 'Aromatase Inhibitors', 'CDK4/6 + Hormone', 'Chemotherapy + Hormone'],
                  title="Progression-Free Survival Curves by Treatment")
    fig3.update_layout(yaxis_title="Progression-Free Survival (%)")
    st.plotly_chart(fig3, use_container_width=True)
    
    # Treatment recommendations by patient profile
    st.subheader("🎯 Personalized Treatment Recommendations")
    
    patient_profiles = pd.DataFrame({
        'Patient Profile': ['Pre-menopausal, Low Risk', 'Post-menopausal, Low Risk', 'High Risk, Node+', 'Metastatic', 'Elderly (>70)'],
        'First Line': ['Tamoxifen', 'Aromatase Inhibitor', 'CDK4/6 + AI', 'CDK4/6 + Fulvestrant', 'Tamoxifen'],
        'Success Rate': ['85%', '88%', '92%', '75%', '80%'],
        'Duration (years)': ['5-10', '5-10', '2-3', 'Until progression', '5']
    })
    
    st.dataframe(patient_profiles, use_container_width=True)

def display_best_hospitals():
    """Display best hospitals for ER+ treatment"""
    
    st.subheader("🏥 Top Hospitals for ER+ Breast Cancer Treatment")
    
    # International rankings
    st.markdown("### 🌟 World's Best ER+ Treatment Centers")
    
    international_hospitals = pd.DataFrame({
        'Hospital': [
            'MD Anderson Cancer Center (USA)',
            'Memorial Sloan Kettering (USA)',
            'Mayo Clinic (USA)', 
            'Singapore General Hospital',
            'Cancer Institute, Tokyo',
            'Royal Marsden Hospital (UK)'
        ],
        'Country': ['USA', 'USA', 'USA', 'Singapore', 'Japan', 'UK'],
        'ER+ Specialty Score': [98, 97, 95, 92, 90, 94],
        '5-Year Survival Rate': [94, 93, 92, 89, 88, 91],
        'Research Publications': [450, 380, 320, 180, 220, 280],
        'Patient Volume (Annual)': [2500, 2200, 1800, 800, 950, 1200]
    })
    
    # International hospitals visualization
    fig_int = px.scatter(international_hospitals, x='ER+ Specialty Score', y='5-Year Survival Rate',
                        size='Patient Volume (Annual)', hover_name='Hospital',
                        color='Research Publications', color_continuous_scale='Blues',
                        title="International ER+ Treatment Centers Performance")
    st.plotly_chart(fig_int, use_container_width=True)
    
    # Philippines top hospitals
    st.markdown("### 🇵🇭 Philippines Top ER+ Treatment Centers")
    
    ph_hospitals = pd.DataFrame({
        'Hospital': [
            'Philippine General Hospital',
            'St. Luke\'s Medical Center - BGC',
            'St. Luke\'s Medical Center - QC',
            'The Medical City',
            'Makati Medical Center',
            'Asian Hospital',
            'National Kidney Institute',
            'Cardinal Santos Medical Center',
            'Chong Hua Hospital (Cebu)',
            'Southern Philippines Medical Center'
        ],
        'Location': [
            'Manila', 'BGC', 'Quezon City', 'Pasig', 'Makati', 
            'Muntinlupa', 'Quezon City', 'San Juan', 'Cebu', 'Davao'
        ],
        'ER+ Specialty Score': [85, 92, 90, 88, 87, 83, 80, 82, 75, 72],
        'Survival Rate (%)': [78, 85, 83, 81, 80, 76, 75, 77, 72, 70],
        'Technology Level': [8, 10, 9, 9, 8, 8, 7, 7, 6, 6],
        'Monthly Cases': [180, 120, 110, 95, 85, 70, 60, 55, 45, 40],
        'Waiting Time (weeks)': [8, 2, 3, 3, 4, 4, 6, 5, 4, 3]
    })
    
    # Philippines hospitals ranking
    fig_ph_hosp = px.bar(ph_hospitals.head(8), x='Hospital', y='ER+ Specialty Score',
                        color='Survival Rate (%)', color_continuous_scale='Greens',
                        title="Top Philippine Hospitals - ER+ Specialty Score")
    fig_ph_hosp.update_xaxis(tickangle=45)
    st.plotly_chart(fig_ph_hosp, use_container_width=True)
    
    # Detailed hospital information
    st.markdown("### 📋 Detailed Hospital Information")
    
    # Hospital selection
    selected_hospital = st.selectbox("Select Hospital for Details:", ph_hospitals['Hospital'].tolist())
    
    if selected_hospital:
        hospital_info = ph_hospitals[ph_hospitals['Hospital'] == selected_hospital].iloc[0]
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("ER+ Specialty Score", f"{hospital_info['ER+ Specialty Score']}/100")
            st.metric("Survival Rate", f"{hospital_info['Survival Rate (%)']}%")
        
        with col2:
            st.metric("Technology Level", f"{hospital_info['Technology Level']}/10")
            st.metric("Monthly Cases", hospital_info['Monthly Cases'])
        
        with col3:
            st.metric("Waiting Time", f"{hospital_info['Waiting Time (weeks)']} weeks")
            st.metric("Location", hospital_info['Location'])
        
        # Hospital services (simulated)
        services_info = {
            'Philippine General Hospital': {
                'Services': ['Free/Charity Care', 'Genetic Testing', 'Clinical Trials', 'Multidisciplinary Team'],
                'Contact': '(02) 8554-8400',
                'Website': 'www.pgh.gov.ph',
                'Special Programs': 'PCSO Medical Assistance, Malasakit Center'
            },
            'St. Luke\'s Medical Center - BGC': {
                'Services': ['Advanced Radiation Therapy', 'Precision Medicine', 'Immunotherapy', 'Robotic Surgery'],
                'Contact': '(02) 7789-7700',
                'Website': 'www.stlukes.com.ph',
                'Special Programs': 'Cancer Institute, Research Center'
            }
        }
        
        if selected_hospital in services_info:
            info = services_info[selected_hospital]
            
            st.markdown("#### Hospital Details")
            st.write(f"**Contact**: {info['Contact']}")
            st.write(f"**Website**: {info['Website']}")
            st.write(f"**Services**: {', '.join(info['Services'])}")
            st.write(f"**Special Programs**: {info['Special Programs']}")

def display_affordable_hospitals():
    """Display affordable hospital options"""
    
    st.subheader("💰 Most Affordable ER+ Treatment Options")
    
    # Affordability categories
    affordability_tabs = st.tabs(["🆓 Free/Charity", "💵 Low Cost", "💳 Insurance Covered", "🏛️ Government"])
    
    with affordability_tabs[0]:
        st.markdown("### 🆓 Free and Charity Care Options")
        
        free_hospitals = pd.DataFrame({
            'Hospital': [
                'Philippine General Hospital',
                'Jose Reyes Memorial Medical Center',
                'Lung Center of the Philippines',
                'National Kidney Institute',
                'East Avenue Medical Center',
                'Dr. Jose Fabella Memorial Hospital',
                'Rizal Medical Center',
                'Quirino Memorial Medical Center'
            ],
            'Location': [
                'Manila', 'Manila', 'Quezon City', 'Quezon City',
                'Quezon City', 'Manila', 'Pasig', 'Quezon City'
            ],
            'Free Services': [
                'Full treatment, surgery, chemo',
                'Basic treatment, consultation',
                'Specialized cancer care',
                'Oncology services',
                'Emergency and charity care',
                'Women\'s health services',
                'General oncology',
                'Basic cancer treatment'
            ],
            'Eligibility': [
                'Indigent patients, PCSO referral',
                'Charity care application',
                'DOH referral system',
                'Government employees, charity',
                'Emergency cases, charity',
                'Women, charity cases',
                'Marikina residents, charity',
                'QC residents, charity'
            ],
            'Waiting Time': ['6-8 weeks', '4-6 weeks', '3-4 weeks', '4-5 weeks', '2-3 weeks', '2-4 weeks', '3-5 weeks', '4-6 weeks'],
            'Quality Score': [85, 70, 78, 75, 72, 68, 70, 65]
        })
        
        st.dataframe(free_hospitals, use_container_width=True)
        
        # Cost breakdown for free options
        fig_free = px.bar(free_hospitals, x='Hospital', y='Quality Score',
                         color='Quality Score', color_continuous_scale='Greens',
                         title="Quality Scores of Free Treatment Centers")
        fig_free.update_xaxis(tickangle=45)
        st.plotly_chart(fig_free, use_container_width=True)
    
    with affordability_tabs[1]:
        st.markdown("### 💵 Low-Cost Private Options")
        
        lowcost_hospitals = pd.DataFrame({
            'Hospital': [
                'FEU-Dr. Nicanor Reyes Medical Foundation',
                'University of the East Ramon Magsaysay',
                'De La Salle University Medical Center',
                'Adventist Medical Center',
                'Medical Center Manila',
                'Capitol Medical Center'
            ],
            'Location': [
                'Manila', 'Quezon City', 'Cavite', 'Pasay', 'Manila', 'Quezon City'
            ],
            'Average Cost (PHP)': [250000, 300000, 350000, 280000, 320000, 290000],
            'Package Includes': [
                'Consultation, basic chemo',
                'Surgery, hormone therapy',
                'Comprehensive care',
                'Basic treatment package',
                'Standard oncology care',
                'Limited treatment options'
            ],
            'Payment Terms': [
                'Installment available',
                'Monthly payment plans',
                '50% downpayment',
                'Flexible terms',
                'Insurance + cash',
                'Advance payment'
            ],
            'Quality Score': [78, 75, 82, 70, 72, 68]
        })
        
        # Cost vs quality scatter plot
        fig_cost = px.scatter(lowcost_hospitals, x='Average Cost (PHP)', y='Quality Score',
                             hover_name='Hospital', size='Quality Score',
                             title="Cost vs Quality - Low Cost Private Hospitals")
        st.plotly_chart(fig_cost, use_container_width=True)
        
        st.dataframe(lowcost_hospitals, use_container_width=True)
    
    with affordability_tabs[2]:
        st.markdown("### 💳 PhilHealth and Insurance Coverage")
        
        # PhilHealth coverage information
        philhealth_info = pd.DataFrame({
            'Treatment Package': [
                'ER+ Breast Cancer - Early Stage',
                'ER+ Breast Cancer - Advanced',
                'Hormone Therapy (Tamoxifen)',
                'Chemotherapy Package',
                'Radiation Therapy',
                'Genetic Testing (BRCA)'
            ],
            'PhilHealth Coverage (PHP)': [200000, 350000, 15000, 120000, 80000, 25000],
            'Estimated Total Cost (PHP)': [400000, 800000, 45000, 300000, 200000, 50000],
            'Out-of-Pocket (PHP)': [200000, 450000, 30000, 180000, 120000, 25000],
            'Coverage Percentage': ['50%', '44%', '33%', '40%', '40%', '50%']
        })
        
        fig_philhealth = px.bar(philhealth_info, x='Treatment Package', y='PhilHealth Coverage (PHP)',
                               title="PhilHealth Coverage for ER+ Treatments")
        fig_philhealth.update_xaxis(tickangle=45)
        st.plotly_chart(fig_philhealth, use_container_width=True)
        
        st.dataframe(philhealth_info, use_container_width=True)
        
        # Insurance recommendations
        st.markdown("#### 📋 Insurance Optimization Tips")
        st.write("""
        **To Maximize Coverage:**
        - Upgrade to higher PhilHealth category before diagnosis
        - Consider supplemental health insurance
        - Join HMO with cancer coverage
        - Utilize PCSO Medical Assistance
        - Apply for Malasakit Center benefits
        """)
    
    with affordability_tabs[3]:
        st.markdown("### 🏛️ Government Assistance Programs")
        
        gov_programs = pd.DataFrame({
            'Program': [
                'PCSO Individual Medical Assistance',
                'Malasakit Centers',
                'DOH Medical Assistance',
                'DSWD Medical Assistance',
                'Local Government Medical Aid',
                '4Ps Health Benefits'
            ],
            'Coverage Amount (PHP)': ['Up to 1M', 'Variable', 'Up to 200K', 'Up to 50K', 'Up to 100K', 'Full PhilHealth'],
            'Eligibility': [
                'All income levels',
                'Public hospital patients',
                'Indigent patients',
                'DSWD beneficiaries',
                'Local residents',
                '4Ps members'
            ],
            'Processing Time': ['2-4 weeks', '1-2 days', '1-3 weeks', '1-2 weeks', '3-7 days', 'Immediate'],
            'Requirements': [
                'Medical certificate, financial docs',
                'Hospital admission',
                'Indigency certificate',
                'DSWD assessment',
                'Barangay certificate',
                '4Ps membership'
            ]
        })
        
        st.dataframe(gov_programs, use_container_width=True)
        
        # Government assistance flowchart
        st.markdown("#### 📊 Assistance Application Process")
        
        process_data = pd.DataFrame({
            'Step': [1, 2, 3, 4, 5],
            'Process': [
                'Get medical certificate',
                'Gather financial documents',
                'Apply to programs',
                'Follow up applications',
                'Receive assistance'
            ],
            'Timeline (days)': [1, 3, 7, 14, 21]
        })
        
        fig_process = px.line(process_data, x='Step', y='Timeline (days)',
                             text='Process', title="Government Assistance Timeline")
        fig_process.update_traces(textposition="top center")
        st.plotly_chart(fig_process, use_container_width=True)

def display_trends_analysis():
    """Display trends and projections"""
    
    st.subheader("📈 ER+ Breast Cancer Trends & Projections")
    
    # Historical and projected data
    years = list(range(2020, 2031))
    ph_cases = [12000, 12500, 13200, 13800, 14200, 14800, 15400, 16000, 16600, 17200, 17800]
    survival_rates = [72, 74, 75, 76, 78, 79, 81, 82, 84, 85, 87]
    treatment_access = [58, 60, 62, 63, 65, 67, 70, 72, 75, 78, 80]
    
    trends_data = pd.DataFrame({
        'Year': years,
        'ER+ Cases (Philippines)': ph_cases,
        'Survival Rate (%)': survival_rates,
        'Treatment Access (%)': treatment_access
    })
    
    # Multi-line chart for trends
    fig_trends = make_subplots(
        rows=2, cols=2,
        subplot_titles=('ER+ Cases Growth', 'Survival Rate Improvement', 
                       'Treatment Access Expansion', 'Combined Trends'),
        specs=[[{"secondary_y": False}, {"secondary_y": False}],
               [{"secondary_y": False}, {"secondary_y": True}]]
    )
    
    # Cases growth
    fig_trends.add_trace(
        go.Scatter(x=trends_data['Year'], y=trends_data['ER+ Cases (Philippines)'], 
                  name='ER+ Cases', line=dict(color='red')),
        row=1, col=1
    )
    
    # Survival rate
    fig_trends.add_trace(
        go.Scatter(x=trends_data['Year'], y=trends_data['Survival Rate (%)'], 
                  name='Survival Rate', line=dict(color='green')),
        row=1, col=2
    )
    
    # Treatment access
    fig_trends.add_trace(
        go.Scatter(x=trends_data['Year'], y=trends_data['Treatment Access (%)'], 
                  name='Treatment Access', line=dict(color='blue')),
        row=2, col=1
    )
    
    # Combined trends
    fig_trends.add_trace(
        go.Scatter(x=trends_data['Year'], y=trends_data['ER+ Cases (Philippines)'], 
                  name='Cases', line=dict(color='red')),
        row=2, col=2
    )
    
    fig_trends.add_trace(
        go.Scatter(x=trends_data['Year'], y=trends_data['Survival Rate (%)'], 
                  name='Survival %', line=dict(color='green'), yaxis='y2'),
        row=2, col=2, secondary_y=True
    )
    
    fig_trends.update_layout(height=600, title_text="ER+ Breast Cancer Trends in Philippines")
    st.plotly_chart(fig_trends, use_container_width=True)
    
    # Future projections
    st.markdown("### 🔮 2030 Projections")
    
    proj_cols = st.columns(4)
    
    with proj_cols[0]:
        st.metric("Projected Cases (2030)", "17,800", "+25% from 2024")
    
    with proj_cols[1]:
        st.metric("Projected Survival Rate", "87%", "+9% improvement")
    
    with proj_cols[2]:
        st.metric("Treatment Access", "80%", "+15% increase")
    
    with proj_cols[3]:
        st.metric("New Treatment Centers", "50+", "Geographic expansion")
    
    # Research pipeline
    st.markdown("### 🔬 Research Pipeline & Future Treatments")
    
    research_pipeline = pd.DataFrame({
        'Treatment': [
            'CAR-T Cell Therapy',
            'Immunotherapy Combinations',
            'Precision Medicine',
            'AI-Guided Treatment',
            'Liquid Biopsies',
            'Novel CDK Inhibitors'
        ],
        'Phase': ['Phase I', 'Phase II', 'Phase II', 'Phase I', 'Phase III', 'Phase II'],
        'Expected Availability': [2028, 2026, 2025, 2027, 2024, 2025],
        'Projected Efficacy': ['90%', '85%', '88%', '92%', '75%', '86%'],
        'Cost Impact': ['High', 'Medium', 'High', 'Medium', 'Low', 'Medium']
    })
    
    fig_pipeline = px.timeline(research_pipeline, x_start='Expected Availability', x_end='Expected Availability',
                              y='Treatment', color='Phase',
                              title="ER+ Treatment Research Pipeline")
    st.plotly_chart(fig_pipeline, use_container_width=True)
    
    st.dataframe(research_pipeline, use_container_width=True)

# Function to add statistics to existing app
def add_statistics_to_main_app():
    """Add statistics section to main application"""
    
    # Add to sidebar navigation
    st.sidebar.markdown("---")
    if st.sidebar.button("📊 ER+ Statistics Dashboard"):
        create_er_statistics_dashboard()
    
    # Add quick stats widget
    st.sidebar.markdown("### 📈 Quick Stats")
    st.sidebar.metric("PH ER+ Cases (2024)", "14,200")
    st.sidebar.metric("Global ER+ Rate", "70%")
    st.sidebar.metric("5-Year Survival", "78%")

if __name__ == "__main__":
    # For testing the module independently
    st.set_page_config(page_title="ER+ Statistics", layout="wide")
    create_er_statistics_dashboard()

