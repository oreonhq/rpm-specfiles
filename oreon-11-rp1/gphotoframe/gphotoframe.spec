%global source0_hash 4163630679b410d6d140c8894ce2ee8b0b34e112184286dd35f0faa781f0e4a3

# Please check again if someone wants to import
# this also to EPEL.

# Upstream uses hg for SCM
# googlecode now no longer provide source, create
# it from SCM
#
# hg clone https://code.google.com/p/gphotoframe/
# cd gphotoframe/
# hg archive -t tbz2 "gphotoframe-<version>-hg%h.tar.bz2"

%global	hghash		2084299dffb6

%global	mainver	2.0.2
#%%define	minorver	-b1

%global	baserelease	40

%global	rpmminorver	%(echo "%minorver" | sed -e 's|^-||' | sed -e 's|\\\.||')
%global	fedorarel	%{?minorver:0.}%{baserelease}%{?minorver:.%rpmminorver}%{?hghash:.hg%hghash}

Name:		gphotoframe
Version:	%{mainver}
Release:	%{fedorarel}%{?dist}
Summary:	Photo Frame Gadget for the GNOME Desktop

# Overall	GPL-3.0-or-later
# help/C/gphotoframe.xml	GFDL-1.1-or-later
# lib/utils/EXIF.py	BSD-3-Clause
# lib/utils/urlget.py	MIT
# share/history/jquery.lazyload.js	MIT
# Some images (see COPYING)	GPL-2.0-or-later
# SPDX confirmed
License:	GPL-3.0-or-later AND GPL-2.0-or-later AND MIT AND BSD-3-Clause AND GFDL-1.1-or-later
URL:		http://code.google.com/p/gphotoframe/
#Source0:	http://gphotoframe.googlecode.com/files/%{name}-%{mainver}%{?minorver}.tar.gz
Source:	%{name}-%{mainver}%{?minorver}%{?hghash:-hg%hghash}.tar.bz2
# bug 1078155
# The following file missing
#Source1:	https://gphotoframe.googlecode.com/hg/share/assistant_facebook.glade

# Handle exif file with zero denominator on geometry information
# bug 845418
Patch2:	gphotoframe-2.0a2-parseexif-geom-zerovalue.patch
# Fix yet another case on exif information with zero denominator
# bug 885377
Patch3:	gphotoframe-1.5.1-parseexif-fraction-zerodiv.patch
# Support python-twisted 13.x API
#Patch4:	gphotoframe-2.0-a3-twisted-13-API.patch
# https://git.gnome.org/browse/gdk-pixbuf/commit/?id=112eab418137df2d2f5f97e75fb48f17e7f771e7
# gdk-pixbuf 2.31.2 changed API
Patch4:	gphotoframe-2.0.1-gdk-pixbuf2-2_31_2_API.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1296817
# disable libproxy support for now
Patch5:	gphotoframe-2.0.2-disable-libproxy.patch
# F-26+: Switch to WebKit2 (on Fedora: it is webkitgtk4)
Patch6:	gphotoframe-2.0.2-WebKit2.patch
# F-31+: Switch to python3
Patch100:	gphotoframe-2.0.2-python3.patch
# F-34: Patch to support feedparser 6
Patch101:	gphotoframe-2.0.2-feedparser-6.patch
# F-33+: Patch for python3x: bunch of fixes for plugins, mainly for authentification
Patch102:	gphotoframe-2.0.2-plugin-bunch-fix-py3x.patch
# Limit number of times for checking idle status when service is not available
# to shutdown warning
Patch103:	gphotoframe-2.0.2-idle-check-limit-time.patch
# python3x: fix for urlget
Patch104:	gphotoframe-2.0.2-urlget-py3.patch
# Move help URL according to freedesktop specification
Patch105:	gphotoframe-2.0.2-help-url-spec.patch
# Again, Patch for python3x: fixes for plugins, mainly for configuring plugins
Patch106:	gphotoframe-2.0.2-plugin-bunch-fix-py3x-02.patch
# Don't try to open file with double click on window at startup, when
# no photo is loaded yet:
# Fixes https://retrace.fedoraproject.org/faf/reports/61954/
Patch107:	gphotoframe-2.0.2-fix-double-click-at-startup.patch
# Borrow python-twisted 21.7 HTTPDownloader for now
Patch108:	gphotoframe-twisted-2107-HTTPDownloader.patch
# Port to setuptools: PEP632
Patch109:	gphotoframe-2.0.2-pep632-distutils-port.patch
# randrange argument needs to be int, python 3.12 causes error when
# argument is float
Patch110:	gphotoframe-2.0.2-python312-random-argument-int.patch
# Rescue GdkPixbuf.Pixbuf.new error
Patch111:	gphotoframe-2.0.2-gdkpixbuf_error-handling.patch
# Remove obsolete cgi module
Patch112:	gphotoframe-2.0.2-python308-remove-cgi.patch
# When loading rss is taking loong time (then aborted),
# trying to show rss photo causes exception
Patch113:	gphotoframe-2.0.2-rss-taking-long-time-exception.patch
Provides:	bundle(python3-twisted) = 21.7

