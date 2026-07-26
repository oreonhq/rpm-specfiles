%global source0_hash 526b7b881c34b698e2bc33f4a21ea155726d645451bf06c3d7319d29a0a81712

%global commit ed4b0826a7ebdb66ad172a3e317cf39c6614f1bd
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20200822
%global debug_package %{nil}
%global py_install_args --no-glib-compile-schemas

Name:           rhythmbox-ampache
Version:        0
Release:        45.%{date}git%{shortcommit}%{?dist}
Summary:        Ampache plugin for Rhythmbox
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/lotan/rhythmbox-ampache
Source0:        https://github.com/lotan/rhythmbox-ampache/archive/%{commit}/%{name}-%{commit}.tar.gz
ExcludeArch:    s390 s390x
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       rhythmbox%{?_isa}

%description
The Rhythmbox Ampache Plugin is a plugin for the music player
Rhythmbox that enables browsing the metadata and streaming music
from an Ampache media server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}

# Fix FTBFS with setuptools >= 61.0.0
# Upstream issue: https://github.com/lotan/rhythmbox-ampache/issues/27
sed -i "33i packages=[]," setup.py

%build
%py3_build

%install
%py3_install -- %py_install_args

%files
%doc README
%license LICENSE
%{_libdir}/rhythmbox/plugins/ampache
%{_datadir}/glib-2.0/schemas/org.gnome.rhythmbox.plugins.ampache.gschema.xml
%{_datadir}/rhythmbox/plugins/ampache
%{python3_sitelib}/rhythmbox_ampache-*-py*.egg-info

%changelog
%autochangelog
