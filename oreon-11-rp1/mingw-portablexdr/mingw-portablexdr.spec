%global source0_hash 5cf4bdd153cf4d44eaf10b725f451d0cfadc070b4b9a9ccfb64094b8f78de72c
%?mingw_package_header
Name:		mingw-portablexdr
Version:	4.9.1
Release:        1%{?dist}
Summary:        MinGW Windows PortableXDR / RPC Library
License:	LicenseRef-Callaway-LGPLv2+
URL:		https://people.redhat.com/~rjones/portablexdr/
Source0:        https://people.redhat.com/~rjones/portablexdr/files/portablexdr-%{version}.tar.gz
BuildArch:	noarch
Patch0:		portablexdr-4.9.1-no-config-h.patch
Patch1:		portablexdr-build-use-intptr_t-and-uintptr_t-to-cast-ptr-to-int.patch
# oreon:deps
BuildRequires:  bison
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
# /oreon:deps
%description
MinGW Windows PortableXDR XDR / RPC library.

# Win32
%package -n mingw32-portablexdr
Summary:	MinGW Windows PortableXDR / RPC Library
%description -n mingw32-portablexdr
MinGW Windows PortableXDR XDR / RPC library.

%package -n mingw32-portablexdr-static
Summary:       MinGW Windows PortableXDR XDR / RPC library, static version
%description -n mingw32-portablexdr-static
MinGW Windows PortableXDR XDR / RPC library, static version.

# Win64
%package -n mingw64-portablexdr
Summary:        MinGW Windows PortableXDR / RPC Library
%description -n mingw64-portablexdr
MinGW Windows PortableXDR XDR / RPC library.

%package -n mingw64-portablexdr-static
Summary:       MinGW Windows PortableXDR XDR / RPC library, static version
%description -n mingw64-portablexdr-static
MinGW Windows PortableXDR XDR / RPC library, static version.

%?mingw_debug_package

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir portablexdr-%{version}
%oreon_prep
%build

%mingw_configure --enable-static CFLAGS="-std=gnu89" 
export POSIXLY_CORRECT=1
rm -f rpcgen_parse.c rpcgen_parse.h
%mingw_make %{?_smp_flags}
%install
%mingw_make DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT -name "*.la" -delete
%oreon_autofiles mingw32-portablexdr usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-portablexdr-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-portablexdr usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-portablexdr-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-portablexdr -f %{oreon_filedir}/mingw32-portablexdr.list
%files -n mingw32-portablexdr-static -f %{oreon_filedir}/mingw32-portablexdr-static.list
%files -n mingw64-portablexdr -f %{oreon_filedir}/mingw64-portablexdr.list
%files -n mingw64-portablexdr-static -f %{oreon_filedir}/mingw64-portablexdr-static.list

%changelog

%autochangelog
