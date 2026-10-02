%global source0_hash 6271c35f8ab8d2565962c0a6140aa191226430f7c99cb3355f4d499a8938f068

Summary: Driver for QPDL/SPL2 printers (Samsung and several Xerox printers)
Name: splix
Version: 2.0.2
Release: 1%{?dist}
License: GPL-2.0-only
URL: https://openprinting.github.io/splix/
Source0:        https://github.com/OpenPrinting/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz

# sent upstream as https://github.com/OpenPrinting/splix/pull/2
# IEEE 1284 Device IDs
# rules.mk misses LDFLAGS


# postscriptdriver tags
BuildRequires: cups
# gcc-c++ is no longer in buildroot by default
BuildRequires: gcc-c++
# JBIG1 lossless image compression
BuildRequires: jbigkit-devel
# uses make
BuildRequires: make
# _cups_serverbin macro, CUPS and IPP API
BuildRequires: pkgconfig(cups)
# postscriptdriver tags
BuildRequires: python3-cups
# for pkg-config in configure and in SPEC file
BuildRequires: pkgconf-pkg-config

Requires: cups


%description
This driver is usable by all printer devices which understand the QPDL
(Quick Page Description Language) also known as SPL2 (Samsung Printer Language)
language. It covers several Samsung, Xerox and Dell printers.
Splix doesn't support old SPL(1) printers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

# remove old PPDs (not sure why some PPDs are outside ppd/)
rm -f *.ppd

pushd ppd
# remove old PPDs
make distclean
popd


%build
%set_build_flags
# *.drv.in -> *.drv
%make_build drv

CXXFLAGS="%{optflags} -fno-strict-aliasing" \
%make_build all V=1 DRV_ONLY=1 LDFLAGS="%{build_ldflags} -pie"

%install
%make_install DRV_ONLY=1 CUPSDRV=%{_datadir}/cups/drv/splix

%files
%license COPYING
%doc AUTHORS ChangeLog THANKS
%{_cups_serverbin}/filter/pstoqpdl
%{_cups_serverbin}/filter/rastertoqpdl
%{_datadir}/cups/drv/splix

%changelog
%autochangelog
