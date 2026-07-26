%global source0_hash c09fce8fb71b1496fc762b9069311dd641853f9ba0a7c6d02ffbdf31ca2c43cf

Name:           libglib-testing
Version:        0.1.0
Release:        16%{?dist}
Summary:        GLib-based test library and harness

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://gitlab.gnome.org/pwithnall/libglib-testing
Source0:        https://gitlab.gnome.org/pwithnall/libglib-testing/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(gio-2.0)

%description
libglib-testing is a test library providing test harnesses and mock classes
which complement the classes provided by GLib. It is intended to be used by
any project which uses GLib and which wants to write internal unit tests.

%package devel
Summary:        Development files for %{name}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the pkg-config file and development headers
for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%{_libdir}/libglib-testing-0.so.0*

%files devel
%{_datadir}/gtk-doc/
%{_includedir}/glib-testing-0/
%{_libdir}/libglib-testing-0.so
%{_libdir}/pkgconfig/glib-testing-0.pc

%changelog
%autochangelog
