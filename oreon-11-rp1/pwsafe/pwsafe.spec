%global source0_hash 61e91dc5114fe014a49afabd574eda5ff49b36c81a6d492c03fcb10ba6af47b7
Name:           pwsafe
Version:        0.2.0
Release:        47%{?dist}
Summary:        A unix commandline program that manages encrypted password databases
License:        GPL-2.0-or-later
URL:            http://nsd.dyndns.org/pwsafe/
Source0:        http://nsd.dyndns.org/pwsafe/releases/pwsafe-%{version}.tar.gz
Patch0:         pwsafe-0.2.0-paste-gnome-terminal.patch
Patch1:         pwsafe-0.2.0-aarch64.patch
Patch2:         pwsafe-configure-c99.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libXau-devel
BuildRequires:  libXdmcp-devel
BuildRequires:  libXext-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXt-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  readline-devel
# /oreon:deps
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
iconv -f iso-8859-1 -t utf8 pwsafe.1 -o pwsafe.1.utf8
mv pwsafe.1.utf8 pwsafe.1
make install DESTDIR=$RPM_BUILD_ROOT
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
