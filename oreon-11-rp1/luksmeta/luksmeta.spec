%global source0_hash a842538ba39680c8319c41dac0bcc082fe40fb43342561761925c0daa1a48f28

Name:           luksmeta
Version:        10
Release:        %autorelease
Summary:        Utility for storing small metadata in the LUKSv1 header

License:        LGPL-2.1-or-later
URL:            https://github.com/latchset/%{name}
Source0:        https://github.com/latchset/luksmeta/releases/download/v10/luksmeta-10.tar.bz2

BuildRequires:  gcc
BuildRequires:  asciidoc
BuildRequires:  pkgconfig
BuildRequires:  cryptsetup-devel
BuildRequires:  cryptsetup
BuildRequires: make
Requires: lib%{name}%{?_isa} = %{version}-%{release}

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install
rm -rf %{buildroot}/%{_libdir}/libluksmeta.la

%check
make %{?_smp_mflags} check

%ldconfig_scriptlets -n lib%{name}

%files
%{_bindir}/luksmeta
%{_mandir}/man8/luksmeta.8*

%files -n lib%{name}
%license COPYING
%{_libdir}/libluksmeta.so.*

%files -n lib%{name}-devel
%{_includedir}/luksmeta.h
%{_libdir}/libluksmeta.so
%{_libdir}/pkgconfig/luksmeta.pc

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 10-1
- Import
