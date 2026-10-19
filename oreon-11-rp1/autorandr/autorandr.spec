%global source0_hash 1579b6b4d44669a0db22268524ea512f60da02eeecffddf81f7327aaf56485f5
Name:           autorandr
Version:        1.15
Release:        1%{?dist}
Summary:        Automatically select a display configuration based on connected devices
BuildArch:      noarch
License:        GPL-3.0-only
URL:            https://github.com/phillipberndt/%{name}
Source0:        https://github.com/phillipberndt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  systemd
BuildRequires:  udev
# /oreon:deps
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
%oreon_autofiles autorandr-bash-completion usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles autorandr-zsh-completion usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/autorandr.desktop
desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/autorandr-kde.desktop
%files -f %{oreon_filedir}/main.list
%files -n autorandr-bash-completion -f %{oreon_filedir}/autorandr-bash-completion.list
%files -n autorandr-zsh-completion -f %{oreon_filedir}/autorandr-zsh-completion.list

%changelog

%autochangelog
