Name:           libdecor
Version:        0.2.5
Release:        2%{?dist}
Summary:        Wayland client side decoration library

License:        MIT
URL:            https://gitlab.freedesktop.org/libdecor/libdecor
Source:         %{url}/-/releases/%{version}/downloads/libdecor-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  gtk3
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(gtk+-3.0)

%description
Libdecor provides a small helper library for providing client side decoration
to Wayland clients.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
%meson -Ddemo=false
%meson_build


%install
%meson_install


%files
%license LICENSE
%doc README.md
%{_libdir}/libdecor-0.so.0*
%dir %{_libdir}/libdecor/
%dir %{_libdir}/libdecor/plugins-1
%{_libdir}/libdecor/plugins-1/libdecor-cairo.so
%{_libdir}/libdecor/plugins-1/libdecor-gtk.so

%files devel
%{_includedir}/libdecor-0/
%{_libdir}/libdecor-0.so
%{_libdir}/pkgconfig/libdecor-0.pc


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2.5-2
- Prepare for Oreon 11 (RP1)
