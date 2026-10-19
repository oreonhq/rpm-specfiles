%global source0_hash 046439dd165af6a79b989c2085863e25c7c7006be580cef937b32bf60b7aa53f
Name:           feedbackd
Version:        0.8.9
Release:        1%{?dist}
Summary:        Feedback library for GNOME
License:        GPL-3.0-or-later
URL:            https://gitlab.freedesktop.org/agx/feedbackd
Source0:        https://gitlab.freedesktop.org/agx/feedbackd/-/archive/v%{version}/%{name}-v%{version}.tar.gz
%{?sysusers_requires_compat}
Requires:       lib%{name}%{?_isa} = %{version}-%{release}
Requires:       wireplumber >= 0.5.13
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  dbus-daemon
BuildRequires:  gcc
BuildRequires:  gobject-introspection-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmobile)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(umockdev-1.0)
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  vala
# /oreon:deps
%description
feedbackd provides a DBus daemon (feedbackd) to act on events to provide
haptic, visual and audio feedback. It offers a library (libfeedback) and
GObject introspection bindings to ease using it from applications.

%package -n libfeedbackd
Summary: Library for %{name}
%description -n libfeedbackd
The lib%{name} package contains libraries for %{name}

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: lib%{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-v%{version}

%conf
%meson -Dmedia-roles=true

%build

%meson_build
%install
%meson_install
%oreon_autofiles libfeedbackd usr/*/lib*.so.*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%post

%systemd_user_post fbd-alert-slider.service
%pre

%sysusers_create_compat %{_sysusersdir}/feedbackd.conf
%preun

%systemd_user_preun fbd-alert-slider.service
%postun

%systemd_user_postun_with_reload fbd-alert-slider.service
%files -f %{oreon_filedir}/main.list
%files -n libfeedbackd -f %{oreon_filedir}/libfeedbackd.list
%files -n feedbackd-devel -f %{oreon_filedir}/feedbackd-devel.list

%changelog

%autochangelog
