%global source0_hash 5cf4bdd153cf4d44eaf10b725f451d0cfadc070b4b9a9ccfb64094b8f78de72c

%?mingw_package_header

Name:		mingw-portablexdr
Version:	4.9.1
Release:	39%{?dist}
Summary:	MinGW Windows PortableXDR / RPC Library

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+
URL:		https://people.redhat.com/~rjones/portablexdr/
Source0:	https://people.redhat.com/~rjones/portablexdr/files/portablexdr-%{version}.tar.gz
BuildArch:	noarch

BuildRequires: make
BuildRequires:	mingw32-filesystem >= 95
BuildRequires:	mingw32-gcc
BuildRequires:	mingw32-binutils

BuildRequires:	mingw64-filesystem >= 95
BuildRequires:	mingw64-gcc
BuildRequires:	mingw64-binutils

BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  bison

# Remove include of config.h from public header.
Patch0:		portablexdr-4.9.1-no-config-h.patch
Patch1:		portablexdr-build-use-intptr_t-and-uintptr_t-to-cast-ptr-to-int.patch

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

%autosetup -S git -n portablexdr-%{version}

%build
%mingw_configure --enable-static CFLAGS="-std=gnu89" 
# Force bison to generate yylex() prototype to avoid build
# failure with new GCC which is strict about missing prototypes
export POSIXLY_CORRECT=1
rm -f rpcgen_parse.c rpcgen_parse.h
%mingw_make %{?_smp_flags}

%install
%mingw_make DESTDIR=$RPM_BUILD_ROOT install

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete

# Win32
%files -n mingw32-portablexdr
%license COPYING.LIB
%{mingw32_bindir}/portable-rpcgen.exe
%{mingw32_bindir}/libportablexdr-0.dll
%{mingw32_libdir}/libportablexdr.dll.a
%{mingw32_includedir}/rpc

%files -n mingw32-portablexdr-static
%{mingw32_libdir}/libportablexdr.a

# Win64
%files -n mingw64-portablexdr
%license COPYING.LIB
%{mingw64_bindir}/portable-rpcgen.exe
%{mingw64_bindir}/libportablexdr-0.dll
%{mingw64_libdir}/libportablexdr.dll.a
%{mingw64_includedir}/rpc

%files -n mingw64-portablexdr-static
%{mingw64_libdir}/libportablexdr.a

%changelog
%autochangelog
