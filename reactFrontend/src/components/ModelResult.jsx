import React from "react";
import Box from "@material-ui/core/Box";

export default function Block(props) {
  return (
    <div style={{ width: "100%" }}>
      <Box
        component="span"
        display="block"
        p={1}
        m={1}
        bgcolor="background.paper"
      >
        {props.info}
      </Box>
    </div>
  );
}
