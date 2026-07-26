%global source0_hash 929871abae9be902d4fb592f2e76e52b58b386d208f127c826ae1d7b7bade9ef

Name:           zork
Version:        1.0.3
Release:        12%{?dist}
Summary:        Public Domain original DUNGEON game (AKA, Zork)

License:        LicenseRef-Fedora-Public-Domain
URL:            https://github.com/devshane/zork
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:         zork-tweak-makefile.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel

%description
Public Domain Source Code for the Mainframe Game "Dungeon". This repository contains the Public Domain source code for
Dungeon, the mainframe version of the game that served as the precursor to Infocom's commercial Zork trilogy. This
codebase is a C port derived from the FORTRAN source of Zork 2.6.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%global _hardened_build 1
%autosetup

%build
%make_build \
    CFLAGS="%{optflags} -std=c17" \
    DATADIR="%{_datadir}/%{name}" \
    LDFLAGS="%{__global_ldflags}"

%install
%make_install \
    BINDIR="%{buildroot}%{_bindir}" \
    DATADIR="%{buildroot}%{_datadir}/%{name}/" \
    LIBDIR="%{buildroot}%{_datadir}" \
    MANDIR="%{buildroot}%{_mandir}"
echo ".so dungeon.6" > %{buildroot}%{_mandir}/man6/zork.6

%files
%doc history
%doc README.md
%license readme.txt
%{_bindir}/%{name}
%{_datadir}/%{name}/dtextc.dat
%{_mandir}/man6/dungeon.6.gz
%{_mandir}/man6/zork.6*

%changelog
%autochangelog
