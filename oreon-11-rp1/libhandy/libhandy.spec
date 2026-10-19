%global source0_hash 05b497229073ff557f10b326e074c5066f8743a302d4820ab97bcb5cd2dab087
%bcond glade %[!(0%{?rhel} >= 10)]
Name:           libhandy
Version:        1.8.3
Release:        1%{?dist}
Summary:        Building blocks for modern adaptive GNOME apps
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/libhandy
%global majmin %(echo %{version} | cut -d . -f -2)
Source0:        https://download.gnome.org/sources/%{name}/%{majmin}/%{name}-%{version}.tar.xz
%if %{with glade}
%endif
Obsoletes:      libhandy1 < 1.1.90-2
Conflicts:      libhandy1 < 1.1.90-2
Provides:       libhandy1 = %{version}-%{release}
Provides:       libhandy1%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gi-docgen
BuildRequires:  mesa-dri-drivers
BuildRequires:  meson
BuildRequires:  mutter
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gladeui-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  rsvg-pixbuf-loader
BuildRequires:  vala
BuildRequires:  xwayland-run
# /oreon:deps
%description
libhandy provides GTK+ widgets and GObjects to ease developing
applications for mobile phones.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Recommends:     gi-docgen-fonts
Obsoletes:      libhandy1-devel < 1.1.90-2
Conflicts:      libhandy1-devel < 1.1.90-2
Provides:       libhandy1-devel = %{version}-%{release}
Provides:       libhandy1-devel%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Dgtk_doc=true -Dexamples=false \
%if %{without glade}
    -Dglade_catalog=disabled \
%endif
    %{nil}
%meson_build
%install
%meson_install
%find_lang libhandy
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export NO_AT_BRIDGE=1
%{shrink:xwfb-run -c mutter -- %meson_test}
%files -f %{oreon_filedir}/main.list
%files -n libhandy-devel -f %{oreon_filedir}/libhandy-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.8.3-1
- Prepare for Oreon 11 (RP1)
