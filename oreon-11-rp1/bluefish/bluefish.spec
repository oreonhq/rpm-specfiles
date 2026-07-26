%global source0_hash 3d0d0ac6553c83251a2031d4ea9e36a8c8947dd6e5e40a868e34ad0f5d2ea822

%global pkgver 2.4.0
#global prerel rc1
%global baserelease 1

Name:		bluefish
Version:	%{pkgver}
Release:	%{?prerel:0.}%{baserelease}%{?prerel:.%{prerel}}%{?dist}
Summary:	Web development application for experienced users
License:	GPL-3.0-or-later
URL:		http://bluefish.openoffice.nl/
Source0:	http://www.bennewitz.com/bluefish/stable/source/bluefish-%{version}%{?prerel:-%{prerel}}.tar.bz2
Patch0:		bluefish-2.2.13-strict-aliasing.patch
Patch1:		bluefish-2.2.16-shellbang.patch
BuildRequires:	coreutils
BuildRequires:	desktop-file-utils
BuildRequires:	enchant2-devel
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	gettext >= 0.19.7
BuildRequires:	glib2-devel >= 2.76
BuildRequires:	gtk3-devel >= 3.2
BuildRequires:	gucharmap-devel >= 2.90
BuildRequires:	hardlink
BuildRequires:	intltool
BuildRequires:	libxml2-devel
BuildRequires:	make
BuildRequires:	python3-devel >= 3.3
BuildRequires:	libappstream-glib >= 0.3.6
BuildRequires:	which
# Needed to check man pages
BuildRequires:	/usr/bin/man
# For the Advanced Open function
Requires:	findutils, grep
Requires:	%{name}-shared-data = %{version}-%{release}

# Automatically upgrade bluefish-unstable
Obsoletes:	bluefish-unstable < %{version}-%{release}
Provides:	bluefish-unstable = %{version}-%{release}

# XML Catalog registration
Requires(post): /usr/bin/xmlcatalog, xml-common
Requires(postun): /usr/bin/xmlcatalog, xml-common

# Explicitly disable automatic byte-compilation of python in non-python library locations
%global _python_bytecompile_extra 0

%description
Bluefish is a powerful editor for experienced web designers and programmers.
Bluefish supports many programming and markup languages, but it focuses on
editing dynamic and interactive websites.

%package shared-data
Summary:	Architecture-independent data for %{name}
BuildArch:	noarch
# So that we pull in the binary when someone installs the data (#1091613)
Requires:	%{name} = %{version}-%{release}

# Automatically upgrade bluefish-unstable-shared-data
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

# Make zencoding plugin scripts executable to placate rpmlint
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

# Manually install docs so that they go into
# %%{_pkgdocdir} even though we put them in the
# shared-data subpackage
install -m 644 -p -t %{buildroot}%{_pkgdocdir}/ \
	AUTHORS ChangeLog README TODO

# Unpackaged files
rm -f %{buildroot}%{_libdir}/bluefish/*.la

# Explicitly byte-compile "extra" python code using Python 3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/bluefish

# hardlink identical images together
hardlink -cv %{buildroot}%{_datadir}/{icons,pixmaps}

# hardlink identical message files together
hardlink -cv %{buildroot}%{_datadir}/locale

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

%files
%license COPYING
%{_bindir}/bluefish
%{_libdir}/bluefish/

%files shared-data -f %{name}.lang
%doc %{_pkgdocdir}/
%{_datadir}/bluefish/
%{_datadir}/metainfo/bluefish.appdata.xml
%{_datadir}/applications/bluefish.desktop
%{_datadir}/mime/packages/bluefish.xml
%{_datadir}/icons/hicolor/*/mimetypes/application-x-bluefish-project.png
%{_datadir}/icons/hicolor/*/apps/bluefish.png
%{_datadir}/icons/hicolor/scalable/mimetypes/bluefish-project.svg
%{_datadir}/icons/hicolor/scalable/apps/bluefish-icon.svg
%{_datadir}/pixmaps/application-x-bluefish-project.png
%{_datadir}/pixmaps/bluefish.png
%{_datadir}/xml/bluefish/
%{_mandir}/man1/bluefish.1*

%changelog
%autochangelog
