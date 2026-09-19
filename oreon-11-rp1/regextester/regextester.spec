%global source0_hash 619e9cb465f98119c17864078d3f308ab5eed4ff1af59f4b45254033cd10a05e

Name:           regextester
Version:        1.1.1
Release:        12%{?dist}
Summary:        Regex Tester for elementary OS

# For license file: https://github.com/artemanufrij/regextester/issues/25
License:        GPL-2.0-or-later
URL:            https://github.com/artemanufrij/regextester
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         appdata.patch
Patch1:         regextester-appdata.patch

BuildRequires:  desktop-file-utils
BuildRequires:  vala vala-devel
BuildRequires:  granite-devel
BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  libappstream-glib
Requires:       hicolor-icon-theme

%description
Regex Tester for elementary OS

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P0 -p0
%patch -P1 -p0

%build
%meson
%meson_build

%install
%meson_install

%find_lang com.github.artemanufrij.regextester

%check
%meson_test

%files -f com.github.artemanufrij.regextester.lang
%doc README.md
%{_bindir}/com.github.artemanufrij.regextester
%{_datadir}/applications/com.github.artemanufrij.regextester.desktop
%{_datadir}/com.github.artemanufrij.regextester/
%{_datadir}/metainfo/com.github.artemanufrij.regextester.appdata.xml
%{_datadir}/glib-2.0/schemas/com.github.artemanufrij.regextester.gschema.xml
%{_datadir}/icons/hicolor/*/apps/com.github.artemanufrij.regextester.*

%changelog
%autochangelog
