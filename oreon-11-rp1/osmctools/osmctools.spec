%global source0_hash 35c2c176ef28b519d025f7bfeccf4bf25016cbd51223d7e1f96c7bd2f7d9968b

%global commit f341f5f237737594c1b024338f0a2fc04fabdff3

Name:           osmctools
Version:        0.9
Release:        21%{?dist}
Summary:        Tools to manipulate OpenStreetMap files

# Debian man pages are GPLv2+
# Automatically converted from old format: AGPLv3 and GPLv2+ - review is highly recommended.
License:        AGPL-3.0-only AND GPL-2.0-or-later
URL:            https://gitlab.com/osm-c-tools/osmctools
Source0:        https://gitlab.com/osm-c-tools/osmctools/repository/archive.tar.gz?ref=%{version}#/%{name}-%{version}.tar.gz
# Man pages from Debian
Source1:        osmconvert.1
Source2:        osmfilter.1
Source3:        osmupdate.1
# Fix building with gcc 15
Patch0:         %{name}-0.9-gcc15.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  zlib-devel
BuildRequires:  autoconf
BuildRequires:  automake
Requires:       wget

%description
Small collection of basic OpenStreetMap tools, include converter, filter and
updater files.

Programs include:
* osmconvert - Converter of OSM files
* osmfilter - The experimental OSM filters data
* osmupdate - Update OSM files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}-%{commit} -p1

%build
autoreconf -fvi
%configure
%make_build

%install
%make_install

# Install man pages
install -d %{buildroot}%{_mandir}/man1/
for i in %{SOURCE1} %{SOURCE2} %{SOURCE3}; do
  install -p -m 0644 ${i} %{buildroot}%{_mandir}/man1/
done

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/osmconvert
%{_bindir}/osmfilter
%{_bindir}/osmupdate
%{_mandir}/man1/osmconvert.1*
%{_mandir}/man1/osmfilter.1*
%{_mandir}/man1/osmupdate.1*

%changelog
%autochangelog
