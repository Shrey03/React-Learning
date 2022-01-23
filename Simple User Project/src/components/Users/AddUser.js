const AddUser = (props) => {
  const addUserHandler = (event) => {
    event.preventDefault();
  };

  return (
    <form onSubmit={addUserHandler}>
      <label htmlFor="username">UserName</label>
      <input id="username" type="text"></input>
      <label htmlFor="age">Age</label>
      <input id="age" type="number"></input>
      <button type="submit"> ADD USER</button>
    </form>
  );
};

export default AddUser;
