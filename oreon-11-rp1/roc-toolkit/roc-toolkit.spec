%global source0_hash 60501dfdc8c0de385898dbd1eb8239d93ef962667ddb064ad796b887a41a1a46
Name:		roc-toolkit
Version:	0.4.0
Release:        6%{?dist}
Summary:        Real-time audio streaming
License:	MPL-2.0 AND LGPL-2.1-or-later AND CECILL-C
URL:		https://github.com/roc-streaming/roc-toolkit
Source0:        https://github.com/roc-streaming/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:		roc-toolkit-0.3.0-no-explicit-cpp98.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cpputest-devel
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gengetopt
BuildRequires:  libsndfile-devel
BuildRequires:  libunwind-devel
BuildRequires:  libuv-devel
BuildRequires:  openfec-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  python3-breathe
BuildRequires:  python3-devel
BuildRequires:  python3-scons
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinxemoji
BuildRequires:  ragel
BuildRequires:  sox-devel
BuildRequires:  speexdsp-devel
# /oreon:deps
%description
Roc is a toolkit for real-time audio streaming over the network.

%package devel
Summary: Development libraries for roc-toolkit
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The roc-toolkit-devel package contains header files necessary for
developing programs using roc-toolkit.

%package utils
Summary: Utilities for roc-toolkit
Requires: %{name}%{?_isa} = %{version}-%{release}
%description utils
Utilities for roc-toolkit.

%package doc
Summary: Documentation for roc-toolkit
%description doc
Documentation for roc-toolkit.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

scons %{?_smp_mflags} --with-openfec-includes=%{_includedir}/openfec --libdir=%{_libdir} \
  CFLAGS="%{build_cflags}" CXXFLAGS="%{build_cxxflags}" LDFLAGS="%{build_ldflags}"
scons docs --enable-doxygen --enable-sphinx
%install
scons install --with-openfec-includes=%{_includedir}/openfec --prefix=%{buildroot}%{_prefix} \
  --libdir=%{buildroot}%{_libdir}
%ifnarch s390x
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

scons test --with-openfec-includes=%{_includedir}/openfec --enable-tests
%endif
%files -f %{oreon_filedir}/main.list
%files -n roc-toolkit-devel -f %{oreon_filedir}/roc-toolkit-devel.list
%files -n roc-toolkit-utils -f %{oreon_filedir}/roc-toolkit-utils.list
%files -n roc-toolkit-doc -f %{oreon_filedir}/roc-toolkit-doc.list

%changelog

%autochangelog

