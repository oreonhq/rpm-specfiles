# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 0619da31af08152600af95c481527ef6d756c0a8404fca7544a4fdf6dfc2c0f9
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global common_desc %{expand:
Capstone is a disassembly framework with the target of becoming the ultimate
disasm engine for binary analysis and reversing in the security community.}

%define _lto_cflags %{nil}

Name: capstone
Version: 5.0.9
Release: 1%{?dist}
Summary: A lightweight multi-platform, multi-architecture disassembly framework
License: BSD-3-Clause AND BSD-4-Clause AND APSL-2.0 AND NCSA AND MIT
URL: https://www.capstone-engine.org/
Source0: https://github.com/capstone-engine/capstone/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: cstool.1

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: make
BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: pyproject-rpm-macros

%description
%{common_desc}

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%{common_desc}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package static
Summary: Static linking of %{name} library

%description static
%{common_desc}
The %{name}-static package contains files needed for static linking
of %{name} library into static binaries.

%package -n python3-capstone
Summary: Python3 bindings for %{name}
BuildArch: noarch
Provides: %{name}-python3 = %{version}-%{release}
Obsoletes: %{name}-python3 < %{version}-%{release}
Requires: %{name} = %{version}-%{release}

%description -n python3-capstone
%{common_desc}
The python3-capstone package contains python3 bindings for %{name}.

%prep
%oreon_sha256
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires --directory bindings/python

%build
V=1 CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" \
PREFIX="%{_prefix}" LIBDIRARCH="%{_lib}" INCDIR="%{_includedir}" \
%make_build CC=%{__cc} PYTHON3=%{__python3}
grep -v archive capstone.pc > capstone.pc.tmp
mv capstone.pc.tmp capstone.pc
pushd bindings/python
export LIBCAPSTONE_PATH=%{buildroot}%{_libdir}
%pyproject_wheel
popd

%install
DESTDIR=%{buildroot} PREFIX="%{_prefix}" LIBDIRARCH=%{_lib} \
INCDIR="%{_includedir}" make CC=%{__cc} install
find %{buildroot} -name '*.la' -delete
install -d %{buildroot}%{_mandir}/man1
install -p -m 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/
pushd bindings/python
%pyproject_install
%pyproject_save_files -l capstone
popd

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%pyproject_check_import
make CC=%{__cc} check
pushd bindings/python
export LIBCAPSTONE_PATH=%{buildroot}%{_libdir}
%pytest -sv -k "not testcb and not test_cs_disasm_quick" --ignore 'tests/test_sh.py'
popd

%files
%license LICENSE.TXT LICENSE_LLVM.TXT
%doc CREDITS.TXT ChangeLog README.md SPONSORS.TXT
%{_libdir}/libcapstone.so.5
%{_bindir}/cstool
%{_mandir}/man1/cstool.1*

%files devel
%{_includedir}/capstone/
%{_libdir}/libcapstone.so
%{_libdir}/pkgconfig/capstone.pc

%files static
%license LICENSE.TXT LICENSE_LLVM.TXT
%{_libdir}/libcapstone.a

%files -n python3-capstone -f %{pyproject_files}

%changelog
%autochangelog
