%global source0_hash bca4ac1e982a2d923ccd24cce2c98f4ceeed5009694430f73fc0dcebca8f098f

%global _hardened_build 1
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name: fstrm
Summary: Frame Streams implementation in C
Version: 0.6.1
Release: 14%{?dist}
License: MIT AND NTP
URL: https://github.com/farsightsec/fstrm
Source0:        https://dl.farsightsecurity.com/dist/%{name}/%{name}-%{version}.tar.gz
# Patches to libmy library
# https://github.com/farsightsec/libmy/pull/4
Patch1: fstrm-0.6.1-Fix-deadcode-and-check-return-code.patch
Patch2: fstrm-0.6.1-Invalid-dereference.patch
Patch3: fstrm-0.6.1-Possible-resource-leak-fix.patch
Patch4: fstrm-0.6.1-Fix-CLANG_WARNING.patch
BuildRequires: autoconf automake libtool
BuildRequires: libevent-devel
# Upstream repository without a single release
# https://github.com/farsightsec/libmy
# Always included as sources copy in farsightsec projects
Provides: bundled(libmy)

%description
Frame Streams is a light weight, binary clean protocol that allows for the
transport of arbitrarily encoded data payload sequences with minimal framing
overhead -- just four bytes per data frame. Frame Streams does not specify
an encoding format for data frames and can be used with any data serialization
format that produces byte sequences, such as Protocol Buffers, XML, JSON,
MessagePack, YAML, etc.

%package utils
Summary: Frame Streams (fstrm) utilities
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
Frame Streams is a light weight, binary clean protocol that allows for the
transport of arbitrarily encoded data payload sequences with minimal framing
overhead -- just four bytes per data frame. Frame Streams does not specify
an encoding format for data frames and can be used with any data serialization
format that produces byte sequences, such as Protocol Buffers, XML, JSON,
MessagePack, YAML, etc.

The fstrm-utils package contains command line utilities.

%package devel
Summary: Development Files for fstrm library
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The fstrm-devel package contains header files required to build an application
using fstrm library.

%package doc
Summary: API documentation for fstrm library
BuildArch: noarch
BuildRequires: doxygen
BuildRequires: make
Requires: %{name} = %{version}-%{release}

%description doc
The fstrm-doc package contains Doxygen generated API documentation for
fstrm library.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1
# regenerated build scripts to:
# - remove RPATHs
# - allow dynamic linking and execution of 'make check'
autoreconf -fi

%build
%configure --disable-static
%make_build
make html

%install
# install the library
%make_install
rm %{buildroot}%{_libdir}/libfstrm.la

# install documentation
mkdir -p %{buildroot}%{_pkgdocdir}/
cp -ar html %{buildroot}%{_pkgdocdir}/html

%check
make check

%if 0%{?fedora} || 0%{?rhel} > 7
# https://fedoraproject.org/wiki/Changes/Removing_ldconfig_scriptlets
%else
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif

%files
%doc COPYRIGHT LICENSE
%exclude %{_pkgdocdir}/html
%{_libdir}/libfstrm.so.*

%files utils
%{_bindir}/fstrm_capture
%{_bindir}/fstrm_dump
%{_bindir}/fstrm_replay
%{_mandir}/man1/fstrm_*

%files devel
%doc README.md
%{_includedir}/fstrm.h
%{_includedir}/fstrm/
%{_libdir}/pkgconfig/libfstrm.pc
%{_libdir}/libfstrm.so

%files doc
%doc %{_pkgdocdir}/html

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.1-14
- Prepare for Oreon 11 (RP1)
