%global source0_hash ada02c59aa7e9f56bd2522faedaed16421dd2f3ddb5fe28628c0be5abcbf3c74

%global		gem_name	gettext

%global		locale_ver		2.0.5
%global		repoid			67096

Name:		rubygem-%{gem_name}
Version:	3.5.2
Release:	1%{?dist}
Summary:	RubyGem of Localization Library and Tools for Ruby

# Ruby OR LGPL-3.0-or-later:	gemspec
# Ruby:	lib/gettext/mo.rb
# SPDX confirmed
License:	(Ruby OR LGPL-3.0-or-later) AND Ruby
URL:		http://www.yotabanana.com/hiki/ruby-gettext.html?ruby-gettext
Source0:	http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem

Requires:	ruby(release)
BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
# For %%check

BuildRequires:	rubygem(erubi)
BuildRequires:	rubygem(locale) >= %{locale_ver}
BuildRequires:	rubygem(prime)
BuildRequires:	rubygem(test-unit)
BuildRequires:	rubygem(test-unit-notify)
BuildRequires:	rubygem(test-unit-rr)
BuildRequires:	rubygem(text)
# test/tools/test_task.rb -> lib/gettext/tools/task.rb
BuildRequires:	rubygem(rake)
BuildRequires:	gettext

BuildRequires:	rubygem(racc)

Requires:	ruby(rubygems)
Provides:	rubygem(%{gem_name}) = %{version}-%{release}

Obsoletes:	ruby-gettext-package <= %{version}-%{release}
Provides:	ruby-gettext-package = %{version}-%{release}

BuildArch:	noarch

%description
Ruby-GetText-Package is a GNU GetText-like program for Ruby.
The catalog file(po-file) is same format with GNU GetText.
So you can use GNU GetText tools for maintaining.

This package provides gem for Ruby-Gettext-Package.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

#%%{__rm} -f .%{gem_instdir}/Rakefile
%{__rm} -f .%{gem_instdir}/%{gem_name}.gemspec
%{__rm} -rf .%{gem_instdir}/po/
%{__chmod} 0755 .%{gem_instdir}/bin/*
%{__chmod} 0644 .%{gem_dir}/cache/*.gem
find .%{gem_instdir}/ -name \*.po | xargs %{__chmod} 0644

# Cleanups for rpmlint
find .%{gem_instdir}/lib/ -name \*.rb | while read f
do
	%{__sed} -i -e '/^#!/d' $f
done

# fix timestamps
find . -type f -print0 | xargs -0 touch -r %{SOURCE0}

%install
%{__mkdir_p} %{buildroot}{%{gem_dir},%{_bindir}}

%{__cp} -a .%{_bindir}/* %{buildroot}/%{_bindir}/
%{__cp} -a .%{gem_dir}/* %{buildroot}%{gem_dir}/
find %{buildroot}%{gem_dir} -name \*.rb.patch\* -delete

# For --short-circult
%{__rm} -f *.lang

# modify find-lang.sh to deal with gettext .mo files under
# %%{gem_instdir}/locale
#%%{__sed} -e 's|/share/locale/|/data/locale/|' \
#	/usr/lib/rpm/find-lang.sh \
#	> find-lang-modified.sh
#
#sh find-lang-modified.sh %{buildroot} gettext gettext-gem.lang
%find_lang gettext
mv gettext.lang gettext-gem.lang

%{__cat} *-gem.lang >> %{name}-gem.lang

# list directories under %%{gem_instdir}/locale/
find %{buildroot}%{gem_instdir}/locale -type d | while read dir
do
	echo "%%dir ${dir#%{buildroot}}" >> %{name}-gem.lang
done

# clean up
rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	Rakefile \
	.yardopts \
	src/ \
	test/ \
	%{nil}
popd

%check
pushd .%{gem_instdir}
export LANG=C.UTF-8
export LANGUAGE=ja_JP.utf8
export RUBYLIB=$(pwd)/lib

# Umm...
pushd test/po
locales=$(ls -1d */ | sed -e 's|/||')
popd
catalogues=$(ls -1 test/po/ja/*.po | while read f ; do basename $f | sed -e 's|\.po||' ; done)
for l in $locales
do
	for d in $catalogues
	do
		if [ -f test/po/${l}/${d}.po ] ; then
			mkdir -p  test/locale/${l}/LC_MESSAGES/ || true
			bin/rmsgfmt -o test/locale/${l}/LC_MESSAGES/${d}.mo test/po/${l}/${d}.po
		fi
	done
done

pushd samples/po
locales=$(ls -1d */ | sed -e 's|/||')
popd
catalogues=$(ls -1 samples/po/ja/*.po | while read f ; do basename $f | sed -e 's|\.po||' ; done)
for l in $locales
do
	for d in $catalogues
	do
		if [ -f samples/po/${l}/${d}.po ] ; then
			mkdir -p  samples/locale/${l}/LC_MESSAGES/ || true
			bin/rmsgfmt -o samples/locale/${l}/LC_MESSAGES/${d}.mo samples/po/${l}/${d}.po
		fi
	done
done

pushd samples/cgi/po
locales=$(ls -1d */ | sed -e 's|/||')
popd
catalogues=$(ls -1 samples/cgi/po/ja/*.po | while read f ; do basename $f | sed -e 's|\.po||' ; done)
for l in $locales
do
	for d in $catalogues
	do
		if [ -f samples/cgi/po/${l}/${d}.po ] ; then
			mkdir -p  samples/cgi/locale/${l}/LC_MESSAGES/ || true
			bin/rmsgfmt -o samples/cgi/locale/${l}/LC_MESSAGES/${d}.mo samples/cgi/po/${l}/${d}.po
		fi
	done
done

ruby -Ilib:test test/run-test.rb

popd

%files	-f %{name}-gem.lang
%{_bindir}/rxgettext
%{_bindir}/rmsginit
%{_bindir}/rmsgcat
%{_bindir}/rmsgfmt
%{_bindir}/rmsgmerge

%dir %{gem_instdir}/
%doc %{gem_instdir}/[A-Z]*
%dir %{gem_instdir}/doc/
%dir	%{gem_instdir}/doc/text/
%license	%{gem_instdir}/doc/text/*txt
%doc	%{gem_instdir}/doc/text/news.md

%{gem_instdir}/bin/
%{gem_instdir}/lib/

%{gem_spec}

%files		doc
%{gem_docdir}/
%{gem_instdir}/samples/

%changelog
%autochangelog
