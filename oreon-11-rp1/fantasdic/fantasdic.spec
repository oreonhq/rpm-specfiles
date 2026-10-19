%global source0_hash f337663d3bd4a875f84b08146a58ff3b600f219e2e4647de17bc8c6ec762183c
%define	BothRequires() \
Requires:	%1 \
%{nil}
%define		mainver		1.0
%define		betaver		beta7
%define		baserelease	29
%define		fullrel		%{?betaver:0.}%{baserelease}%{?betaver:.%betaver}
Name:		fantasdic
Version:	%{mainver}
Release:        1%{?dist}
Summary:        Dictionary application using Ruby
License:	GPL-2.0-or-later
URL:		http://www.gnome.org/projects/fantasdic/
Source0:        http://www.mblondel.org/files/%{name}/%{name}-%{version}-%{betaver}.tar.gz
Patch10:	fantasdic-1.0-beta7-ruby19-utf8.patch
Patch11:	fantasdic-1.0-beta7-ruby19-syntax.patch
Patch12:	fantasdic-1.0-beta7-ruby19-pathfix.patch
Patch13:	fantasdic-1.0-beta7-guard-sigtrap.patch
Patch14:	fantasdic-1.0-beta7-ruby22-rbconfig-fix.patch
Patch15:	fantasdic-1.0-beta7-use-pango-gi.patch
Patch16:	fantasdic-1.0-beta7-yaml-unsafe-load.patch
Patch17:	fantasdic-1.0-beta7-testsuite-remove-dupes.patch
Patch18:	fantasdic-1.0-beta7-ruby32-file_exist.patch
Patch19:	fantasdic-1.0-beta7-ruby32-misc-fix.patch
Patch20:	fantasdic-1.0-beta7-dict-server-update.patch
BuildArch:	noarch
Requires:	ruby(release)
%BothRequires	ruby
%BothRequires	rubygem(gettext)
%BothRequires	ruby(libglade2)
%BothRequires	ruby(gconf2)
%BothRequires	ruby(gnome2)
%BothRequires	ruby(gtk2)
%BothRequires	rubygem(pango)
# oreon:deps
BuildRequires:  /usr/bin/xvfb-run
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  ruby
BuildRequires:  ruby(gconf2)
BuildRequires:  ruby(gnome2)
BuildRequires:  ruby(gtk2)
BuildRequires:  ruby(libglade2)
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(gettext)
BuildRequires:  rubygem(pango)
BuildRequires:  rubygem(test-unit)
# /oreon:deps
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
target="../../../.."
for n in 16 22 24 32 48
	do
	%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${n}x${n}/apps
	%{__ln_s} -f \
		${target}/%{name}/icons/%{name}_${n}x${n}.png \
		$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${n}x${n}/apps/%{name}.png
done
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
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/doc/
%{find_lang} %{name}
%oreon_autofiles main

%check

STATUS=0
sed -i.save lib/fantasdic/config.rb -e "s|'%{_prefix}|'%{buildroot}%{_prefix}|"
NET_STATUS=0
ping -w3 www.google.co.jp || NET_STATUS=1
if [ $NET_STATUS != 0 ] ; then
	mv test/test_dict_server.rb{,.save}
fi
mv test/test_google_translate.rb{,.save}
export PATH=/bin:$PATH
export LANG=C.utf8
xvfb-run \
	ruby -Ilib:. -e "Dir.glob('test/**/test_*.rb'){|f| require f}" || \
	STATUS=1
find . -name \*.save | while read f ; do
	mv $f ${f%.save}
done
exit $STATUS
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
