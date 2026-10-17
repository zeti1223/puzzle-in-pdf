# Homelab Detective - the full story

*An interactive detective game (choose-your-own-adventure), written for a clickable PDF.*

It is 3 a.m. Your phone buzzes on the nightstand: an alert from your homelab. Something is very wrong. Every choice you make leads somewhere else, and some doors only open if you are carrying the right item.

This file contains **the whole story**: every scene, every choice and every ending. Links like [Start](#start) jump to the scene they point to.

**Size:** 133 scenes, 12 endings (6 successes, 6 failures: see the list at the end).

## Rules of the game

1. This is a detective game played entirely inside this PDF. Click the blue buttons to make your choices and move between pages.
2. Your inventory is shown at the top of every page. Some choices are greyed out until you are carrying the right item.
3. Page numbers are shuffled, so flipping ahead will not help you. Use the buttons, not the scroll bar.
4. There are 12 different endings. Some are triumphant. Some are educational.

## Items

| Item | Picked up at | Needed at |
|---|---|---|
| Ai answer | [Ask an AI](#ask_ai) | [Something happened](#unknown_event) |
| Backup key | [The attic](#attic), [The attic](#attic_clean), [The attic](#attic_late) | [The local backups](#backups), [The local backups](#backups_clean), [Wipe and reinstall](#clean_install) |
| Kev's handle | [A new message](#phone_dm), [The other comments](#reddit_comments), [Hidden tools](#scan_backdoor), [Traces](#traces) | [Hunt for the attacker](#hunt_kev) |
| Log excerpt | [Read the traffic logs](#read_logs) | [Call Greg](#call_greg) |
| Restored data | [Restore the offsite backup](#offsite_clean_restore) | [At the police station](#police_station) |
| USB rescue stick | [Search the desk](#desk_search), [Flash a rescue USB](#flash_usb), [Flash a rescue USB](#flash_usb_home) | [A second opinion](#ai_review), [The Arch wiki](#arch_wiki), [Inspect the damage](#check_changes), [Greg, again](#greg_kernel), [Kernel deleted](#kernel_deleted), [Kernel panic](#panic_loop), [The other comments](#reddit_comments), [A 47-minute tutorial](#youtube_tutorial) |
| random guy from reddit | [Ask Reddit](#ask_reddit) | [Something happened](#unknown_event) |

## Contents

- Act I - The 3 a.m. alert (18 scenes)
- Act II - Cut it off or lock it down (17 scenes)
- Act III - The deleted kernel (19 scenes)
- Act IV - The rescue USB (9 scenes)
- Act V - A clean system (11 scenes)
- Act VI - The infected server (11 scenes)
- Act VII - Wipe, restore, rebuild (12 scenes)
- Act VIII - The hunt for the attacker (24 scenes)
- The endings (12 scenes)

---

## Act I - The 3 a.m. alert

*The first minutes: panic, logs, and a lot of suspicious devices.*

<a id="start"></a>
### Start

It is 3 a.m. Your phone buzzes on the nightstand: an alert from your homelab. Something is very wrong.

- Open the dashboard -> [Homelab DDoS](#ddos)

<a id="ddos"></a>
### Homelab DDoS

Traffic graphs are through the roof. Thousands of requests per second are hammering your homelab. The router fans are screaming. You have to act now.

- Remove the Internet connection -> [Remove Internet connection](#remove_internet)
- Close all open ports on the router -> [Close all open ports on router](#close_ports)
- Read the traffic logs first -> [Read the traffic logs](#read_logs)
- Call Greg, your sysadmin friend -> [Call Greg](#call_greg)
- Go back to sleep -> [Five more minutes](#oversleep)

<a id="oversleep"></a>
### Five more minutes

You read the alert, decide it is probably the cat on the keyboard again, and put the phone face down. The nightstand glows with a second notification, then a third. The pillow is very soft.

- Sleep -> [Snoozed](#ending_oversleep)
- Fine. Open the dashboard -> [Homelab DDoS](#ddos)

<a id="read_logs"></a>
### Read the traffic logs

Every single request carries the same User-Agent: 'GregBot/1.0'. Greg is your friend. Greg is a sysadmin. Greg has a sense of humor. Or does he?

> Picked up: **Log excerpt**

- Block that User-Agent -> [Block the User-Agent](#block_ua)
- Call Greg. Right now. -> [Call Greg](#call_greg)
- Check the Pi-hole DNS log -> [Pi-hole query log](#pihole_log)
- Close all open ports on the router -> [Close all open ports on router](#close_ports)

<a id="pihole_log"></a>
### Pi-hole query log

Pi-hole shows 40,000 lookups for 'cdn-update.gregbot.lol' in ten minutes. The domain was registered yesterday. Blocking it would feel great, if the attack used DNS at all.

- Block the domain anyway -> [Block the domain](#block_domain)
- Back to the traffic logs -> [Read the traffic logs](#read_logs)
- Close all open ports on the router -> [Close all open ports on router](#close_ports)

<a id="block_domain"></a>
### Block the domain

One click. The graph does not even flinch: the bots talk to raw IP addresses, and the domain was only there to look scary. Somewhere, a script kiddie is giggling.

- Check who is connected to the router -> [The DHCP list](#check_dhcp)
- Close all open ports on the router -> [Close all open ports on router](#close_ports)

<a id="block_ua"></a>
### Block the User-Agent

One line in the reverse proxy config. The traffic drops for exactly three seconds, then returns with a new User-Agent: 'GregBot/1.1'. Someone is mocking you.

- Check who is connected to the router -> [The DHCP list](#check_dhcp)
- Close all open ports on the router -> [Close all open ports on router](#close_ports)

<a id="call_greg"></a>
### Call Greg

Greg picks up on the ninth ring. 'It is 3 a.m. This better be a death.' You explain. He yawns. 'Turn it off and on again. I am going back to sleep.'

- Follow his advice: pull the plug -> [Remove Internet connection](#remove_internet)
- Read him the log lines -> [Greg wakes up](#greg_logs) *(requires: Log excerpt)*
- Hang up and close the ports -> [Close all open ports on router](#close_ports)

<a id="greg_logs"></a>
### Greg wakes up

Silence. Then: 'That is NOT my bot. Check your IoT junk, this looks like a Mirai variant.' He sounds fully awake now, and slightly offended.

- Check who is connected to the router -> [The DHCP list](#check_dhcp)
- Ask why he knows so much about this -> [Accuse Greg](#accuse_greg)
- Close all open ports on the router -> [Close all open ports on router](#close_ports)

<a id="accuse_greg"></a>
### Accuse Greg

'You think I would DDoS my own friend?!' Greg hangs up. Your phone shows one missed call from him and zero chances of more help tonight. You feel a little bad.

- Check who is connected to the router -> [The DHCP list](#check_dhcp)
- Close all open ports on the router -> [Close all open ports on router](#close_ports)

<a id="check_dhcp"></a>
### The DHCP list

Fourteen devices: laptop, phone, TV, the cat feeder, the smart fridge, and one host called 'unknown-7f3a' that you have never seen in your life.

- Unplug the smart fridge -> [Unplug the fridge](#fridge)
- Block unknown-7f3a -> [Block unknown-7f3a](#block_host)
- Check the server room camera -> [Server room camera](#cat_cam)
- Open the Proxmox dashboard -> [Proxmox](#proxmox)
- Close all open ports on the router -> [Close all open ports on router](#close_ports)

<a id="proxmox"></a>
### Proxmox

Eleven VMs, and one you have forgotten: VM 104, 'test-DO-NOT-DELETE', uptime 411 days, CPU at 100 percent. You do not remember creating it. You do not remember anyone creating it.

- Shut down VM 104 -> [Shut down VM 104](#vm_stop)
- Open its console -> [VM 104 console](#vm_console)
- Back to the DHCP list -> [The DHCP list](#check_dhcp)

<a id="vm_stop"></a>
### Shut down VM 104

The VM powers off and the traffic graph drops by a third. Sixty seconds later a cron job on the host starts it again, as if nothing had happened. Interesting. Very interesting.

- Open its console -> [VM 104 console](#vm_console)
- Back to the DHCP list -> [The DHCP list](#check_dhcp)

<a id="vm_console"></a>
### VM 104 console

A bare shell. The bash history ends with 'nohup ./gregbot &'. Whoever wrote this has an unusual relationship with your friend, and a poor imagination.

- Back to Proxmox -> [Proxmox](#proxmox)
- Back to the DHCP list -> [The DHCP list](#check_dhcp)
- Close all open ports on the router -> [Close all open ports on router](#close_ports)

<a id="fridge"></a>
### Unplug the fridge

The fridge was running firmware from 2014 and was indeed part of a botnet, but a very small part. The attack does not even notice. Your ice cream begins to melt for nothing.

- Block unknown-7f3a -> [Block unknown-7f3a](#block_host)
- Close all open ports on the router -> [Close all open ports on router](#close_ports)

<a id="block_host"></a>
### Block unknown-7f3a

Blocked. A second later 'unknown-7f3b' appears. Then 7f3c. New hosts keep spawning, and they are not coming from the Internet. They are coming from inside your server.

- Close all open ports on the router -> [Close all open ports on router](#close_ports)
- Pull the Internet cable -> [Remove Internet connection](#remove_internet)

<a id="cat_cam"></a>
### Server room camera

On the feed: Pixel the cat, asleep on top of the server, one paw on the keyboard. Suspicious, but she has been there since 2 a.m. and has an alibi: she is a cat.

- Back to the DHCP list -> [The DHCP list](#check_dhcp)
- Zoom in on the keyboard -> [Zoom in on the keyboard](#pixel_zoom)
- Close all open ports on the router -> [Close all open ports on router](#close_ports)

<a id="pixel_zoom"></a>
### Zoom in on the keyboard

Pixel's paw rests on the Enter key. On the screen sits a half-typed command from last night: 'sudo rm -rf ./old_logs /'. Note the space before the slash. You have never been so grateful to a sleeping cat.

- Back to the camera -> [Server room camera](#cat_cam)
- Back to the DHCP list -> [The DHCP list](#check_dhcp)

## Act II - Cut it off or lock it down

*Pull the plug or close the ports; either way the attacker was already inside.*

<a id="remove_internet"></a>
### Remove Internet connection

You rip the ethernet cable out of the router. The blinking lights go quiet. But the attack was already writing to your disks when the link dropped.

> Lost: **Log excerpt**

- Check the damage -> [20% data loss](#data_loss_a)

<a id="close_ports"></a>
### Close all open ports on router

You log into the router and shut every forwarded port: SSH, HTTPS, the Jellyfin stream, everything. The router is quiet for a moment, then the logs start scrolling again.

> Lost: **Log excerpt**

- Check the damage -> [20% data loss](#data_loss_b)
- Check the server console -> [Kernel deleted](#kernel_deleted)
- Read the firewall logs -> [Firewall logs](#firewall_logs)

<a id="data_loss_a"></a>
### 20% data loss

A fifth of your files are gone or corrupted. The rest of the lab is cut off from the world.

- Stay offline and think -> [No internet](#no_internet)
- Plug the ethernet cable back in -> [Plug back ethernet](#plug_back)

<a id="data_loss_b"></a>
### 20% data loss

The ports are closed, but the attacker was already inside. A fifth of your files are gone or corrupted, and the system is acting strangely.

- Look at the system more closely -> [Kernel deleted](#kernel_deleted)
- Read the firewall logs -> [Firewall logs](#firewall_logs)

<a id="no_internet"></a>
### No internet

Silence. Without a connection you cannot look up fixes, ask for help or download anything. You are alone with the damage.

- Plug the ethernet cable back in -> [Plug back ethernet](#plug_back)
- Search your desk for anything useful -> [Search the desk](#desk_search)
- Knock on Mrs. Nagy's door for Wi-Fi -> [Mrs. Nagy's Wi-Fi](#neighbor_wifi)
- Walk to the 24h gas station -> [The 24h gas station](#gas_station)
- Wait for the sun to come up -> [3:33 a.m.](#logic_bomb)

<a id="desk_search"></a>
### Search the desk

Under three tangled chargers you find a USB stick labelled 'RESCUE - tested never'. Past you was either a genius or an optimist. Behind it, a sticky note: 'check the attic'.

> Picked up: **USB rescue stick**

- Climb up to the attic -> [The attic](#attic)
- Go back to the server room -> [3:33 a.m.](#logic_bomb)

<a id="attic"></a>
### The attic

Dust, a plastic Christmas tree and a shoebox. Inside: a laminated card in your handwriting. 'OFFSITE BACKUP KEY - bucket homelab-bkp'. You had completely forgotten that you made one.

> Picked up: **Backup key**

- Go back to the server room -> [3:33 a.m.](#logic_bomb)

<a id="neighbor_wifi"></a>
### Mrs. Nagy's Wi-Fi

Mrs. Nagy opens the door in a dressing gown, holding a rolling pin. After a lecture about what time it is, she gives you the password: 'macska1234'. Her router is, somehow, very secure.

- Download a rescue ISO and flash a USB stick -> [Flash a rescue USB](#flash_usb)
- Thank her and go home -> [No internet](#no_internet)

<a id="flash_usb"></a>
### Flash a rescue USB

At her kitchen table you download the ISO and flash it while Mrs. Nagy watches you like a hawk. Twenty minutes and one cookie later, you hold a bootable stick.

> Picked up: **USB rescue stick**

- Go home and check the server -> [3:33 a.m.](#logic_bomb)

<a id="gas_station"></a>
### The 24h gas station

Fluorescent lights, hot dogs rotating since Tuesday, and a teenager in a hoodie buying three energy drinks. The sticker on his laptop shows a cat in sunglasses. You buy a coffee that tastes like regret.

- Ask the teenager what he is working on -> ['Homework'](#teen_chat)
- Go home -> [No internet](#no_internet)

<a id="teen_chat"></a>
### 'Homework'

'Homework,' he says, far too quickly, and leaves without paying for the third drink. The cashier shrugs: 'Kids.' It is the middle of the night, and you have bigger problems.

- Go home -> [No internet](#no_internet)

<a id="plug_back"></a>
### Plug back ethernet

The link light turns green again. For a few seconds everything looks fine. Then the traffic graph spikes.

- Check the graphs -> [Still attacking](#still_attacking)

<a id="still_attacking"></a>
### Still attacking

The attack never stopped. Whoever is behind it is still hammering your lab, and the router is wide open again.

- Close all open ports on the router -> [Close all open ports on router](#close_ports)

<a id="firewall_logs"></a>
### Firewall logs

Between thousands of junk requests hides a single successful SSH login at 02:41, using a key you did not create.

- Check the authorized_keys file -> [authorized_keys](#authkeys)
- Check the server console -> [Kernel deleted](#kernel_deleted)

<a id="authkeys"></a>
### authorized_keys

Three keys. Yours. 'greg@old-laptop' from 2021. And one with the comment 'backup@localhost', added at 02:41 tonight.

- Remove the strange key -> [Remove the key](#remove_key)
- Call Greg about his old key -> [Accuse Greg](#accuse_greg)
- Check the server console -> [Kernel deleted](#kernel_deleted)

<a id="remove_key"></a>
### Remove the key

You delete the key. The terminal answers: 'Connection closed by remote host.' He was already using something else, something much deeper than SSH.

- Check the server console -> [Kernel deleted](#kernel_deleted)

<a id="logic_bomb"></a>
### 3:33 a.m.

A cron job nobody wrote wakes up. Every fan on the rack changes pitch, the console fills with red text, and /boot disappears. The DDoS was only a smokescreen: the real attack was already inside.

- Open the console -> [Kernel deleted](#kernel_deleted)

## Act III - The deleted kernel

*Who do you trust with a dead machine at 3:33 a.m.?*

<a id="kernel_deleted"></a>
### Kernel deleted

You open the console. The kernel has been deleted. The machine is still running from memory, but it will not survive a reboot. You need to get it back, and fast.

- Ask an AI how to recover the kernel -> [Ask an AI](#ask_ai)
- Ask Reddit how to recover the kernel -> [Ask Reddit](#ask_reddit)
- Boot the rescue USB -> [The rescue USB](#rescue_usb) *(requires: USB rescue stick)*
- Call Greg again -> [Greg, again](#greg_kernel)
- Search the Arch wiki on your phone -> [The Arch wiki](#arch_wiki)

<a id="greg_kernel"></a>
### Greg, again

Greg answers on the first ring. Grumpy, but he cannot resist a broken kernel. 'Do NOT paste random commands. Boot a live USB, chroot in, reinstall from the package cache. Like a civilized person.'

- Boot the rescue USB -> [The rescue USB](#rescue_usb) *(requires: USB rescue stick)*
- Admit you have no USB stick -> [No USB stick](#no_usb)
- Ignore Greg and ask Reddit -> [Ask Reddit](#ask_reddit)

<a id="no_usb"></a>
### No USB stick

'Then make one,' says Greg. 'You need a laptop, an ISO and a connection. Phone hotspot will do.' He hangs up to go back to bed. Again.

- Tether your phone and flash a stick -> [Flash a rescue USB](#flash_usb_home)
- Ask the AI instead -> [Ask an AI](#ask_ai)

<a id="flash_usb_home"></a>
### Flash a rescue USB

The phone hotspot crawls, the ISO downloads, the progress bar lies about its percentage. Eventually you hold a bootable stick with a freshly written 'RESCUE' label.

> Picked up: **USB rescue stick**

- Boot the rescue USB -> [The rescue USB](#rescue_usb)

<a id="arch_wiki"></a>
### The Arch wiki

Three hours of reading compressed into twelve minutes. Verdict: you need a live USB, a chroot and patience. It also says, in bold, not to run commands you do not understand.

- Boot the rescue USB -> [The rescue USB](#rescue_usb) *(requires: USB rescue stick)*
- No USB. Make one -> [Flash a rescue USB](#flash_usb_home)
- Watch a YouTube tutorial instead -> [A 47-minute tutorial](#youtube_tutorial)
- Ignore the bold text, ask an AI -> [Ask an AI](#ask_ai)

<a id="youtube_tutorial"></a>
### A 47-minute tutorial

Intro, sponsor segment, a second sponsor segment, 'before we begin, smash that like button'. The actual fix starts at 38:12: a live USB, a chroot and a reinstall. The top comment says the author never tested any of it.

- Boot the rescue USB -> [The rescue USB](#rescue_usb) *(requires: USB rescue stick)*
- Make a rescue USB -> [Flash a rescue USB](#flash_usb_home)
- Skip it and ask Reddit -> [Ask Reddit](#ask_reddit)

<a id="ask_ai"></a>
### Ask an AI

You paste the panic-induced error logs into an AI chatbot. It confidently outputs a multi-step kernel compilation and reinstallation command string. You copy-paste and execute it.

> Picked up: **Ai answer**

- See what happens -> [Something happened](#unknown_event)
- Read the answer line by line first -> [Read the answer first](#ai_read)

<a id="ai_read"></a>
### Read the answer first

You read the command line by line. Most of it looks plausible. Two parts do not: a download from a URL ending in '.ru/k.sh', and a flag you cannot find in any manual. The AI sounds exactly as confident as before.

- Run it anyway -> [Something happened](#unknown_event)
- Look up the strange flag on the Arch wiki -> [The Arch wiki](#arch_wiki)
- Ask a second AI to review it -> [A second opinion](#ai_review)

<a id="ai_review"></a>
### A second opinion

The second AI says the first AI is wrong. Then it says it is also wrong. Then it offers a third solution, with a bullet list and a warning in bold that is somehow even more confident.

- Run the third solution -> [Something happened](#unknown_event)
- Give up on AIs and make a rescue USB -> [Flash a rescue USB](#flash_usb_home)
- Boot the rescue USB -> [The rescue USB](#rescue_usb) *(requires: USB rescue stick)*

<a id="ask_reddit"></a>
### Ask Reddit

You post on r/homelab with the title: 'PLEASE HELP MY KERNEL IS DELETED'. Almost instantly a user called kev_the_kernel replies with a helpful-looking shell script.

> Picked up: **random guy from reddit**

- Execute the Reddit advice -> [Something happened](#unknown_event)
- Read the other comments first -> [The other comments](#reddit_comments)

<a id="reddit_comments"></a>
### The other comments

The top comment, from a moderator: 'Boot a live USB. Never paste scripts from strangers.' Kev's reply was posted forty seconds after you. Nobody diagnoses a kernel in forty seconds. Unless they already knew.

> Picked up: **Kev's handle**

- Run Kev's script anyway -> [Something happened](#unknown_event)
- Boot the rescue USB -> [The rescue USB](#rescue_usb) *(requires: USB rescue stick)*
- Make a rescue USB -> [Flash a rescue USB](#flash_usb_home)

<a id="unknown_event"></a>
### Something happened

The terminal flashes a cascade of cryptic messages. The screen freezes for a moment. You aren't entirely sure what just executed, but the system state has fundamentally shifted.

- Try to revert using the AI method -> [Kernel deleted](#kernel_deleted) *(requires: Ai answer)*
- Inspect what the AI command changed -> [Inspect the damage](#check_changes) *(requires: Ai answer)*
- Wait for the system response -> [Everything goes black](#blackout) *(requires: random guy from reddit)*

<a id="check_changes"></a>
### Inspect the damage

The AI built a kernel for the wrong CPU architecture, set the root password to 'password' 'for convenience' and disabled the firewall 'to avoid conflicts'. Impressive, honestly.

- Reboot and hope for the best -> [Kernel panic](#panic_loop)
- Ask the AI to fix its own mistake -> [The AI apologizes](#ai_followup)
- Boot the rescue USB -> [The rescue USB](#rescue_usb) *(requires: USB rescue stick)*

<a id="panic_loop"></a>
### Kernel panic

The machine boots, panics, reboots, panics. A loop. The fans spin up and down like a broken ventilator. Each cycle takes forty seconds, and your patience takes forty seconds less.

- Pull the plug and rethink -> [Kernel deleted](#kernel_deleted)
- Boot the rescue USB -> [The rescue USB](#rescue_usb) *(requires: USB rescue stick)*
- Rage-quit the whole hobby -> [Touch Grass](#ending_touch_grass)

<a id="ai_followup"></a>
### The AI apologizes

'You are absolutely right, and I apologize!' it says, then offers a cleaner solution: 'rm -rf /boot /etc /var' followed by a fresh install. It sounds extremely confident.

- Run it. It sounds confident -> [Run the command](#ai_wipe)
- Check the Arch wiki instead -> [The Arch wiki](#arch_wiki)

<a id="ai_wipe"></a>
### Run the command

The terminal scrolls for a very long time. Then it stops. Then the terminal itself disappears, because the thing that was running it no longer exists.

- Look at what is left -> [Bricked](#ending_bricked)

<a id="blackout"></a>
### Everything goes black

The monitors click off. The server chassis fans wind down to complete silence. Total darkness fills the room.

> *Your inventory is cleared when you leave this scene.*

- Hit the physical power button to restart -> [Restart](#restart)
- Wait in the dark -> [Everything goes black](#blackout)
- Check your phone -> [A new message](#phone_dm)

<a id="phone_dm"></a>
### A new message

One new DM from kev_the_kernel: 'thx for the root password lol. have fun rebuilding'. He deletes the message while you are still reading it.

> Picked up: **Kev's handle**

- Hit the physical power button to restart -> [Restart](#restart)

<a id="restart"></a>
### Restart

The BIOS splash screen appears. Services begin initializing one by one as the OS boots back up from disk.

- Check the container status -> [Containers offline](#containers_down)

## Act IV - The rescue USB

*The one proper way to fix it, and the traps around it.*

<a id="rescue_usb"></a>
### The rescue USB

The stick boots on the first try, which feels like a personal gift from past you. A live shell, a blinking cursor, and your dead disks waiting to be mounted.

> Lost: **Ai answer**
> Lost: **random guy from reddit**

- Unlock and mount the disks -> [Enter passphrase](#luks_prompt)

<a id="luks_prompt"></a>
### Enter passphrase

The root disk is encrypted. A prompt blinks: 'Enter passphrase for /dev/sda2'. The passphrase lives in Vaultwarden. Vaultwarden lives on the disk you are trying to unlock. Past you left no instructions, but present you is optimistic.

- Type the passphrase you always use -> [No key available](#luks_wrong)
- Look under the keyboard -> [The sticky note](#luks_ok)

<a id="luks_wrong"></a>
### No key available

'No key available with this passphrase.' You try the version with an exclamation mark. Then the version with a year. The prompt stays polite about it, which makes it worse.

- Try again -> [Enter passphrase](#luks_prompt)
- Look under the keyboard -> [The sticky note](#luks_ok)

<a id="luks_ok"></a>
### The sticky note

Under the keyboard, a yellow note in your handwriting: 'LUKS: correct horse battery staple 2'. Past you was lazy, but not stupid. The disk unlocks with a satisfied click.

- Chroot and reinstall the kernel -> [Kernel reinstalled](#kernel_ok)

<a id="kernel_ok"></a>
### Kernel reinstalled

The package cache comes through. A fresh kernel sits in /boot again. Before rebooting, you notice the disk still has other surprises hiding in it.

- Scan the disk for hidden tools -> [Hidden tools](#scan_backdoor)
- Verify the package signatures first -> [Package signatures](#sig_check)
- Reboot right now -> [Reboot right now](#reboot_risky)

<a id="sig_check"></a>
### Package signatures

Every signature is valid except one: a package 'updated' at 02:44 tonight, signed by nobody. You reinstall it from the official mirror and feel quietly brilliant.

- Scan the disk for hidden tools -> [Hidden tools](#scan_backdoor)
- Reboot right now -> [Reboot right now](#reboot_risky)

<a id="reboot_risky"></a>
### Reboot right now

The system boots. Twenty minutes later the logic bomb you did not remove fires a second time and the kernel vanishes again. At least the rescue stick is still warm.

- Open the console -> [Kernel deleted](#kernel_deleted)

<a id="scan_backdoor"></a>
### Hidden tools

Hidden in /etc and /usr/lib: a logic-bomb cron job, a rogue SSH key and a text file called README_KEV.txt: 'gg ez - kev_the_kernel'. Whoever he is, he is proud of it.

> Picked up: **Kev's handle**

- Document it, delete it and reboot -> [A clean boot](#clean_boot)

<a id="clean_boot"></a>
### A clean boot

The BIOS splash, then the login prompt. No red text, no strange kernel modules. Services start one by one, politely, like a system with nothing to hide.

> Lost: **USB rescue stick**

- Check the container status -> [Clean slate](#clean_hub)

## Act V - A clean system

*The machine is clean. Now what is left on it?*

<a id="clean_hub"></a>
### Clean slate

The system is clean, finally. SSH works, the OS is healthy. But Docker is empty: no containers, no databases, no media server. You have a clean slate and a very long list.

- Check the backups -> [The local backups](#backups_clean)
- Rebuild from your compose files -> [The GitHub mirror](#github_mirror)
- Hunt for the attacker -> [Hunt for the attacker](#hunt_kev)
- Harden the lab -> [Harden the lab](#harden)
- Call Greg to come over -> [Greg arrives](#greg_arrives)

<a id="greg_arrives"></a>
### Greg arrives

Twenty minutes later Greg is at your door with two coffees, a spare SSD and a look that says 'I told you so'. He has also forgiven you for anything you said earlier.

- Let him help with the backups -> [The local backups](#backups_clean)
- Let him help you hunt the attacker -> [Hunt for the attacker](#hunt_kev)
- Send him home and keep going -> [Clean slate](#clean_hub)

<a id="harden"></a>
### Harden the lab

Key-only SSH. fail2ban. Automatic updates. You feel the smug satisfaction of locking the door after the burglar has already left, and you enjoy every second of it.

- Move the IoT junk to its own VLAN -> [The IoT VLAN](#vlan_iot)
- Rotate every password -> [Rotate every password](#rotate_pw)
- Ask Mrs. Nagy for advice -> [Mrs. Nagy's advice](#nagy_advice)
- Set up real alerting -> [Alerts that alert](#alerting)
- Back to the lab -> [Clean slate](#clean_hub)

<a id="vlan_iot"></a>
### The IoT VLAN

The smart fridge, the TV and the cat feeder are moved into a room with no windows and no keys. The fridge is not happy about it, but then again, it never was.

- Back to the lab -> [Clean slate](#clean_hub)

<a id="rotate_pw"></a>
### Rotate every password

Two hundred fourteen accounts. By the 150th you stop using the generator and start typing keyboard patterns. The 215th, your own, is still 'Summer2019!'. You change it twice, out of shame.

- Back to hardening -> [Harden the lab](#harden)

<a id="nagy_advice"></a>
### Mrs. Nagy's advice

Mrs. Nagy puts down the rolling pin, pours you tea and explains network segmentation as if she had invented it. 'In 1994 I ran a university network with forty machines and no incidents.' She hands you a handwritten list of rules and a cookie.

- Back to hardening -> [Harden the lab](#harden)

<a id="alerting"></a>
### Alerts that alert

Uptime Kuma, ntfy and an actual escalation policy. At 3 a.m. your phone will buzz again, but now with a severity level and a link to a runbook. It is somehow worse, and somehow better.

- Back to hardening -> [Harden the lab](#harden)

<a id="backups_clean"></a>
### The local backups

Your NAS holds years of backups. All encrypted, with a note: 'Send 0.5 BTC for the key. You have 24 hours.' The offsite bucket was untouched, if you can unlock it.

- Decrypt the offsite backup -> [Restore the offsite backup](#offsite_clean_restore) *(requires: Backup key)*
- Search the attic for the key -> [The attic](#attic_clean)
- Pay the ransom -> [Pay the ransom](#pay_ransom_b)
- Open the 'support' chat from the ransom note -> [Customer success](#ransom_chat_b)
- Back to the lab -> [Clean slate](#clean_hub)

<a id="attic_clean"></a>
### The attic

Same attic, same dust, same plastic tree. A laminated card: 'OFFSITE BACKUP KEY'. You promise to buy past you a coffee.

> Picked up: **Backup key**

- Back to the backups -> [The local backups](#backups_clean)

<a id="pay_ransom_b"></a>
### Pay the ransom

The wallet is open again. You know this system is clean, which makes paying even sillier. Your finger hovers anyway.

- Send the payment -> [Paid and Played](#ending_paid)
- Close the wallet -> [The local backups](#backups_clean)

<a id="ransom_chat_b"></a>
### Customer success

A chat window opens: 'Hello! My name is Brenda from Customer Success. How can I help your recovery journey today?' Brenda offers a test decryption for a small 0.01 BTC verification fee, and a loyalty discount if you act in the next ten minutes.

- Pay the verification fee -> [Paid and Played](#ending_paid)
- Close the chat -> [The local backups](#backups_clean)

## Act VI - The infected server

*You got a working OS, but not a trustworthy one.*

<a id="containers_down"></a>
### Containers offline

SSH access is restored, and the base OS is healthy. However, Docker is completely empty—all your containers, databases, and media servers failed to start up automatically.

- Check the backups -> [The local backups](#backups)
- Search the server for traces -> [Traces](#traces)
- Run a rootkit scanner -> [Rootkit scanner](#rkhunter)
- Rebuild from your compose files -> [Rebuild from compose files](#compose_git)
- Burn it all down and walk away -> [Touch Grass](#ending_touch_grass)

<a id="traces"></a>
### Traces

In /root: README_KEV.txt. 'gg ez. i was never here. - kev_the_kernel'. Next to it a hidden cron job, an unknown kernel module and a very smug piece of ASCII-art cat.

> Picked up: **Kev's handle**

- Check the backups -> [The local backups](#backups)
- Run a rootkit scanner -> [Rootkit scanner](#rkhunter)
- Back to the container status -> [Containers offline](#containers_down)

<a id="rkhunter"></a>
### Rootkit scanner

The scanner takes forever, then prints one word in red: INFECTED. The kernel from the Reddit script carries a backdoor, and so does half of /usr/bin. Nothing on this machine can be trusted.

- Wipe the server and reinstall -> [Wipe and reinstall](#clean_install)
- Check the backups -> [The local backups](#backups)
- Back to the container status -> [Containers offline](#containers_down)

<a id="backups"></a>
### The local backups

Your NAS holds years of backups. All encrypted, with a note: 'Send 0.5 BTC for the key. You have 24 hours.' The offsite bucket is a different story, if you can unlock it.

- Pay the ransom -> [Pay the ransom](#pay_ransom)
- Search for the offsite backup key -> [The attic](#attic_late)
- Decrypt the offsite backup -> [Decrypt the offsite backup](#offsite_restore) *(requires: Backup key)*
- Open the 'support' chat from the ransom note -> [Customer success](#ransom_chat)
- Back to the container status -> [Containers offline](#containers_down)

<a id="pay_ransom"></a>
### Pay the ransom

The wallet is open. 0.5 BTC is more than the server cost. Your finger hovers over the button. In your head Greg says: 'Never pay.'

- Send the payment -> [Paid and Played](#ending_paid)
- Close the wallet -> [The local backups](#backups)

<a id="ransom_chat"></a>
### Customer success

A chat window opens: 'Hello! My name is Brenda from Customer Success. How can I help your recovery journey today?' Brenda offers a test decryption for a small 0.01 BTC verification fee, and a loyalty discount if you act in the next ten minutes.

- Pay the verification fee -> [Paid and Played](#ending_paid)
- Close the chat -> [The local backups](#backups)

<a id="attic_late"></a>
### The attic

Dust, a plastic Christmas tree and a shoebox. Inside, a laminated card in your handwriting: 'OFFSITE BACKUP KEY - bucket homelab-bkp'. Past you really was a genius.

> Picked up: **Backup key**

- Go back to the backups -> [The local backups](#backups)

<a id="offsite_restore"></a>
### Decrypt the offsite backup

The key works. The bucket holds your data from last Tuesday: photos, databases, the media library. But the server in front of you is running a kernel that Kev wrote.

- Restore onto this server right now -> [Restore onto the infected server](#restore_infected)
- Wipe the server, then restore -> [Wipe and reinstall](#clean_install)

<a id="restore_infected"></a>
### Restore onto the infected server

Eight hours later every file is back. You sleep like a baby. At 3 a.m. your phone buzzes: everything is encrypted again. The backdoor was just waiting for fresh data.

- Wipe and reinstall for real -> [Wipe and reinstall](#clean_install)
- Throw the server out of the window -> [Touch Grass](#ending_touch_grass)

<a id="compose_git"></a>
### Rebuild from compose files

Your compose files lived in a Git repo. On this server. You stare at the empty disk and a cold realization settles in. Also, this server is still full of Kev.

- Wipe the server and start fresh -> [Wipe and reinstall](#clean_install)
- Rebuild right here, right now -> [Rebuild on the infected host](#rebuild_infected)

<a id="rebuild_infected"></a>
### Rebuild on the infected host

The containers come up one by one. So does Kev's backdoor, now with a front-row seat to your brand-new database passwords. At dawn every service is sending spam to the entire Internet.

- Wipe and reinstall for real -> [Wipe and reinstall](#clean_install)
- Pull the plug and walk away -> [Touch Grass](#ending_touch_grass)

## Act VII - Wipe, restore, rebuild

*Starting over, the slow way.*

<a id="clean_install"></a>
### Wipe and reinstall

You boot an installer, delete every partition and watch a clean OS go on. The backdoor is gone. So is everything else, until you bring it back.

- Restore the offsite backup -> [Restore the offsite backup](#offsite_clean_restore) *(requires: Backup key)*
- Rebuild from the GitHub mirror -> [The GitHub mirror](#github_mirror)
- Rebuild by hand, from memory -> [Rebuild by hand](#rebuild_by_hand)

<a id="offsite_clean_restore"></a>
### Restore the offsite backup

On a clean system the bucket finally gives up your data from last Tuesday. Photos, databases, the media library, byte by byte. It takes hours. It is the best hours of your week.

> Picked up: **Restored data**
> Lost: **Backup key**

- Verify the checksums -> [Checksums match](#backup_verify)
- Start the containers right away -> [Start the containers](#containers_up)

<a id="containers_up"></a>
### Start the containers

docker compose up -d. Pi-hole, Jellyfin and Vaultwarden greet you like old friends. Three containers refuse to start because their images disappeared. You decide to check the data anyway.

- Verify the checksums -> [Checksums match](#backup_verify)

<a id="backup_verify"></a>
### Checksums match

Every checksum matches. For the first time tonight something is exactly as it should be. But somewhere out there, kev_the_kernel is still laughing.

- Hunt for the attacker -> [Hunt for the attacker](#hunt_kev)
- Harden the lab -> [Harden the lab](#harden)

<a id="github_mirror"></a>
### The GitHub mirror

Three months ago you mirrored the repo to GitHub 'just in case'. The compose files are there. The data is not. Rebuilding means starting every service empty.

- Rebuild every service from the mirror -> [Rebuild the services](#rebuild_services)
- See if any data survived -> [Survivors](#survivors)
- Pull all the images at once -> [Rate limited](#docker_limit)

<a id="docker_limit"></a>
### Rate limited

'toomanyrequests: You have reached your pull rate limit.' Fourteen images, six pulls, one very long night. Docker Hub would like you to log in, pay, or wait six hours.

- Wait six hours -> [Six hours later](#rebuild_wait)
- Go back and rebuild one service at a time -> [Rebuild the services](#rebuild_services)

<a id="rebuild_wait"></a>
### Six hours later

You nap on the server room floor next to a very tolerant Pixel. When you wake up, the limit has reset and every image pulls in four minutes. You feel personally wronged by the universe.

- Rebuild every service -> [Rebuild the services](#rebuild_services)

<a id="survivors"></a>
### Survivors

On an old laptop and the attic Raspberry Pi you find 2019 photos, a database dump from March and half the media library. It is not much, but it is yours.

- Rebuild every service -> [Rebuild the services](#rebuild_services)

<a id="rebuild_by_hand"></a>
### Rebuild by hand

You rebuild from memory. You forget three passwords, two port numbers and why Nextcloud needed that one weird cron job. After six hours half the services work.

- Keep going until it all works -> [Rebuild the services](#rebuild_services)
- Pull the plug on this madness -> [Touch Grass](#ending_touch_grass)

<a id="rebuild_services"></a>
### Rebuild the services

One by one the green lights appear: Jellyfin, Nextcloud, the databases. Empty, but alive. The dashboards look beautiful and hollow, like a brand new apartment.

- Set up proper, tested backups -> [3-2-1 and a test](#new_backups)
- Hunt for the attacker first -> [Hunt for the attacker](#hunt_kev)

<a id="new_backups"></a>
### 3-2-1 and a test

Three copies. Two kinds of media. One offsite. And, for the first time in your life, an actual restore test. Past you would be proud. Future you will be grateful.

- Close the laptop. It is morning -> [Sunrise](#morning)
- Not done: find who did this -> [Hunt for the attacker](#hunt_kev)

<a id="morning"></a>
### Sunrise

Birds. A very ordinary morning. Mrs. Nagy knocks with a plate of cookies and a mild lecture about the time. Greg texts: 'alive?' You reply with a photo of a green dashboard.

- Eat a cookie and go to sleep -> [Phoenix](#ending_phoenix)

## Act VIII - The hunt for the attacker

*Who is kev_the_kernel, and what do you do when you find him?*

<a id="hunt_kev"></a>
### Hunt for the attacker

You have a README file, a forum name and a lot of anger. You open a terminal and a browser, and start digging.

- Search for the username -> [Who is kev_the_kernel?](#whois_kev) *(requires: Kev's handle)*
- Look through his connection logs -> [Connection logs](#kev_logs)
- Set a honeypot -> [Set a honeypot](#honeypot_setup)
- Find out how he got in -> [How did he get in?](#root_cause)

<a id="kev_logs"></a>
### Connection logs

He came through three proxies and a Tor exit node. Professional? Or just someone who follows tutorials very carefully?

- Set a honeypot -> [Set a honeypot](#honeypot_setup)
- Back to the investigation -> [Hunt for the attacker](#hunt_kev)

<a id="root_cause"></a>
### How did he get in?

You trace the first request backwards. Not the SSH key, not the fridge: a login on Portainer, port 9443, forwarded 'temporarily' in 2022. The password was 'admin'. It was not temporary.

- Open Portainer's audit log -> [Portainer's audit log](#portainer_log)
- Back to the investigation -> [Hunt for the attacker](#hunt_kev)

<a id="portainer_log"></a>
### Portainer's audit log

One login at 02:38, user 'admin', from a Tor exit node. Then a container named 'backup' started, mounted the Docker socket you exposed 'for convenience', and walked straight into the host. Every door was open, and you were the one who opened it.

- Write the post-mortem -> [The post-mortem](#postmortem_draft)
- Harden the lab -> [Harden the lab](#harden)
- Back to the investigation -> [Hunt for the attacker](#hunt_kev)

<a id="postmortem_draft"></a>
### The post-mortem

Blameless format: timeline, impact, root cause, what went well, action items. 'Do not forward ports temporarily' is action item number one. Action item number two is also 'do not forward ports temporarily'. It feels good to write.

- Send it to Greg for review -> [Greg's review](#greg_review)
- Publish it on your blog -> [Blameless](#ending_postmortem)
- Back to the investigation -> [Hunt for the attacker](#hunt_kev)

<a id="greg_review"></a>
### Greg's review

Greg returns it in eleven minutes with forty comments and one line in green: 'Good. Now go to sleep.' Under the action items he adds: 'Expire my old key. Sorry.' You publish it together.

- Publish it -> [Blameless](#ending_postmortem)

<a id="whois_kev"></a>
### Who is kev_the_kernel?

The username shows up on a forum, a game server and a school coding club page. His avatar is a cat in sunglasses. His latest post: 'anyone know how to bypass a firewall? asking for homework'.

> Lost: **Kev's handle**

- Set a honeypot to catch him -> [Set a honeypot](#honeypot_setup)
- Send him a message -> [Talk to Kev](#dm_kev)
- Report the username -> [Report Kev](#report_kev)
- Open the coding club page -> [The coding club page](#club_page)

<a id="club_page"></a>
### The coding club page

'Thursday Coding Club, 4 p.m., room 12. Mentor: G. Horvath.' A group photo: nine kids, one beaming sysadmin who is definitely Greg, and an old laptop with a sticker: 'donated by Greg, 2021'. The authorized_keys file suddenly makes a lot more sense.

- Call Greg -> [Greg confesses](#greg_confession)
- Back to the investigation -> [Hunt for the attacker](#hunt_kev)

<a id="greg_confession"></a>
### Greg confesses

Greg goes quiet for a long time. 'The old laptop. I donated it to the club in 2021 and never wiped it. The key was still on it. Oh no. Oh no.' He is not defending himself. He is just very, very sorry.

- Visit the club with Greg on Thursday -> [Thursday, room 12](#club_visit)
- Make the deal with Kev directly -> [The deal](#kev_deal)
- Take it to the police -> [Report Kev](#report_kev)

<a id="club_visit"></a>
### Thursday, room 12

Greg opens the door of a classroom that smells of whiteboard markers and pizza. Eight kids look up. One goes pale. Kev stands up slowly, laptop in hand, cat-in-sunglasses sticker and all. Nobody speaks for a very long time.

- Offer him a deal -> [The deal](#kev_deal)
- Turn it into a lesson for the whole club -> [A teachable moment](#club_lesson)
- Hand it over to the school principal -> [The principal](#principal)

<a id="club_lesson"></a>
### A teachable moment

You ask Greg for the projector. You show the logs, the Portainer screen, the 'admin' password. Then you ask the room: how would you have stopped this? Hands go up. Kev's goes up last, and then fastest.

- Turn your lab into a capture-the-flag -> [Capture the Flag](#ending_club)
- Go back and make the deal with Kev -> [The deal](#kev_deal)

<a id="principal"></a>
### The principal

The principal listens, nods, takes notes and says the school has a policy for this. It involves forms. And three weeks. Kev's face tells you everything about how he feels about forms.

- Insist on the police instead -> [Report Kev](#report_kev)
- Settle it with Kev directly -> [The deal](#kev_deal)

<a id="honeypot_setup"></a>
### Set a honeypot

You leave a fake server with a fake SSH door 'accidentally' open, full of files named passwords_final_v2.xlsx. Now you wait.

> Lost: **Kev's handle**

- Wait for Kev -> [Kev returns](#kev_returns)

<a id="kev_returns"></a>
### Kev returns

At 5:12 a.m. the honeypot lights up. Someone logs in and starts exploring. He types very slowly. 'ls'. 'cd'. 'ls' again. He seems nervous.

- Just watch what he does -> [Watch him](#watch_kev)
- Trace the connection -> [Trace the connection](#trace_kev)
- Open a chat window in his terminal -> [Talk to Kev](#dm_kev)
- Hack him back -> [Hack him back](#counter_hack)

<a id="watch_kev"></a>
### Watch him

You do nothing and watch. Kev opens a text editor, types 'how to look like a hacker', closes it, tries 'sudo rm -rf /' on the honeypot, laughs nervously and then types 'is anyone there?' into the shell. He is clearly alone and clearly not a professional.

- Trace the connection -> [Trace the connection](#trace_kev)
- Open a chat window in his terminal -> [Talk to Kev](#dm_kev)
- Hack him back -> [Hack him back](#counter_hack)

<a id="trace_kev"></a>
### Trace the connection

Behind the proxies: a residential IP, then a student account at a school in the next county. Kev is, at the very most, sixteen years old.

- Send him a message -> [Talk to Kev](#dm_kev)
- Report him to the police -> [Report Kev](#report_kev)
- Hack him back -> [Hack him back](#counter_hack)
- Post what you found on r/homelab -> [Post it](#doxx_post)

<a id="dm_kev"></a>
### Talk to Kev

You type: 'Hi Kev. We need to talk.' A long pause. Then: 'omg pls dont call my mom'. He sounds exactly as scared as a sixteen-year-old should.

- Ask how he got in -> [Kev explains](#kev_confession)
- Offer him a deal -> [The deal](#kev_deal)
- Tell him you are calling the police -> [Report Kev](#report_kev)

<a id="kev_confession"></a>
### Kev explains

Kev types for a full minute without stopping. Portainer with 'admin' as the password. A leftover SSH key from a donated laptop at his coding club. A script he found on a forum. 'Honestly I thought nobody would notice for a week,' he adds, apologetically.

- Offer him a deal -> [The deal](#kev_deal)
- Ask whose laptop that was -> [Greg confesses](#greg_confession)
- Write the post-mortem -> [The post-mortem](#postmortem_draft)
- Tell him you are calling the police -> [Report Kev](#report_kev)

<a id="kev_deal"></a>
### The deal

You offer: help rebuild and harden the lab, write a full report on how he got in, and apologize to Greg. In exchange: no police, no mom. He says yes in under two seconds.

- Shake on it -> [Redemption Arc](#ending_redemption)

<a id="report_kev"></a>
### Report Kev

You write a thorough report: logs, timestamps, the README, the Reddit thread. The officer reads it twice, sips her coffee and says: 'Wow. Please do not hack anyone back.'

- Hand over the evidence at the station -> [At the police station](#police_station)

<a id="police_station"></a>
### At the police station

A detective with a tired face takes your USB stick full of logs. 'We will be in touch,' she says. 'And your data? Is it safe?'

- Tell her it is fully restored -> [Full Recovery](#ending_full_recovery) *(requires: Restored data)*
- Tell her honestly: a fifth is gone -> [Justice, With Gaps](#ending_justice)

<a id="counter_hack"></a>
### Hack him back

You fire a stress-testing tool at his IP. It feels incredible for eleven seconds. Then you notice the IP belongs to a shared school router.

- Keep going. He deserves it -> [The Wrong Tool](#ending_counterhack)
- Stop. Think -> [Hunt for the attacker](#hunt_kev)

<a id="doxx_post"></a>
### Post it

Title: 'FOUND THE KID WHO WRECKED MY LAB'. You attach his school and his handle. 400 upvotes in ten minutes. 4,000 in an hour. Somebody has already found his home address, and somebody else the school's phone number. Your inbox fills up.

- Keep refreshing -> [The Internet Never Forgets](#ending_doxx)
- Delete the post. Now -> [Deleted](#doxx_delete)

<a id="doxx_delete"></a>
### Deleted

The post is gone from your account. The screenshots are not. Somewhere in the county a sixteen-year-old's phone starts ringing, and it is not yet seven in the morning.

- Call the police yourself and explain -> [Report Kev](#report_kev)
- Face what you did -> [The Internet Never Forgets](#ending_doxx)

## The endings

*Twelve ways this night can end.*

<a id="ending_oversleep"></a>
### Snoozed

**ENDING 1 of 12 - Failure**

You wake up at 9:40 to forty-one notifications and the smell of hot dust. Every disk is encrypted, the router is a brick, and Pixel is still asleep on the warm server. The alert was not the cat.

- Play again -> [Start](#start)

<a id="ending_postmortem"></a>
### Blameless

**ENDING 2 of 12 - Success**

Your post-mortem reaches the front page of r/homelab. Strangers thank you for being honest about the 'admin' password. Three of them confess to theirs. The fridge is still on a VLAN, and the lesson is public, permanent and free.

- Play again -> [Start](#start)

<a id="ending_club"></a>
### Capture the Flag

**ENDING 3 of 12 - Success**

Two weeks later your rebuilt, hardened homelab is the practice target of the Thursday club. Kev wins his own challenge and loses the argument about whether it was fair. Greg brings pizza. The fridge refuses to be a flag.

- Play again -> [Start](#start)

<a id="ending_doxx"></a>
### The Internet Never Forgets

**ENDING 4 of 12 - Failure**

Kev changes schools. You are banned from three forums and your lab is still half-rebuilt. The post that made you feel powerful is now the first search result for your name. The wrong tool, again.

- Play again -> [Start](#start)

<a id="ending_full_recovery"></a>
### Full Recovery

**ENDING 5 of 12 - Success**

Your lab is back, your data is back, and Kev's case sits in a folder somewhere in the county. You set up alerting, expire Greg's old key and hang a sign over the rack: 'THE RESCUE USB IS NOT DECORATION.' Pixel sleeps on the server again.

- Play again -> [Start](#start)

<a id="ending_phoenix"></a>
### Phoenix

**ENDING 6 of 12 - Success**

The photos are gone, the databases are gone. But the compose files are alive, the lab is new, and for the first time you have real backups. Starting over is the oldest homelab tradition there is.

- Play again -> [Start](#start)

<a id="ending_redemption"></a>
### Redemption Arc

**ENDING 7 of 12 - Success**

Kev writes a forty-page report, fixes every hole he used, and now maintains your lab on weekends. Greg gets a public apology. The fridge lives on a VLAN. Everyone is safer, a bit embarrassed and strangely proud.

- Play again -> [Start](#start)

<a id="ending_justice"></a>
### Justice, With Gaps

**ENDING 8 of 12 - Success**

Kev gets a stern talk from a very tired detective. Your lab recovers, with a fifth of its memories missing. You learn to love the numbers 3-2-1, and you never forget them again.

- Play again -> [Start](#start)

<a id="ending_bricked"></a>
### Bricked

**ENDING 9 of 12 - Failure**

Nothing boots. Nothing mounts. Your disks hold a very organized pile of zeros. The AI would like to apologize again, but its server is not your server.

- Play again -> [Start](#start)

<a id="ending_paid"></a>
### Paid and Played

**ENDING 10 of 12 - Failure**

The payment goes through. Nothing happens. Then a second note appears: 'Thanks! The price is now 1.0 BTC.' You are poorer, the data is still encrypted, and Kev has a new gaming PC.

- Play again -> [Start](#start)

<a id="ending_touch_grass"></a>
### Touch Grass

**ENDING 11 of 12 - Failure**

You unplug everything. The silence is wonderful. You sell the rack, buy a plant and discover that sunlight exists. You do not miss the 3 a.m. alerts. You do, slightly, miss the lab.

- Play again -> [Start](#start)

<a id="ending_counterhack"></a>
### The Wrong Tool

**ENDING 12 of 12 - Failure**

You took down a school network three days before exams. Kev gets a warning. You get a very serious letter from a lawyer. Greg offers to be a character witness. It is not enough.

- Play again -> [Start](#start)

---

## Ending list

| # | Ending | Result |
|---|---|---|
| 1 | [Snoozed](#ending_oversleep) | Fail |
| 2 | [Blameless](#ending_postmortem) | Success |
| 3 | [Capture the Flag](#ending_club) | Success |
| 4 | [The Internet Never Forgets](#ending_doxx) | Fail |
| 5 | [Full Recovery](#ending_full_recovery) | Success |
| 6 | [Phoenix](#ending_phoenix) | Success |
| 7 | [Redemption Arc](#ending_redemption) | Success |
| 8 | [Justice, With Gaps](#ending_justice) | Success |
| 9 | [Bricked](#ending_bricked) | Fail |
| 10 | [Paid and Played](#ending_paid) | Fail |
| 11 | [Touch Grass](#ending_touch_grass) | Fail |
| 12 | [The Wrong Tool](#ending_counterhack) | Fail |
