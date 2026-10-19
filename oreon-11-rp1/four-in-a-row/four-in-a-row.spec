%global source0_hash 21d2769b804114d1cf0f337426fd88181ecefd6092cf562637eb37d716305182
Name:           four-in-a-row
Version:        3.38.1
Release:        1%{?dist}
Summary:        GNOME Four-in-a-row game
License:        GPL-3.0-or-later AND CC-BY-SA-3.0
URL:            https://wiki.gnome.org/Apps/Four-in-a-row
Source0:        https://download.gnome.org/sources/four-in-a-row/3.38/four-in-a-row-%{version}.tar.xz
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  gsound-devel
BuildRequires:  gtk3-devel
BuildRequires:  itstool
BuildRequires:  librsvg2-devel
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  zlib-devel
# /oreon:deps
%description
The objective of Four-in-a-row is to build a line of four of your marbles
while trying to stop your opponent (human or computer) building a line
of his or her own.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name} --all-name --with-gnome
%oreon_autofiles main

%check

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Four-in-a-row.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
