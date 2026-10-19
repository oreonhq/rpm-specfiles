%global source0_hash 2de3ce77d7309699ab2cf6124ad12aa20c7d600e9f01dec8f66fa3ea678be2ec
Name:           bustle
Version:        0.14.0
Release:        1%{?dist}
Summary:        Visualize D-Bus activity
SourceLicense:  LGPL-2.1-or-later
License:        %{shrink:
    LGPL-2.1-or-later AND
    MIT AND
    Unicode-3.0 AND
    Unicode-DFS-2016 AND
    (Apache-2.0 OR MIT) AND
    (Unlicense OR MIT)
}
URL:            https://gitlab.gnome.org/World/bustle
Source0:        https://gitlab.gnome.org/World/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
Patch:          0001-adapt-meson-wrapper-code-for-cargo-for-compatibility.patch
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cargo-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  meson
# /oreon:deps
%description
Bustle draws sequence diagrams of D-Bus activity, showing signal
emissions, method calls and their corresponding returns, with timestamps
for each individual event and the duration of each method call. This can
help you check for unwanted D-Bus traffic, and pinpoint why your
D-Bus-based application isn't performing as well as you like. It also
provides statistics like signal frequencies and average method call
times.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir bustle-%{version}
%oreon_prep
%build

%meson
%meson_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%meson_install
%find_lang bustle
%oreon_autofiles main

%check

desktop-file-validate \
    %{buildroot}%{_datadir}/applications/org.freedesktop.Bustle.desktop
appstream-util validate-relax --nonet \
    %{buildroot}%{_datadir}/metainfo/org.freedesktop.Bustle.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
