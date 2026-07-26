%global source0_hash b5d82e2cb167d22fb819ab739bbd8d6ca77b87367d4e3d23728e439d65fb93c3

Name:           geany-themes
Version:        1.27
Release:        22%{?dist}
Summary:        A collection of syntax highlighting color schemes for Geany

# Some of the color schemes are clearly stated as GPLv2+, some are BSD
# Automatically converted from old format: GPLv2+ and BSD - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-BSD

URL:            https://github.com/geany/geany-themes
Source0:        https://github.com/geany/geany-themes/releases/download/%{version}/geany-themes-%{version}.tar.bz2

Requires:       geany >= 1.24
BuildArch:      noarch

%description
Geany-Themes is a set of syntax highlighting color schemes for the Geany IDE.
Simply install this package, restart Geany and find the themes in
View->Editor->Color Schemes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
# Nothing to build here. We just have to place some configuraton files into the
# proper directory..

%install
install -d $RPM_BUILD_ROOT%{_datadir}/geany/colorschemes
install -pm 644 colorschemes/*.conf $RPM_BUILD_ROOT%{_datadir}/geany/colorschemes

%files
%doc AUTHORS COPYING README.md
%{_datadir}/geany/colorschemes/*.conf

%changelog
%autochangelog
