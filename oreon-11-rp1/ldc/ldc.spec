%global source0_hash d655aad0daf0ce9a17b2ffffb947bb79ec6968bc7fb88bc918316dbe78c616e7
%global llvm_version 20
%global soversion 112
%bcond_with bootstrap
%undefine _hardened_build
%undefine _package_note_file
Name:           ldc
Epoch:          1
Version:        1.43.0
Release:        1%{?dist}
Summary:        LLVM D Compiler
License:        BSD
URL:            https://github.com/ldc-developers/ldc
Source0:        https://github.com/ldc-developers/ldc/releases/download/v%{version}/%{name}-%{version}-src.tar.gz
Source3:        macros.%{name}
Patch:          ldc-include-path.patch
Patch:          ldc-no-default-rpath.patch
ExclusiveArch:  %{ldc_arches} ppc64le
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       gcc
Requires:       zlib-devel
Recommends:     compiler-rt%{?llvm_version}
# oreon:deps
BuildRequires:  bash-completion
BuildRequires:  cmake
BuildRequires:  compiler-rt20
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ldc
BuildRequires:  libconfig-devel
BuildRequires:  libcurl-devel
BuildRequires:  libedit-devel
BuildRequires:  llvm20-devel
BuildRequires:  llvm20-static
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
%description
LDC is a portable compiler for the D programming language with modern
optimization and code generation capabilities.

It uses the official DMD compiler frontend to support the latest version
of D, and relies on the LLVM Core libraries for code generation.

%package        libs
Summary:        LLVM D Compiler libraries
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
mkdir -p %{buildroot}/%{_rpmconfigdir}/macros.d/
install --mode=0644 %{SOURCE3} %{buildroot}%{_rpmconfigdir}/macros.d/macros.ldc
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ldc-libs -f %{oreon_filedir}/ldc-libs.list

%changelog

%autochangelog
