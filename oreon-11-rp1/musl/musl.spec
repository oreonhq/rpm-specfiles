%global source0_hash d585fd3b613c66151fc3249e8ed44f77020cb5e6c1e635a616d3f9f82460512a
%bcond_with system_libc
%bcond_with multiarch
%bcond_without crossmode
%ifarch %{x86_64}
%global _musl_target_cpu x86_64
%endif
%ifarch %{ix86}
%global _musl_target_cpu i386
%endif
%ifarch %{arm}
%ifarch armv3l armv4b armv4l armv4tl armv5tl armv5tel armv5tejl armv6l armv7l
%global _musl_target_cpu arm
%else
%global _musl_target_cpu armhf
%endif
%global _musl_platform_suffix eabi
%endif
%ifarch %{mips64}
%global _musl_target_cpu mips64
%endif
%ifarch %{mips32}
%global _musl_target_cpu mips
%endif
%ifarch ppc
%global _musl_target_cpu powerpc
%endif
%ifarch %{power64}
%ifarch ppc64le
%global _musl_target_cpu powerpc64le
%else
%global _musl_target_cpu powerpc64
%endif
%endif
%ifnarch %{x86_64} %{ix86} %{arm} %{mips} %{power64} ppc
%global _musl_target_cpu %{_target_cpu}
%endif
%global _musl_platform %{_musl_target_cpu}-linux-musl%{?_musl_platform_suffix}
%if %{without crossmode}
%if %{without system_libc}
%if %{without multiarch}
%global _libdir %{_prefix}/%{_lib}/%{_musl_platform}
%else
%global _libdir %{_prefix}/lib/%{_musl_platform}
%endif
%global _includedir %{_prefix}/include/%{_musl_platform}
%endif
%else
%global _libdir %{_prefix}/%{_musl_platform}/%{_lib}
%global _includedir %{_prefix}/%{_musl_platform}/include
%endif
%if %{without multiarch}
%global _syslibdir /%{_lib}
%else
%global _syslibdir /lib
%endif
Name:		musl
Version:	1.2.6
Release:        1%{?dist}
Summary:        Fully featured lightweight standard C library for Linux
License:	MIT
URL:		https://musl.libc.org
Source0:        https://%{name}.libc.org/releases/%{name}-%{version}.tar.gz
Source1:	%{url}/releases/%{name}-%{version}.tar.gz.asc
Source2:	%{url}/musl.pub
Patch0:		musl-1.1.18-Makefile-rename-INSTALL-var.patch
Patch1:		musl-1.2.0-Support-static-pie-with-musl-gcc-specs.patch
Patch10:        https://git.musl-libc.org/cgit/musl/patch/?id=fde29c04adbab9d5b081bf6717b5458188647f1c#/musl-1.2.5-stdio-skip-empty-iovec-when-buffering-is-disabled.patch
ExclusiveOS:	linux
ExcludeArch:	s390
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
# /oreon:deps
%description
musl is a C standard library to power a new generation
of Linux-based devices. It is lightweight, fast, simple,
free, and strives to be correct in the sense of standards
conformance and safety.

%package libc
Summary:	Fully featured lightweight standard C library for Linux
Obsoletes:	%{name}-libs < %{version}-%{release}
Provides:	%{name}-libs = %{version}-%{release}
Provides:	%{name}-libs%{?_isa} = %{version}-%{release}
%if %{without system_libc}
Requires:	%{name}-filesystem%{?_isa} = %{version}-%{release}
%endif
%description libc
musl is a C standard library to power a new generation
of Linux-based devices. It is lightweight, fast, simple,
free, and strives to be correct in the sense of standards
conformance and safety.

This package provides the system dynamic linker library.
It also provides the dynamic libraries for linking
programs and libraries against musl.

%if %{without system_libc}
%package filesystem
Summary:	Base filesystem for %{name}
%description filesystem
musl is a C standard library to power a new generation
of Linux-based devices. It is lightweight, fast, simple,
free, and strives to be correct in the sense of standards
conformance and safety.

This package provides the base filesystem directories
for libraries and headers linked against musl.
%endif

