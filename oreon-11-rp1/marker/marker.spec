%global source3_hash 1c0c9496d9e9b693ae364860f0b66c403b87337db1b5a78275a0c78a07495286
%global source2_hash 60237a813383b44891e57049ba1f86cc5b89c28eee620b6ee90582a0c7ba6f8a
%global source1_hash 31e63658e2e79b5c5b0497d568e548f177fc89cb1dd9b6d78aba7685f0506ff0
%global source0_hash 097a6e3811f0c4c14c574b8aafee27ee62232ae3ad3084e18a35c2dc8a1e93dd
%global uuid    com.github.fabiocolacio.%{name}
%global submodule1              scidown
%global submodule1_commit       a7b7f063de4f272ef0ec12d00b98470888e8cb32
%global submodule1_shortcommit  %(c=%{submodule1_commit}; echo ${c:0:7})
%global submodule2              charter
%global submodule2_commit       a25dee1214ea9ba5882325066555cb813efbb489
%global submodule2_shortcommit  %(c=%{submodule2_commit}; echo ${c:0:7})
%global submodule3              tinyexpr
%global submodule3_commit       9476568b69de4c384903f1d5f255907b92592f45
%global submodule3_shortcommit  %(c=%{submodule3_commit}; echo ${c:0:7})
Name:           marker
Version:        2023.05.02
Release:        1%{?dist}
Summary:        GTK 3 markdown editor
License:        GPL-3.0-or-later AND GPL-2.0-only AND LGPL-3.0-or-later AND CC-BY-SA-3.0 AND CC-BY-SA-4.0 AND CC0-1.0 AND ISC AND BSD-3-Clause AND Apache-2.0 AND MIT AND CC0-1.0 AND OFL-1.1 AND Zlib
URL:            https://github.com/fabiocolacio/Marker
Source0:        https://github.com/fabiocolacio/Marker/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/Mandarancio/%{submodule1}/archive/%{submodule1_commit}/%{submodule1}-%{submodule1_shortcommit}.tar.gz
Source2:        https://github.com/Mandarancio/%{submodule2}/archive/%{submodule2_commit}/%{submodule2}-%{submodule2_shortcommit}.tar.gz
Source3:        https://github.com/codeplea/%{submodule3}/archive/%{submodule3_commit}/%{submodule3}-%{submodule3_shortcommit}.tar.gz
Patch:          0001-fix-incompatible-pointer-type.patch
Requires:       %{name}-data = %{version}-%{release}
Requires:       hicolor-icon-theme
Provides:       bundled(highlight-js) = 9.12.0
Provides:       bundled(katex)
Provides:       bundled(mathjax) = 2.7.4
Provides:       bundled(scidown) = 0.1.0~a7b7f06
Provides:       bundled(asana-math-fonts)
Provides:       bundled(gyre-pagella-fonts)
Provides:       bundled(gyre-termes-fonts)
Provides:       bundled(katex-fonts)
Provides:       bundled(latin-modern-fonts)
Provides:       bundled(neo-euler-fonts)
Provides:       bundled(stix-web-fonts)
Provides:       bundled(tex-fonts)
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(gtkspell3-3.0)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
# /oreon:deps
%description
Marker is a markdown editor for Linux made with Gtk+-3.0.

%package        data
Summary:        Data files for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%description    data
Data files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Marker-%{version} -p1
%autosetup -n Marker-%{version} -D -T -a1 -N
%autosetup -n Marker-%{version} -D -T -a2 -N
%autosetup -n Marker-%{version} -D -T -a3 -N

cp %{submodule1}-%{submodule1_commit}/LICENSE LICENSE.%{submodule1}
cp %{submodule2}-%{submodule2_commit}/LICENSE LICENSE.%{submodule2}
cp %{submodule3}-%{submodule3_commit}/LICENSE LICENSE.%{submodule3}

mv %{submodule1}-%{submodule1_commit}/* src/%{submodule1}/
mv %{submodule2}-%{submodule2_commit}/* src/%{submodule1}/src/%{submodule2}/
mv %{submodule3}-%{submodule3_commit}/* src/%{submodule1}/src/%{submodule2}/src/%{submodule3}/

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name}
%find_lang Marker --with-gnome
rm %{buildroot}%{_datadir}/%{uuid}/icons/hicolor/generate.sh
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list
%files -n marker-data -f %{oreon_filedir}/marker-data.list

%changelog

%autochangelog
