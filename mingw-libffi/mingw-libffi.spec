%{?mingw_package_header}

Name:		mingw-libffi
Version:	3.5.2
Release:	2%{?dist}
Summary:	A portable foreign function interface library for MinGW

License:	MIT
URL:		http://sourceware.org/libffi
Source0:        https://github.com/libffi/libffi/releases/download/v%{version}/libffi-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:  make

BuildRequires:	mingw32-filesystem >= 95
BuildRequires:	mingw32-binutils
BuildRequires:	mingw32-gcc

BuildRequires:	mingw64-filesystem >= 95
BuildRequires:	mingw64-binutils
BuildRequires:	mingw64-gcc


%description
Foreign function interface library for MinGW.


# Win32
%package -n mingw32-libffi
Summary:	A portable foreign function interface library for MinGW

%description -n mingw32-libffi
Foreign function interface library for MinGW.

# Win32 static
%package -n mingw32-libffi-static
Summary:       A portable foreign function interface static library for MinGW

%description -n mingw32-libffi-static
Foreign function interface static library for MinGW.


# Win64
%package -n mingw64-libffi
Summary:	A portable foreign function interface library for MinGW

%description -n mingw64-libffi
Foreign function interface library for MinGW.

# Win64 static
%package -n mingw64-libffi-static
Summary:       A portable foreign function interface static library for MinGW

%description -n mingw64-libffi-static
Foreign function interface static library for MinGW.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n libffi-%{version}

%build
%mingw_configure --enable-shared
%mingw_make


%install
%mingw_make_install

rm -rf %{buildroot}%{mingw32_infodir}
rm -rf %{buildroot}%{mingw64_infodir}
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}

# Drop all .la files
find %{buildroot} -name "*.la" -delete


%files -n mingw32-libffi
%license LICENSE
%{mingw32_bindir}/libffi-8.dll
%{mingw32_includedir}/ffi.h
%{mingw32_includedir}/ffitarget.h
%{mingw32_libdir}/libffi.dll.a
%{mingw32_libdir}/pkgconfig/libffi.pc

%files -n mingw32-libffi-static
%{mingw32_libdir}/libffi.a

%files -n mingw64-libffi
%license LICENSE
%{mingw64_bindir}/libffi-8.dll
%{mingw64_includedir}/ffi.h
%{mingw64_includedir}/ffitarget.h
%{mingw64_libdir}/libffi.dll.a
%{mingw64_libdir}/pkgconfig/libffi.pc

%files -n mingw64-libffi-static
%{mingw64_libdir}/libffi.a


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.5.2-2
- Prepare for Oreon 11 (RP1)
