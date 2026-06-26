import Soundcloud from "soundcloud.ts"
import PromptSync from "prompt-sync"
import { config } from "./config"

const soundcloud = new Soundcloud(config.clientId,config.clientSecret);
const prompt = PromptSync();

(async () => {
    const query: string = prompt("Enter a SoundCloud track Name: ");

    const tracks = await soundcloud.tracks.search({q: query, limit: 5});
    console.log(tracks)

})();