import { useEffect, useRef, useState } from "react";

import "./App.css";

import Button from "@mui/material/Button";
import QuestionMarkIcon from "@mui/icons-material/QuestionMark";
import TextField from "@mui/material/TextField";
import { Alert, Chip, CircularProgress, Snackbar, Stack } from "@mui/material";

/**
 * Fetch the pokemon from pokeapi and return the JSON.
 * @param {*} name The name of the pokemon.
 * @returns The pokemon JSON.
 */
async function FetchPokemonFromApi(name) {
  const result = await fetch(`https://pokeapi.co/api/v2/pokemon/${name}`);
  const resultJson = await result.json();

  return resultJson;
}

function App() {
  // Initialize state hooks
  const [requiredPokemonName, setRequiredPokemonName] = useState("");
  const [pokemonName, setPokemonName] = useState("Mystery Pokemon");
  const [pokemonImage, setPokemonImage] = useState(
    <QuestionMarkIcon sx={{ fontSize: 180, border: "1px solid black" }} />
  );
  const [pokemonType, setPokemonType] = useState(null);
  const [fetchingSnackInfo, setfetchingSnackInfo] = useState(false);
  const [fetchingSnackError, setfetchingSnackError] = useState(false);
  const [fetchingSnackSuccess, setfetchingSnackSuccess] = useState(false);

  // Initialize refs
  const pokemonNameRef = useRef(null);

  // Fetch the pokemon details only once at the component loaded state
  useEffect(() => {
    // Only fetch if the required does not match the pokemon name
    // Only fetch if the required is not empty
    if (requiredPokemonName !== pokemonName && requiredPokemonName !== "") {
      // Fetch the pokemon details from the api
      FetchPokemonFromApi(requiredPokemonName.toLowerCase())
        .then((pokemonJson) => {
          setPokemonName(pokemonJson.name);
          setPokemonImage(
            <img
              src={pokemonJson.sprites.front_default}
              alt={pokemonName}
              height="180px"
              width="180px"
            />
          );

          // Set the pokemon types state
          let pokemonTypeHtml = [];
          for (let i = 0; i < pokemonJson.types.length; i++) {
            pokemonTypeHtml.push(
              <Chip label={pokemonJson.types[i].type.name} color="primary" />
            );
          }
          setPokemonType(pokemonTypeHtml);

          // Display only the success snackbar
          handleCloseSnackInfo();
          handleCloseSnackError();
          setfetchingSnackSuccess(true);
        })
        .catch((error) => {
          setPokemonName("Mystery Pokemon");
          setPokemonImage(
            <QuestionMarkIcon
              sx={{ fontSize: 180, border: "1px solid black" }}
            />
          );
          console.error(
            `Fetching ${pokemonName} from pokeapi failed. ERROR: ${error}`
          );

          // Display only the error snackbar
          handleCloseSnackInfo();
          handleCloseSnackSuccess();
          setfetchingSnackError(true);
        });
    } else {
      // TODO: Handle this
    }

    setRequiredPokemonName("");
  }, [requiredPokemonName]);

  // Handling of snackbars; info, error, success
  const handleCloseSnackInfo = (event, reason) => {
    if (reason === "clickaway") {
      return;
    }

    setfetchingSnackInfo(false);
  };
  const handleCloseSnackError = (event, reason) => {
    if (reason === "clickaway") {
      return;
    }

    setfetchingSnackError(false);
  };
  const handleCloseSnackSuccess = (event, reason) => {
    if (reason === "clickaway") {
      return;
    }

    setfetchingSnackSuccess(false);
  };

  // Handle loading of a new pokemon
  const loadPokemon = (event) => {
    setRequiredPokemonName(pokemonNameRef.current.lastChild.firstChild.value);
    setPokemonName("Loading...");
    setPokemonImage(<CircularProgress size={180} />);

    // Display only the info snackbar
    handleCloseSnackError();
    handleCloseSnackSuccess();
    setfetchingSnackInfo(true);
  };

  // Snackbar positioning
  const vertical = "bottom";
  const horizontal = "right";

  return (
    <div className="App">
      <header>
        <h1>Pokedex</h1>
      </header>
      {pokemonImage}
      <h2>
        Name: {pokemonName}
        <div>
          Type:{" "}
          <Stack direction="row" spacing={1} display={"inline-flex"}>
            {pokemonType}
          </Stack>
        </div>
      </h2>
      <TextField
        ref={pokemonNameRef}
        id="outlined-basic"
        label="Pokemon"
        variant="outlined"
      />
      <Button onClick={loadPokemon} variant="contained">
        Load
      </Button>
      <Snackbar
        anchorOrigin={{ vertical, horizontal }}
        open={fetchingSnackInfo}
        autoHideDuration={3000}
        onClose={handleCloseSnackInfo}
      >
        <Alert
          onClose={handleCloseSnackInfo}
          severity="info"
          sx={{ width: "100%" }}
        >
          Fetching {requiredPokemonName}...
        </Alert>
      </Snackbar>
      <Snackbar
        anchorOrigin={{ vertical, horizontal }}
        open={fetchingSnackError}
        autoHideDuration={3000}
        onClose={handleCloseSnackError}
      >
        <Alert
          onClose={handleCloseSnackError}
          severity="error"
          sx={{ width: "100%" }}
        >
          Fetching {requiredPokemonName} failed!
        </Alert>
      </Snackbar>
      <Snackbar
        anchorOrigin={{ vertical, horizontal }}
        open={fetchingSnackSuccess}
        autoHideDuration={3000}
        onClose={handleCloseSnackSuccess}
      >
        <Alert
          onClose={handleCloseSnackSuccess}
          severity="success"
          sx={{ width: "100%" }}
        >
          Successful fetching of {requiredPokemonName}.
        </Alert>
      </Snackbar>
    </div>
  );
}

export default App;
