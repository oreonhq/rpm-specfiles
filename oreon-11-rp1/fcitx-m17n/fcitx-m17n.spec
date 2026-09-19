%global source0_hash cf82158b907ba6b79aad3e4c26f9e0e2457a270619548adc31e9f77412144597

Name:		fcitx-m17n
Version:	0.2.4
Release:	23%{?dist}
Summary:	M17n Engine for Fcitx
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+
URL:		https://fcitx-im.org/wiki/M17N
Source0:	http://download.fcitx-im.org/fcitx-m17n/%{name}-%{version}.tar.xz

BuildRequires:	gcc
BuildRequires:	cmake, fcitx-devel, gettext, intltool, m17n-lib-devel
Requires:	fcitx

%description
Fcitx-m17n is a M17n engine wrapper for Fcitx. 
It allows input of many languages using the 
input table maps from m17n-db.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING README.rst
%{_libdir}/fcitx/%{name}.so
%{_datadir}/fcitx/addon/%{name}.conf
%{_datadir}/fcitx/configdesc/%{name}.desc
%{_datadir}/fcitx/m17n/default

%changelog
%autochangelog
