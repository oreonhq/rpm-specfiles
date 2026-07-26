%global source0_hash 9e315b929232f1b5b36bd7ffde235f3704eaa74aca2a56031034ffb597c418d2

Name:           binclock
Summary:        Fullscreen console binary clock
Version:        0.4.0
Release:        25%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://github.com/frenzymadness/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%description
Fullscreen console binary clock.
Features:

* Written in Python
* Uses ncurses
* In color
* Proper SIGWINCH handling

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%install
#Install the executable
install -Dp -m0755 binclock.py %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/binclock

%changelog
%autochangelog
