%global source0_hash 4c980c2b5938694d36ab3117eb286b9ffa7187c768ac66e7805662a3dd22edf1
%global libmodulemd_version 2.3.0
%define __cmake_in_source_build 1
%global bash_completion %{_datadir}/bash-completion/completions/*
%bcond_without drpm
%bcond_without zchunk
%bcond_without libmodulemd
%bcond_with legacy_hashes
%bcond_with sanitizers
%if %{defined gitrev}
%define package_version %{?gitrev}
%else
%define package_version 1.2.4
%endif
Summary:        Creates a common metadata repository
Name:           createrepo_c
Version:        %{package_version}
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            https://github.com/rpm-software-management/createrepo_c
Source0:        https://github.com/rpm-software-management/createrepo_c/archive/refs/tags/1.2.4.tar.gz#/createrepo_c-1.2.1.tar.gz
%global epoch_dep %{?epoch:%{epoch}:}
%if %{with zchunk}
%endif
%if %{with libmodulemd}
Requires:       libmodulemd%{?_isa} >= %{libmodulemd_version}
%endif
Requires:       %{name}-libs = %{epoch_dep}%{version}-%{release}
Requires: rpm >= 4.9.0
%if %{with drpm}
%endif
%if %{with sanitizers}
%endif
# oreon:deps
BuildRequires:  bash-completion-devel
BuildRequires:  bzip2-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  drpm-devel
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  libcurl-devel
BuildRequires:  libmodulemd
BuildRequires:  libxml2-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(modulemd-2.0)
BuildRequires:  pkgconfig(zck)
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  rpm-devel
BuildRequires:  sqlite-devel
BuildRequires:  xz
BuildRequires:  xz-devel
BuildRequires:  zchunk
BuildRequires:  zlib-devel
# /oreon:deps
%description
C implementation of Createrepo.
A set of utilities (createrepo_c, mergerepo_c, modifyrepo_c)
for generating a common metadata repository from a directory of
rpm packages and maintaining it.

%package libs
Summary:    Library for repodata manipulation
%description libs
Libraries for applications using the createrepo_c library
for easy manipulation with a repodata.

%package devel
Summary:    Library for repodata manipulation
Requires:   %{name}-libs%{?_isa} = %{epoch_dep}%{version}-%{release}
%description devel
This package contains the createrepo_c C library and header files.
These development files are for easy manipulation with a repodata.

%package -n python3-%{name}
Summary:        Python 3 bindings for the createrepo_c library
%{?python_provide:%python_provide python3-%{name}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
Requires:       %{name}-libs = %{epoch_dep}%{version}-%{release}
%description -n python3-%{name}
Python 3 bindings for the createrepo_c library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
%py3_shebang_fix examples/python
mkdir build-py3

%build

pushd build-py3
  %cmake .. \
      -DWITH_ZCHUNK=%{?with_zchunk:ON}%{!?with_zchunk:OFF} \
      -DWITH_LIBMODULEMD=%{?with_libmodulemd:ON}%{!?with_libmodulemd:OFF} \
      -DWITH_LEGACY_HASHES=%{?with_legacy_hashes:ON}%{!?with_legacy_hashes:OFF} \
      -DENABLE_DRPM=%{?with_drpm:ON}%{!?with_drpm:OFF} \
      -DWITH_SANITIZERS=%{?with_sanitizers:ON}%{!?with_sanitizers:OFF}
  %cmake_build
  %cmake_build -t doc-c
popd
%check

pushd build-py3
  %cmake_build -t tests
  %ctest -V
popd
%install
pushd build-py3
  %cmake_install
popd
%ldconfig_scriptlets libs
%oreon_autofiles createrepo_c-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles createrepo_c-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles python3-createrepo_c usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n createrepo_c-libs -f %{oreon_filedir}/createrepo_c-libs.list
%files -n createrepo_c-devel -f %{oreon_filedir}/createrepo_c-devel.list
%files -n python3-createrepo_c -f %{oreon_filedir}/python3-createrepo_c.list

%changelog

%autochangelog
