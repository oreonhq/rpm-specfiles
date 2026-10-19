%global source0_hash 8db629f44378cac62b4931f725520334024e62c1951c4396682f1add63c1e3d1
%?mingw_package_header
Name:           mingw-cairomm
Version:        1.15.5
Release:        1%{?dist}
Summary:        MinGW Windows C++ API for the cairo graphics library
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.cairographics.org
Source0:        http://www.cairographics.org/releases/cairomm-%{version}.tar.gz
Patch0:         0001-Fix-the-build-with-MinGW-headers.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-cairo
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-libsigc++20
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-cairo
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-libsigc++20
# /oreon:deps
%description
Cairomm is the C++ API for the cairo graphics library. It offers all the power
of cairo with an interface familiar to C++ developers, including use of the 
Standard Template Library where it makes sense.

# Win32
%package -n mingw32-cairomm
Summary:        MinGW Windows C++ API for the cairo graphics library
%description -n mingw32-cairomm
Cairomm is the C++ API for the cairo graphics library. It offers all the power
of cairo with an interface familiar to C++ developers, including use of the
Standard Template Library where it makes sense.

%package -n mingw32-cairomm-static
Summary:        Static cross compiled version of the cairomm library
Requires:       mingw32-cairomm = %{version}-%{release}
%description -n mingw32-cairomm-static
Static cross compiled version of the cairomm library.

%package -n mingw64-cairomm
Summary:        MinGW Windows C++ API for the cairo graphics library
%description -n mingw64-cairomm
Cairomm is the C++ API for the cairo graphics library. It offers all the power
of cairo with an interface familiar to C++ developers, including use of the
Standard Template Library where it makes sense.

%package -n mingw64-cairomm-static
Summary:        Static cross compiled version of the cairomm library
Requires:       mingw64-cairomm = %{version}-%{release}
%description -n mingw64-cairomm-static
Static cross compiled version of the cairomm library.

%?mingw_debug_package

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n cairomm-%{version}
%patch -P0 -p1

%build

export lt_cv_deplibs_check_method="pass_all"
%mingw_configure --enable-static --disable-documentation
%mingw_make %{?_smp_mflags}
%install
%mingw_make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT/%{mingw32_datadir}/{devhelp,doc}
rm -rf $RPM_BUILD_ROOT/%{mingw64_datadir}/{devhelp,doc}
rm $RPM_BUILD_ROOT%{mingw32_libdir}/*.la
rm $RPM_BUILD_ROOT%{mingw64_libdir}/*.la
%oreon_autofiles mingw32-cairomm usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-cairomm-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-cairomm usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-cairomm-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-cairomm -f %{oreon_filedir}/mingw32-cairomm.list
%files -n mingw32-cairomm-static -f %{oreon_filedir}/mingw32-cairomm-static.list
%files -n mingw64-cairomm -f %{oreon_filedir}/mingw64-cairomm.list
%files -n mingw64-cairomm-static -f %{oreon_filedir}/mingw64-cairomm-static.list

%changelog

%autochangelog
