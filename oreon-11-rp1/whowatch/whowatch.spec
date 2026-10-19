%global source0_hash 1b8d54e3de4d8325c47a0fb8765cbaaeee8744359b5dacd4bdb3e40b4e31797e
Summary:        Display information about users currently logged on
Name: whowatch
Version: 1.8.6
Release:        22%{?dist}
License: GPL-2.0-only
URL: http://wizard.ae.krakow.pl/~mike/
Source0:        https://github.com/mtsuszycki/whowatch/archive/whowatch-%{version}.tar.gz
Patch0: whowatch-configure-c99.patch
Patch1: whowatch-gcc15-fixes.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
%description
Whowatch is an interactive who-like program that displays information about the
users currently logged on to the machine, in real time. Besides standard
information (login name, tty, host, user's process), the type of the connection
(ie. telnet or ssh) is shown. You can toggle display between users' command or
idle time. You can watch processes tree, navigate in it and send INT and KILL
signals.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

touch aclocal.m4 Makefile.in src/config.h.in
%configure
%{__make} %{?_smp_mflags}
%install
%{__install} -d -m0755 %{buildroot}%{_mandir}/man1/ \
			%{buildroot}%{_bindir}
%makeinstall
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
