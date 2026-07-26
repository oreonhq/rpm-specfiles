%global source0_hash a64e03e5948d074f8309b036ca0acaf9ae4025c19cef6174f2319c504fb32d8c

%global baseversion 2.2

Name:           c++-gtk-utils
Version:        2.2.20
Release:        13%{?dist}
Summary:        A library for GTK+ programming with C++

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            http://cxx-gtk-utils.sourceforge.net/
Source0:        http://downloads.sourceforge.net/cxx-gtk-utils/%{name}-%{version}.tar.gz
Patch0:         %{name}-gcc11.patch

BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  make

%description
c++-gtk-utils is a lightweight library containing a number of classes and
functions for programming GTK+ programs using C++ in POSIX (Unix-like)
environments, where the user does not want to use a full-on wrapper such as
gtkmm or wxWidgets, or is concerned about exception safety or thread safety of
the wrapper and their documentation.

%package gtk2
Summary:        A library for GTK+ programming with C++ - GTK2 version
BuildRequires:  gtk2-devel

%description gtk2
c++-gtk-utils is a lightweight library containing a number of classes and
functions for programming GTK+ programs using C++ in POSIX (Unix-like)
environments, where the user does not want to use a full-on wrapper such as
gtkmm or wxWidgets, or is concerned about exception safety or thread safety of
the wrapper and their documentation.

This version is built against GTK2.

%package gtk3
Summary:        A library for GTK+ programming with C++ - GTK3 version
BuildRequires:  gtk3-devel

%description gtk3
c++-gtk-utils is a lightweight library containing a number of classes and
functions for programming GTK+ programs using C++ in POSIX (Unix-like)
environments, where the user does not want to use a full-on wrapper such as
gtkmm or wxWidgets, or is concerned about exception safety or thread safety of
the wrapper and their documentation.

This version is built against GTK3.

%package gtk4
Summary:        A library for GTK+ programming with C++ - GTK4 version
BuildRequires:  gtk4-devel

%description gtk4
c++-gtk-utils is a lightweight library containing a number of classes and
functions for programming GTK+ programs using C++ in POSIX (Unix-like)
environments, where the user does not want to use a full-on wrapper such as
gtkmm or wxWidgets, or is concerned about exception safety or thread safety of
the wrapper and their documentation.

This version is built against GTK4.

%package gtk2-devel
Summary:        Development files for the c++-gtk-utils library - GTK2 version
Requires:       %{name}-gtk2%{?_isa} = %{version}-%{release}

%description gtk2-devel
This package contains libraries and header files needed for development of
applications or toolkits which use c++-gtk-utils.

This version is built against GTK2.

%package gtk3-devel
Summary:        Development files for the c++-gtk-utils library - GTK3 version
Requires:       %{name}-gtk3%{?_isa} = %{version}-%{release}

%description gtk3-devel
This package contains libraries and header files needed for development of
applications or toolkits which use c++-gtk-utils.

This version is built against GTK3.

%package gtk4-devel
Summary:        Development files for the c++-gtk-utils library - GTK4 version
Requires:       %{name}-gtk4%{?_isa} = %{version}-%{release}

%description gtk4-devel
This package contains libraries and header files needed for development of
applications or toolkits which use c++-gtk-utils.

This version is built against GTK4.

%package devel-doc
Summary:        Development documentation for the c++-gtk-utils library
BuildArch:      noarch

%description devel-doc
This package contains documentation files for development of applications or
toolkits which use c++-gtk-utils.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version} -c
pushd %{name}-%{version}
%patch -P0 -p1
popd
mv %{name}-{,gtk2-}%{version}
cp -a %{name}-gtk{2,3}-%{version}
cp -a %{name}-gtk{2,4}-%{version}

%build
pushd %{name}-gtk2-%{version}
mv -f configure-gtk2 configure
%configure --disable-static
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build V=1
popd

pushd %{name}-gtk3-%{version}
%configure --disable-static
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build V=1
popd

pushd %{name}-gtk4-%{version}
mv -f configure-gtk4 configure
%configure --disable-static
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build V=1
popd

%install
pushd %{name}-gtk2-%{version}
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la
popd

pushd %{name}-gtk3-%{version}
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la
popd

pushd %{name}-gtk4-%{version}
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la
popd

%files gtk2
%{_libdir}/libcxx-gtk-utils-2-%{baseversion}.so.0*
%dir %{_defaultdocdir}/%{name}
%dir %{_defaultdocdir}/%{name}/%{baseversion}
%{_defaultdocdir}/%{name}/%{baseversion}/BUGS
%{_defaultdocdir}/%{name}/%{baseversion}/COPYING
%{_defaultdocdir}/%{name}/%{baseversion}/NEWS
%{_defaultdocdir}/%{name}/%{baseversion}/README

%files gtk3
%{_libdir}/libcxx-gtk-utils-3-%{baseversion}.so.0*
%dir %{_defaultdocdir}/%{name}
%dir %{_defaultdocdir}/%{name}/%{baseversion}
%{_defaultdocdir}/%{name}/%{baseversion}/BUGS
%{_defaultdocdir}/%{name}/%{baseversion}/COPYING
%{_defaultdocdir}/%{name}/%{baseversion}/NEWS
%{_defaultdocdir}/%{name}/%{baseversion}/README

%files gtk4
%{_libdir}/libcxx-gtk-utils-4-%{baseversion}.so.0*
%dir %{_defaultdocdir}/%{name}
%dir %{_defaultdocdir}/%{name}/%{baseversion}
%{_defaultdocdir}/%{name}/%{baseversion}/BUGS
%{_defaultdocdir}/%{name}/%{baseversion}/COPYING
%{_defaultdocdir}/%{name}/%{baseversion}/NEWS
%{_defaultdocdir}/%{name}/%{baseversion}/README

%files gtk2-devel
%{_libdir}/pkgconfig/%{name}-2-%{baseversion}.pc
%{_libdir}/libcxx-gtk-utils-2-%{baseversion}.so
%{_includedir}/%{name}-2-%{baseversion}

%files gtk3-devel
%{_libdir}/pkgconfig/%{name}-3-%{baseversion}.pc
%{_libdir}/libcxx-gtk-utils-3-%{baseversion}.so
%{_includedir}/%{name}-3-%{baseversion}

%files gtk4-devel
%{_libdir}/pkgconfig/%{name}-4-%{baseversion}.pc
%{_libdir}/libcxx-gtk-utils-4-%{baseversion}.so
%{_includedir}/%{name}-4-%{baseversion}

%files devel-doc
%dir %{_defaultdocdir}/%{name}
%dir %{_defaultdocdir}/%{name}/%{baseversion}
%{_defaultdocdir}/%{name}/%{baseversion}/COPYING
%{_defaultdocdir}/%{name}/%{baseversion}/PORTING-TO-%{baseversion}
%{_defaultdocdir}/%{name}/%{baseversion}/html

%changelog
%autochangelog
