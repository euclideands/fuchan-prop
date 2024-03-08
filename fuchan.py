import streamlit as st

def main():
    st.title("Message From Abil!")

    # Button to trigger the pop-up
    button_clicked = st.button("Click Me!")

    # Display pop-up if button is clicked
    if button_clicked:
        st.markdown("""
        <style>
        .popup {
            position: fixed;
            top: 70%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: #f7d794; /* Warna background pop-up */
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            z-index: 9999;
        }

        .message {
            font-size: 24px; /* Ukuran font pesan */
            color: #6c5ce7; /* Warna teks pesan */
            text-align: center;
            margin-bottom: 10px;
        }

        .emoji {
            font-size: 48px; /* Ukuran font emoji */
            text-align: center;
        }
        </style>
        <div class="popup" id="popup">
            <div class="message">Hai Mas Fuu Chan!!</div>
            <p>Thank you for being super ramah dan mau jadi temen aku dan temen-temen MBKM lain di BP! It is nice to know U. U also need to know that our intern experience wouldn't be complete without U! I hope all your wish come true! Hope we can meet again in better place and better time.</p>
            <div class="emoji">😊</div>
        </div>

        <script>
        // Set timeout untuk mengarahkan pengguna ke halaman baru setelah 3 detik
        setTimeout(function(){
            window.location.href = 'https://example.com'; // Ganti 'https://example.com' dengan URL halaman baru Anda
        }, 5000); // Set waktu tunda dalam milidetik (dalam contoh ini 5 detik)
        </script>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
