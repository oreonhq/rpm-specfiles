%global source0_hash 0b68dfc6313c6cc90ac989c6d722a1bf0585ad13846e79746aa87cb265904786

%?mingw_package_header

Name:           mingw-libsigc++20
Version:        2.10.3
Release:        16%{?dist}
Summary:        MinGW Windows port of the typesafe signal framework for C++

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://libsigc.sourceforge.net/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/libsigc++/2.10/libsigc++-%{version}.tar.xz

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils

BuildRequires:  m4

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

# Win32
%files -n mingw32-libsigc++20
%license COPYING
%{mingw32_bindir}/libsigc-2.0-0.dll
%{mingw32_libdir}/libsigc-2.0.dll.a
%{mingw32_libdir}/pkgconfig/sigc++-2.0.pc
%{mingw32_includedir}/sigc++-2.0
%{mingw32_libdir}/sigc++-2.0

%files -n mingw32-libsigc++20-static
%{mingw32_libdir}/libsigc-2.0.a

# Win64
%files -n mingw64-libsigc++20
%license COPYING
%{mingw64_bindir}/libsigc-2.0-0.dll
%{mingw64_libdir}/libsigc-2.0.dll.a
%{mingw64_libdir}/pkgconfig/sigc++-2.0.pc
%{mingw64_includedir}/sigc++-2.0
%{mingw64_libdir}/sigc++-2.0

%files -n mingw64-libsigc++20-static
%{mingw64_libdir}/libsigc-2.0.a

%changelog
%autochangelog
