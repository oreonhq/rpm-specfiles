%global source0_hash db9791a54255742c924ef82a6a882042636d61de0fa61bc14c5e56279cf5791c
ExcludeArch: %{ix86}
%global oldname compton-ng
%global tarball_version %%(echo %{version} | tr '~' '-')
Name:           picom
Version:        13
Release:        1%{?dist}
Summary:        Lightweight compositor for X11
License:        MPL-2.0 AND MIT
URL:            https://github.com/yshui/picom
Source0:        https://github.com/yshui/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       hicolor-icon-theme
Conflicts:      compton%{?_isa}
Provides:       %{oldname}%{?_isa} = %{version}-%{release}
Obsoletes:      %{oldname} =< 7.5-1
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libev-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libconfig)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libxdg-basedir)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-damage)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-present)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xinerama)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  rubygem-asciidoctor
BuildRequires:  uthash-devel
# /oreon:deps
%description
picom is a compositor for X, and a fork of Compton.

This is a development branch, bugs to be expected

You can leave your feedback or thoughts in the discussion tab.

%package        devel
Summary:        Devel files for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%description    devel
Devel files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson               \
    -Dwith_docs=true \
    %{nil}
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list
%files -n picom-devel -f %{oreon_filedir}/picom-devel.list

%changelog

%autochangelog
