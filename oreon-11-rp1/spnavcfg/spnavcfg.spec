%global source0_hash 59bd470109b9b70a0f88b75183021db2170c84e0ce7a64ff83ce484d09c3616d

# Required for suid binary
%global _hardened_build 1

Name:           spnavcfg
Version:        1.3
Release:        3%{?dist}
Summary:        Spacenav daemon interactive configuration program

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://spacenav.sourceforge.net/
Source0:        https://github.com/FreeSpacenav/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libspnav-devel
BuildRequires:  libX11
BuildRequires:  qt6-qtbase-devel
BuildRequires:  desktop-file-utils

Requires:       spacenavd

%description
Spacenav daemon interactive configuration program.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{optflags}"
%configure 

# Remove -O3 from build flags
sed -i 's/\-O3/\-O2/g' Makefile

%make_build

%install
%make_install

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

%changelog
%autochangelog
