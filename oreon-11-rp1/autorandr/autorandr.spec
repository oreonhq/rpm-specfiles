%global source0_hash 1579b6b4d44669a0db22268524ea512f60da02eeecffddf81f7327aaf56485f5

Name:           autorandr
Version:        1.15
Release:        %autorelease
Summary:        Automatically select a display configuration based on connected devices

BuildArch:      noarch
BuildRequires:  python3-devel

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/phillipberndt/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: systemd
BuildRequires: udev
BuildRequires: desktop-file-utils

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%py3_shebang_fix ./autorandr.py

%post
udevadm control --reload-rules
%systemd_post autorandr.service

%preun
%systemd_preun autorandr.service

%postun
%systemd_postun autorandr.service

%package bash-completion
Summary: Bash completion for autorandr
Requires: %{name}
Requires: bash-completion
%description bash-completion
This package provides bash-completion files for autorandr

%package zsh-completion
Summary: Zsh completion for autorandr
Requires: zsh
Requires: %{name}
%description zsh-completion
This package provides zsh-completion files for autorandr

%install
%make_install
install -vDm 644 README.md -t "%{buildroot}/usr/share/doc/%{name}/"
install -vDm 644 contrib/bash_completion/autorandr -t %{buildroot}%{_datadir}/bash-completion/completions/
install -vDm 644 contrib/zsh_completion/_autorandr -t %{buildroot}%{_datadir}/zsh/site-functions/
install -vDm 644 autorandr.1 -t %{buildroot}%{_mandir}/man1/

%check
desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/autorandr.desktop
desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/autorandr-kde.desktop

%files
%license gpl-3.0.txt
%doc README.md
%{_mandir}/man1/*
%{_bindir}/autorandr
%{_unitdir}/autorandr.service
%{_unitdir}/autorandr-lid-listener.service
%{_sysconfdir}/xdg/autostart/autorandr.desktop
%{_sysconfdir}/xdg/autostart/autorandr-kde.desktop
%{_udevrulesdir}/40-monitor-hotplug.rules

%files bash-completion
%{_datadir}/bash-completion/completions/autorandr

%files zsh-completion
%{_datadir}/zsh/site-functions/_autorandr

%changelog
%autochangelog
