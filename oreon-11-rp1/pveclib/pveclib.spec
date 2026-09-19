%global source0_hash 0edba4459af00939cc0bc12341a0a12b71ef70cd52d7de076992ceb9f71b2baf

Name:    pveclib
Version: 1.0.4.5
Release: 20%{?dist}
Summary: Library for simplified access to PowerISA vector operations
License: Apache-2.0
URL:     https://github.com/open-power-sdk/pveclib
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

ExclusiveArch: ppc %{power64}
BuildRequires: make
BuildRequires: libtool autoconf-archive gcc-c++
%{?el7:BuildRequires: devtoolset-9-gcc-c++}

%description
A library of useful vector operations for PowerISA 2.06 or later. Pveclib
builds on the PPC vector built-ins provided by <altivec.h> to provide higher
level operations. These operations also bridge gaps in compiler builtin
support for the latest PowerISA and functional differences between versions
of the PowerISA. The intent is to improve the productivity of application
developers who need to optimize their applications or dependent libraries for
POWER. This release also adds the "vec_int512_ppc.h" interface with supporting
runtime libraries. The DSO support IFUNC selection for power8/9.

%package devel
Summary: Header files for pveclib
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Contains header files for using pveclib operations as inline vector
instructions.

%package static
Summary:  This package contains static libraries for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description static
This package contains static libraries for pveclib.
So far only constant vectors used in conversions and
target specific version of the int512 runtime.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%define __cflags_arch_ppc64le %{-O3 -g}
# use project's compiler/linker flags for tests
%undefine _auto_set_build_flags
# disable LTO. Most operations are static inline and int512
# runtime is specifically tuned to avoid register spill.
%global _lto_cflags %nil
# don't use distro -mcpu/-mtune flags, they conflict with the use of IFUNC
%global __cflags_arch_ppc64le %nil
# filter out -O2 as we want to use -O3
%global optflags $(echo %optflags | sed -e 's/-O2//g')

%{?el7:source /opt/rh/devtoolset-9/enable}
%configure --docdir=%{_docdir}/%{name}
%make_build

%install
%make_install

%check
%{?el7:source /opt/rh/devtoolset-9/enable}
# do not fail on test failures as builder might not support all required features
make check || :

# we are installing it using doc
find %{buildroot} -type f -name "*.la" -delete
find %{buildroot} -type f -name "libpvec.a" -delete
find %{buildroot} -type l -name "libpvecstatic.so" -delete
find %{buildroot} -type l -name "libpvecstatic.so.0" -delete
find %{buildroot} -type f -name "libpvecstatic.so.0.0.0" -delete
find %{buildroot} -type f -name "libpvecstatic.so.0.0.0*.debug" -delete

%files
%license LICENSE COPYING
%doc COPYING README.md CONTRIBUTING.md ChangeLog.md
%{_libdir}/libpvec.so.1
%{_libdir}/libpvec.so.1.*
%{?el7:%exclude %{_docdir}/%{name}}
%{?el7:%exclude %{_datadir}/licenses/%{name}}

%files devel
%doc README.md
%{_libdir}/libpvec.so
%{_includedir}/pveclib

%files static
%doc README.md
%{_libdir}/libpvecstatic.a

%changelog
%autochangelog
