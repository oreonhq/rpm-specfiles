%global source0_hash 1cb944a4b88847f5fb6551683bc799db59f04990f5d8be07aba2acbf38601089

%{?mingw_package_header}

%global pkgname poppler

Name:          mingw-%{pkgname}
Version:       26.01.0
Release:       1%{?dist}
Summary:       MinGW Windows Poppler library

License:       (GPL-2.0-only OR GPL-3.0-only) AND GPL-2.0-or-later AND LGPL-2.0-or-later AND MIT
BuildArch:     noarch
URL:           http://poppler.freedesktop.org/
Source0:       http://poppler.freedesktop.org/%{pkgname}-%{version}.tar.xz

# Downstream fix for CVE-2017-9083 (#1453200)
Patch1:        poppler_CVE-2017-9083.patch

BuildRequires: make
BuildRequires: cmake
BuildRequires: gettext-devel
BuildRequires: perl(File::Temp)

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-boost
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-libjpeg-turbo
BuildRequires: mingw32-libtiff
BuildRequires: mingw32-openjpeg2
BuildRequires: mingw32-openjpeg2-tools
BuildRequires: mingw32-cairo
BuildRequires: mingw32-gtk3
BuildRequires: mingw32-lcms2
BuildRequires: mingw32-qt5-qtbase-devel
BuildRequires: mingw32-qt6-qtbase
BuildRequires: mingw32-curl

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-boost
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-libjpeg-turbo
BuildRequires: mingw64-libtiff
BuildRequires: mingw64-openjpeg2
BuildRequires: mingw64-openjpeg2-tools
BuildRequires: mingw64-cairo
BuildRequires: mingw64-gtk3
BuildRequires: mingw64-lcms2
BuildRequires: mingw64-qt5-qtbase-devel
BuildRequires: mingw64-qt6-qtbase
BuildRequires: mingw64-curl

%description
MinGW Windows Poppler library.

###############################################################################

%package -n mingw32-%{pkgname}
Summary:       MinGW Windows Poppler library

%description -n mingw32-%{pkgname}
MinGW Windows Poppler library.

###############################################################################

%package -n mingw32-%{pkgname}-glib
Summary:       MinGW Windows Poppler-Glib library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-glib
MinGW Windows Poppler-Glib library.

###############################################################################

%package -n mingw32-%{pkgname}-qt5
Summary:       MinGW Windows Poppler-Qt5 library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-qt5
MinGW Windows Poppler-Qt5 library.

###############################################################################

%package -n mingw32-%{pkgname}-qt6
Summary:       MinGW Windows Poppler-Qt6 library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-qt6
MinGW Windows Poppler-Qt6 library.

###############################################################################

%package -n mingw32-%{pkgname}-cpp
Summary:       MinGW Windows C++ Poppler library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-cpp
MinGW Windows C++ Poppler library.

###############################################################################

%package -n mingw64-%{pkgname}
Summary:       MinGW Windows Poppler library

%description -n mingw64-%{pkgname}
MinGW Windows Poppler library.

###############################################################################

%package -n mingw64-%{pkgname}-glib
Summary:       MinGW Windows Poppler-Glib library
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-glib
MinGW Windows Poppler-Glib library.

###############################################################################

%package -n mingw64-%{pkgname}-qt5
Summary:       MinGW Windows Poppler-Qt5 library
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-qt5
MinGW Windows Poppler-Qt5 library.

###############################################################################

%package -n mingw64-%{pkgname}-qt6
Summary:       MinGW Windows Poppler-Qt6 library
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-qt6
MinGW Windows Poppler-Qt6 library.

###############################################################################

%package -n mingw64-%{pkgname}-cpp
Summary:       MinGW Windows C++ Poppler library
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-cpp
MinGW Windows C++ Poppler library.

###############################################################################

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}-%{version}

%build
export MINGW32_CXXFLAGS="%{mingw32_cflags} -msse2"
export MINGW64_CXXFLAGS="%{mingw64_cflags} -msse2"
# FIXME: gcc-16 does not properly export std::__get_once_callable
export MINGW32_LDFLAGS="%{mingw32_ldflags} -static-libstdc++"
export MINGW64_LDFLAGS="%{mingw64_ldflags} -static-libstdc++"

