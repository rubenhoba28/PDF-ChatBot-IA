css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://res.cloudinary.com/imagist/image/fetch/q_auto,f_auto,c_scale,w_2624/https%3A%2F%2Fimages.ctfassets.net%2Fdm4oa8qtogq0%2F6J5ynhwMSyYSJdgKFOkEym%2F8dd1ae730b3ee901fb8af6405346239b%2FAI-Assistant_512-Big.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://t3.ftcdn.net/jpg/03/26/78/92/360_F_326789207_j2xiy5Ih9k6k0wtzZWs1n5dWpnlu7kEh.jpg">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''