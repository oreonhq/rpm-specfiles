%global source0_hash dc4b54956caa6279cb47ed7bc806c2b819a79e303902a4db15bd5ab31e0e9f64
%define BothRequires() \
Requires:       %{*} \
%{nil}
%define		majorver	0.7.11
%undefine		minorver	
%undefine		ifpre	
%define		baserelease	13
%define		rel		%{?ifpre:0.}%{baserelease}%{?minorver:.%minorver}
Name:		alexandria
Version:	%{majorver}
Release:        1%{?dist}
Summary:        Book collection manager
License:	GPL-2.0-or-later AND GPL-2.0-or-later
URL:		https://github.com/mvz/alexandria-book-collection-manager/
Source0:        https://github.com/mvz/%{name}-book-collection-manager//archive/v%{version}/%{name}-%{version}.tar.gz
Patch3:		alexandria-0.7.4-dont_use_thread_when_adding_file_by_isdn.patch
Patch14:	alexandria-0.7.9-ascii-fix.patch
Patch18:	alexandria-0.7.9-utf8-convert.patch
Patch19:	alexandria-0.7.4-export-to-HTML-with-ruby19.patch
Patch20:	alexandria-0.7.5-export-to-CSV-bintex-with-ruby19.patch
Patch21:	alexandria-0.7.4-iconview-multibyte.patch
Patch22:	alexandria-0.7.9-yaml-unescape.patch
Patch23:	alexandria-0.7.4-delete-broken-yaml.patch
Patch25:	alexandria-0.7.6-newbook-nothread.patch
Patch26:	alexandria-0.7.9-z3950-zoom-count.patch
Patch29:	alexandria-0.7.4-glade-gettext.patch
Patch30:	alexandria-0.7.4-title-force-encoding.patch
Patch31:	alexandria-0.7.4-remove-undefined-method.patch
Patch32:	alexandria-0.7.8-reset-search-when-adding-new-book.patch
Patch33:	alexandria-0.7.8-explicitly-specify_gem_image_size.patch
BuildArch:	noarch
Requires:	ruby(release)
%BothRequires	rubygem(rexml)
%BothRequires	rubygem(gettext)
%BothRequires	rubygem(htmlentities)
%BothRequires	rubygem(image_size)
%BothRequires	rubygem(nokogiri)
%BothRequires	rubygem(psych)
%BothRequires	rubygem(zoom) >= 0.3.0
%BothRequires	rubygem(marc)
Requires:	GConf2
%BothRequires	rubygem(gdk_pixbuf2)
%BothRequires	rubygem(glib2)
%BothRequires	rubygem(goocanvas) >= 2
%BothRequires	rubygem(gstreamer)
%BothRequires	rubygem(gtk3)
%BothRequires	rubygem(syck)
Requires(pre):		GConf2
Requires(post):		GConf2
Requires(preun):	GConf2
# oreon:deps
BuildRequires:  /usr/bin/ping
BuildRequires:  /usr/bin/xvfb-run
BuildRequires:  GConf2
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  gstreamer1-plugins-base
BuildRequires:  gstreamer1-plugins-good
BuildRequires:  intltool
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(gdk_pixbuf2)
BuildRequires:  rubygem(gettext)
BuildRequires:  rubygem(glib2)
BuildRequires:  rubygem(goocanvas)
BuildRequires:  rubygem(gstreamer)
BuildRequires:  rubygem(gtk3)
BuildRequires:  rubygem(htmlentities)
BuildRequires:  rubygem(image_size)
BuildRequires:  rubygem(json)
BuildRequires:  rubygem(marc)
BuildRequires:  rubygem(nokogiri)
BuildRequires:  rubygem(pry)
BuildRequires:  rubygem(psych)
BuildRequires:  rubygem(rake)
BuildRequires:  rubygem(rexml)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(syck)
BuildRequires:  rubygem(webmock)
BuildRequires:  rubygem(zoom)
# /oreon:deps
%description
Alexandria is a GNOME application to help you manage your book collection.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-book-collection-manager-%{majorver}%{?minorver:-%{?minorver}}

# Check if patch2 issue is fixed in rev 1154
#%%patch -P2 -p0 -b .up25348
%patch -P3 -p1 -b .up28263.isdn
#%%patch -P4 -p0 -b .up29479.search
%patch -P14 -p1 -b .ascii -Z
#%%patch -P15 -p1 -b .kcodefix 
%patch -P18 -p1 -b .ruby19_utf8 -Z
%patch -P19 -p1 -b .export_html -Z
%patch -P20 -p1 -b .export_csv -Z
%patch -P21 -p1 -b .icon_kanji -Z
%patch -P22 -p1 -b .broken_yaml -Z
%patch -P23 -p1 -b .delete_yaml -Z
%patch -P25 -p1 -b .nothread -Z
%patch -P26 -p1 -b .z3950_count -Z
#%%patch -P27 -p1 -b .negative -Z
%patch -P29 -p1 -b .gettext -Z
%patch -P30 -p1 -b .utf8_2 -Z
%patch -P31 -p1 -b .undefined_method -Z
%patch -P32 -p1 -b .reset_search -Z
%patch -P33 -p1 -b .image_size -Z

