%global source0_hash 5561c54d0629489fcf689ebacc4f8bc3b6305b02ef5675a5d9669dc6669fd6e7
%global driver asekey
%global dropdir %(pkg-config libpcsclite --variable usbdropdir 2>/dev/null)
%global rulesdir %(pkg-config udev --variable udevdir 2>/dev/null)/rules.d
Name:           pcsc-lite-%{driver}
Version:        3.7
Release:        1%{?dist}
Summary:        ASEKey USB token driver
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-LGPLv2+
URL:            http://www.athena-scs.com/
Source0:        http://www.athena-scs.com/docs/reader-drivers/%{driver}-3-7-tar.bz2
Patch0:         %{driver}-3.7-bundle.patch
Patch1:         %{driver}-3.7-Fix-compiler-warnings.patch
Requires:       pcsc-lite >= 1.8.0
Requires(post):     systemd
Requires(postun):   systemd
Provides:       pcsc-ifd-handler
%global __provides_exclude_from %{?__provides_exclude_from:%{__provides_exclude_from}|}^%{dropdir}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libusb-compat-0.1-devel
BuildRequires:  make
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:  pkgconfig(udev)
BuildRequires:  sed
# /oreon:deps
%description
This is a driver for the ASEKey USB cryptographic token in form of a PCSC
plug-in.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{driver}-%{version}

%build

%configure --with-udev-rules-dir="%{rulesdir}"
%ifarch armv7hl
sed -i -e '/^BUILD=/ s/-gnu$/-gnueabi/' Makefile.inc
%else
sed -i -e '/^BUILD=/ s/-gnu$//' Makefile.inc
%endif
%{make_build}
%install
%{make_install}
%oreon_autofiles main

%post

/bin/systemctl try-restart pcscd.service >/dev/null 2>&1 || :
%postun

/bin/systemctl try-restart pcscd.service >/dev/null 2>&1 || :
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
