### Act 1 - The attack

#### `read_logs` - Read the traffic logs

Every single request carries the same User-Agent: 'GregBot/1.0'. Greg is your friend. Greg is a sysadmin. Greg has a sense of humor. Or does he?

gives: Log excerpt

Choices:

- **Block that User-Agent** -> `block_ua`
- **Call Greg. Right now.** -> `call_greg`
- **Close all open ports on the router** -> `close_ports`

#### `block_ua` - Block the User-Agent

One line in the reverse proxy config. The traffic drops for exactly three seconds, then returns with a new User-Agent: 'GregBot/1.1'. Someone is mocking you.

Choices:

- **Check who is connected to the router** -> `check_dhcp`
- **Close all open ports on the router** -> `close_ports`

#### `call_greg` - Call Greg

Greg picks up on the ninth ring. 'It is 3 a.m. This better be a death.' You explain. He yawns. 'Turn it off and on again. I am going back to sleep.'

Choices:

- **Follow his advice: pull the plug** -> `remove_internet`
- **Read him the log lines** -> `greg_logs` *(needs: Log excerpt)*
- **Hang up and close the ports** -> `close_ports`

#### `greg_logs` - Greg wakes up

Silence. Then: 'That is NOT my bot. Check your IoT junk, this looks like a Mirai variant.' He sounds fully awake now, and slightly offended.

Choices:

- **Check who is connected to the router** -> `check_dhcp`
- **Ask why he knows so much about this** -> `accuse_greg`
- **Close all open ports on the router** -> `close_ports`

#### `accuse_greg` - Accuse Greg

'You think I would DDoS my own friend?!' Greg hangs up. Your phone shows one missed call from him and zero chances of more help tonight. You feel a little bad.

Choices:

- **Check who is connected to the router** -> `check_dhcp`
- **Close all open ports on the router** -> `close_ports`

#### `check_dhcp` - The DHCP list

Fourteen devices: laptop, phone, TV, the cat feeder, the smart fridge, and one host called 'unknown-7f3a' that you have never seen in your life.

Choices:

- **Unplug the smart fridge** -> `fridge`
- **Block unknown-7f3a** -> `block_host`
- **Check the server room camera** -> `cat_cam`
- **Close all open ports on the router** -> `close_ports`

#### `fridge` - Unplug the fridge

The fridge was running firmware from 2014 and was indeed part of a botnet, but a very small part. The attack does not even notice. Your ice cream begins to melt for nothing.

Choices:

- **Block unknown-7f3a** -> `block_host`
- **Close all open ports on the router** -> `close_ports`

#### `block_host` - Block unknown-7f3a

Blocked. A second later 'unknown-7f3b' appears. Then 7f3c. New hosts keep spawning, and they are not coming from the Internet. They are coming from inside your server.

Choices:

- **Close all open ports on the router** -> `close_ports`
- **Pull the Internet cable** -> `remove_internet`

#### `cat_cam` - Server room camera

On the feed: Pixel the cat, asleep on top of the server, one paw on the keyboard. Suspicious, but she has been there since 2 a.m. and has an alibi: she is a cat.

Choices:

- **Back to the DHCP list** -> `check_dhcp`
- **Close all open ports on the router** -> `close_ports`

#### `desk_search` - Search the desk

Under three tangled chargers you find a USB stick labelled 'RESCUE - tested never'. Past you was either a genius or an optimist. Behind it, a sticky note: 'check the attic'.

gives: USB rescue stick

Choices:

- **Climb up to the attic** -> `attic`
- **Go back to the server room** -> `logic_bomb`

#### `attic` - The attic

Dust, a plastic Christmas tree and a shoebox. Inside: a laminated card in your handwriting. 'OFFSITE BACKUP KEY - bucket homelab-bkp'. You had completely forgotten that you made one.

gives: Backup key

Choices:

- **Go back to the server room** -> `logic_bomb`

#### `neighbor_wifi` - Mrs. Nagy's Wi-Fi

Mrs. Nagy opens the door in a dressing gown, holding a rolling pin. After a lecture about what time it is, she gives you the password: 'macska1234'. Her router is, somehow, very secure.

Choices:

