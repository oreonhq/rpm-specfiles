%global source0_hash 4ad4abdd3258874f61c2e2a41d08e9930677976d303653cd1670d3e9f35463e9

%{?mingw_package_header}

%global name1 libxml++

Name:           mingw-%{name1}
Version:        2.40.1
Release:        26%{?dist}
Summary:        MinGW Windows C++ wrapper for the libxml2 XML parser library

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://libxmlplusplus.sourceforge.net/
Source:         http://ftp.gnome.org/pub/GNOME/sources/libxml++/2.40/libxml++-%{version}.tar.xz

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-libxml2 >= 2.6.1
BuildRequires:  mingw64-libxml2 >= 2.6.1
BuildRequires:  mingw32-glibmm24 >= 2.4.0
BuildRequires:  mingw64-glibmm24 >= 2.4.0
BuildRequires:  mingw32-filesystem >= 68
BuildRequires:  mingw64-filesystem >= 68
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-gettext
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-gettext
BuildRequires:  perl

%description
libxml++ is a C++ wrapper for the libxml2 XML parser library.

%package -n mingw32-%{name1}
Summary:        MinGW Windows C++ wrapper for the libxml2 XML parser library
Requires:       pkgconfig

%description -n mingw32-%{name1}
libxml++ is a C++ wrapper for the libxml2 XML parser library.

%package -n mingw64-%{name1}
Summary:        MinGW Windows C++ wrapper for the libxml2 XML parser library
Requires:       pkgconfig

%description -n mingw64-%{name1}
libxml++ is a C++ wrapper for the libxml2 XML parser library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name1}-%{version}

%build
%{mingw_configure} --disable-static --disable-documentation
%{mingw_make} %{?_smp_mflags}

%install
%{mingw_make} install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{mingw32_docdir}
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{mingw64_docdir}
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/*.la

%files -n mingw32-%{name1}
%license COPYING
%doc AUTHORS NEWS README ChangeLog
%{mingw32_bindir}/libxml++-2.6-2.dll
%{mingw32_includedir}/*
%{mingw32_libdir}/libxml++-2.6.dll.a
%{mingw32_libdir}/pkgconfig/*
%dir %{mingw32_libdir}/%{name1}-2.6
%dir %{mingw32_libdir}/%{name1}-2.6/include
%{mingw32_libdir}/%{name1}-2.6/include/*.h

%files -n mingw64-%{name1}
%license COPYING
%doc AUTHORS NEWS README ChangeLog
%{mingw64_bindir}/libxml++-2.6-2.dll
%{mingw64_includedir}/*
%{mingw64_libdir}/libxml++-2.6.dll.a
%{mingw64_libdir}/pkgconfig/*
%dir %{mingw64_libdir}/%{name1}-2.6
%dir %{mingw64_libdir}/%{name1}-2.6/include
%{mingw64_libdir}/%{name1}-2.6/include/*.h

%changelog
%autochangelog