BuildRequires:	GConf2
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	python3-devel
BuildRequires:	python3-distutils-extra
# For creating symlink -> python-bytecompiling
#BuildRequires:	python3-exif
# From 1.2-b6: setup.py needs this
BuildRequires:	python3-pyxdg
# Documents
BuildRequires:	%{_bindir}/xsltproc
BuildRequires:	%{_bindir}/xml2po
# F-35+: use fixed xml2po (ref: bug 2014227)
BuildRequires:	gnome-doc-utils >= 0.20.10-27

# Mandatory
Requires:	python3-gobject
#Requires:	python3-exif
Requires:	python3-twisted
# twisted favors service-identity
Requires:	python3-service-identity
# twisted/internet/ssl.py
Requires:	python3-pyOpenSSL
Requires:	python3-pyxdg
# lib/plugins/tumblr/account.py
#Requires:	python2-oauth

# girepository
Requires:	gtk3
Requires:		webkit2gtk4.1
# Optional
# see bug 1296817
# Requires:	libproxy-python
# girepository
Requires:	clutter-gtk
Requires:	python3-feedparser
# girepository
Requires:	libchamplain-gtk
# .ico image files
%if 0%{?fedora} >= 41
Requires:	gdk-pixbuf2-modules-extra
%endif
# Scriptlets
Requires(pre):	GConf2

BuildArch:	noarch

%description
Gnome Photo Frame is a photo frame gadget for the GNOME Desktop.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{mainver}%{?minorver}%{?hghash:-hg%hghash}

%patch -P2 -p2 -b .zeroden -Z
%patch -P3 -p1 -b .zeroden2 -Z
%patch -P4 -p1 -b .pixbuf_23102 -Z
%patch -P5 -p1 -b .libproxy_disable -Z
%patch -P6 -p1 -b .wk2 -Z

# https://github.com/pypa/setuptools/pull/4870/
# setuptools 78 no longer allows dash-separated and uppercase options in setup.cfg
sed -i setup.cfg -e 's|icon-dir=|icon_dir=|'

# Remove unneeded shebangs
grep -rl '^#![ \t]*%{_bindir}' lib/ | \
	xargs sed -i -e '\@^#![ \t]*%{_bindir}@d'

# install missing glade file
# bug 1078155
#cp -p %%{SOURCE1} share/
sed -i.glade \
	-e "s|'share/menu.ui',|'share/menu.ui','share/assistant_facebook.glade',|" \
	setup.py

# Explicitly don't use clutter-gtk for now
# Enable again with 2.0-a3
%if 0
grep -rl 'import clutter' lib/ | \
	xargs sed -i -e 's|import clutter|import dont_use_clutter|'
%endif

%if 0
# Use system-wide EXIF
ln -sf %{python_sitelib}/EXIF.py lib/utils/EXIF.py
%endif