- **Download a rescue ISO and flash a USB stick** -> `flash_usb`
- **Thank her and go home** -> `no_internet`

#### `flash_usb` - Flash a rescue USB

At her kitchen table you download the ISO and flash it while Mrs. Nagy watches you like a hawk. Twenty minutes and one cookie later, you hold a bootable stick.

gives: USB rescue stick

Choices:

- **Go home and check the server** -> `logic_bomb`

#### `logic_bomb` - 3:33 a.m.

A cron job nobody wrote wakes up. Every fan on the rack changes pitch, the console fills with red text, and /boot disappears. The DDoS was only a smokescreen: the real attack was already inside.

Choices:

- **Open the console** -> `kernel_deleted`

#### `firewall_logs` - Firewall logs

Between thousands of junk requests hides a single successful SSH login at 02:41, using a key you did not create.

Choices:

- **Check the authorized_keys file** -> `authkeys`
- **Check the server console** -> `kernel_deleted`

#### `authkeys` - authorized_keys

Three keys. Yours. 'greg@old-laptop' from 2021. And one with the comment 'backup@localhost', added at 02:41 tonight.

Choices:

- **Remove the strange key** -> `remove_key`
- **Call Greg about his old key** -> `accuse_greg`
- **Check the server console** -> `kernel_deleted`

#### `remove_key` - Remove the key

You delete the key. The terminal answers: 'Connection closed by remote host.' He was already using something else, something much deeper than SSH.

Choices:

- **Check the server console** -> `kernel_deleted`

#### `greg_kernel` - Greg, again

Greg answers on the first ring. Grumpy, but he cannot resist a broken kernel. 'Do NOT paste random commands. Boot a live USB, chroot in, reinstall from the package cache. Like a civilized person.'

Choices:

- **Boot the rescue USB** -> `rescue_usb` *(needs: USB rescue stick)*
- **Admit you have no USB stick** -> `no_usb`
- **Ignore Greg and ask Reddit** -> `ask_reddit`

#### `no_usb` - No USB stick

'Then make one,' says Greg. 'You need a laptop, an ISO and a connection. Phone hotspot will do.' He hangs up to go back to bed. Again.

Choices:

- **Tether your phone and flash a stick** -> `flash_usb_home`
- **Ask the AI instead** -> `ask_ai`

#### `flash_usb_home` - Flash a rescue USB

The phone hotspot crawls, the ISO downloads, the progress bar lies about its percentage. Eventually you hold a bootable stick with a freshly written 'RESCUE' label.

gives: USB rescue stick

Choices:

- **Boot the rescue USB** -> `rescue_usb`

#### `arch_wiki` - The Arch wiki

Three hours of reading compressed into twelve minutes. Verdict: you need a live USB, a chroot and patience. It also says, in bold, not to run commands you do not understand.

Choices:

- **Boot the rescue USB** -> `rescue_usb` *(needs: USB rescue stick)*
- **No USB. Make one** -> `flash_usb_home`
- **Ignore the bold text, ask an AI** -> `ask_ai`

#### `reddit_comments` - The other comments

The top comment, from a moderator: 'Boot a live USB. Never paste scripts from strangers.' Kev's reply was posted forty seconds after you. Nobody diagnoses a kernel in forty seconds. Unless they already knew.

gives: Kev's handle

Choices:

- **Run Kev's script anyway** -> `unknown_event`
- **Boot the rescue USB** -> `rescue_usb` *(needs: USB rescue stick)*
- **Make a rescue USB** -> `flash_usb_home`

#### `check_changes` - Inspect the damage

The AI built a kernel for the wrong CPU architecture, set the root password to 'password' 'for convenience' and disabled the firewall 'to avoid conflicts'. Impressive, honestly.

Choices:

- **Reboot and hope for the best** -> `panic_loop`
- **Ask the AI to fix its own mistake** -> `ai_followup`
- **Boot the rescue USB** -> `rescue_usb` *(needs: USB rescue stick)*

#### `panic_loop` - Kernel panic

The machine boots, panics, reboots, panics. A loop. The fans spin up and down like a broken ventilator. Each cycle takes forty seconds, and your patience takes forty seconds less.

Choices:

