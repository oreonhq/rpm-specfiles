%global source0_hash 048a6df57983a3a5a31ac7c4ec12df16aa49e652a29676d93d4ef959d50aeee0
Name:           ophcrack
Version:        3.8.0
Release:        1%{?dist}
Summary:        Free Windows password cracker based on rainbow tables
License:        LicenseRef-Callaway-GPLv2+-with-exceptions
URL:            https://ophcrack.sourceforge.io
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:         0001-correct-FSF-address.patch
# oreon:deps
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  expat-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(qwt5-qt5)
BuildRequires:  qt5-qtcharts-devel
# /oreon:deps
%description
Ophcrack is a free Windows password cracker based on rainbow tables. 
It is a very efficient implementation of rainbow tables done by the 
inventors of the method. It comes with a Graphical User Interface and 
runs on multiple platforms. 

Features:

    * Runs on Windows, Linux/Unix, Mac OS X, ...
    * Cracks LM and NTLM hashes.
    * Free tables available for Windows XP and Vista.
    * Brute-force module for simple passwords.
    * Audit mode and CSV export.
    * Real-time graphs to analyze the passwords.
    * LiveCD available to simplify the cracking.
    * Loads hashes from encrypted SAM recovered from a Windows partition,
      Vista included.
    * Free and open source software (GPL).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
install -Dp -m0644 src/gui/pixmaps/os.png %{buildroot}%{_datadir}/pixmaps/ophcrack.png
install -dm0755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Type=Application
Exec=%{name}
Name=Ophcrack
Comment=Windows password cracker
GenericName=Windows password cracker
Icon=ophcrack
Terminal=false
Categories=System;Security;
StartupNotify=true
EOF
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