# Part of https://github.com/mvz/alexandria-book-collection-manager/commit/d9116e99242c209129bf09c3c1ad9a4ff6fdcf44
# Needed for ruby3.2 - removes File.exists?
sed -i util/rake/gettextgenerate.rb -e 's|unless FileTest.exists.*$||'

# Embed Fedora EVR
%{__sed} -i.evr \
	-e "s|\(DISPLAY_VERSION = \).*$|\1'%{version}-%{release}'|" \
	Rakefile

# Make msgfmt verbose
%{__sed} -i.msgfmt \
	 -e '/system/s|msgfmt |msgfmt --statistics |' \
	util/rake/gettextgenerate.rb

# Workaround for directory hierarchy
ln -sf share data

# Use system wide directory for datadir
sed -i lib/alexandria/config.rb \
	-e "\@^[ \t]*SHARE_DIR@s|SHARE_DIR[ \t]*=.*|SHARE_DIR = '/usr/share'|"

%build

rake build --trace
%install
rake install_package_staging \
	DESTDIR=$RPM_BUILD_ROOT \
	RUBYLIBDIR=%{ruby_vendorlibdir}
desktop-file-install \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications/ \
	--delete-original \
	$RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
%{__mkdir_p} $RPM_BUILD_ROOT%{_sysconfdir}
%{__mv} \
	$RPM_BUILD_ROOT%{_datadir}/gconf/ \
	$RPM_BUILD_ROOT%{_sysconfdir}/
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/menu/
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/pixmaps/
%{__rm} -f $RPM_BUILD_ROOT%{_bindir}/%{name}.*
mkdir -p $RPM_BUILD_ROOT%{_datadir}/metainfo
cat > $RPM_BUILD_ROOT%{_datadir}/metainfo/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!--
BugReportURL: https://github.com/mvz/alexandria-book-collection-manager/issues/2
SentUpstream: 2014-09-18
-->
<application>
  <id type="desktop">alexandria.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Manage your physical book collection</summary>
  <description>
    <p>
      Alexandria is an application that allows you to manage your book library.
      It lets you build and keep a detailed database (on your local machine) of
      information about books you own and have read.
    </p>
    <p>
      Alexandria also allows you to rate books, note when you have read them,
      and even track who you have loaned books out to.
      It also has interfaces with a online book information sources so you don’t
      have to type in all the information about a book, and also provides book
      cover art for many books.
    </p>
  </description>
  <url type="homepage">http://alexandria.rubyforge.org/</url>
  <screenshots>
    <screenshot type="default">https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/alexandria/a.png</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF
%find_lang %{name}
%oreon_autofiles main

%check

export LANG=C.utf8
sed -i.testsuite lib/alexandria/config.rb \
	-e 's|/usr/share|%{buildroot}%{_datadir}|'
disable_test() {
	sed -i.testsuite $1 -e "\@$2@s|it|xit|"
}
rm -rf .config/gconf
mkdir -p .config/gconf
export XDG_CONFIG_HOME=$(pwd)/.config
mkdir -p FAKE/bundler
touch FAKE/bundler/setup.rb
touch FAKE/simplecov.rb
export RUBYLIB=$(pwd)/FAKE
disable_test spec/alexandria/book_providers/bl_provider_spec.rb "works"
ping -w3 www.google.co.jp && \
	{
		disable_test spec/alexandria/book_providers/loc_provider_spec.rb "works for a book";
		true;
	} \
	|| \
	{
		disable_test spec/alexandria/book_providers/thalia_provider_spec.rb "works when searching by ISBN";
		disable_test spec/alexandria/book_providers/loc_provider_spec.rb "works for a book";
		disable_test spec/alexandria/book_providers/sbn_provider_spec.rb "works";
		sed -i spec/alexandria/book_providers_spec.rb -e "\@Alexandria::BookProviders::SBNProvider@{n;s|it|xit|}";
	}
xvfb-run \
	-s "-screen 0 640x480x24" \
	rake spec:unit
find . -name \*.testsuite | while read f
do
	mv ${f} ${f%.testsuite}
done
%pre

%gconf_schema_prepare %{name}
%post

%gconf_schema_upgrade %{name}
%preun

%gconf_schema_remove %{name}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
