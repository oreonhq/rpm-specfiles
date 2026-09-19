%global source0_hash 747fc4a6eb3fff8298f84bbc2423fef96d96bd0ba894faaa4bab2432ad6ec275

# LTO breaks unit tests
%global _lto_cflags %nil

Name:		tlf
Version:	1.4.1
Release:	22%{?dist}
Summary:	Ham radio contest logger
# GPLv3+ are some m4 macros
# Automatically converted from old format: GPLv2+ and GPLv3+ - review is highly recommended.
License:	GPL-2.0-or-later AND GPL-3.0-or-later
URL:		https://github.com/Tlf/tlf
Source0:	%{url}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:	%{url}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz.sig
Source2:	tlf-release-key.asc
ExcludeArch:    i686
BuildRequires:	gnupg2
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	glib2-devel
BuildRequires:	ncurses-devel
BuildRequires:	hamlib-devel
BuildRequires:	xmlrpc-c-devel
BuildRequires:	libcmocka-devel
# autoconf, automake can be dropped when the FSF patch is dropped
BuildRequires:	autoconf
BuildRequires:	automake
Recommends:	xplanet
Recommends:	sox
Recommends:	cwdaemon
# Backported from upstream
Patch:		tlf-1.4.1-hamlib-4.2-build-fix.patch
# Fixed FSF address, updated license to the current license text
# https://github.com/Tlf/tlf/pull/270
Patch:		tlf-1.4.1-fsf-address-fix.patch
# Already fixed upstream, but different way which is not easily backportable,
# no upstream release yet
Patch:		tlf-1.4.1-format-security-fix.patch
Patch:		tlf-c99.patch
# Already fixed in the upstream git
Patch:		tlf-1.4.1-gcc-15-fix.patch
# Already fixed in the upstream git
Patch:		tlf-1.4.1-gcc-16-fix.patch

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
# it can be dropped when the FSF patch is dropped
autoreconf -fi
%configure --enable-fldigi-xmlrpc
%make_build

%install
%make_install

%check
cd test
make check

%files
%doc AUTHORS ChangeLog NEWS README.md
%doc %{_docdir}/%{name}/*
%license COPYING
%{_bindir}/tlf
%{_bindir}/play_vk
%{_bindir}/soundlog
%{_datadir}/%{name}
%{_mandir}/man1/*

%changelog
%autochangelog
