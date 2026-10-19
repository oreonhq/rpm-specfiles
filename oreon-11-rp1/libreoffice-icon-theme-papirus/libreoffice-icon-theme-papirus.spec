%global source0_hash 396402c9327506a729d3c01e339528dd5b5f9b205cb3edabca4eb85b5db5df6d
%global upstream_name   papirus-libreoffice-theme
%global debug_package %{nil}
Name:           libreoffice-icon-theme-papirus
Version:        20170228
Release:        1%{?dist}
Summary:        Papirus theme for LibreOffice
License:        GPL-3.0-only
URL:            https://github.com/PapirusDevelopmentTeam/papirus-libreoffice-theme
Source0:        https://github.com/PapirusDevelopmentTeam/%{upstream_name}/archive/%{version}/%{upstream_name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  make
# /oreon:deps
%description
Papirus theme for LibreOffice.

It is available in three variants:

 - ePapirus
 - Papirus
 - Papirus Dark

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{upstream_name}-%{version}

%build

%install
%make_install PREFIX=%{_libdir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
