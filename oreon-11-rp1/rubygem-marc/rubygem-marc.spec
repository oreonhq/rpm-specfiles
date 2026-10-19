%global source0_hash 89f31a66c21f5a11e8fcf65fe06d207e121fb45ac6b23abef403f9ce912c7d10
%global		gem_name	marc
Name:		rubygem-%{gem_name}
Version:	1.4.0
Release:        1%{?dist}
Summary:        Ruby library for MARC catalog
License:	MIT
URL:		https://github.com/ruby-marc/ruby-marc
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires:	ruby(release)
BuildArch:	noarch
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygem(ensure_valid_encoding)
BuildRequires:  rubygem(nokogiri)
BuildRequires:  rubygem(rexml)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(scrub_rb)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygem(xml-simple)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
marc is a ruby library for reading and writing MAchine Readable Cataloging
(MARC). More information about MARC can be found at <http://www.loc.gov/marc>.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
%description	doc
This package contains documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

find ./{lib,test} -name \*.rb -print0 | xargs -0 chmod 0644
find ./{lib,test} -name \*.rb -print0 | \
	xargs -0 grep -l --null '#![ \t]*%{_bindir}' | \
	xargs -0 chmod 0755

# warning gem is not actually needed
sed -i \
	test/tc_xml.rb \
	test/tc_parsers.rb \
		-e 's|^\(require.*warning.*$\)|#\1|' \
		-e 's|\(Warning.ignore\)|#\1|' \
		%{nil}

%build

gem build %{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
mkdir -p %{buildroot}%{_bindir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/
cp -a .%{_bindir}/* %{buildroot}%{_bindir}/
pushd %{buildroot}%{_bindir}/
for f in *
do
	mv $f rb_$f
done
popd
rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -fr \
	.github/ \
	.gitignore \
	.standard.yml \
	Gemfile \
	Rakefile \
	marc.gemspec \
	test/ \
	spec/ \
	%{nil}
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
LANG=C.UTF-8
ruby -w -Ilib:. -e 'gem "test-unit"; require "marc" ; Dir.glob("test/**/tc_*.rb"){|f| require f }'
sed -i spec/reader_char_encodings_spec.rb \
	-e '\@replaces bad source bytes when configured@s|do|do ; skip|'
rspec spec/
%files -f %{oreon_filedir}/main.list
%files -n rubygem-marc-doc -f %{oreon_filedir}/rubygem-marc-doc.list

%changelog

%autochangelog
