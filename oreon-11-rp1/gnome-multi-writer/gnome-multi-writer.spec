%global source0_hash b7fe3667e23402ee1d5b01c5d271dd6475a79e4a70843f0e3c97f5dca4fc6f1f
Name:      gnome-multi-writer
Version:   3.35.90
Release:        17%{?dist}
Summary:        Write an ISO file to multiple USB devices at once
License:   GPL-2.0-or-later
URL:       https://wiki.gnome.org/Apps/MultiWriter
Source0:        https://download.gnome.org/sources/gnome-multi-writer/3.35/gnome-multi-writer-%{version}.tar.xz
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  libcanberra-devel
BuildRequires:  libgudev1-devel
BuildRequires:  libgusb-devel
BuildRequires:  libudisks2-devel
BuildRequires:  meson
BuildRequires:  polkit-devel
# /oreon:deps
%description
GNOME MultiWriter can be used to write an ISO file to multiple USB devices
simultaneously.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
