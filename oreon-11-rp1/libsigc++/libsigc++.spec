%global source0_hash d9163d90e259bfde9164c7b218475a7664a7907a1b3197f17bc1035f36112225

Name:           libsigc++
Version:        1.2.7
Release:        45%{?dist}
Summary:        Typesafe signal framework for C++
License:        LGPL-2.1-or-later
URL:            http://libsigc.sourceforge.net/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/libsigc++/1.2/%{name}-%{version}.tar.bz2
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  m4
BuildRequires:  doxygen
BuildRequires:  libxslt docbook-style-xsl
BuildRequires: make

Patch1:         libsigc++-1.2.5-stylesheet.patch
Patch2:         libsigc++-1.2.5-configure.patch
%description
This library implements a full callback system for use in widget libraries,
abstract interfaces, and general programming. Originally part of the Gtk--
widget set, %name is now a separate library to provide for more general
use. It is the most complete library of its kind with the ablity to connect
an abstract callback to a class method, function, or function object. It
contains adaptor classes for connection of dissimilar callbacks and has an
ease of use unmatched by other C++ callback libraries.

Package gtkmm (previously gtk--), which is a C++ binding to the GTK+
library, starting with version 1.1.2, uses %name.

%package        devel
Summary:        Development tools for the typesafe signal framework for C++
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
The %name-devel package contains the static libraries and header files
needed for development with %name.

%package        doc
Summary:        Documentation for %{name}, includes full API docs
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    doc
This package contains the full API documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p1 -b .stylesheet
%patch -P2 -p1 -b .configure

%build
%configure %{!?_with_static: --disable-static}
%make_build
cd doc/manual
make
cd -

%install
rm -rf ${RPM_BUILD_ROOT}
%make_install
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
# Clean up a temporary doc dir prior to including files from it.
rm -rf _doc ; cp -a doc _doc
find _doc -type f -name "Makefile*" -exec rm -f {} ';'
find _doc -type f -empty -exec rm -f {} ';'
find _doc -type d -empty -print0 | xargs -0r rmdir

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING.LIB README IDEAS NEWS ChangeLog TODO
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/sigc++-1.2/
%{?_with_static: %{_libdir}/*.a}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/sigc++-1.2/

%files doc
%doc _doc/*

%changelog
%autochangelog
