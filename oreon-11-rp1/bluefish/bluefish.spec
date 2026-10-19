%global source0_hash 3d0d0ac6553c83251a2031d4ea9e36a8c8947dd6e5e40a868e34ad0f5d2ea822
%global pkgver 2.4.0
%global baserelease 1
Name:		bluefish
Version:	%{pkgver}
Release:        1%{?dist}
Summary:        Web development application for experienced users
License:	GPL-3.0-or-later
URL:		http://bluefish.openoffice.nl/
Source0:        http://www.bennewitz.com/%{name}/stable/source/%{name}-%{version}.tar.bz2
Patch0:		bluefish-2.2.13-strict-aliasing.patch
Patch1:		bluefish-2.2.16-shellbang.patch
Requires:	findutils, grep
Requires:	%{name}-shared-data = %{version}-%{release}
Obsoletes:	bluefish-unstable < %{version}-%{release}
Provides:	bluefish-unstable = %{version}-%{release}
Requires(post): /usr/bin/xmlcatalog, xml-common
Requires(postun): /usr/bin/xmlcatalog, xml-common
%global _python_bytecompile_extra 0
# oreon:deps
BuildRequires:  /usr/bin/man
BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
BuildRequires:  enchant2-devel
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  gucharmap-devel
BuildRequires:  hardlink
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  which
# /oreon:deps
%description
Bluefish is a powerful editor for experienced web designers and programmers.
Bluefish supports many programming and markup languages, but it focuses on
editing dynamic and interactive websites.

%package shared-data
Summary:	Architecture-independent data for %{name}
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}
Obsoletes:	bluefish-unstable-shared-data < %{version}-%{release}
Provides:	bluefish-unstable-shared-data = %{version}-%{release}
%description shared-data
Files common to every architecture version of %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}%{?prerel:-%{prerel}}

# Avoid potential aliasing issues in zencoding plugin
%patch -P 0

# Avoid use of /usr/bin/env in shipped scripts
# Also change /usr/bin/python → /usr/bin/python3
%patch -P 1

%build

%configure	--disable-dependency-tracking \
		--disable-static \
		--disable-update-databases \
		--disable-xml-catalog-update \
		--docdir=%{_pkgdocdir}
%{make_build}
%install
mkdir -p %{buildroot}%{_datadir}/applications
%{make_install}
find %{buildroot}%{_datadir}/bluefish/plugins/zencoding -name '*.py' |
	xargs awk '/^#!/ { print FILENAME }' |
	xargs chmod -c +x
%find_lang %{name}
%find_lang %{name}_plugin_about
%find_lang %{name}_plugin_charmap
%find_lang %{name}_plugin_entities
%find_lang %{name}_plugin_htmlbar
%find_lang %{name}_plugin_snippets
%find_lang %{name}_plugin_zencoding
cat %{name}_plugin_{about,charmap,entities,htmlbar,snippets,zencoding}.lang >> \
	%{name}.lang
appstream-util --nonet validate-relax \
	%{buildroot}%{_datadir}/metainfo/bluefish.appdata.xml
desktop-file-validate \
	%{buildroot}%{_datadir}/applications/bluefish.desktop
install -m 644 -p -t %{buildroot}%{_pkgdocdir}/ \
	AUTHORS ChangeLog README TODO
rm -f %{buildroot}%{_libdir}/bluefish/*.la
%py_byte_compile %{python3} %{buildroot}%{_datadir}/bluefish
hardlink -cv %{buildroot}%{_datadir}/{icons,pixmaps}
hardlink -cv %{buildroot}%{_datadir}/locale
%oreon_autofiles bluefish-shared-data usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post shared-data

xmlcatalog --noout --add 'delegateURI' \
	'http://bluefish.openoffice.nl/ns/bflang/2.0/' \
	'%{_datadir}/xml/bluefish' \
	%{_sysconfdir}/xml/catalog &> /dev/null || :
%postun shared-data

if [ "$1" = 0 ]; then
	xmlcatalog --noout --del \
		'http://bluefish.openoffice.nl/ns/bflang/2.0/' \
		%{_sysconfdir}/xml/catalog &> /dev/null || :
fi
%files -f %{oreon_filedir}/main.list
%files -n bluefish-shared-data -f %{oreon_filedir}/bluefish-shared-data.list

%changelog

%autochangelog