- **Pull the plug and rethink** -> `kernel_deleted`
- **Boot the rescue USB** -> `rescue_usb` *(needs: USB rescue stick)*
- **Rage-quit the whole hobby** -> `ending_touch_grass`

#### `ai_followup` - The AI apologizes

'You are absolutely right, and I apologize!' it says, then offers a cleaner solution: 'rm -rf /boot /etc /var' followed by a fresh install. It sounds extremely confident.

Choices:

- **Run it. It sounds confident** -> `ai_wipe`
- **Check the Arch wiki instead** -> `arch_wiki`

#### `ai_wipe` - Run the command

The terminal scrolls for a very long time. Then it stops. Then the terminal itself disappears, because the thing that was running it no longer exists.

Choices:

- **Look at what is left** -> `ending_bricked`

#### `phone_dm` - A new message

One new DM from kev_the_kernel: 'thx for the root password lol. have fun rebuilding'. He deletes the message while you are still reading it.

gives: Kev's handle

Choices:

- **Hit the physical power button to restart** -> `restart`

### Act 3A - The rescue USB (clean system)

#### `rescue_usb` - The rescue USB

The stick boots on the first try, which feels like a personal gift from past you. A live shell, a blinking cursor, and your dead disks waiting to be mounted.

drops: Ai answer, random guy from reddit

Choices:

- **Mount, chroot and reinstall the kernel** -> `kernel_ok`

#### `kernel_ok` - Kernel reinstalled

The package cache comes through. A fresh kernel sits in /boot again. Before rebooting, you notice the disk still has other surprises hiding in it.

Choices:

- **Scan the disk for hidden tools** -> `scan_backdoor`
- **Reboot right now** -> `reboot_risky`

#### `reboot_risky` - Reboot right now

The system boots. Twenty minutes later the logic bomb you did not remove fires a second time and the kernel vanishes again. At least the rescue stick is still warm.

Choices:

- **Open the console** -> `kernel_deleted`

#### `scan_backdoor` - Hidden tools

Hidden in /etc and /usr/lib: a logic-bomb cron job, a rogue SSH key and a text file called README_KEV.txt: 'gg ez - kev_the_kernel'. Whoever he is, he is proud of it.

gives: Kev's handle

Choices:

- **Document it, delete it and reboot** -> `clean_boot`

#### `clean_boot` - A clean boot

The BIOS splash, then the login prompt. No red text, no strange kernel modules. Services start one by one, politely, like a system with nothing to hide.

drops: USB rescue stick

Choices:

- **Check the container status** -> `clean_hub`

#### `clean_hub` - Clean slate

The system is clean, finally. SSH works, the OS is healthy. But Docker is empty: no containers, no databases, no media server. You have a clean slate and a very long list.

Choices:

- **Check the backups** -> `backups_clean`
- **Rebuild from your compose files** -> `github_mirror`
- **Hunt for the attacker** -> `hunt_kev`
- **Harden the lab** -> `harden`
- **Call Greg to come over** -> `greg_arrives`

#### `greg_arrives` - Greg arrives

Twenty minutes later Greg is at your door with two coffees, a spare SSD and a look that says 'I told you so'. He has also forgiven you for anything you said earlier.

Choices:

- **Let him help with the backups** -> `backups_clean`
- **Let him help you hunt the attacker** -> `hunt_kev`
- **Send him home and keep going** -> `clean_hub`

#### `harden` - Harden the lab

Key-only SSH. fail2ban. Automatic updates. You feel the smug satisfaction of locking the door after the burglar has already left, and you enjoy every second of it.

Choices:

- **Move the IoT junk to its own VLAN** -> `vlan_iot`
- **Back to the lab** -> `clean_hub`

#### `vlan_iot` - The IoT VLAN

The smart fridge, the TV and the cat feeder are moved into a room with no windows and no keys. The fridge is not happy about it, but then again, it never was.

Choices:

- **Back to the lab** -> `clean_hub`

#### `backups_clean` - The local backups

Your NAS holds years of backups. All encrypted, with a note: 'Send 0.5 BTC for the key. You have 24 hours.' The offsite bucket was untouched, if you can unlock it.

Choices:

