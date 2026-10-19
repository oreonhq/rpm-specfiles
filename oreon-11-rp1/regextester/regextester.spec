%global source0_hash 619e9cb465f98119c17864078d3f308ab5eed4ff1af59f4b45254033cd10a05e
Name:           regextester
Version:        1.1.1
Release:        1%{?dist}
Summary:        Regex Tester for elementary OS
License:        GPL-2.0-or-later
URL:            https://github.com/artemanufrij/regextester
Source0:        https://github.com/artemanufrij/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         appdata.patch
Patch1:         regextester-appdata.patch
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  granite-devel
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  vala-devel
# /oreon:deps
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
%oreon_autofiles main

%check

%meson_test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