%package devel
Summary:	Development files for %{name}
Provides:	%{name}-headers = %{version}-%{release}
Provides:	%{name}-headers%{?_isa} = %{version}-%{release}
Requires:	%{name}-libc = %{version}-%{release}
%description devel
musl is a C standard library to power a new generation
of Linux-based devices. It is lightweight, fast, simple,
free, and strives to be correct in the sense of standards
conformance and safety.

This package provides the development files for using
musl with programs and libraries.

%package libc-static
Summary:	Static link library for %{name}
Obsoletes:	%{name}-static < %{version}-%{release}
Provides:	%{name}-static = %{version}-%{release}
Provides:	%{name}-static%{?_isa} = %{version}-%{release}
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}
%description libc-static
musl is a C standard library to power a new generation
of Linux-based devices. It is lightweight, fast, simple,
free, and strives to be correct in the sense of standards
conformance and safety.

This package provides the additional development files for
statically linking musl into programs and libraries.

%package gcc
Summary:	Wrapper for using gcc with musl
Requires:	%{name}-devel = %{version}-%{release}
Requires:	gcc
%description gcc
musl is a C standard library to power a new generation
of Linux-based devices. It is lightweight, fast, simple,
free, and strives to be correct in the sense of standards
conformance and safety.

This package provides a wrapper around gcc to compile
programs and libraries with musl easily.

%package clang
Summary:	Wrapper for using clang with musl
Requires:	%{name}-devel = %{version}-%{release}
Requires:	clang
%description clang
musl is a C standard library to power a new generation
of Linux-based devices. It is lightweight, fast, simple,
free, and strives to be correct in the sense of standards
conformance and safety.

This package provides a wrapper around clang to compile
programs and libraries with musl easily.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Verify *before* actually unpacking!
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

# Unpack sources and apply patches
%autosetup -p1

%build

%define _lto_cflags %{nil}
%ifarch %{power64}
export CC="gcc -mlong-double-64"
%endif
export LDFLAGS="%{?build_ldflags} -Wl,-soname,ld-musl-%{_musl_target_cpu}.so.1"
%configure --enable-debug --enable-wrapper=all
%make_build
%install
%make_install
rm %{buildroot}/lib/ld-musl-%{_musl_target_cpu}.so.1
mv %{buildroot}%{_libdir}/libc.so %{buildroot}/lib/ld-musl-%{_musl_target_cpu}.so.1
ln -sr %{buildroot}/lib/ld-musl-%{_musl_target_cpu}.so.1 %{buildroot}%{_libdir}/ld-musl-%{_musl_target_cpu}.so.1
ln -sr %{buildroot}%{_libdir}/ld-musl-%{_musl_target_cpu}.so.1 %{buildroot}%{_libdir}/libc.so
mkdir -p %{buildroot}%{_sysconfdir}
touch %{buildroot}%{_sysconfdir}/ld-musl-%{_musl_target_cpu}.path
cat > %{buildroot}%{_sysconfdir}/ld-musl-%{_musl_target_cpu}.path <<EOF
%{_libdir}
EOF
%if %{without multiarch}
mkdir -p %{buildroot}%{_syslibdir}
%if "%{_lib}" == "lib64"
ln -sr %{buildroot}/lib/ld-musl-%{_musl_target_cpu}.so.1 %{buildroot}%{_syslibdir}/ld-musl-%{_musl_target_cpu}.so.1
%endif
%endif
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
touch %{buildroot}%{_rpmconfigdir}/macros.d/macros.musl
cat > %{buildroot}%{_rpmconfigdir}/macros.d/macros.musl <<EOF
%%_musl_libdir %{_libdir}
%%_musl_includedir %{_includedir}
EOF
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n musl-libc -f %{oreon_filedir}/musl-libc.list
%files -n musl-filesystem -f %{oreon_filedir}/musl-filesystem.list
%files -n musl-devel -f %{oreon_filedir}/musl-devel.list
%files -n musl-libc-static -f %{oreon_filedir}/musl-libc-static.list
%files -n musl-gcc -f %{oreon_filedir}/musl-gcc.list
%files -n musl-clang -f %{oreon_filedir}/musl-clang.list

%changelog

%autochangelog
