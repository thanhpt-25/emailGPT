import json, os

import openai


class Chatter:
    def __init__(self):

        openai.api_key = os.getenv("OPENAI_API_KEY")

        return None

    def get_response(self, prompt):
        """Basic ChatGPT query. Give a prompt, get a response.

        Parameters
        ----------
        prompt : str
            the instructions/dialogue provided to ChatGPT
        """
        message = openai.Completion.create(
          model="text-davinci-003",
          prompt=prompt,
          temperature=0.7,
          max_tokens=1024,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0
        )
        return message.choices[0].text

    def parse_job(self, job):
        """Creates a prompt from a job dict

        Parameters
        ----------
        job : dict
            expects a job dict as defined in app.py
            {
                "sender": sender,
                "recipient": recipient,
                "subject": subject,
                "topic": topic,
                "tone": tone,
            }
        """
        if job["no_emails"] in ["2", "3"]:
            prompt = "Write %s examples " % job["no_emails"]
        else:
            prompt = "Write an example "
        prompt += "of ".format(tone=job["tone"])

        if job["tone"] in ["excited", "angry"]:
            prompt += "an %s newsletter " % job["tone"]
        elif job["tone"] in ["happy", "sad"]:
            prompt += "a %s newsletter  " % job["tone"]
        else:  # includes "newsletter"
            prompt += "an newsletter "

        if job["no_emails"] in ["2", "3"]:
            prompt += "emails "
        else:
            prompt += "email "

        if job["max_length"] != "":
            prompt += "with no more than %s characters " % job["max_length"]

        if job["language"] == "日本語":
            prompt += "in %s " % "japanese"
        else:
            
            prompt += "in %s " % "english"

        if job["sender_attr"] == "30代女性":
            prompt += "from %s " % "a female in her 30s "
        elif job["sender_attr"] == "40代女性":
            prompt += "from %s " % "a female in her 40s "
        else:
            prompt += "from %s " % "a female in her 50s "

        if job["receiver_attr"] == "30代女性":
            prompt += "to a target who is %s " % "a female in her 30s."
        elif job["receiver_attr"] == "40代女性":
            prompt += "to a target who is %s " % "a female in her 40s."
        else:
            prompt += "to a target who is %s " % "a female in her 50s."

        if job["subject"] != "":
            prompt += "The email must has the subject line '%s' " % job["subject"]
        if job["theme"] != "":
            prompt += "and its content theme is about '%s' ." % job["theme"]
        while prompt[-1] == " ":
            prompt = prompt[:-1]
        return prompt

    def email_from_job(self, job):
        """Given a job dict, generates an email.

        Parameters
        ----------
        job : dict
            expects a job dict as defined in app.py
            {
                "sender": sender,
                "recipient": recipient,
                "subject": subject,
                "topic": topic,
                "tone": tone,
            }
        """
        prompt = self.parse_job(job)
        # message = self.get_response(prompt)
        return prompt
