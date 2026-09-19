%global source0_hash 396402c9327506a729d3c01e339528dd5b5f9b205cb3edabca4eb85b5db5df6d

%global upstream_name   papirus-libreoffice-theme
%global debug_package %{nil}

Name:           libreoffice-icon-theme-papirus
Version:        20170228
Release:        %autorelease
Summary:        Papirus theme for LibreOffice

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/PapirusDevelopmentTeam/papirus-libreoffice-theme
Source0:        %url/archive/%{version}/%{upstream_name}-%{version}.tar.gz

BuildRequires:  make

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
# Nothing to build

%install
%make_install PREFIX=%{_libdir}

%files
%license LICENSE
%doc AUTHORS README.md
%dir %{_libdir}/libreoffice
%dir %{_libdir}/libreoffice/share
%dir %{_libdir}/libreoffice/share/config
%{_libdir}/libreoffice/share/config/images_*.zip

%changelog
%autochangelog
