%global source0_hash 747fc4a6eb3fff8298f84bbc2423fef96d96bd0ba894faaa4bab2432ad6ec275
%global _lto_cflags %nil
Name:		tlf
Version:	1.4.1
Release:        22%{?dist}
Summary:        Ham radio contest logger
License:	GPL-2.0-or-later AND GPL-3.0-or-later
URL:		https://github.com/Tlf/tlf
Source0:        https://github.com/Tlf/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:	%{url}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz.sig
Source2:	tlf-release-key.asc
ExcludeArch:    i686
Recommends:	xplanet
Recommends:	sox
Recommends:	cwdaemon
Patch:		tlf-1.4.1-hamlib-4.2-build-fix.patch
Patch:		tlf-1.4.1-fsf-address-fix.patch
Patch:		tlf-1.4.1-format-security-fix.patch
Patch:		tlf-c99.patch
Patch:		tlf-1.4.1-gcc-15-fix.patch
Patch:		tlf-1.4.1-gcc-16-fix.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gnupg2
BuildRequires:  hamlib-devel
BuildRequires:  libcmocka-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  xmlrpc-c-devel
# /oreon:deps
%description
Tlf is a console (ncurses) mode general purpose CW/VOICE keyer,
logging and contest program for hamradio. It supports the CQWW,
the WPX, the ARRL-DX , the ARRL-FD, the PACC and the EU SPRINT
contests (single operator) as well as a LOT MORE basic contests,
general QSO and DXpedition mode.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

autoreconf -fi
%configure --enable-fldigi-xmlrpc
%make_build
%install
%make_install
%oreon_autofiles main

%check

cd test
make check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
