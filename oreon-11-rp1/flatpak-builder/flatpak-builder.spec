%global source0_hash 8d5b791f7a8449d6a8ebcff0c8d6abd5335113f56703bf5777ee4c7db4bda378
%global appstream_version 0.16.3
%global debugedit_version 5.0
%global glib2_version 2.66
%global ostree_version 2017.14
%global flatpak_version 0.99.1
%global __requires_exclude ^/usr/bin/python2$
Name:           flatpak-builder
Version:        1.4.12
Release:        1%{?dist}
Summary:        Tool to build flatpaks from source
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            https://flatpak.org/
Source0:        https://github.com/flatpak/flatpak-builder/releases/download/%{version}/%{name}-%{version}.tar.xz
Requires:       appstream-compose >= %{appstream_version}
Requires:       debugedit >= %{debugedit_version}
Requires:       flatpak%{?_isa} >= %{flatpak_version}
Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       ostree-libs%{?_isa} >= %{ostree_version}
Requires:       /usr/bin/rofiles-fuse
Recommends:     /usr/bin/bsdunzip
Recommends:     /usr/bin/bzip2
Recommends:     /usr/bin/eu-strip
Recommends:     /usr/bin/git
Recommends:     /usr/bin/git-lfs
Recommends:     /usr/bin/patch
Recommends:     /usr/bin/strip
Recommends:     /usr/bin/tar
Recommends:     /usr/bin/zstd
Recommends:     ccache
# oreon:deps
BuildRequires:  /usr/bin/xmlto
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  appstream-compose
BuildRequires:  debugedit
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  flatpak
BuildRequires:  gettext
BuildRequires:  libcap-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(ostree-1)
BuildRequires:  pkgconfig(yaml-0.1)
# /oreon:deps
%description
Flatpak-builder is a tool for building flatpaks from sources.

See https://flatpak.org/ for more information.

%package tests
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description tests
This package contains installed tests for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Ddocs=enabled -Dfuse=3 -Dinstalled_tests=true -Dyaml=enabled
%meson_build
%install
%meson_install
install -pm 644 NEWS README.md %{buildroot}/%{_pkgdocdir}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n flatpak-builder-tests -f %{oreon_filedir}/flatpak-builder-tests.list

%changelog

%autochangelog
