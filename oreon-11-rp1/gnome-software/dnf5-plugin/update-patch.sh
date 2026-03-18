#!/bin/bash

if [ ! -d checkout-gs-dnf5 ]; then
	git clone --branch main https://gitlab.gnome.org/mcrha/gnome-software.git checkout-gs-dnf5 && \
	cd checkout-gs-dnf5 && \
	git checkout -b wip/dnf5daemon origin/wip/dnf5daemon && \
	cd - >/dev/null

	if [ "$?" != "0" ]; then
		echo "Failed to clone dnf5-plugin repository" 1>&2
		exit 1;
	fi
fi

PATCH_PATH=../0001-dnf5-plugin.patch

cd checkout-gs-dnf5 && \
echo "Updating gs-dnf5 git 'main' repository" && \
git checkout main && \
git pull --rebase && \
echo "Updating gs-dnf5 git 'dnf5-pugin' repository" && \
git checkout wip/dnf5daemon && \
git pull --rebase && \
echo -n "at " >../${PATCH_PATH} && \
git log HEAD | head -n 5 | grep -E "commit|Date" >>../${PATCH_PATH} && \
echo "" >>../${PATCH_PATH} && \
git diff main >>../${PATCH_PATH} && \
cd - >/dev/null

if [ "$?" = "0" ]; then
	echo "Patch '${PATCH_PATH}' updated"
else
	echo "Failed to update patch '${PATCH_PATH}'" 1>&2
	exit 1
fi
