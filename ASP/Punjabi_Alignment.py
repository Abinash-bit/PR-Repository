def punjabi(path, textgrid):
    st.write("<h7 class = 'stLang'>Running Alignment for Punjabi...</h7>", unsafe_allow_html=True)
    align_command = ['conda', 'run', '--name', 'aligner', 'mfa', 'align', path, 
                     "C:/Users/Administrator/Desktop/ASP-Project/pretrained_models_tanishka/dictionary/punjabi_cv.dict",
                     "C:/Users/Administrator/Desktop/ASP-Project/pretrained_models_tanishka/acoustic/new_acoustic_model.zip",
                     path, '--beam', '400']
    try:
        sp.run(align_command, shell=True, check=True)
    except sp.CalledProcessError:
        st.error('The voice in the file does not match.')
        return None  # Return None to indicate failure
    if not os.path.exists(textgrid):
        raise FileNotFoundError(f"{textgrid} not found after alignment process.")
    with open(textgrid, 'r', encoding='utf-8') as file:
        out = file.read()
    st.write("<h7 class = 'stLang'>Alignment Complete.</h7>", unsafe_allow_html=True)
    return out

# Example usage:
path = 'C:/Users/Administrator/Desktop/ASP-Project/forced_alignment'
textgrid_path = 'C:/Users/Administrator/Desktop/ASP-Project/forced_alignment/output.TextGrid'
punjabi(path, textgrid_path)
