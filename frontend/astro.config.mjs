// @ts-check
import { defineConfig } from 'astro/config';
// @ts-ignore
import htmx from 'astro-htmx';
import tailwind from "@astrojs/tailwind";
//import node from "@astrojs/node";

// https://astro.build/config
export default defineConfig({
    integrations: [ htmx(), tailwind() ],
    //output: 'server',
    //adapter: node({
        //mode: 'middleware',
      //}),
});
