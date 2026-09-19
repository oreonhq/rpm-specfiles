%global source0_hash 48bb55a6340564379cc233cd356bd2120136f44ab43a720f8442c722e37833ad

Summary:	A text-mode maze game
Name:		lsnipes
Version:	0.9.4
Release:	%autorelease
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
Source:		http://www.ugcs.caltech.edu/~boultonj/snipes/%{name}-%{version}.tgz
URL:		http://www.ugcs.caltech.edu/~boultonj/snipes.html
Patch1:		lsnipes-adapt-CFLAGS-LIBS.patch
# Man page update about levels from Debian package
Patch2:		lsnipes-man-levels-doc.patch

BuildRequires:  gcc
BuildRequires:	ncurses-devel
BuildRequires: make

%description
Linux Snipes is a reimplementation of an old text-mode DOS game. You
are in a maze with a number of enemies (the "snipes") and a few
"hives" which create more of the enemies. Your job is to kill the
snipes and their hives before they get the best of you.  26 "option
levels" let you change characteristics of the game such as whether or
not diagonal shots bounce off the walls.  10 levels of difficulty (only
partially implemented) let you build your skills gradually.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p1 -b .cflags
%patch -P2 -p1 -b .man-levels

%build
%{__make} RPM_CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -p -m 0755 -d	%{buildroot}%{_bindir}
%{__install} -p -m 0755 snipes	%{buildroot}%{_bindir}/snipes
%{__install} -p -m 0755 -d	%{buildroot}%{_mandir}/man6
%{__install} -p -m 0644 snipes.6 %{buildroot}%{_mandir}/man6/snipes.6

%files
%doc README TODO COPYING CHANGELOG
%{_bindir}/snipes
%{_mandir}/man6/snipes.6*

%changelog
%autochangelog
