%global source0_hash 507ccdb1dc3958aa6cc7bece5e8911cb226b835dec4a4f83dacf11cdd3e5285a

%global extension   blur-my-shell
%global uuid        %{extension}@aunetx

Name:           gnome-shell-extension-%{extension}
Version:        70
Release:        %autorelease
Summary:        Adds a blur look to different parts of the GNOME Shell
License:        GPL-3.0-or-later
URL:            https://github.com/aunetx/blur-my-shell
BuildArch:      noarch

Source:         %{url}/archive/v%{version}/%{extension}-%{version}.tar.gz
# https://github.com/aunetx/blur-my-shell/pull/626
Patch:          0001-Use-meson-build-system.patch
# https://github.com/aunetx/blur-my-shell/pull/830
Patch:          0002-Support-GNOME-50-and-add-to-supported-versions.patch

BuildRequires:  meson
BuildRequires:  glib2
BuildRequires:  gettext
Requires:       gnome-shell >= 46
Recommends:     gnome-extensions-app
Provides:       %{extension} = %{version}-%{release}

%description
Adds a blur look to different parts of the GNOME Shell, including the top
panel, dash and overview.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n %{extension}-%{version}

%conf
%meson

%build
%meson_build

%install
%meson_install
%find_lang %{uuid}

%files -f %{uuid}.lang
%license LICENSE
%{_datadir}/gnome-shell/extensions/%{uuid}
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml

%changelog
%autochangelog
