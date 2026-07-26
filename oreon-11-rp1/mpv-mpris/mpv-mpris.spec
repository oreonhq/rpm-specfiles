%global source0_hash ecdc66f0182a38164b8bdc79502c575df3d2c4453bae5bff225c4e5ce9dbef6c

Name:           mpv-mpris
Version:        1.2
Release:        2%{?dist}
Summary:        MPRIS plugin for mpv

License:        MIT
URL:            https://github.com/hoyon/mpv-mpris
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(mpv)
BuildRequires:  pkgconfig(libavformat)

Requires:       mpv

%description
mpv-mpris allows control of mpv using standard media keys

This plugin implements the MPRIS D-Bus interface and can
be controlled using tools such as playerctl or through
many Linux DEs, such as Gnome and KDE.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%make_build

%install
mkdir -p %{buildroot}/%{_libdir}/mpv
mkdir -p %{buildroot}/%{_sysconfdir}/mpv/scripts/

install -p -m 0755 mpris.so %{buildroot}/%{_libdir}/mpv/mpris.so
ln -sf %{_libdir}/mpv/mpris.so %{buildroot}/%{_sysconfdir}/mpv/scripts/

%files
%dir %{_libdir}/mpv/
%{_libdir}/mpv/mpris.so
%dir %{_sysconfdir}/mpv/scripts
%{_sysconfdir}/mpv/scripts/mpris.so
%license LICENSE
%doc README.md

%changelog
%autochangelog
