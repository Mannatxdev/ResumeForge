import React, { useState } from "react";
import API from "../api/api";

function CreateResume() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [mobile, setMobile] = useState("");
  const [linkedin, setLinkedin] = useState("");
  const [github, setGithub] = useState("");

  const handleSubmit = async () => {
    await API.post("resumes/", {
      name,
      email,
      mobile,
      linkedin,
      github
    });

    alert("Resume Created!");
  };

  return (
    <div>
      <h1>Create Resume</h1>

      <input placeholder="Name" onChange={(e) => setName(e.target.value)} />
      <input placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
      <input placeholder="Mobile" onChange={(e) => setMobile(e.target.value)} />
      <input placeholder="LinkedIn" onChange={(e) => setLinkedin(e.target.value)} />
      <input placeholder="GitHub" onChange={(e) => setGithub(e.target.value)} />

      <button onClick={handleSubmit}>Submit</button>
    </div>
  );
}

export default CreateResume;