%mingw_cmake \
  -DENABLE_CMS=lcms2 \
  -DENABLE_DCTDECODER=libjpeg \
  -DENABLE_LIBOPENJPEG=openjpeg2 \
  -DENABLE_UNSTABLE_API_ABI_HEADERS=ON \
  -DENABLE_NSS3=OFF \
  -DENABLE_GPGME=OFF \
  -DENABLE_ZLIB=OFF \

%mingw_make_build

%install
%mingw_make_install

# Delete man files
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}

# Delete exe files
rm -f %{buildroot}%{mingw32_bindir}/*.exe
rm -f %{buildroot}%{mingw64_bindir}/*.exe

%files -n mingw32-%{pkgname}
%license COPYING
%doc README.md
%{mingw32_bindir}/libpoppler-156.dll
%{mingw32_includedir}/poppler/
%exclude %{mingw32_includedir}/poppler/cpp/
%exclude %{mingw32_includedir}/poppler/glib/
%exclude %{mingw32_includedir}/poppler/qt5/
%{mingw32_libdir}/libpoppler.dll.a
%{mingw32_libdir}/pkgconfig/poppler.pc

%files -n mingw32-%{pkgname}-glib
%{mingw32_bindir}/libpoppler-glib-8.dll
%{mingw32_includedir}/poppler/glib/
%{mingw32_libdir}/libpoppler-glib.dll.a
%{mingw32_libdir}/pkgconfig/poppler-glib.pc

%files -n mingw32-%{pkgname}-qt5
%{mingw32_bindir}/libpoppler-qt5-1.dll
%{mingw32_includedir}/poppler/qt5/
%{mingw32_libdir}/libpoppler-qt5.dll.a
%{mingw32_libdir}/pkgconfig/poppler-qt5.pc

%files -n mingw32-%{pkgname}-qt6
%{mingw32_bindir}/libpoppler-qt6-3.dll
%{mingw32_includedir}/poppler/qt6/
%{mingw32_libdir}/libpoppler-qt6.dll.a
%{mingw32_libdir}/pkgconfig/poppler-qt6.pc

%files -n mingw32-%{pkgname}-cpp
%{mingw32_bindir}/libpoppler-cpp-3.dll
%{mingw32_includedir}/poppler/cpp/
%{mingw32_libdir}/libpoppler-cpp.dll.a
%{mingw32_libdir}/pkgconfig/poppler-cpp.pc

%files -n mingw64-%{pkgname}
%license COPYING
%doc README.md
%{mingw64_bindir}/libpoppler-156.dll
%{mingw64_includedir}/poppler/
%exclude %{mingw64_includedir}/poppler/cpp/
%exclude %{mingw64_includedir}/poppler/glib/
%exclude %{mingw64_includedir}/poppler/qt5/
%{mingw64_libdir}/libpoppler.dll.a
%{mingw64_libdir}/pkgconfig/poppler.pc

%files -n mingw64-%{pkgname}-glib
%{mingw64_bindir}/libpoppler-glib-8.dll
%{mingw64_includedir}/poppler/glib/
%{mingw64_libdir}/libpoppler-glib.dll.a
%{mingw64_libdir}/pkgconfig/poppler-glib.pc

%files -n mingw64-%{pkgname}-qt5
%{mingw64_bindir}/libpoppler-qt5-1.dll
%{mingw64_includedir}/poppler/qt5/
%{mingw64_libdir}/libpoppler-qt5.dll.a
%{mingw64_libdir}/pkgconfig/poppler-qt5.pc

%files -n mingw64-%{pkgname}-qt6
%{mingw64_bindir}/libpoppler-qt6-3.dll
%{mingw64_includedir}/poppler/qt6/
%{mingw64_libdir}/libpoppler-qt6.dll.a
%{mingw64_libdir}/pkgconfig/poppler-qt6.pc

%files -n mingw64-%{pkgname}-cpp
%{mingw64_bindir}/libpoppler-cpp-3.dll
%{mingw64_includedir}/poppler/cpp/
%{mingw64_libdir}/libpoppler-cpp.dll.a
%{mingw64_libdir}/pkgconfig/poppler-cpp.pc

%changelog
%autochangelog
