%global source0_hash df2934f886d9d225f27062a783df3f32d73151d32f53b20f37415492932837e4
Name:           zork
Version:        1.1.0
Release:        1%{?dist}
Summary:        Public Domain original DUNGEON game (AKA, Zork)
License:        LicenseRef-Fedora-Public-Domain
URL:            https://github.com/devshane/zork
Source0:        https://github.com/devshane/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         zork-tweak-makefile.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
