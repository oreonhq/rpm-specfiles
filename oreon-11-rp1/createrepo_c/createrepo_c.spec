# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 21d068aac366052d6de56d7f92aa58322547b5e4adaebdc001d1bb0a8dd260ce
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global libmodulemd_version 2.3.0

%define __cmake_in_source_build 1

%bcond doc_c 1
%bcond zchunk 1
%bcond libmodulemd 1

Name: createrepo_c
Version: 1.2.6
Release: 1%{?dist}
Summary: Creates a common metadata repository
License: GPL-2.0-or-later
URL: https://github.com/rpm-software-management/createrepo_c
Source0: https://github.com/rpm-software-management/createrepo_c/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: cmake >= 3.7.0
BuildRequires: make
BuildRequires: gcc
BuildRequires: bzip2-devel
%if %{with doc_c}
BuildRequires: doxygen
%endif
BuildRequires: glib2-devel >= 2.22.0
BuildRequires: libcurl-devel
BuildRequires: libxml2-devel
BuildRequires: openssl-devel
BuildRequires: rpm-devel >= 4.8.0-28
BuildRequires: sqlite-devel >= 3.6.18
BuildRequires: xz
BuildRequires: xz-devel
BuildRequires: zlib-devel
BuildRequires: pkgconfig(libzstd)
BuildRequires: bash-completion-devel
%if %{with zchunk}
BuildRequires: pkgconfig(zck) >= 0.9.11
BuildRequires: zchunk
%endif
%if %{with libmodulemd}
BuildRequires: pkgconfig(modulemd-2.0) >= %{libmodulemd_version}
BuildRequires: libmodulemd
Requires: libmodulemd%{?_isa} >= %{libmodulemd_version}
%endif
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: rpm >= 4.9.0

Obsoletes: createrepo < 0.11.0
Provides: createrepo = %{version}-%{release}

%description
C implementation of Createrepo.
A set of utilities (createrepo_c, mergerepo_c, modifyrepo_c)
for generating a common metadata repository from a directory of
rpm packages and maintaining it.

%package libs
Summary: Library for repodata manipulation

%description libs
Libraries for applications using the createrepo_c library
for easy manipulation with a repodata.

%package devel
Summary: Library for repodata manipulation
%if %{with doc_c}
License: GPL-2.0-or-later AND MIT
%endif
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains the createrepo_c C library and header files.
These development files are for easy manipulation with a repodata.

%package -n python3-%{name}
Summary: Python 3 bindings for the createrepo_c library
BuildRequires: python3-devel
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description -n python3-%{name}
Python 3 bindings for the createrepo_c library.

%prep
%oreon_sha256
%autosetup -p1
%py3_shebang_fix examples/python
mkdir build-py3

%build
pushd build-py3
  %cmake .. \
      -DBUILD_DOC_C=%{?with_doc_c:ON}%{!?with_doc_c:OFF} \
      -DWITH_ZCHUNK=%{?with_zchunk:ON}%{!?with_zchunk:OFF} \
      -DWITH_LIBMODULEMD=%{?with_libmodulemd:ON}%{!?with_libmodulemd:OFF} \
      -DWITH_LEGACY_HASHES=OFF \
      -DENABLE_DRPM=OFF \
      -DWITH_SANITIZERS=OFF
  %cmake_build
%if %{with doc_c}
  %cmake_build -t doc-c
%endif
popd

%install
pushd build-py3
  %cmake_install
popd

ln -sr %{buildroot}%{_bindir}/createrepo_c %{buildroot}%{_bindir}/createrepo
ln -sr %{buildroot}%{_bindir}/mergerepo_c %{buildroot}%{_bindir}/mergerepo
ln -sr %{buildroot}%{_bindir}/modifyrepo_c %{buildroot}%{_bindir}/modifyrepo

%check
pushd build-py3
  %cmake_build -t tests
  %ctest -V
popd

%ldconfig_scriptlets libs

%files
%doc README.md
%{_mandir}/man8/createrepo_c.8*
%{_mandir}/man8/mergerepo_c.8*
%{_mandir}/man8/modifyrepo_c.8*
%{_mandir}/man8/sqliterepo_c.8*
%{_datadir}/bash-completion/completions/*
%{_bindir}/createrepo_c
%{_bindir}/mergerepo_c
%{_bindir}/modifyrepo_c
%{_bindir}/sqliterepo_c
%{_bindir}/createrepo
%{_bindir}/mergerepo
%{_bindir}/modifyrepo

%files libs
%license COPYING
%{_libdir}/lib%{name}.so.*

%files devel
%if %{with doc_c}
%doc build-py3/doc/html
%endif
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}/

%files -n python3-%{name}
%doc examples/python/*
%{python3_sitearch}/%{name}/
%{python3_sitearch}/%{name}-*.dist-info

%changelog
%autochangelog
