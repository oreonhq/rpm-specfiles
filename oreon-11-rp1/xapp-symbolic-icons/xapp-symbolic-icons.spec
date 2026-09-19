%global source0_hash 0ebb603eaa34f34d44bc419119595c91785caf0e29a2ad2adaa7fea9cc2e6ebb

Name:           xapp-symbolic-icons
Version:        1.0.9
Release:        1%{?dist}
Summary:        A set of symbolic icons which replaces the GNOME-specific Adwaita set
License:        CC0-1.0 AND CC-BY-SA-4.0 AND LGPL-3.0-only AND MIT
URL:            https://github.com/xapp-project/xapp-symbolic-icons
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  meson
Requires:       hicolor-icon-theme

%description
A set of symbolic icons which replaces the GNOME-specific Adwaita set.
All provided icons are prefixed with xsi-.
Icon names loosely follow the Adwaita names.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%transfiletriggerin -- %{_datadir}/icons/hicolor
gtk-update-icon-cache --force %{_datadir}/icons/hicolor &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/hicolor
gtk-update-icon-cache --force %{_datadir}/icons/hicolor &>/dev/null || :

%files
%license LICENSE LICENSES/*.txt
%doc AUTHORS README.md
%{_bindir}/xsi-replace-adwaita-symbolic
%{_datadir}/icons/hicolor/scalable/actions/xsi-*.svg
%{_datadir}/xapp/

%changelog
%autochangelog
