%global source0_hash b32dbe25085fd1ca313a1f5f8c9af01cd630c37778b857bab43a3fc403efd528

%global uuid          ibus-font-setting@ibus.github.com
%global shortname     ibus-font
%global snapshot_date 20230705

Name:       gnome-shell-extension-%{shortname}
Version:    0.%{snapshot_date}
Release:    8%{?dist}
Summary:    A GNOME Shell extension for ibus-setup custom font settings

License:    GPL-3.0-or-later
URL:        https://extensions.gnome.org/extension/1121/ibus-font-setting/
Source0:    https://pwu.fedorapeople.org/ibus/ibus-font-setting/%{name}-%{snapshot_date}.tar.gz
BuildArch:  noarch

Requires:   gnome-shell
Requires:   ibus

%description
use ibus font setting of ibus setup dialog to enhance the user experience

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

%build
# None

%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
install -Dp -m 0644 {extension.js,metadata.json,prefs.js,stylesheet.css} \
  %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/

%files
%license COPYING
%{_datadir}/gnome-shell/extensions/%{uuid}/

%changelog
%autochangelog
