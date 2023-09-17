# CookingHelper

Created for ShellHacks 2023.

## Inspiration

Cass was inspired to make this project by a 2023 LibrePlanet virtual talk fae attended titled "The Immortal Cookbook".
The idea for this project was to make a software that could take in all conventional forms of recipes, store them, allow users to share them, and to create combined ingredient shopping lists from multiple recipes.

## What it does

In it's current state, we have a front-end and a back-end that don't yet communicate.
The back-end does serve up a GraphQL API, but the front-end does not consume that API.

## How we built it

Cass primarily built the back-end, bringing faer internship experience of working with Django and GraphQL.
Everyone except Cass worked on the front-end mockups.
Kameron made significant process on the front-end implementation.

## Challenges we ran into

We primarily ran into time and human energy constraints.
Hackathons, including ShellHacks, feel simultaneously short and long; short in that there's never enough time for everything, and long in that one might want to leave early because they're just too tired.

## Accomplishments that we're proud of

The back-end's GraphQL API works quite nicely.

## What we learned

Cass: I was reminded of something very important for me: that I need a significant amount of sleep to be a good developer.

## What's next for CookingHelper

Authentication is an important thing to add.
Right now, it exists as a single user / everything shared service.
Anyone with access to the service's API can preform any queries or mutations they want.
