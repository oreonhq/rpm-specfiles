%global source0_hash 89bae1a05731f4aaafb04066ea0186e181117b74fcfbf89d686cf205459220b7

Name:       git-extras
Version:    7.3.0
Release:    4%{?dist}
Summary:    Little git extras

License:    MIT
URL:        https://github.com/tj/%{name}
Source0:    %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:  noarch

BuildRequires: sed
BuildRequires: make
Requires:   git

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

%files
%doc AUTHORS Commands.md History.md Readme.md html/ md/
%license LICENSE
%config(noreplace) %{bash_completions_dir}
%{_bindir}/*
%{_mandir}/man*/*

%changelog
%autochangelog
