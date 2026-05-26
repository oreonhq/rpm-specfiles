# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 533946d57897bf62a2cf8f74e488258e11fa0c55028fad43ada24c5686f38a06
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Summary: Driver for QPDL/SPL2 printers (Samsung and several Xerox printers)
Name: splix
Version: 2.0.1
Release: 6%{?dist}
License: GPL-2.0-only
URL: https://openprinting.github.io/splix/
Source0: https://github.com/OpenPrinting/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz

# sent upstream as https://github.com/OpenPrinting/splix/pull/2
# IEEE 1284 Device IDs
Patch0: splix-deviceID.patch
# rules.mk misses LDFLAGS
Patch1: splix-ldflags.patch
Patch2: splix-use-pkg-conf.patch


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
%oreon_verify_sources
%setup -q

# remove old PPDs (not sure why some PPDs are outside ppd/)
rm -f *.ppd

pushd ppd
# remove old PPDs
make distclean
popd

%patch -P 0 -p1 -b .deviceID
%patch -P 1 -p1 -b .ldflags
%patch -P 2 -p1 -b .pkg-conf

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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.1-6
- Prepare for Oreon 11 (RP1)