# Once doing this
grep -rlZ "/usr/bin/python$" . | xargs --null sed -i -e 's|/usr/bin/python$|/usr/bin/python2|'
# Then patch
%patch -P100 -p1 -b .py3 -Z
%patch -P101 -p1 -b .feedparser6 -Z
%patch -P102 -p1 -b .bunchfix -Z
%patch -P103 -p1 -b .idle -Z
%patch -P104 -p1 -b .urlget_py3 -Z
%patch -P105 -p1 -b .helpurl -Z
%patch -P106 -p1 -b .py3_config -Z
%patch -P107 -p1 -b .open_startup -Z
%patch -P108 -p1 -Z
%patch -P109 -p1 -Z
%patch -P110 -p1 -b .py312 -Z
%patch -P111 -p1 -b .pixbuf_err -Z
%patch -P112 -p1 -b .cgi -Z
%patch -P113 -p1 -b .rss_loong -Z

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%if 0
# And again use system-wide EXIF.py
ln -sf %{python_sitelib}/EXIF.py \
	%{buildroot}%{python_sitelib}/%{name}/utils/EXIF.py
%endif

# Gsettings Schemas
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas
install -cpm 0644 \
	share/com.googlecode.gphotoframe.gschema.xml.in \
	%{buildroot}%{_datadir}/glib-2.0/schemas/com.googlecode.gphotoframe.gschema.xml

# Desktop
desktop-file-validate \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

# Move help documents according to freedesktop specification
for lang in \
	C it ja \
	%{nil}
do
	mkdir -p %{buildroot}%{_datadir}/help/${lang}/%{name}
	mv \
		%{buildroot}%{_datadir}/gnome/help/%{name}/${lang}/* \
		%{buildroot}%{_datadir}/help/${lang}/%{name}
	if [ -f %{buildroot}%{_datadir}/help/${lang}/%{name}/%{name}.xml ]
	then
		mv \
			%{buildroot}%{_datadir}/help/${lang}/%{name}/%{name}.xml \
			%{buildroot}%{_datadir}/help/${lang}/%{name}/index.docbook
	fi
done
# Cleanups
find %{buildroot}%{_datadir}/gnome/help/ -type d | sort -r | xargs rmdir

# gnome-screensver related
# FIXME: I don't use gnome-screensaver...
mkdir -p \
	%{buildroot}%{_libexecdir}/gnome-screensaver
# ignore failure (if any) for screensaver desktop
desktop-file-validate \
	%{buildroot}%{_datadir}/applications/screensavers/gphotoframe-screensaver.desktop || true
# lib/ is hardcoded in setup.py
mv %{buildroot}%{_prefix}/lib/gnome-screensaver/gnome-screensaver/gphotoframe-screensaver \
	%{buildroot}%{_libexecdir}/gnome-screensaver/

rm -rf \
	%{buildroot}%{_libexecdir}/gnome-screensaver/ \
	%{buildroot}%{_datadir}/applications/screensavers/ \
	%{nil}

find %{buildroot}%{_prefix} -name \*.py3 -delete

%find_lang %{name}

%if 0
# Treak brp-python-bytecompile
%global	__os_install_post_orig		%{__os_install_post}
%global	__os_install_post \
	%__os_install_post_orig \
	for f in %{python_sitelib}/EXIF.py* \
	do \
		ln -sf $f %{buildroot}%{python_sitelib}/%{name}/utils/$(basename $f) \
	done \
	%{nil}
%endif

%pre
%gconf_schema_obsolete %{name}

%files	-f %{name}.lang
%defattr(-,root,root,-)
%license	COPYING
%license	GPL
%doc	README
%doc	changelog

%{_bindir}/%{name}
%{python3_sitelib}/%{name}-*.*-info
%{python3_sitelib}/%{name}/

%dir	%{_datadir}/%{name}/
%{_datadir}/%{name}/*.ui
%{_datadir}/%{name}/*.png
%{_datadir}/%{name}/*.glade
%{_datadir}/%{name}/extra/
%{_datadir}/%{name}/history/

%{_datadir}/help/*/%{name}/
%{_datadir}/omf/%{name}/

#%%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_datadir}/glib-2.0/schemas/com.googlecode.%{name}.gschema.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*

%{_datadir}/appdata/%{name}.appdata.xml

%changelog
%autochangelog
