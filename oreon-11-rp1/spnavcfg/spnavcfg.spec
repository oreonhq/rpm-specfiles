%global source0_hash 59bd470109b9b70a0f88b75183021db2170c84e0ce7a64ff83ce484d09c3616d
%global _hardened_build 1
Name:           spnavcfg
Version:        1.3
Release:        1%{?dist}
Summary:        Spacenav daemon interactive configuration program
License:        GPL-3.0-or-later
URL:            http://spacenav.sourceforge.net/
Source0:        https://github.com/FreeSpacenav/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Requires:       spacenavd
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libX11
BuildRequires:  libspnav-devel
BuildRequires:  make
BuildRequires:  qt6-qtbase-devel
# /oreon:deps
%description
Spacenav daemon interactive configuration program.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CFLAGS="%{optflags}"
export LDFLAGS="%{optflags}"
%configure 
sed -i 's/\-O3/\-O2/g' Makefile
%make_build
%install
%make_install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
