%global source1_hash 79c33e8349550516f952cc784d76524fa2d1920da1357977c7324bc6b86b99f6
%global source0_hash 79c33e8349550516f952cc784d76524fa2d1920da1357977c7324bc6b86b99f6
%global forgeurl https://github.com/WayfireWM/wf-shell
%global gvc_commit      5f9768a2eac29c1ed56f1fbb449a77a3523683b6
%global gvc_shortcommit %(c=%{gvc_commit}; echo ${c:0:7})
Name:           wf-shell
Version:        0.11.0
%forgemeta
Release:        1%{?dist}
Summary:        A GTK4-based panel for wayfire
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/GNOME/libgnome-volume-control/tarball/%{gvc_commit}#/gvc-%{gvc_shortcommit}.tar.gz
Recommends:     wayland-logout
Requires:       hicolor-icon-theme
Provides:       bundled(gvc) = 0.git%{gvc_shortcommit}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  glm-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(wayfire)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wf-config)
# /oreon:deps
%description
wf-shell is a repository which contains the various components needed to built a
fully functional DE based around wayfire. Currently it has only a GTK-based
panel and background client.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
Development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1
%autosetup -D -T -a1
mv GNOME-libgnome-volume-control-%{gvc_shortcommit}/* \
    %{_builddir}/%{name}-%{version}/subprojects/gvc

%build

%meson \
    -Dwayland-logout=false
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n wf-shell-devel -f %{oreon_filedir}/wf-shell-devel.list

%changelog

%autochangelog
