%global source0_hash b1bf56239269d101a6391ad4553c910eff9cc6170b803916405477ef60a66c84
%global apiver  1
%global gtk_version 4.17.5
%global glib_version 2.89.3
%global tarball_version %(echo %{version} | tr '~' '.')
Name:           libadwaita
Version:        1.10.0
Release:        1%{?dist}
Summary:        Building blocks for modern GNOME applications
License:        LGPL-2.1-or-later AND MIT
URL:            https://gitlab.gnome.org/GNOME/libadwaita
Source0:        https://download.gnome.org/sources/%{name}/%{apiver}.%{apiver}0/%{name}-%{version}.tar.xz
Requires:       gtk4%{?_isa} >= %{gtk_version}
# oreon:deps
BuildRequires:  /usr/bin/sassc
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(appstream)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  vala
# /oreon:deps
%description
Building blocks for modern GNOME applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       vala
Recommends:     %{name}-doc = %{version}-%{release}
Suggests:       %{name}-demo = %{version}-%{release}
%description    devel
Development files for %{name}.

%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch
Recommends:     %{name}-devel = %{version}-%{release}
Recommends:     gi-docgen-fonts
%description    doc
Documentation files for %{name}.

%package        demo
Summary:        Demo files for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Suggests:       %{name}-devel = %{version}-%{release}
%description    demo
Demo files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson \
    -Ddocumentation=true \
    %{nil}
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.*

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list
%files -n libadwaita-devel -f %{oreon_filedir}/libadwaita-devel.list
%files -n libadwaita-doc -f %{oreon_filedir}/libadwaita-doc.list
%files -n libadwaita-demo -f %{oreon_filedir}/libadwaita-demo.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.9.0-1
- Import
