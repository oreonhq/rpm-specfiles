%global source0_hash b7dc2f34fac745b1283a42fece4e00c4d0cdb7044d00d4daa317ba7fd1f106b2

%global extension   vertical-workspaces
%global uuid        %{extension}@G-dH.github.com
%global commit      c87dafbe50a74050eb62c201be0097a91f9ec775
%global shortcommit %{sub %{commit} 1 7}

Name:           gnome-shell-extension-%{extension}
Version:        50.0~^1.%{shortcommit}
Release:        %autorelease
Summary:        Customize your GNOME Shell UX to suit your workflow
License:        GPL-3.0-only
URL:            https://github.com/G-dH/vertical-workspaces
BuildArch:      noarch

Source:         %{url}/archive/%{commit}/%{extension}-%{shortcommit}.tar.gz

BuildRequires:  meson
BuildRequires:  glib2
BuildRequires:  gettext
Requires:       gnome-shell >= 45
Recommends:     gnome-extensions-app
Provides:       %{extension} = %{version}-%{release}

%description
Customize your GNOME Shell UX to suit your workflow, whether you like
horizontally or vertically stacked workspaces.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{extension}-%{commit}

%conf
%meson

%build
%meson_build

%install
%meson_install
%find_lang %{extension}

%files -f %{extension}.lang
%license LICENSE
%doc CHANGELOG.md
%{_datadir}/gnome-shell/extensions/%{uuid}
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml

%changelog
%autochangelog
