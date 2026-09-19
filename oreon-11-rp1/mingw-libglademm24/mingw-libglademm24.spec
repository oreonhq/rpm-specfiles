%global source0_hash 38543c15acf727434341cc08c2b003d24f36abc22380937707fc2c5c687a2bc3

%{?mingw_package_header}

%global mingw_pkg_name libglademm24

# 64 bit does not build due to too old autotools
%global mingw_build_win64 0

Name:           mingw-%{mingw_pkg_name}
Version:        2.6.7
Release:        44%{?dist}

Summary:        MinGW Windows C++ wrapper for libglade

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://gtkmm.sourceforge.net/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/libglademm/2.6/libglademm-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 68
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-gtkmm24 >= 2.6.0
BuildRequires:  mingw32-libglade2 >= 2.6.1
BuildRequires:  mingw32-libpng
BuildRequires:  mingw64-filesystem >= 68
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-gtkmm24 >= 2.6.0
BuildRequires:  mingw64-libglade2 >= 2.6.1
BuildRequires:  mingw64-libpng

%description
This package provides a C++ interface for libglademm. It is a
subpackage of the GTKmm project.  The interface provides a convenient
interface for C++ programmers to create Gnome GUIs with GTK+'s
flexible object-oriented framework.

%if 0%{?mingw_build_win32} == 1
%package -n mingw32-%{mingw_pkg_name}
Summary:        MinGW Windows C++ wrapper for libglade

%description -n mingw32-%{mingw_pkg_name}
This package provides a C++ interface for libglademm. It is a
subpackage of the GTKmm project.  The interface provides a convenient
interface for C++ programmers to create Gnome GUIs with GTK+'s
flexible object-oriented framework.
%endif

%if 0%{?mingw_build_win64} == 1
%package -n mingw64-%{mingw_pkg_name}
Summary:        MinGW Windows C++ wrapper for libglade

%description -n mingw64-%{mingw_pkg_name}
This package provides a C++ interface for libglademm. It is a
subpackage of the GTKmm project.  The interface provides a convenient
interface for C++ programmers to create Gnome GUIs with GTK+'s
flexible object-oriented framework.
%endif

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n libglademm-%{version}

%build
MINGW32_CXXFLAGS='-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions --param=ssp-buffer-size=4 -std=c++11'
MINGW64_CXXFLAGS='-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions --param=ssp-buffer-size=4 -std=c++11'
export MINGW32_CXXFLAGS
export MINGW64_CXXFLAGS
%mingw_configure --disable-static
%mingw_make %{?_smp_mflags}

%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT
%if 0%{?mingw_build_win32} == 1
rm -rf ${RPM_BUILD_ROOT}%{mingw32_docdir}/gnomemm-2.6/libglademm-2.4/*
rm -f ${RPM_BUILD_ROOT}%{mingw32_datadir}/devhelp/books/libglademm-2.4/*
%endif
%if 0%{?mingw_build_win64} == 1
rm -rf ${RPM_BUILD_ROOT}%{mingw64_docdir}/gnomemm-2.6/libglademm-2.4/*
rm -f ${RPM_BUILD_ROOT}%{mingw64_datadir}/devhelp/books/libglademm-2.4/*
%endif
find ${RPM_BUILD_ROOT} -type f -name "*.la" -exec rm -f {} ';'
find ${RPM_BUILD_ROOT} -type f -name "*.exe" -exec rm -f {} ';'

%if 0%{?mingw_build_win32} == 1
%files -n mingw32-%{mingw_pkg_name}
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{mingw32_bindir}/libglademm-2.4-1.dll
%{mingw32_includedir}/libglademm-2.4
%{mingw32_libdir}/libglademm-2.4.dll.a
%{mingw32_libdir}/libglademm-2.4
%{mingw32_libdir}/pkgconfig/*.pc
%endif

%if 0%{?mingw_build_win64} == 1
%files -n mingw64-%{mingw_pkg_name}
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{mingw64_bindir}/libglademm-2.4-1.dll
%{mingw64_includedir}/libglademm-2.4
%{mingw64_libdir}/libglademm-2.4.dll.a
%{mingw64_libdir}/libglademm-2.4
%{mingw64_libdir}/pkgconfig/*.pc
%endif

%changelog
%autochangelog
