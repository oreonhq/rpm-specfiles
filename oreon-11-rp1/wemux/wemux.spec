%global source0_hash 8de6607df116b86e2efddfe3740fc5eef002674e551668e5dde23e21b469b06c

Name:           wemux
Version:        3.2.0
Release:        24%{?dist}
Summary:        Multi-user terminal multiplexing utility
License:        MIT
URL:            https://github.com/zolrath/wemux
Source0:        https://github.com/zolrath/wemux/archive/v%{version}.tar.gz
Patch0:         0001-Added-ability-to-specify-groups-of-users-who-are-hos.patch
Patch1:         0002-Modified-user-group-detection-to-use-regex.patch
BuildArch:      noarch
Requires:       tmux

%description
Wemux enhances tmux to make multi-user terminal multiplexing both easier and
more powerful. It allows users to host a wemux server and have clients join
in either:

**Mirror Mode** gives clients (another SSH user on your machine) read-only
access to the session, allowing them to see you work, or

**Pair Mode** allows the client and yourself to work in the same terminal
(shared cursor)

**Rogue Mode** allows the client to pair or work independently in another
window (separate cursors) in the same tmux session.

It features multi-server support as well as user listing
and notifications when users attach/detach.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
# Drop undue paths, don't use env to detect bash.
sed -i 's|/usr/local||g;s|#!/usr/bin/env bash|#!/bin/bash|g' wemux

%build
# Nothing here.

%install
install -pDm755 %{name} %{buildroot}%{_bindir}/%{name}
install -pDm644 %{name}.conf.example %{buildroot}%{_sysconfdir}/%{name}.conf

%files
%doc README.md
%license MIT-LICENSE
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf

%changelog
%autochangelog
