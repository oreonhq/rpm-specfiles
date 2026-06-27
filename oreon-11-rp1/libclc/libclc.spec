%global source0_hash none

# this stop us generating an empty debuginfo
%global debug_package %{nil}

%global shortname clc
%global libclc_version 22.1.1
#global rc_ver 3
%global src_tarball_dir llvm-project-%{libclc_version}%{?rc_ver:-rc%{rc_ver}}.src

Name:           libclc
Version:        %{libclc_version}%{?rc_ver:~rc%{rc_ver}}
Release:        1%{?dist}
Summary:        An open source implementation of the OpenCL 1.1 library requirements

License:        Apache-2.0 WITH LLVM-exception OR NCSA OR MIT
URL:            https://libclc.llvm.org
Source0:        https://github.com/llvm/llvm-project/releases/download/llvmorg-%{libclc_version}%{?rc_ver:-rc%{rc_ver}}/%{src_tarball_dir}.tar.xz
Source1:        https://github.com/llvm/llvm-project/releases/download/llvmorg-%{libclc_version}%{?rc_ver:-rc%{rc_ver}}/%{src_tarball_dir}.tar.xz.sig
Source2:        release-keys.asc

BuildRequires:  clang-devel >= %{version}
BuildRequires:  libedit-devel
BuildRequires:  llvm-devel >= %{version}
BuildRequires:  python-unversioned-command
BuildRequires:  zlib-devel
BuildRequires:  cmake
BuildRequires:  spirv-llvm-translator-tools

# For signature verification
BuildRequires:  gnupg2

Requires:       %{name}-spirv%{?_isa} = %{version}-%{release}

%description
libclc is an open source, BSD licensed implementation of the library
requirements of the OpenCL C programming language, as specified by the
OpenCL 1.1 Specification. The following sections of the specification
impose library requirements:

  * 6.1: Supported Data Types
  * 6.2.3: Explicit Conversions
  * 6.2.4.2: Reinterpreting Types Using as_type() and as_typen()
  * 6.9: Preprocessor Directives and Macros
  * 6.11: Built-in Functionsj
  * 9.3: Double Precision Floating-Point
  * 9.4: 64-bit Atomics
  * 9.5: Writing to 3D image memory objects
  * 9.6: Half Precision Floating-Point

libclc is intended to be used with the Clang compiler's OpenCL frontend.

libclc is designed to be portable and extensible. To this end, it provides
generic implementations of most library requirements, allowing the target
to override the generic implementation at the granularity of individual
functions.

libclc currently only supports the PTX target, but support for more
targets is welcome.


%package        spirv
Summary:        Spirv subset of %{name}

%description    spirv
The %{name}-spirv package contains the spirv*-mesa3d-.spv files only,
which are the subset required for upstream Mesa OpenCL support with RustiCL.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{src_tarball_dir}

%build
export CFLAGS="%{build_cflags} -D__extern_always_inline=inline"
%set_build_flags
cd libclc
%cmake -DCMAKE_INSTALL_DATADIR:PATH=%{_lib}

%cmake_build

%install
cd libclc
%cmake_install

%check
cd libclc
%cmake_build --target test

%files
%license libclc/LICENSE.TXT
%doc libclc/README.md libclc/CREDITS.TXT
%{_libdir}/%{shortname}/*.bc

%files spirv
%license libclc/LICENSE.TXT
%doc libclc/README.md libclc/CREDITS.TXT
%dir %{_libdir}/%{shortname}
%{_libdir}/%{shortname}/spirv-mesa3d-.spv
%{_libdir}/%{shortname}/spirv64-mesa3d-.spv

%files devel
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
