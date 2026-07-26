%global source0_hash 5561c54d0629489fcf689ebacc4f8bc3b6305b02ef5675a5d9669dc6669fd6e7

%global driver asekey
%global dropdir %(pkg-config libpcsclite --variable usbdropdir 2>/dev/null)
%global rulesdir %(pkg-config udev --variable udevdir 2>/dev/null)/rules.d

Name:           pcsc-lite-%{driver}
Version:        3.7
Release:        28%{dist}
Summary:        ASEKey USB token driver
# 92_pcscd_asekey.rules:    LGPLv2+
# other files:              BSD
# Automatically converted from old format: BSD and LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-LGPLv2+
# The address does not exist anymore.
URL:            http://www.athena-scs.com/
Source0:        %{url}docs/reader-drivers/%{driver}-%(echo %{version}|tr '.' '-')-tar.bz2
# Fix PCSC bundle
Patch0:         %{driver}-3.7-bundle.patch
# Fix GCC-8 warnings
Patch1:         %{driver}-3.7-Fix-compiler-warnings.patch
BuildRequires:  gcc
BuildRequires:  libusb-compat-0.1-devel
BuildRequires:  make
BuildRequires:  pkgconfig(libpcsclite) >= 1.8.0
BuildRequires:  pkgconfig(udev)
BuildRequires:  sed
Requires:       pcsc-lite >= 1.8.0
Requires(post):     systemd
Requires(postun):   systemd
Provides:       pcsc-ifd-handler

%global __provides_exclude_from %{?__provides_exclude_from:%{__provides_exclude_from}|}^%{dropdir}

%description
This is a driver for the ASEKey USB cryptographic token in form of a PCSC
plug-in.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{driver}-%{version}

%build
%configure --with-udev-rules-dir="%{rulesdir}"
# Work around bug #893432:
# All platforms calls the compiler without "-gnu" suffix, except armv7hl which
# uses "-gnueabi" suffix.
%ifarch armv7hl
sed -i -e '/^BUILD=/ s/-gnu$/-gnueabi/' Makefile.inc
%else
sed -i -e '/^BUILD=/ s/-gnu$//' Makefile.inc
%endif
%{make_build}

%install
%{make_install}

%post
/bin/systemctl try-restart pcscd.service >/dev/null 2>&1 || :

%postun
/bin/systemctl try-restart pcscd.service >/dev/null 2>&1 || :

%files
%license LICENSE
%doc ChangeLog README
%{dropdir}/ifd-ASEKey.bundle
%{rulesdir}/*

%changelog
%autochangelog
