%global source0_hash bcfe0eabdccc806e53a10130fed6fb02373720ddeb670eecc5cc84d041d79880
Name:       git-extras
Version:    7.5.0
Release:        1%{?dist}
Summary:        Little git extras
License:    MIT
URL:        https://github.com/tj/%{name}
Source0:        https://github.com/tj/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:  noarch
Requires:   git
# oreon:deps
BuildRequires:  make
BuildRequires:  sed
# /oreon:deps
%description
%{name} adds the following extra-commands to git:

alias, archive-file, bug, changelog, commits-since, contrib, count,
create-branch, delete-branch, delete-submodule, delete-tag, effort,
extras, feature, fresh-branch, gh-pages, graft, ignore, info,
local-commits, obliterate, promote, refactor, release, repl, setup,
squash, summary, touch, undo

For more information about the extra-commands, see the included
README.md, HTML, mark-down or man-pages.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# scripts already use bash
# remove `/usr/bin/env` from hashbang
sed -i -e "s#/usr/bin/.*sh#/bin/bash#g" \
    bin/*

#Disable self-update feature
cat << EOF > bin/git-extras
#!/bin/sh
echo "Self-update feature disabled by maintainer."
EOF

%build

%install
%make_install PREFIX=%{_prefix} SYSCONFDIR=%{_datadir}
mkdir -p html md
install -pm 0644 man/*.html html
install -pm 0644 man/*.md md
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
