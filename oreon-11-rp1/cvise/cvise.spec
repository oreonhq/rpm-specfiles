%global source0_hash d015050cfc4015460ca5793378c4899a36104ddcf084f29f0f5f6233f6187cb1
Name: cvise
Version: 2.12.0
Release:        1%{?dist}
Summary:        Super-parallel Python port of the C-Reduce
License: LicenseRef-Callaway-BSD
URL: https://github.com/marxin/cvise
Source0:        https://github.com/marxin/cvise/archive/v%{version}.tar.gz
Requires: astyle
Requires: clang-tools-extra
Requires: unifdef
Requires: python3-pebble
Requires: python3-psutil
Requires: python3-chardet
Requires: indent
Requires: colordiff
# oreon:deps
BuildRequires:  astyle
BuildRequires:  clang-devel
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  indent
BuildRequires:  llvm-devel
BuildRequires:  make
BuildRequires:  ninja-build
BuildRequires:  python3-chardet
BuildRequires:  python3-pebble
BuildRequires:  python3-psutil
BuildRequires:  python3-pytest
BuildRequires:  unifdef
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
