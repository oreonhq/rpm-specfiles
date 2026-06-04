%global source0_hash 58493387c7c9c70d61e711ec2feec5db0a59d164556642d2b427dde4ef756bc1

%{?mingw_package_header}

%global pkgname win-iconv

Name:          mingw-%{pkgname}
Version:       0.0.10
Release:       4%{?dist}
Summary:       Iconv implementation using Win32 API

BuildArch:     noarch
License:       LicenseRef-Fedora-Public-Domain
URL:           https://github.com/win-iconv/win-iconv
Source0:        https://github.com/win-iconv/win-iconv/archive/refs/tags/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires: make
BuildRequires: cmake

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++


%description
MinGW Windows Iconv library


%{?mingw_debug_package}


# Win32
%package -n mingw32-win-iconv
Summary:       MinGW Windows Iconv library

%description -n mingw32-win-iconv
MinGW Windows cross compiled Iconv library.

%package -n mingw32-win-iconv-static
Summary:       Static version of the MinGW Windows Iconv library
Requires:      mingw32-win-iconv = %{version}-%{release}

%description -n mingw32-win-iconv-static
Static version of the MinGW Windows Iconv library.

# Win64
%package -n mingw64-win-iconv
Summary:       MinGW Windows Iconv library

%description -n mingw64-win-iconv
MinGW Windows Iconv library

%package -n mingw64-win-iconv-static
Summary:       Static version of the MinGW Windows Iconv library
Requires:      mingw64-win-iconv = %{version}-%{release}

%description -n mingw64-win-iconv-static
Static version of the MinGW Windows Iconv library.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{pkgname}-%{version}
sed -i 's|\r||' readme.txt ChangeLog


%build
%mingw_cmake -DDISABLE_LOCALE_CHARSET=ON
%mingw_make_build


%install
%mingw_make_install

rm %{buildroot}/%{mingw32_bindir}/win_iconv.exe
rm %{buildroot}/%{mingw64_bindir}/win_iconv.exe

# Fix file conflict with mingw-libcharset
rm -f %{buildroot}%{mingw32_includedir}/localcharset.h
rm -f %{buildroot}%{mingw64_includedir}/localcharset.h


%files -n mingw32-win-iconv
%doc ChangeLog readme.txt
%{mingw32_bindir}/iconv.dll
%{mingw32_includedir}/iconv.h
%{mingw32_libdir}/libiconv.dll.a

%files -n mingw32-win-iconv-static
%{mingw32_libdir}/libiconv.a

%files -n mingw64-win-iconv
%doc ChangeLog readme.txt
%{mingw64_bindir}/iconv.dll
%{mingw64_includedir}/iconv.h
%{mingw64_libdir}/libiconv.dll.a

%files -n mingw64-win-iconv-static
%{mingw64_libdir}/libiconv.a


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.0.10-4
- Prepare for Oreon 11 (RP1)
