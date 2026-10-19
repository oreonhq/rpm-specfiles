%global source0_hash 5bdd4e73db4f8f6ac3967cfe63413837d125cbc1f2178d95d681f4b2df072878
%global	gem_name	flexmock
Summary:        Mock object library for ruby
Name:		rubygem-%{gem_name}
Version:	3.0.2
Release:        1%{?dist}
License:	MIT
URL:		https://github.com/doudou/flexmock
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	%{gem_name}-%{version}-test-missing-files.tar.gz
Source2:	flexmock-create-missing-test-files.sh
Patch0:	flexmock-3.0.2-testsuite-ruby34-formatting.patch
Patch1:	flexmock-3.0.2-ruby34-string-literal-frozen.patch
Requires:	ruby(release)
Requires:	ruby(rubygems)
Provides:	rubygem(%{gem_name}) = %{version}-%{release}
BuildArch:	noarch
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
FlexMock is a simple, but flexible, mock object library for Ruby unit
testing.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
%description	doc
This package contains documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -a 1
mv ../%{gem_name}-%{version}.gemspec .

mv flexmock/test .

%patch -P0 -p1
%patch -P1 -p1

find . -name \*.rb | xargs sed -i -e '\@/usr/bin/env@d'
find . -name \*.gem -or -name \*.rb -or -name \*.rdoc | xargs chmod 0644

%build

gem build %{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.autotest .gitignore .togglerc .travis.yml .yardopts \
	.github \
	Gemfile \
	Rakefile \
	flexmock.blurb \
	flexmock.gemspec \
	install.rb \
	test/ \
	%{nil}
popd
rm -f %{buildroot}%{gem_cache}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

cp -a test .%{gem_instdir}
pushd .%{gem_instdir}
export RUBYOPT=-W:deprecated
export RUBYLIB=$(pwd)/lib:$(pwd):$(pwd)/test
ruby \
	-e 'Dir.glob("test/*_test.rb").each {|f| require f}'
rspec test/rspec_integration/ \
	--exclude-pattern 'test/rspec_integration/spy_example_spec.rb' \
	%{nil}
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-flexmock-doc -f %{oreon_filedir}/rubygem-flexmock-doc.list

%changelog

%autochangelog
