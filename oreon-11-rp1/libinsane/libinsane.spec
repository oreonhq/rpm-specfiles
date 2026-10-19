%global source0_hash a9b8daaef03eb3bc4a8e638131e506ff3c2f99f715170da572e7f5ce7ba76467
Name:           libinsane
Version:        1.0.10
Release:        1%{?dist}
Summary:        Cross-platform access to image scanners
License:        LGPL-3.0-or-later
URL:            https://doc.openpaper.work/libinsane/latest/
Source0:        https://gitlab.gnome.org/World/OpenPaperwork/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
ExcludeArch: %{ix86}
%ifarch %{valgrind_arches}
%endif
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(cunit)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(sane-backends)
BuildRequires:  vala
# /oreon:deps
%description
Libinsane is the library to access scanners on both Linux and Windows. It's
cross-platform, cross-programming languages, cross-scanners :-). It takes care
of all the quirks of all the platforms and scanners.

%package devel
Summary:        Development files for libinsane
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development libraries and header files for libinsane.

%package gobject
Summary:        GObject access to image scanners
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description gobject
Libinsane is the library to access scanners on both Linux and Windows. It's
cross-platform, cross-programming languages, cross-scanners :-). It takes care
of all the quirks of all the platforms and scanners.

This package provides GObject wrappers around the main library.

%package gobject-devel
Summary:        Development files for libinsane-gobject
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-gobject%{?_isa} = %{version}-%{release}
%description gobject-devel
Development libraries and header files for libinsane-gobject.

%package vala
Summary:        Vala bindings for libinsane
BuildArch:      noarch
BuildRequires:  vala
Requires:       %{name}-gobject-devel = %{version}-%{release}
%description vala
Vala bindings for libinsane.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%meson_build doc
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

%meson_test -v -t 10
%files -f %{oreon_filedir}/main.list
%files -n libinsane-devel -f %{oreon_filedir}/libinsane-devel.list
%files -n libinsane-gobject -f %{oreon_filedir}/libinsane-gobject.list
%files -n libinsane-gobject-devel -f %{oreon_filedir}/libinsane-gobject-devel.list
%files -n libinsane-vala -f %{oreon_filedir}/libinsane-vala.list

%changelog

%autochangelog
