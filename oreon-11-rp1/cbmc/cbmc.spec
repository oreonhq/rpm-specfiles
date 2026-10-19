%global source1_hash ee5f63da1388ba6c11885d335a49387ea97313ba160ac0d43a43f699aedc63a8
%global source0_hash 217e5ed631bbd4b39659fde37a603482003605abd4cb2586b09c2da344d925db
%define _lto_cflags %{nil}
%define utils_version 1.3
Name:           cbmc
Version:        6.11.0
Release:        1%{?dist}
Summary:        Bounded Model Checker for ANSI-C and C++ programs
License:        BSD-4-Clause
URL:            https://www.cprover.org/cbmc
Source0:        https://github.com/diffblue/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/aufover/%{name}-utils/archive/v%{utils_version}/%{name}-utils-%{utils_version}.tar.gz
Patch:         %{name}-add-cmd-line-arg.patch
Patch:         %{name}-f41-fix-build.patch
%ifarch x86_64
%endif
Requires:       gcc-c++
# oreon:deps
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  glpk-devel
BuildRequires:  minisat2-devel
BuildRequires:  ninja-build
BuildRequires:  zlib-devel
# /oreon:deps
%description
CBMC generates traces that demonstrate how an assertion can be violated, or
proves that the assertion cannot be violated within a given number of loop
iterations.

%package doc
Summary:        Documentation for %{name}
%description doc
Documentation for %{name}.

%package utils
Summary:        Output conversion utilities for CBMC
%description utils
Output conversion utilities for CBMC (GCC like format).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -T -q -b 1 -n %{name}-utils-%{utils_version}
%autosetup -p1 -b 0 -S git_am -n %{name}-%{name}-%{version}

sed -i 's/-Werror//g' CMakeLists.txt src/ansi-c/library_check.sh src/config.inc

%build

%cmake -GNinja -DWITH_JBMC:BOOL=OFF \
               -Dsat_impl:STRING=system-minisat2 \
%ifarch %{ix86} x86_64
               -DWITH_MEMORY_ANALYZER:BOOL=ON \
%endif
               -DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build
%cmake_build --target doc
%install
%cmake_install
install -p -m 0755 "%{_builddir}/%{name}-utils-%{utils_version}/cbmc_utils/formatCBMCOutput.py" %{buildroot}%{_bindir}/%{name}-convert-output
install -p -m 0755 "%{_builddir}/%{name}-utils-%{utils_version}/cbmc_utils/csexec-cbmc.sh" %{buildroot}%{_bindir}/csexec-%{name}
rm -rf %{buildroot}%{_includedir}
rm -rf %{buildroot}%{_libdir}/libcprover.*.a
mkdir -p %{buildroot}%{bash_completions_dir}
mv %{buildroot}{/usr/etc/bash_completion.d/cbmc,%{bash_completions_dir}}
%ifarch x86_64
%oreon_autofiles cbmc-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cbmc-utils usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%py3_shebang_fix scripts/cpplint.py
%ctest --label-regex CORE
%ctest --tests-regex unit-xfail
%endif
%files -f %{oreon_filedir}/main.list
%files -n cbmc-doc -f %{oreon_filedir}/cbmc-doc.list
%files -n cbmc-utils -f %{oreon_filedir}/cbmc-utils.list

%changelog

%autochangelog
