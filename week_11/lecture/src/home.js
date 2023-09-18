import { useState } from "react";

const Home = () => {
  const [name, setName] = useState("");
  const [age, setAge] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await fetch("http://localhost:2000/add-student", {
        method: "POST",
        headers: {"Content-Type" : "application/json"},
        body: JSON.stringify({ name, age }),
      });
      alert("successfull");
    } catch (err) {
      alert("unsuccessful");
      console.error(err);
    }
  };
  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label for="name">
          Name:
          <input
            type="text"
            for="name"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </label>
        <label for="age">
          Age:
          <input
            type="number"
            for="age"
            value={age}
            onChange={(e) => setAge(e.target.value)}
          />
        </label>
        <button type="submit">submit</button>
      </form>
    </div>
  );
};
export default Home;
