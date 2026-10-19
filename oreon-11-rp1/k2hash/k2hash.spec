%global source0_hash b9c592387482db97381017384c6e01ca5ec5440ff022e26803413956b0fae5cb
%if %{undefined package_revision}
%global package_revision 1
%endif
%if %{undefined make_build}
%global make_build %{__make} %{?_smp_mflags}
%endif
%if %{undefined autosetup}
%global autosetup %setup -q
%endif
%global release_version 1.0.103
%global gittag v%{release_version}
%if %{undefined make_check}
%global make_check 1
%endif
Summary:        NoSQL Key Value Store(KVS) tools and library
Name: k2hash
Version: %{release_version}
Release:        1%{?dist}
License: MIT
URL: https://github.com/yahoojapan/k2hash
Source0:        https://github.com/yahoojapan/%{name}/archive/%{gittag}/%{name}-%{version}.tar.gz
Requires: libfullock%{?_isa} >= 1.0.36
ExcludeArch: i686 armv7hl
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  libfullock-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  nss-devel
# /oreon:deps
%description
K2HASH provides a NoSQL(key value store) tools and a library under
MIT license. K2HASH tools create/write/read files or memory which
is allocated by K2HASH library. K2HASH library stores its data in 
three ways: on-memory, fully mapping file and partially mapping
file and directly accessing a file.

Please visit the website and get more details at:

https://github.com/yahoojapan/k2hash

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

./autogen.sh
%configure --disable-static --with-nss
%make_build
%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%{__make} check
find %{_builddir} -name '*.log' -exec echo {} ';'
find %{_builddir} -name '*.log' -exec cat {} ';'
%if %{defined ldconfig_scriptlets}
%ldconfig_scriptlets
%else
%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%endif
%package devel
Summary: NoSQL Key Value Store(KVS) tools and library (development)
Requires: %{name}%{?_isa} = %{version}-%{release}, libfullock-devel%{?_isa} >= 1.0.36
%description devel
Development package for building with k2hash shared library.
This package has header files and symbols for it.

%files -f %{oreon_filedir}/main.list
%files -n k2hash-devel -f %{oreon_filedir}/k2hash-devel.list

%changelog

%autochangelog