- **Decrypt the offsite backup** -> `offsite_clean_restore` *(needs: Backup key)*
- **Search the attic for the key** -> `attic_clean`
- **Pay the ransom** -> `pay_ransom_b`
- **Back to the lab** -> `clean_hub`

#### `attic_clean` - The attic

Same attic, same dust, same plastic tree. A laminated card: 'OFFSITE BACKUP KEY'. You promise to buy past you a coffee.

gives: Backup key

Choices:

- **Back to the backups** -> `backups_clean`

#### `pay_ransom_b` - Pay the ransom

The wallet is open again. You know this system is clean, which makes paying even sillier. Your finger hovers anyway.

Choices:

- **Send the payment** -> `ending_paid`
- **Close the wallet** -> `backups_clean`

#### `traces` - Traces

In /root: README_KEV.txt. 'gg ez. i was never here. - kev_the_kernel'. Next to it a hidden cron job, an unknown kernel module and a very smug piece of ASCII-art cat.

gives: Kev's handle

Choices:

- **Check the backups** -> `backups`
- **Run a rootkit scanner** -> `rkhunter`
- **Back to the container status** -> `containers_down`

#### `rkhunter` - Rootkit scanner

The scanner takes forever, then prints one word in red: INFECTED. The kernel from the Reddit script carries a backdoor, and so does half of /usr/bin. Nothing on this machine can be trusted.

Choices:

- **Wipe the server and reinstall** -> `clean_install`
- **Check the backups** -> `backups`
- **Back to the container status** -> `containers_down`

#### `backups` - The local backups

Your NAS holds years of backups. All encrypted, with a note: 'Send 0.5 BTC for the key. You have 24 hours.' The offsite bucket is a different story, if you can unlock it.

Choices:

- **Pay the ransom** -> `pay_ransom`
- **Search for the offsite backup key** -> `attic_late`
- **Decrypt the offsite backup** -> `offsite_restore` *(needs: Backup key)*
- **Back to the container status** -> `containers_down`

#### `pay_ransom` - Pay the ransom

The wallet is open. 0.5 BTC is more than the server cost. Your finger hovers over the button. In your head Greg says: 'Never pay.'

Choices:

- **Send the payment** -> `ending_paid`
- **Close the wallet** -> `backups`

#### `attic_late` - The attic

Dust, a plastic Christmas tree and a shoebox. Inside, a laminated card in your handwriting: 'OFFSITE BACKUP KEY - bucket homelab-bkp'. Past you really was a genius.

gives: Backup key

Choices:

- **Go back to the backups** -> `backups`

#### `offsite_restore` - Decrypt the offsite backup

The key works. The bucket holds your data from last Tuesday: photos, databases, the media library. But the server in front of you is running a kernel that Kev wrote.

Choices:

- **Restore onto this server right now** -> `restore_infected`
- **Wipe the server, then restore** -> `clean_install`

#### `restore_infected` - Restore onto the infected server

Eight hours later every file is back. You sleep like a baby. At 3 a.m. your phone buzzes: everything is encrypted again. The backdoor was just waiting for fresh data.

Choices:

- **Wipe and reinstall for real** -> `clean_install`
- **Throw the server out of the window** -> `ending_touch_grass`

#### `compose_git` - Rebuild from compose files

Your compose files lived in a Git repo. On this server. You stare at the empty disk and a cold realization settles in. Also, this server is still full of Kev.

Choices:

- **Wipe the server and start fresh** -> `clean_install`
- **Rebuild right here, right now** -> `rebuild_infected`

#### `rebuild_infected` - Rebuild on the infected host

The containers come up one by one. So does Kev's backdoor, now with a front-row seat to your brand-new database passwords. At dawn every service is sending spam to the entire Internet.

Choices:

- **Wipe and reinstall for real** -> `clean_install`
- **Pull the plug and walk away** -> `ending_touch_grass`

### Act 4 - Recovery

#### `clean_install` - Wipe and reinstall

You boot an installer, delete every partition and watch a clean OS go on. The backdoor is gone. So is everything else, until you bring it back.

Choices:

- **Restore the offsite backup** -> `offsite_clean_restore` *(needs: Backup key)*
- **Rebuild from the GitHub mirror** -> `github_mirror`
- **Rebuild by hand, from memory** -> `rebuild_by_hand`

