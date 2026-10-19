%global source0_hash a2efd7ae0eabfa43c3da2a8f2b34bbc53f6d7b067c697ada569cf1fa21f36346
%global extension   no-overview
%global uuid        %{extension}@fthx
Name:           gnome-shell-extension-%{extension}
Version:        51
Release:        1%{?dist}
Summary:        GNOME Shell extension for no overview at start-up
License:        GPL-3.0-only
URL:            https://extensions.gnome.org/extension/4099/no-overview/
Source0:        https://github.com/fthx/no-overview/archive/refs/tags/v%{version}.zip#/no-overview-%{version}.zip
Source1:        no-overview-LICENSE
Source2:        no-overview-README.md
BuildArch:      noarch
Recommends:     gnome-extensions-app
# oreon:deps
BuildRequires:  git
# /oreon:deps
%description
GNOME Shell extension for no overview at start-up. For GNOME Shell 40+.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{extension}-%{version} -S git

%build

%install
install -d -m 0755 %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
cp -rp *.js metadata.json \
  %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
