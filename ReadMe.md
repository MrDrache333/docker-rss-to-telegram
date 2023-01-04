# Docker RSS to Telegram Bot
[![Create and publish Docker image](https://github.com/MrDrache333/docker-rss-to-telegram/workflows/Create%20and%20publish%20Docker%20image/badge.svg)](https://github.com/MrDrache333/docker-rss-to-telegram/actions?query=workflow:"Create+and+publish+Docker+image")
[![GitHub release](https://img.shields.io/github/release/MrDrache333/docker-rss-to-telegram?include_prereleases=&sort=semver&color=blue)](https://github.com/MrDrache333/docker-rss-to-telegram/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)
[![issues - docker-unhealthy-autorestart](https://img.shields.io/github/issues/MrDrache333/docker-rss-to-telegram)](https://github.com/MrDrache333/docker-rss-to-telegram/issues)

This repository contains a Python script that fetches an RSS feed and sends the new items to a Telegram chat. The script
is intended to be run inside a Docker container.

## Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Installation

Replace `BOT_API_TOKEN` with the API key for your Telegram bot and `YOUR_CHAT_ID` with the ID of the Telegram chat to
send notifications to. You also need to provide a valid RSS-Feed-URL

To start the container, run the following command:

```
docker-compose up -d
```

This will pull the ghcr.io/mrdrache333/docker-rss-to-telegram image from GitHubs Container-Registry and start the
container in the background. The
script will run automatically when the container starts, and it will continue running in the background until the
container is stopped.
