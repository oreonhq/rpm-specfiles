%global source0_hash a842538ba39680c8319c41dac0bcc082fe40fb43342561761925c0daa1a48f28
Name:           luksmeta
Version:        10
Release:        1%{?dist}
Summary:        Utility for storing small metadata in the LUKSv1 header
License:        LGPL-2.1-or-later
URL:            https://github.com/latchset/%{name}
Source0:        https://github.com/latchset/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.bz2
Requires: lib%{name}%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  cryptsetup
BuildRequires:  cryptsetup-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
%description
LUKSMeta is a command line utility for storing small portions of metadata in
the LUKSv1 header for use before unlocking the volume.

%package -n lib%{name}
Summary:        Library for storing small metadata in the LUKSv1 header
%description -n lib%{name}
LUKSMeta is a C library for storing small portions of metadata in the LUKSv1
header for use before unlocking the volume.

%package -n lib%{name}-devel
Summary:        Development files for libluksmeta
Requires:       lib%{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
%description -n lib%{name}-devel
This package contains development files for the LUKSMeta library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir luksmeta-10
%oreon_prep
%build

%configure
%make_build
%install
rm -rf %{buildroot}
%make_install
rm -rf %{buildroot}/%{_libdir}/libluksmeta.la
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make %{?_smp_mflags} check
%ldconfig_scriptlets -n lib%{name}
%files -f %{oreon_filedir}/main.list
%files -n libluksmeta -f %{oreon_filedir}/libluksmeta.list
%files -n libluksmeta-devel -f %{oreon_filedir}/libluksmeta-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 10-1
- Import
