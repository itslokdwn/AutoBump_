 Discord Auto-Bump Bot

A Discord bot that automatically sends the /bump command in a specified channel every specified amount of time in seconds. Built using discord.py and hosted on Railway.app.

## Requirements

- Python 3.8 or higher
- discord.py library
- A Discord bot token
- A Discord server with admin permissions
- A Railway.app account (for hosting)

## Setup Instructions

### 1. Discord Developer Portal Setup
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Go to the "Bot" section
4. Click "Add Bot"
5. Enable these Privileged Gateway Intents:
   - Presence Intent
   - Server Members Intent
   - Message Content Intent
6. Copy the bot token (you'll need this later)

### 2. Get Your Channel ID
1. Enable Developer Mode in Discord:
   - User Settings → App Settings → Advanced
2. Right-click the channel where you want bumps
3. Click "Copy ID"

### 3. Files Required
- `main.py`: Main bot code
- `requirements.txt`: Dependencies list
- `.gitignore`: (optional) For git version control

### 4. Railway.app Deployment
1. Create a GitHub repository
2. Upload your bot files
3. Connect to Railway
4. Add environment variables:
   - `DISCORD_TOKEN`: Your bot token
   - `CHANNEL_ID`: Your channel ID

## Features
- Automatic bumping every 2 hours
- Simple status check command (!ping)
- Error handling for failed bumps
- Console logging of bump activities

## Commands
- `!ping`: Checks if bot is running

## Maintenance
- Monitor Railway.app dashboard for any issues
- Check Discord Developer Portal for bot status
- Reset bot token if compromised

## Troubleshooting
1. Bot not responding:
   - Check Railway logs
   - Verify environment variables
   - Confirm bot has correct permissions

2. Bump command failing:
   - Verify channel ID
   - Check bot permissions in the channel
   - Ensure bot has message send permissions

## Security Notes
- Never share your bot token
- Keep repository private if including sensitive info
- Regularly check Railway dashboard for unusual activity

## Dependencies
- discord.py==2.4.0
- Python 3.8+
- Railway.app for hosting

## Hosting Requirements
Railway.app free tier provides:
- 500 hours per month
- 512MB RAM
- Automatic deployments
