%global source0_hash 6f30092cef9fb839779646608f4ee14ae3cbac989c47fa05e841b0841f09878e
%{?mingw_package_header}
%global build_programs 0
Name:           mingw-libjpeg-turbo
Version:        3.2.0
Release:        1%{?dist}
Summary:        MinGW Windows Libjpeg-turbo library
License:        Zlib AND BSD-3-Clause AND MIT AND IJG
URL:            https://github.com/libjpeg-turbo/libjpeg-turbo
Source0:        https://github.com/libjpeg-turbo/libjpeg-turbo/releases/download/%{version}/libjpeg-turbo-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  nasm
# /oreon:deps
%description
MinGW Windows cross compiled Libjpeg-turbo library.

# Win32
%package -n mingw32-libjpeg-turbo
Summary:        MinGW Windows Libjpeg-turbo library
Obsoletes:      mingw32-libjpeg < 7-4
Provides:       mingw32-libjpeg = 7-4
%description -n mingw32-libjpeg-turbo
MinGW Windows cross compiled Libjpeg-turbo library.

%package -n mingw32-libjpeg-turbo-static
Summary:        Static version of the MinGW Windows Libjpeg-turbo library
Requires:       mingw32-libjpeg-turbo = %{version}-%{release}
Obsoletes:      mingw32-libjpeg-static < 7-4
Provides:       mingw32-libjpeg-static = 7-4
%description -n mingw32-libjpeg-turbo-static
Static version of the MinGW Windows cross compiled Libjpeg-turbo library.

%package -n mingw32-turbojpeg
Summary:        MinGW Windows turbojpeg library
%description -n mingw32-turbojpeg
MinGW Windows cross compiled turbojpeg library.

%package -n mingw32-turbojpeg-static
Summary:        Static version of the MinGW Windows turbojpeg library
Requires:       mingw32-turbojpeg = %{version}-%{release}
%description -n mingw32-turbojpeg-static
Static version of the MinGW Windows turbojpeg library.

# Win64
%package -n mingw64-libjpeg-turbo
Summary:        MinGW Windows Libjpeg-turbo library
Obsoletes:      mingw64-libjpeg < 8a-2%{?dist}
Provides:       mingw64-libjpeg = 8a-2%{?dist}
%description -n mingw64-libjpeg-turbo
MinGW Windows cross compiled Libjpeg-turbo library.

%package -n mingw64-libjpeg-turbo-static
Summary:        Static version of the MinGW Windows Libjpeg-turbo library
Requires:       mingw64-libjpeg-turbo = %{version}-%{release}
Obsoletes:      mingw64-libjpeg-static < 8a-2%{?dist}
Provides:       mingw64-libjpeg-static = 8a-2%{?dist}
%description -n mingw64-libjpeg-turbo-static
Static version of the MinGW Windows cross compiled Libjpeg-turbo library.

%package -n mingw64-turbojpeg
Summary:        MinGW Windows turbojpeg library
%description -n mingw64-turbojpeg
MinGW Windows cross compiled turbojpeg library.

%package -n mingw64-turbojpeg-static
Summary:        Static version of the MinGW Windows turbojpeg library
Requires:       mingw64-turbojpeg = %{version}-%{release}
%description -n mingw64-turbojpeg-static
Static version of the MinGW Windows turbojpeg library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libjpeg-turbo-%{version}
%oreon_prep
%build

%mingw_cmake
%mingw_make_build
%install
%mingw_make_install
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}
rm -rf %{buildroot}%{mingw32_docdir}
rm -rf %{buildroot}%{mingw64_docdir}
rm -rf %{buildroot}%{mingw32_prefix}/doc
rm -rf %{buildroot}%{mingw64_prefix}/doc
%if %build_programs == 0
rm -f %{buildroot}%{mingw32_bindir}/*.exe
rm -f %{buildroot}%{mingw64_bindir}/*.exe
%endif
chmod -x README.md
%oreon_autofiles mingw32-libjpeg-turbo usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-libjpeg-turbo-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-turbojpeg usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-turbojpeg-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libjpeg-turbo usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libjpeg-turbo-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-turbojpeg usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-turbojpeg-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libjpeg-turbo -f %{oreon_filedir}/mingw32-libjpeg-turbo.list
%files -n mingw32-libjpeg-turbo-static -f %{oreon_filedir}/mingw32-libjpeg-turbo-static.list
%files -n mingw32-turbojpeg -f %{oreon_filedir}/mingw32-turbojpeg.list
%files -n mingw32-turbojpeg-static -f %{oreon_filedir}/mingw32-turbojpeg-static.list
%files -n mingw64-libjpeg-turbo -f %{oreon_filedir}/mingw64-libjpeg-turbo.list
%files -n mingw64-libjpeg-turbo-static -f %{oreon_filedir}/mingw64-libjpeg-turbo-static.list
%files -n mingw64-turbojpeg -f %{oreon_filedir}/mingw64-turbojpeg.list
%files -n mingw64-turbojpeg-static -f %{oreon_filedir}/mingw64-turbojpeg-static.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.1.3-1
- Prepare for Oreon 11 (RP1)
