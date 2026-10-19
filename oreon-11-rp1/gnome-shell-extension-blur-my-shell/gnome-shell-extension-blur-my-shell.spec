%global source0_hash 95789fa535f126594c70de9442c4f97b0aeee57ee08e00ab85241547e15c73e3
%global extension   blur-my-shell
%global uuid        %{extension}@aunetx
Name:           gnome-shell-extension-%{extension}
Version:        72
Release:        1%{?dist}
Summary:        Adds a blur look to different parts of the GNOME Shell
License:        GPL-3.0-or-later
URL:            https://github.com/aunetx/blur-my-shell
BuildArch:      noarch
Source0:        https://github.com/aunetx/%{extension}/archive/v%{version}/%{extension}-%{version}.tar.gz
Patch:          0001-Use-meson-build-system.patch
Patch:          0002-Support-GNOME-50-and-add-to-supported-versions.patch
Requires:       gnome-shell >= 46
Recommends:     gnome-extensions-app
Provides:       %{extension} = %{version}-%{release}
# oreon:deps
BuildRequires:  gettext
BuildRequires:  glib2
BuildRequires:  meson
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