#### `offsite_clean_restore` - Restore the offsite backup

On a clean system the bucket finally gives up your data from last Tuesday. Photos, databases, the media library, byte by byte. It takes hours. It is the best hours of your week.

gives: Restored data | drops: Backup key

Choices:

- **Verify the checksums** -> `backup_verify`
- **Start the containers right away** -> `containers_up`

#### `containers_up` - Start the containers

docker compose up -d. Pi-hole, Jellyfin and Vaultwarden greet you like old friends. Three containers refuse to start because their images disappeared. You decide to check the data anyway.

Choices:

- **Verify the checksums** -> `backup_verify`

#### `backup_verify` - Checksums match

Every checksum matches. For the first time tonight something is exactly as it should be. But somewhere out there, kev_the_kernel is still laughing.

Choices:

- **Hunt for the attacker** -> `hunt_kev`
- **Harden the lab** -> `harden`

#### `github_mirror` - The GitHub mirror

Three months ago you mirrored the repo to GitHub 'just in case'. The compose files are there. The data is not. Rebuilding means starting every service empty.

Choices:

- **Rebuild every service from the mirror** -> `rebuild_services`
- **See if any data survived** -> `survivors`

#### `survivors` - Survivors

On an old laptop and the attic Raspberry Pi you find 2019 photos, a database dump from March and half the media library. It is not much, but it is yours.

Choices:

- **Rebuild every service** -> `rebuild_services`

#### `rebuild_by_hand` - Rebuild by hand

You rebuild from memory. You forget three passwords, two port numbers and why Nextcloud needed that one weird cron job. After six hours half the services work.

Choices:

- **Keep going until it all works** -> `rebuild_services`
- **Pull the plug on this madness** -> `ending_touch_grass`

#### `rebuild_services` - Rebuild the services

One by one the green lights appear: Jellyfin, Nextcloud, the databases. Empty, but alive. The dashboards look beautiful and hollow, like a brand new apartment.

Choices:

- **Set up proper, tested backups** -> `new_backups`
- **Hunt for the attacker first** -> `hunt_kev`

#### `new_backups` - 3-2-1 and a test

Three copies. Two kinds of media. One offsite. And, for the first time in your life, an actual restore test. Past you would be proud. Future you will be grateful.

Choices:

- **Close the laptop. It is morning** -> `ending_phoenix`
- **Not done: find who did this** -> `hunt_kev`

### Act 5 - The detective part

#### `hunt_kev` - Hunt for the attacker

You have a README file, a forum name and a lot of anger. You open a terminal and a browser, and start digging.

Choices:

