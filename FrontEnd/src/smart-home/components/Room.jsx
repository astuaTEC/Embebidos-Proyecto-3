import React, { useContext, useMemo } from "react";
import Wall from "./Wall";
import Corner from "./Corner";
import Door from "./Door";
import Light from "./Light";
import { HouseContext } from "../../house-states/context/HouseContext";

const WALL_THICKNESS = 80;

const Room = ({ id, coords, door, light}) => {

  const { lights, doors: doorsContext } = useContext(HouseContext);

  const lightState = lights.find(e => e.id === id);

  const doorsState = doorsContext.find(d => d.id === id);

  //console.log(lightState)

  const walls = useMemo(
    () =>
      coords.map((_, i) => {
        const a = coords[i];
        const b = coords[(i + 1) % coords.length];
        return [a, b];
      }),
    [coords]
  );

  const doors = useMemo(
    () =>
      door.map((_, i) => {
        const a = door[i];
        const b = door[(i + 1) % door.length];
        return [a, b];
      }),
    [door]
  );


  return (
    <g>
      {walls.map(([a, b]) => (
        <Wall
          key={`wall-${a.x},${a.y}-${b.x},${b.y}`}
          corner1={a}
          corner2={b}
          thickness={WALL_THICKNESS}
        />
      ))}
      {coords.map(coord => (
        <Corner
          key={`corner-${coord.x},${coord.y}`}
          at={coord}
          thickness={WALL_THICKNESS}
        />
      ))}
      {
        doors.map(([a, b]) => (
          <Door
            key={`door-${a.x},${a.y}-${b.x},${b.y}`}
            corner1={a}
            corner2={b}
            state={doorsState?.state}
            thickness={WALL_THICKNESS} 
          />
        ))
      }
      {
        <Light 
          key={`light-${light.x},${light.y}`}
          at={light}
          thickness={WALL_THICKNESS}
          lightState={ lightState?.state }
        />
      }
      <text
        x={coords[0].x + 100}
        y={coords[0].y + 240}
        fill="red"
        fontSize="180"
      >
        {id}
      </text>
    </g>
  );
};

export default Room;
