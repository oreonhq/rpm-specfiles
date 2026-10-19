%global source0_hash a4b1742f997f83e1056142d556a8c20845ba764b70365ff9ccf2e3f81c427b2b
%bcond cuefile 0
%global build_type_safety_c 2
%global svn_release 475
%global _legacy_common_support 1
Summary:        Musepack audio decoding library
Name:	 libmpcdec
Version: 1.3.0^20110810svn%{svn_release}
Release:        1%{?dist}
License: BSD-3-Clause
URL: 	 https://www.musepack.net/
Source0:        https://files.musepack.net/source/musepack_src_r475.tar.gz
Patch:   0001-changes-a-seeking-behavior-that-confused-some-people.patch
Patch:   0002-removed-some-gcc-warnings-and-compilation-issues.patch
Patch:   0003-prevent-endless-loops.patch
Patch:   0004-add-extern-keyword-to-global-variable-declaration-do.patch
Patch:   0005-add-raw-output-to-mpcdec-not-really-tested.patch
Patch:   0008-FSF-address-change.patch
Patch:   0011-removed-some-new-gcc-warnings.patch
Patch:   0012-mpcenc-remove-compilation-error-and-a-warning.patch
Patch:   0013-mpc2sv8-fix-a-segfault-caused-by-commit-r476.patch
Patch:  r475-cmake.patch
%if %{with cuefile}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libreplaygain-devel
BuildRequires:  sed
# /oreon:deps
%description
Musepack is an audio compression format with a strong emphasis on high quality.
It's not lossless, but it is designed for transparency, so that you won't be
able to hear differences between the original wave file and the much smaller
MPC file.
It is based on the MPEG-1 Layer-2 / MP2 algorithms, but has rapidly developed
and vastly improved and is now at an advanced stage in which it contains
heavily optimized and patentless code.

%package devel
Summary: Development files for the Musepack audio decoding library
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package -n musepack-tools
Summary: Musepack audio decoding and encoding tools
License: BSD-3-Clause AND LGPL-2.1-or-later
Requires: %{name}%{?_isa} = %{version}-%{release}
%description -n musepack-tools
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n musepack_src_r%{svn_release}

%if %{without cuefile}
sed -i -e '/add_subdirectory.*mpcchap/d' CMakeLists.txt
%endif

# Correct permissions and end of line
find -type f -exec chmod 0644 '{}' +
sed -ibackup 's/\r$//' libwavformat/*

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -Wno-dev .
%cmake_build
%install
%cmake_install
%oreon_autofiles musepack-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n libmpcdec-devel -f %{oreon_filedir}/libmpcdec-devel.list
%files -n musepack-tools -f %{oreon_filedir}/musepack-tools.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.0^20110810svn%{svn_release}-1
- Prepare for Oreon 11 (RP1)
