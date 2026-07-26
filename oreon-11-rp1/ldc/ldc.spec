%global source0_hash 9bb0f628f869f7fc7b53c381a79742d29c17552c6f1a56b0a02aa289e65a0e3b

%global llvm_version 20
%global soversion 112

# bootstrapping is used for updating LDC to a newer version: it relies on an
# older, working LDC compiler in the buildroot, which is then used to build a
# new intermediate LDC version, and finally this in turn is used to build the
# final compiler that gets installed in the rpm.
%bcond_with bootstrap

%undefine _hardened_build
%undefine _package_note_file

Name:           ldc
Epoch:          1
Version:        1.42.0
Release:        2%{?dist}
Summary:        LLVM D Compiler

# The DMD frontend in dmd/* GPL version 1 or artistic license
# The files gen/asmstmt.cpp and gen/asm-*.hG PL version 2+ or artistic license
License:        BSD
URL:            https://github.com/ldc-developers/ldc
Source0:        https://github.com/ldc-developers/ldc/releases/download/v%{version}/%{name}-%{version}-src.tar.gz
Source3:        macros.%{name}

# Make sure /usr/include/d is in the include search path
Patch:          ldc-include-path.patch
# Don't add rpath to standard libdir
Patch:          ldc-no-default-rpath.patch

ExclusiveArch:  %{ldc_arches} ppc64le

BuildRequires:  bash-completion
BuildRequires:  cmake
BuildRequires:  compiler-rt%{?llvm_version}
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ldc
BuildRequires:  libconfig-devel
BuildRequires:  libcurl-devel
BuildRequires:  libedit-devel
BuildRequires:  llvm%{?llvm_version}-devel
BuildRequires:  llvm%{?llvm_version}-static
BuildRequires:  make
BuildRequires:  zlib-devel

Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
# Require gcc for linking
Requires:       gcc
Requires:       zlib-devel
# Recommend compiler-rt for PGO, sanitizers and fuzzing
Recommends:     compiler-rt%{?llvm_version}

%description
LDC is a portable compiler for the D programming language with modern
optimization and code generation capabilities.

It uses the official DMD compiler frontend to support the latest version
of D, and relies on the LLVM Core libraries for code generation.

%package        libs
Summary:        LLVM D Compiler libraries
# Automatically converted from old format: Boost - review is highly recommended.
License:        BSL-1.0

%description    libs
LDC is a portable compiler for the D programming language with modern
optimization and code generation capabilities.

This package contains the Phobos D standard library and the D runtime library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}-src -p1

# Remove bundled zlib
rm -fr runtime/phobos/etc/c/zlib

%build
# This package appears to be failing because links to the LLVM plugins
# are not installed which results in the tools not being able to
# interpret the .o/.a files.  Disable LTO for now
%define _lto_cflags %{nil}

%global optflags %{optflags} -fno-strict-aliasing

%if %{with bootstrap}
mkdir build-bootstrap
pushd build-bootstrap
cmake -DLLVM_CONFIG:PATH=llvm-config%{?llvm_version:-%{llvm_version}} \
      -DPHOBOS_SYSTEM_ZLIB=ON \
      ..
make %{?_smp_mflags}
popd
%endif

%cmake -DMULTILIB:BOOL=OFF \
       -DINCLUDE_INSTALL_DIR:PATH=%{_prefix}/lib/ldc/%{_target_platform}/include/d \
       -DBASH_COMPLETION_COMPLETIONSDIR:PATH=%{_datadir}/bash-completion/completions \
       -DLLVM_CONFIG:PATH=llvm-config%{?llvm_version:-%{llvm_version}} \
       -DCOMPILER_RT_BASE_DIR:PATH=%{_prefix}/lib/clang \
       -DPHOBOS_SYSTEM_ZLIB=ON \
%if %{with bootstrap}
       -DD_COMPILER:PATH=`pwd`/build-bootstrap/bin/ldmd2 \
%endif
       %{nil}

%cmake_build

%install
%cmake_install

# macros for D package
mkdir -p %{buildroot}/%{_rpmconfigdir}/macros.d/
install --mode=0644 %{SOURCE3} %{buildroot}%{_rpmconfigdir}/macros.d/macros.ldc

%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/ldc2.conf
%{_bindir}/ldc2
%{_bindir}/ldmd2
%{_bindir}/ldc-build-plugin
%{_bindir}/ldc-build-runtime
%{_bindir}/ldc-profdata
%{_bindir}/ldc-profgen
%{_bindir}/ldc-prune-cache
%{_bindir}/timetrace2txt
%{_rpmconfigdir}/macros.d/macros.ldc
%dir %{_prefix}/lib/ldc
%dir %{_prefix}/lib/ldc/%{_target_platform}
%dir %{_prefix}/lib/ldc/%{_target_platform}/include
%{_prefix}/lib/ldc/%{_target_platform}/include/d/
%{_libdir}/ldc_rt.dso.o
%{_libdir}/libdruntime-ldc-debug-shared.so
%{_libdir}/libdruntime-ldc-shared.so
%{_libdir}/libphobos2-ldc-debug-shared.so
%{_libdir}/libphobos2-ldc-shared.so
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/ldc2

%files libs
%license runtime/phobos/LICENSE_1_0.txt
%{_libdir}/libdruntime-ldc-debug-shared.so.%{soversion}*
%{_libdir}/libdruntime-ldc-shared.so.%{soversion}*
%{_libdir}/libphobos2-ldc-debug-shared.so.%{soversion}*
%{_libdir}/libphobos2-ldc-shared.so.%{soversion}*

%changelog
%autochangelog