- **Search for the username** -> `whois_kev` *(needs: Kev's handle)*
- **Look through his connection logs** -> `kev_logs`
- **Set a honeypot** -> `honeypot_setup`

#### `kev_logs` - Connection logs

He came through three proxies and a Tor exit node. Professional? Or just someone who follows tutorials very carefully?

Choices:

- **Set a honeypot** -> `honeypot_setup`
- **Back to the investigation** -> `hunt_kev`

#### `whois_kev` - Who is kev_the_kernel?

The username shows up on a forum, a game server and a school coding club page. His avatar is a cat in sunglasses. His latest post: 'anyone know how to bypass a firewall? asking for homework'.

drops: Kev's handle

Choices:

- **Set a honeypot to catch him** -> `honeypot_setup`
- **Send him a message** -> `dm_kev`
- **Report the username** -> `report_kev`

#### `honeypot_setup` - Set a honeypot

You leave a fake server with a fake SSH door 'accidentally' open, full of files named passwords_final_v2.xlsx. Now you wait.

drops: Kev's handle

Choices:

- **Wait for Kev** -> `kev_returns`

#### `kev_returns` - Kev returns

At 5:12 a.m. the honeypot lights up. Someone logs in and starts exploring. He types very slowly. 'ls'. 'cd'. 'ls' again. He seems nervous.

Choices:

- **Trace the connection** -> `trace_kev`
- **Open a chat window in his terminal** -> `dm_kev`
- **Hack him back** -> `counter_hack`

#### `trace_kev` - Trace the connection

Behind the proxies: a residential IP, then a student account at a school in the next county. Kev is, at the very most, sixteen years old.

Choices:

- **Send him a message** -> `dm_kev`
- **Report him to the police** -> `report_kev`
- **Hack him back** -> `counter_hack`

#### `dm_kev` - Talk to Kev

You type: 'Hi Kev. We need to talk.' A long pause. Then: 'omg pls dont call my mom'. He sounds exactly as scared as a sixteen-year-old should.

Choices:

- **Offer him a deal** -> `kev_deal`
- **Tell him you are calling the police** -> `report_kev`

#### `kev_deal` - The deal

You offer: help rebuild and harden the lab, write a full report on how he got in, and apologize to Greg. In exchange: no police, no mom. He says yes in under two seconds.

Choices:

- **Shake on it** -> `ending_redemption`

#### `report_kev` - Report Kev

You write a thorough report: logs, timestamps, the README, the Reddit thread. The officer reads it twice, sips her coffee and says: 'Wow. Please do not hack anyone back.'

Choices:

- **Hand over the evidence at the station** -> `police_station`

#### `police_station` - At the police station

A detective with a tired face takes your USB stick full of logs. 'We will be in touch,' she says. 'And your data? Is it safe?'

Choices:

- **Tell her it is fully restored** -> `ending_full_recovery` *(needs: Restored data)*
- **Tell her honestly: a fifth is gone** -> `ending_justice`

#### `counter_hack` - Hack him back

You fire a stress-testing tool at his IP. It feels incredible for eleven seconds. Then you notice the IP belongs to a shared school router.

Choices:

- **Keep going. He deserves it** -> `ending_counterhack`
- **Stop. Think** -> `hunt_kev`

### Endings

#### `ending_full_recovery` - Full Recovery

Your lab is back, your data is back, and Kev's case sits in a folder somewhere in the county. You set up alerting, expire Greg's old key and hang a sign over the rack: 'THE RESCUE USB IS NOT DECORATION.' Pixel sleeps on the server again.

**Ending (SUCCESS)** | reset inventory on leaving

Choices:

- **Play again** -> `start`

#### `ending_phoenix` - Phoenix

The photos are gone, the databases are gone. But the compose files are alive, the lab is new, and for the first time you have real backups. Starting over is the oldest homelab tradition there is.

**Ending (SUCCESS)** | reset inventory on leaving

Choices:

- **Play again** -> `start`

#### `ending_redemption` - Redemption Arc

Kev writes a forty-page report, fixes every hole he used, and now maintains your lab on weekends. Greg gets a public apology. The fridge lives on a VLAN. Everyone is safer, a bit embarrassed and strangely proud.

**Ending (SUCCESS)** | reset inventory on leaving

Choices:

- **Play again** -> `start`

#### `ending_justice` - Justice, With Gaps

Kev gets a stern talk from a very tired detective. Your lab recovers, with a fifth of its memories missing. You learn to love the numbers 3-2-1, and you never forget them again.

**Ending (SUCCESS)** | reset inventory on leaving

Choices:

- **Play again** -> `start`

#### `ending_bricked` - Bricked

Nothing boots. Nothing mounts. Your disks hold a very organized pile of zeros. The AI would like to apologize again, but its server is not your server.

**Ending (FAIL)** | reset inventory on leaving

Choices:

- **Play again** -> `start`

#### `ending_paid` - Paid and Played

The payment goes through. Nothing happens. Then a second note appears: 'Thanks! The price is now 1.0 BTC.' You are poorer, the data is still encrypted, and Kev has a new gaming PC.

**Ending (FAIL)** | reset inventory on leaving

Choices:

- **Play again** -> `start`

#### `ending_touch_grass` - Touch Grass

You unplug everything. The silence is wonderful. You sell the rack, buy a plant and discover that sunlight exists. You do not miss the 3 a.m. alerts. You do, slightly, miss the lab.

**Ending (FAIL)** | reset inventory on leaving

Choices:

- **Play again** -> `start`

#### `ending_counterhack` - The Wrong Tool

You took down a school network three days before exams. Kev gets a warning. You get a very serious letter from a lawyer. Greg offers to be a character witness. It is not enough.

**Ending (FAIL)** | reset inventory on leaving

Choices:

- **Play again** -> `start`