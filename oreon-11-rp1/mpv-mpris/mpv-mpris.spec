%global source0_hash 47deb26641b2f45edbbaf48a9136177b565b64f544f0fa7b956739fc7a4fc0a8
Name:           mpv-mpris
Version:        1.3
Release:        1%{?dist}
Summary:        MPRIS plugin for mpv
License:        MIT
URL:            https://github.com/hoyon/mpv-mpris
Source0:        https://github.com/hoyon/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Requires:       mpv
# oreon:deps
BuildRequires:  gcc
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(mpv)
# /oreon:deps
%description
mpv-mpris allows control of mpv using standard media keys

This plugin implements the MPRIS D-Bus interface and can
be controlled using tools such as playerctl or through
many Linux DEs, such as Gnome and KDE.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build
%install
mkdir -p %{buildroot}/%{_libdir}/mpv
mkdir -p %{buildroot}/%{_sysconfdir}/mpv/scripts/
install -p -m 0755 mpris.so %{buildroot}/%{_libdir}/mpv/mpris.so
ln -sf %{_libdir}/mpv/mpris.so %{buildroot}/%{_sysconfdir}/mpv/scripts/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
