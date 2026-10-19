%global source0_hash fa9ede366f0a72e4caa52189c3ab0b10c1b56a80c7885b016602558c44dce7d3
%global tarball_version %%(echo %{version} | tr '~' '.')
Name:           tali
Version:        40.9
Release:        1%{?dist}
Summary:        GNOME Tali game
License:        GPL-2.0-or-later AND LicenseRef-Callaway-GFDL
URL:            https://wiki.gnome.org/Apps/Tali
Source0:        https://download.gnome.org/sources/%{name}/40/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libgnome-games-support-1)
# /oreon:deps
%description
Sort of poker with dice and less money. An ancient Roman game.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n tali-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name} --all-name --with-gnome
%oreon_autofiles main

%check

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
