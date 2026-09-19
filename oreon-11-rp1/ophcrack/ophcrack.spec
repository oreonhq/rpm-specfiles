%global source0_hash 048a6df57983a3a5a31ac7c4ec12df16aa49e652a29676d93d4ef959d50aeee0

Name:           ophcrack
Version:        3.8.0
Release:        21%{?dist}
Summary:        Free Windows password cracker based on rainbow tables
# Automatically converted from old format: GPLv2+ with exceptions - review is highly recommended.
License:        LicenseRef-Callaway-GPLv2+-with-exceptions
URL:            https://ophcrack.sourceforge.io
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2

# Wrong FSF address in LICENSE FILE
# https://gitlab.com/objectifsecurite/ophcrack/issues/7
Patch0:         0001-correct-FSF-address.patch

# upstreamable
BuildRequires: make
BuildRequires:  automake libtool
BuildRequires:  openssl-devel
BuildRequires:  expat-devel
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(qwt5-qt5)
BuildRequires:  qt5-qtcharts-devel

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

%autosetup

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

%files
%doc AUTHORS ChangeLog COPYING LICENSE LICENSE.OpenSSL NEWS README.md
%{_bindir}/%{name}
%{_datadir}/pixmaps/ophcrack.png
%{_datadir}/applications/%{name}.desktop

%changelog
%autochangelog
