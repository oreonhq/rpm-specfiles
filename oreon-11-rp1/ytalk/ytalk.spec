%global source0_hash 25f0539a27d6770707da35c4a942a6d0e02ae89806691dd0b211d579fae6fa40

Summary: A chat program for multiple users
Name: ytalk
Version: 3.3.0
Release: %autorelease
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://www.impul.se/ytalk/
Source: http://www.impul.se/ytalk/%{name}-%{version}.tar.bz2
Source1: ytalkrc
Patch1: ytalk-c99.patch
BuildRequires: gcc
BuildRequires: make
BuildRequires: ncurses-devel

%description
The YTalk program is essentially a chat program for multiple users.
YTalk works just like the UNIX talk program and even communicates with
the same talk daemon(s), but YTalk allows for multiple connections
(unlike UNIX talk).  YTalk also supports redirection of program output
to other users as well as an easy-to-use menu of commands.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
export CFLAGS="${CFLAGS} -std=gnu99"
%configure
%make_build

%install
%make_install
%files
%doc COPYING AUTHORS README
%{_bindir}/*
%{_mandir}/*/*
%config(noreplace) /etc/ytalkrc

%changelog
%autochangelog
