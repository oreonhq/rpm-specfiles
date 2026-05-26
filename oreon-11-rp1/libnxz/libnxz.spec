# Keep the *.la file around
# See 
%global __brp_remove_la_files %nil

Name:		libnxz
Version:	0.64
Release:	10%{?dist}
Summary:	Zlib implementation for POWER processors
License:    Apache-2.0 OR GPL-2.0-or-later
Url:		https://github.com/libnxz/power-gzip
BuildRequires:	zlib-devel
Source0:        https://github.com/libnxz/power-gzip/archive/v0.64/libnxz-0.64.tar.gz
# Fixes for GCC 14 and zlib-ng compat usage
Patch0:         %{url}/pull/209.patch
# oreon url source checksums begin
%global source0_sha256 86b11ad8b512204816241d5dd98ac0561d1f6b06180f658c532c3ffbc16925df
%global source0_file libnxz-0.64.tar.gz
# oreon url source checksums end

# Be explicit about the soname in order to avoid unintentional changes.
%global soname libnxz.so.0

ExclusiveArch:	ppc64le
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	systemd-rpm-macros

# udev rules for nx-gzip dev
Requires: powerpc-utils-core > 1.3.10-2

%description
libnxz is a zlib-compatible library that uses the NX GZIP Engine available on
POWER9 or newer processors in order to provide a faster zlib/gzip compression
without using the general-purpose cores.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains header files for developing application that
use %{name}.

%package	static
Summary:	Static library for %{name} development
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description	static
The %{name}-static package contains static libraries for developing
application that use %{name}.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libnxz-0.64.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "86b11ad8b512204816241d5dd98ac0561d1f6b06180f658c532c3ffbc16925df" || { echo "oreon: Source0 SHA256 mismatch for libnxz-0.64.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n power-gzip-%{version}

# Create a sysusers.d config file
cat >libnxz.sysusers.conf <<EOF
g nx-gzip -
EOF

%build
%configure --enable-zlib-api
%make_build

%check
# libnxz tests only work on P9 servers or newer, with Linux >= 5.8.
# This combination is not guaranteed to have at build time.  Check if
# NX GZIP engine device is available before deciding to run the tests.
if [[ -w "/dev/crypto/nx-gzip" ]]; then
	make check
fi

%install
%make_install

install -m0644 -D libnxz.sysusers.conf %{buildroot}%{_sysusersdir}/libnxz.conf


%files
%{_libdir}/%{soname}
%{_libdir}/libnxz.so.0.%{version}
%license %{_docdir}/%{name}/APACHE-2.0.txt
%license %{_docdir}/%{name}/gpl-2.0.txt
%doc README.md
%{_sysusersdir}/libnxz.conf

%files devel
%{_includedir}/libnxz.h
%{_libdir}/libnxz.so

%files static
%{_libdir}/libnxz.a
%{_libdir}/libnxz.la

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.64-10
- Import
