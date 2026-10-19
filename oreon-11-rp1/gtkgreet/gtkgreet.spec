%global source0_hash e5c70219da191a60e2e009412603e05c36cee15bbbf7657dbbeaa1d21a692873
Name:           gtkgreet
Version:        0.8
Release:        1%{?dist}
Summary:        GTK based greeter for greetd
License:        GPL-3.0-only
URL:            https://git.sr.ht/~kennylevinsen/%{name}
Source0:        https://git.sr.ht/~kennylevinsen/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source100:      %{name}-update-environments
Source101:      %{name}.css
Source102:      %{name}-sway.conf
Source103:      %{name}-wayfire.ini
Source104:      %{name}-river-init
Requires:       greetd >= 0.6
Provides:       greetd-greeter = 0.6
Provides:       greetd-%{name} = %{version}
Obsoletes:      greetd-%{name} < 0.7-2
Requires:       (sway or wayfire or river or cage)
Suggests:       sway
Recommends:     desktop-backgrounds-compat
Recommends:     swaybg
Recommends:     wayland-logout
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  sed
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name}
install -D -m755 -vp %{SOURCE100} %{buildroot}%{_libexecdir}/gtkgreet-update-environments
install -D -m644 -vp %{SOURCE101} %{buildroot}%{_sysconfdir}/gtkgreet/gtkgreet.css
install -D -m644 -vp %{SOURCE102} %{buildroot}%{_sysconfdir}/gtkgreet/gtkgreet-sway.conf
install -D -m644 -vp %{SOURCE103} %{buildroot}%{_sysconfdir}/gtkgreet/gtkgreet-wayfire.ini
install -D -m755 -vp %{SOURCE104} %{buildroot}%{_sysconfdir}/gtkgreet/gtkgreet-river-init
mkdir -p %{buildroot}%{_sysconfdir}/greetd
touch %{buildroot}%{_sysconfdir}/greetd/environments
%oreon_autofiles main

%post

if [ ! -f %{_sysconfdir}/greetd/environments ]; then
    %{_libexecdir}/gtkgreet-update-environments -w %{_sysconfdir}/greetd/environments
fi
exit 0
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
