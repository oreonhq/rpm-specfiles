%global source0_hash 235a40bec7346c7b82b6a8caae0456353dc06e71f14bc414bcc858af1838719a
%?mingw_package_header
Name:           mingw-libsigc++20
Version:        2.10.8
Release:        1%{?dist}
Summary:        MinGW Windows port of the typesafe signal framework for C++
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://libsigc.sourceforge.net/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/libsigc++/2.10/libsigc++-%{version}.tar.xz
BuildArch:      noarch
# oreon:deps
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
# /oreon:deps
%description
This library implements a full callback system for use in widget
libraries, abstract interfaces, and general programming. Originally
part of the Gtk-- widget set, libsigc++ is now a separate library to
provide for more general use. It is the most complete library of its
kind with the ability to connect an abstract callback to a class
method, function, or function object. It contains adaptor classes for
connection of dissimilar callbacks and has an ease of use unmatched by
other C++ callback libraries.

Package GTK-- (gtkmm), which is a C++ binding to the GTK+ library,
starting with version 1.1.2, uses libsigc++.

# Win32
%package -n mingw32-libsigc++20
Summary:        MinGW Windows port of the typesafe signal framework for C++
%description -n mingw32-libsigc++20
This library implements a full callback system for use in widget
libraries, abstract interfaces, and general programming. Originally
part of the Gtk-- widget set, libsigc++ is now a separate library to
provide for more general use. It is the most complete library of its
kind with the ability to connect an abstract callback to a class
method, function, or function object. It contains adaptor classes for
connection of dissimilar callbacks and has an ease of use unmatched by
other C++ callback libraries.

Package GTK-- (gtkmm), which is a C++ binding to the GTK+ library,
starting with version 1.1.2, uses libsigc++.

%package -n mingw32-libsigc++20-static
Summary:        Static cross compiled version of the libsigc++ library
Requires:       mingw32-libsigc++20 = %{version}-%{release}
%description -n mingw32-libsigc++20-static
Static cross compiled version of the libsigc++ library.

# Win64
%package -n mingw64-libsigc++20
Summary:        MinGW Windows port of the typesafe signal framework for C++
%description -n mingw64-libsigc++20
This library implements a full callback system for use in widget
libraries, abstract interfaces, and general programming. Originally
part of the Gtk-- widget set, libsigc++ is now a separate library to
provide for more general use. It is the most complete library of its
kind with the ability to connect an abstract callback to a class
method, function, or function object. It contains adaptor classes for
connection of dissimilar callbacks and has an ease of use unmatched by
other C++ callback libraries.

Package GTK-- (gtkmm), which is a C++ binding to the GTK+ library,
starting with version 1.1.2, uses libsigc++.

%package -n mingw64-libsigc++20-static
Summary:        Static cross compiled version of the libsigc++ library
Requires:       mingw64-libsigc++20 = %{version}-%{release}
%description -n mingw64-libsigc++20-static
Static cross compiled version of the libsigc++ library.

%?mingw_debug_package

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n libsigc++-%{version}

%build

%mingw_configure --enable-static --disable-documentation
%mingw_make %{?_smp_mflags}
%install
%mingw_make DESTDIR=$RPM_BUILD_ROOT install
chmod a-x $RPM_BUILD_ROOT/%{mingw32_libdir}/libsigc-2.0.dll.a
chmod a-x $RPM_BUILD_ROOT/%{mingw64_libdir}/libsigc-2.0.dll.a
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/libsigc-2.0.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/libsigc-2.0.la
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
