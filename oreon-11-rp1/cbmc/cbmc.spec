%global source0_hash ee5f63da1388ba6c11885d335a49387ea97313ba160ac0d43a43f699aedc63a8

# FIXME: report to upstream
%define _lto_cflags %{nil}

%define utils_version 1.3

Name:           cbmc
Version:        6.8.0
Release:        1%{?dist}
Summary:        Bounded Model Checker for ANSI-C and C++ programs

License:        BSD-4-Clause
URL:            https://www.cprover.org/cbmc

Source0:        https://github.com/diffblue/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/aufover/%{name}-utils/archive/v%{utils_version}/%{name}-utils-%{utils_version}.tar.gz

# Implements https://github.com/diffblue/cbmc/issues/5965
Patch:         %{name}-add-cmd-line-arg.patch
# Fix compilation on F41+
Patch:         %{name}-f41-fix-build.patch

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

%ifarch x86_64
# For the tests
BuildRequires:  cvc5
BuildRequires:  gdb
BuildRequires:  jq
BuildRequires:  perl
BuildRequires:  python3
BuildRequires:  z3

# For %%py3_shebang_fix
BuildRequires:  python3-devel
%endif

Requires:       gcc-c++

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

# Remove Cprover API stuff because static libraries are not allowed!
rm -rf %{buildroot}%{_includedir}
rm -rf %{buildroot}%{_libdir}/libcprover.*.a

# FIXME: Report to upstream that the target directory for completions is wrong!
mkdir -p %{buildroot}%{bash_completions_dir}
mv %{buildroot}{/usr/etc/bash_completion.d/cbmc,%{bash_completions_dir}}

%ifarch x86_64
%check
# Fix unversioned shebang!
%py3_shebang_fix scripts/cpplint.py

# The tests were written with the assumption that they would be executed on
# an x86_64.  Other platforms suffer a large number of spurious test failures.
%ctest --label-regex CORE
%ctest --tests-regex unit-xfail
%endif

%files
%doc README.md
%license LICENSE
%{_bindir}/cbmc
%{_bindir}/cprover
%{_bindir}/crangler
%{_bindir}/goto-*
%{_bindir}/ls_parse.py
%{_bindir}/symtab2gb
%{bash_completions_dir}
%{_mandir}/man1/cbmc*.1.*
%{_mandir}/man1/crangler*.1.*
%{_mandir}/man1/goto-*.1.*
%ifarch %{ix86} x86_64
%{_mandir}/man1/memory-analyzer.1.*
%endif
%{_mandir}/man1/symtab2gb.1.*

%files doc
%doc %{__cmake_builddir}/doc/html README.md TOOLS_OVERVIEW.md
%license LICENSE

%files utils
%license ../%{name}-utils-%{utils_version}/LICENSE
%{_bindir}/%{name}-convert-output
%{_bindir}/csexec-%{name}

%changelog
%autochangelog
