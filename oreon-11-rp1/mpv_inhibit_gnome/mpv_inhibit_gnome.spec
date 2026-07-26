%global source0_hash 185668823892c6c124ce60068209a1d15da1eefcbef775dcbc90d91c53403f94

Name:           mpv_inhibit_gnome
Version:        0.1.3
Release:        %autorelease
Summary:        Mpv plugin that prevents screen blanking in GNOME

License:        MIT
URL:            https://github.com/Guldoman/mpv_inhibit_gnome
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(mpv)
BuildRequires:  pkgconfig(dbus-1)

Requires:       mpv

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%make_build

%install
mkdir -p %{buildroot}/%{_libdir}/mpv
mkdir -p %{buildroot}/%{_sysconfdir}/mpv/scripts

install -p -m 0755 lib/mpv_inhibit_gnome.so -t %{buildroot}/%{_libdir}/mpv
ln -sf %{_libdir}/mpv/mpv_inhibit_gnome.so %{buildroot}/%{_sysconfdir}/mpv/scripts/

%files
%license LICENSE
%doc README.md
%dir %{_libdir}/mpv/
%{_libdir}/mpv/mpv_inhibit_gnome.so
%dir %{_sysconfdir}/mpv/scripts
%{_sysconfdir}/mpv/scripts/mpv_inhibit_gnome.so

%changelog
%autochangelog
