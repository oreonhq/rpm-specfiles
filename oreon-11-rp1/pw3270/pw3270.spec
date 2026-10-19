%global source0_hash 2022abfd88baa6501e0cfa59aec329c40245bb47a34ac36f5c6f07d2cf0f819d
%global app_name br.app.pw3270
Name:           pw3270
Version:        5.5.0
Release:        1%{?dist}
Summary:        IBM 3270 Terminal emulator for GTK
License:        LGPL-3.0-only
URL:            https://github.com/PerryWerneck/pw3270
Source0:        https://github.com/PerryWerneck/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Requires:       hicolor-icon-theme
Suggests:       font(ibm3270)
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  libappstream-glib
BuildRequires:  libv3270-devel
BuildRequires:  meson
BuildRequires:  python3-scour
# /oreon:deps
%description
GTK-based IBM 3270 terminal emulator with many advanced features. It can be
used to communicate with any IBM host that supports 3270-style connections
over TELNET.

Based on the original x3270 code, pw3270 was originally created for Banco do
Brasil, and is now used worldwide.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name}
mkdir -p %{buildroot}%{_libdir}/%{name}/5.5/plugins/
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_name}.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{app_name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
