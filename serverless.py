import * as fal from "@fal-ai/serverless-client";
 
fal.config({
  credentials: "PASTE_YOUR_FAL_KEY_HERE",
});
 
const connection = fal.realtime.connect("fal-ai/fast-lcm-diffusion", {
  onResult: (result) => {
    console.log(result);
  },
  onError: (error) => {
    console.error(error);
  },
});
 
connection.send({
  prompt:
    "an island near sea, with seagulls, moon shining over the sea, light house, boats int he background, fish flying over the sea",
  sync_mode: true,
  image_url:
    "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==",
});import * as fal from "@fal-ai/serverless-client";
 
fal.config({
  credentials: "PASTE_YOUR_FAL_KEY_HERE",
});
 
const connection = fal.realtime.connect("fal-ai/fast-lcm-diffusion", {
  onResult: (result) => {
    console.log(result);
  },
  onError: (error) => {
    console.error(error);
  },
});
 
connection.send({
  prompt:
    "an island near sea, with seagulls, moon shining over the sea, light house, boats int he background, fish flying over the sea",
  sync_mode: true,
  image_url:
    "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==",
});