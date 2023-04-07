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
          max_tokens=256,
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
        prompt = "An example of ".format(tone=job["tone"])

        if job["tone"] in ["excited", "angry"]:
            prompt += "an %s email " % job["tone"]
        elif job["tone"] in ["happy", "sad"]:
            prompt += "a %s email " % job["tone"]
        else:  # includes "neutral"
            prompt += "an email "
        if job["sender"] != "":
            prompt += "from %s " % job["sender"]
        if job["recipient"] != "":
            prompt += "to %s " % job["recipient"]
        if job["subject"] != "":
            prompt += "with the subject line '%s' " % job["subject"]
        if job["topic"] != "":
            prompt += "about %s " % job["topic"]

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
        message = self.get_response(prompt)
        return message
