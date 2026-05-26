# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 9b18d267c55ec950beeea42d3291d2e77f8f7e351c31c6a48feb90dacb195fc5
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global systemd_unit gnome-ponytail-daemon.service
%global libname ponytail

Name:           gnome-ponytail-daemon
Version:        0.0.11
Release:        9%{?dist}
Summary:        Sort of a bridge for dogtail for GNOME on Wayland

License:        GPL-2.0-or-later
URL:            https://gitlab.gnome.org/ofourdan/gnome-ponytail-daemon
Source0:        https://gitlab.gnome.org/ofourdan/gnome-ponytail-daemon/-/archive/0.0.11/gnome-ponytail-daemon-0.0.11.tar.gz

BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.32
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  systemd-rpm-macros

%if 0%{?fedora} >= 39 || 0%{?rhel} >= 10
BuildRequires:  pkgconfig(libei-1.0) >= 1.0.0
%endif

%{?systemd_requires}
BuildRequires:  systemd

%description
GNOME Ponytail Daemon is a sort of bridge for dogtail for GNOME on Wayland.

%package        -n python3-%{name}
Summary:        Python module for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       python3-dbus
Requires:       python3-gobject
BuildArch:      noarch

%description -n python3-%{name}
Python module for D-BUS interactions with gnome-ponytail-daemon interfaces.

%prep
%oreon_verify_sources
%autosetup -n %{name}-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

%post
%systemd_user_post %{systemd_unit}

%preun
%systemd_user_preun %{systemd_unit}

%postun
%systemd_user_postun_with_restart %{systemd_unit}
%systemd_user_postun_with_reload %{systemd_unit}
%systemd_user_postun %{systemd_unit}

%files
%license LICENSE
%doc README.md
%{_libexecdir}/gnome-ponytail-daemon
%{_userunitdir}/gnome-ponytail-daemon.service
%{_datadir}/dbus-1/services/org.gnome.Ponytail.service

%files -n python3-%{name}
%doc examples/*.py
%{python3_sitelib}/%{libname}/

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.0.11-9
- Prepare for Oreon 11 (RP1)
