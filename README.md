# rpm-specfiles

This repo is the big pile of source trees for packages that ship in Oreon 11 and later. Each directory under a release folder (for example `oreon-11-rp1/<package>/`) is one package: specfile, patches, and whatever else that spec needs. The point is to have one place maintainers can update packages without hunting through individual package source repos.

This is basically the entire source code tree for Oreon. If you are trying to build a batch of related packages in the right order for the Oreon Build Service, read the maintainer note below.

## Updating Packages

Version bumps and stack rebuilds are painful if you build in random order. We wrote a long and helpful guide with copy-paste chain build lines for the big stacks (KDE Plasma, kernel, Qt, and a few others).

[Updating Packages for Oreon 11 - Release Pack 1 (maintainers guide)](oreon-11-rp1/UPDATING.md)

If a chain string drifts from reality (new package added, spec renamed, whatever), fix the guide when you fix the tree. Future you will be less angry.

## Contribution Notice

If you would like to contribute to updates or add new packages, feel free to open a pull request with your changes, or an issue with the proposal if you're lazy and want us to do it. We may accept or deny proposals/PRs.

While random contributors are welcome, we highly encourage joining the Oreon team directly, so it makes coordination easier between other team members. To join the team, contact our Project Lead @brandonlester:matrix.org on Matrix or join our Discord community: https://discord.gg/2Yyacu58Ap

## Project Policies & Guidelines
Read them [here](https://wiki.oreonhq.com/docs/Project%20Policies%20&%20Team%20Information/contributors).
