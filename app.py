import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY = "enter key here"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def main():
    st.set_page_config(page_title="SQL GENRATOR")
    st.markdown(
    """
        <div style="text-align: center;"> 
            <h1>SQL GENERATOR</h1>
            <h3>I can generate SQL queries for you!</h3>
            <h4>with explaination as well!</h4>
            <p>This tool generates sql queries based on your requests.</p>
        </div>
    """,
    unsafe_allow_html=True
    
    
    )

    text_input=st.text_area("Enter your Query in Plain English")
   
    submit=st.button("Generate SQL Query")

    if submit:
         with st.spinner("Generating SQL Query...."):
            template="""
                Create a SQL Query snippet using the below text:

                {text_input}

            """
            formatted_template=template.format(text_input=text_input)
            st.write(formatted_template)
            response=model.generate_content(formatted_template)
            sql_query=response.text
            st.write(sql_query)

            excepted_output="""
                What would be the expected response to this SQL Query snippet:
                        {sql_query}
                
                provide sample tabular resoponse
            """
            expected_formatted_template=excepted_output.format(sql_query=sql_query)
            eoutput=model.generate_content(expected_formatted_template)
            eoutput=eoutput.text
            st.write(eoutput)

            explanation="""
                Explain this SQL Query:
                        {sql_query}
                
                Please provide simplest explanation possible
            """
            explanation_formatted_template=explanation.format(sql_query=sql_query)
            explained=model.generate_content(explanation_formatted_template)
            explained=explained.text
            st.write(explained)


main()
