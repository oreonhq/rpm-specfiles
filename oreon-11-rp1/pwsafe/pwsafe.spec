%global source0_hash 61e91dc5114fe014a49afabd574eda5ff49b36c81a6d492c03fcb10ba6af47b7

Name:           pwsafe
Version:        0.2.0
Release:        47%{?dist}
Summary:        A unix commandline program that manages encrypted password databases

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://nsd.dyndns.org/pwsafe/
Source0:        http://nsd.dyndns.org/pwsafe/releases/pwsafe-%{version}.tar.gz

Patch0:         pwsafe-0.2.0-paste-gnome-terminal.patch
Patch1:         pwsafe-0.2.0-aarch64.patch
Patch2:         pwsafe-configure-c99.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  readline-devel, ncurses-devel, openssl-devel
BuildRequires:  libXt-devel, libXext-devel, libXau-devel, libXdmcp-devel
BuildRequires:  libSM-devel, libICE-devel, libXmu-devel

%description
pwsafe is a unix commandline program that manages encrypted password databases.
Compatible with CounterPane's PasswordSafe Win32 program versions 2.x and 1.x.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p0 -b .paste-gnome-terminal
%patch -P1 -p1 -b .aarch64
%patch -P2 -p1 -b .configure.c99

%build
%configure \
    --disable-dependency-tracking
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

# Convert man page to UTF-8
iconv -f iso-8859-1 -t utf8 pwsafe.1 -o pwsafe.1.utf8
mv pwsafe.1.utf8 pwsafe.1
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/pwsafe
%{_mandir}/man1/pwsafe.1.gz

%changelog
%autochangelog
