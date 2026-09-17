%global source0_hash 7e3e473843aa79afb98f581d2e100efa47db80df3a961565b691d7b4a4ebd14b

Name: cvise
Version: 2.11.0
Release: 2%{?dist}
Summary: Super-parallel Python port of the C-Reduce
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: https://github.com/marxin/cvise
Source: https://github.com/marxin/cvise/archive/v%{version}.tar.gz

BuildRequires: astyle
BuildRequires: cmake
BuildRequires: flex
BuildRequires: llvm-devel
BuildRequires: unifdef
BuildRequires: clang-devel
BuildRequires: ninja-build
BuildRequires: indent
BuildRequires: gcc-c++
BuildRequires: python3-pebble
BuildRequires: python3-pytest
BuildRequires: python3-psutil
BuildRequires: python3-chardet
BuildRequires: make

Requires: astyle
Requires: clang-tools-extra
Requires: unifdef
Requires: python3-pebble
Requires: python3-psutil
Requires: python3-chardet
Requires: indent
Requires: colordiff

%description
C-Vise is a super-parallel Python port of the C-Reduce. The port is fully
compatible to the C-Reduce and uses the same efficient
LLVM-based C/C++ reduction tool named clang_delta.

C-Vise is a tool that takes a large C, C++ or OpenCL program that
has a property of interest (such as triggering a compiler bug) and
automatically produces a much smaller C/C++ or OpenCL program that
has the same property. It is intended for use by people who discover
and report bugs in compilers and other tools that process C/C++ or OpenCL code.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
export CXXFLAGS="$RPM_OPT_FLAGS -Wno-error=restrict"
%cmake -DCMAKE_SKIP_RPATH=TRUE -GNinja
%cmake_build

%check
%cmake_build --target test

%install
%cmake_install

%files
%license COPYING
%{_bindir}/cvise
%{_bindir}/cvise-delta
%dir %{_libexecdir}/cvise
%{_libexecdir}/cvise/clex
%{_libexecdir}/cvise/clang_delta
%{_libexecdir}/cvise/strlex
%{_libexecdir}/cvise/topformflat
%{_datadir}/cvise

%changelog
%autochangelog
