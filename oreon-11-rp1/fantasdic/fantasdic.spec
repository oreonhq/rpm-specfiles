%global source0_hash f337663d3bd4a875f84b08146a58ff3b600f219e2e4647de17bc8c6ec762183c

%define	BothRequires() \
Requires:	%1 \
BuildRequires:	%1 \
%{nil}

%define		mainver		1.0
%define		betaver		beta7

%if 0%{fedora} < 19
%define		rubyabi		1.9.1
%endif

%define		baserelease	29

%define		fullrel		%{?betaver:0.}%{baserelease}%{?betaver:.%betaver}

Name:		fantasdic
Version:	%{mainver}
Release:	%{fullrel}%{?dist}
Summary:	Dictionary application using Ruby

# SPDX confirmed
License:	GPL-2.0-or-later
URL:		http://www.gnome.org/projects/fantasdic/
Source0:	http://www.mblondel.org/files/fantasdic/%{name}-%{mainver}%{?betaver:-%betaver}.tar.gz
# ruby-gnome2-Bugs-2865895
# Patch0:	fantasdic-1.0-beta7-workaround-rg2-bg2865895.patch
# Various ruby19 fixes
# Need utf-8 encoding direction
Patch10:	fantasdic-1.0-beta7-ruby19-utf8.patch
# Syntax error fix
Patch11:	fantasdic-1.0-beta7-ruby19-syntax.patch
# Path fix for modules in ruby 19
Patch12:	fantasdic-1.0-beta7-ruby19-pathfix.patch
# Guard sigtrap when calling Gdk::flush (bug 844754, bug 799804)
Patch13:	fantasdic-1.0-beta7-guard-sigtrap.patch
# ::Config was finally renamed to RbConfig in Ruby 2.2.
Patch14:	fantasdic-1.0-beta7-ruby22-rbconfig-fix.patch
# rbpango 3.1.6: use no-gi for now
# pango 1.44.x changed massively: use rbpango gi
Patch15:	fantasdic-1.0-beta7-use-pango-gi.patch
# ruby psych 4.0.x needs YAML.unsafe_load
Patch16:	fantasdic-1.0-beta7-yaml-unsafe-load.patch
# Remove duplicate test names
Patch17:	fantasdic-1.0-beta7-testsuite-remove-dupes.patch
# # Ruby 3.2 completely removes File.exists?
Patch18:	fantasdic-1.0-beta7-ruby32-file_exist.patch
# Misc fixes for ruby 3.2
Patch19:	fantasdic-1.0-beta7-ruby32-misc-fix.patch
# Dict server configuration update
Patch20:	fantasdic-1.0-beta7-dict-server-update.patch

BuildArch:	noarch

Requires:	ruby(release)
BuildRequires:	ruby(release)

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:  ruby-devel

%BothRequires	ruby
%BothRequires	rubygem(gettext)

%BothRequires	ruby(libglade2)
%BothRequires	ruby(gconf2)
%BothRequires	ruby(gnome2)
%BothRequires	ruby(gtk2)
# F-31+: use rbpango-gi
%BothRequires	rubygem(pango)
BuildRequires:	rubygem(test-unit)
BuildRequires:	%{_bindir}/xvfb-run

%description
Fantasdic is a dictionary application. It allows to look up words in 
various dictionary sources. It is primarily targetting the GNOME 
desktop but it should work with other platforms, including Windows. 
Fantasdic is Free Software.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{mainver}%{?betaver:-%betaver}
#%%patch0 -p1
%patch -P10 -p1
%patch -P11 -p1
%patch -P12 -p1
%patch -P13 -p1
%patch -P14 -p1
ln -sf lib vendor_ruby
%patch -P15 -p4
unlink vendor_ruby
# ruby 3.1 (psych 4.x)
%patch -P16 -p1
%patch -P17 -p1
%patch -P18 -p1
%patch -P19 -p1
%patch -P20 -p1

%{__chmod} 0644 tools/*.rb
%{__sed} -i.path -e 's|%{_bindir}/||' fantasdic.desktop

# Fix up documents directory
%{__sed} \
	-i.dir -e '/html/s|%{name}|%{name}-%{mainver}|' \
	lib/fantasdic/ui/browser.rb

%build
export LANG=C.UTF-8

ruby setup.rb config \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--siterubyver=%{ruby_vendorlibdir} \
	--datadir=%{_datadir} \
	--without-scrollkeeper
ruby setup.rb setup

%install
ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

desktop-file-install \
	--add-category 'GTK' \
	--add-category 'Dictionary' \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	%{name}.desktop

# hicolor png icon symlinks
target="../../../.."
for n in 16 22 24 32 48
	do
	%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${n}x${n}/apps
	%{__ln_s} -f \
		${target}/%{name}/icons/%{name}_${n}x${n}.png \
		$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${n}x${n}/apps/%{name}.png
done

# symlink check
pushd $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${n}x${n}/apps
pushd $target
if [ "x$(pwd)" != "x$RPM_BUILD_ROOT%{_datadir}" ] ; then
	echo "Possibly symlink broken"
	exit 1
fi
popd
popd

%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
%{__ln_s} -f ${target}/%{name}/icons/%{name}.svg \
	$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/

# Clean up documents
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/doc/

%{find_lang} %{name}

%check
STATUS=0

# Tweak configuration for local test (without fantasdic itself being installed)
sed -i.save lib/fantasdic/config.rb -e "s|'%{_prefix}|'%{buildroot}%{_prefix}|"

NET_STATUS=0
ping -w3 www.google.co.jp || NET_STATUS=1

if [ $NET_STATUS != 0 ] ; then
	# disable test requiring net connection
	mv test/test_dict_server.rb{,.save}
fi
# google test not working, skip
mv test/test_google_translate.rb{,.save}

# Test suite expects that /bin/true is found
export PATH=/bin:$PATH

export LANG=C.utf8
xvfb-run \
	ruby -Ilib:. -e "Dir.glob('test/**/test_*.rb'){|f| require f}" || \
	STATUS=1

find . -name \*.save | while read f ; do
	mv $f ${f%.save}
done

exit $STATUS

%files	-f %{name}.lang 
%defattr(-,root,root,-)
%doc	AUTHORS
%license	COPY*
%doc	ChangeLog
%doc	NEWS
%doc	README
%doc	THANKS
%doc	TODO

%doc	tools/
%doc	data/doc/fantasdic/html/

%{_bindir}/%{name}

%{_datadir}/%{name}/
%{_datadir}/gnome/help/%{name}/
%{_datadir}/omf/%{name}/

%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%{_mandir}/man1/%{name}.1*

%{ruby_vendorlibdir}/%{name}.rb
%{ruby_vendorlibdir}/%{name}/

%changelog
%autochangelog
