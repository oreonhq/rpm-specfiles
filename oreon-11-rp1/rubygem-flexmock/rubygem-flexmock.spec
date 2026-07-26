%global source0_hash aa9c44654ce8edb860191ef8b609a356e3915990040c05e67a36281d6a8d9ae5

%global	gem_name	flexmock

Summary:	Mock object library for ruby
Name:		rubygem-%{gem_name}
Version:	3.0.2
Release:	2%{?dist}
License:	MIT
URL:		https://github.com/doudou/flexmock
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	%{gem_name}-%{version}-test-missing-files.tar.gz
# Source1 is created fron Source2
Source2:	flexmock-create-missing-test-files.sh
# make testsuite compatible for ruby34 formatting change
Patch0:	flexmock-3.0.2-testsuite-ruby34-formatting.patch
# Remove warnings for string literal being frozen in the future
Patch1:	flexmock-3.0.2-ruby34-string-literal-frozen.patch

Requires:	ruby(release)
BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	rubygem(minitest) >= 5
BuildRequires:	rubygem(rspec) >= 3
Requires:	ruby(rubygems)
Provides:	rubygem(%{gem_name}) = %{version}-%{release}
BuildArch:	noarch

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

%check
cp -a test .%{gem_instdir}
pushd .%{gem_instdir}

export RUBYOPT=-W:deprecated
export RUBYLIB=$(pwd)/lib:$(pwd):$(pwd)/test
ruby \
	-e 'Dir.glob("test/*_test.rb").each {|f| require f}'

# Note: exclude failing tests for now
rspec test/rspec_integration/ \
	--exclude-pattern 'test/rspec_integration/spy_example_spec.rb' \
	%{nil}
popd

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/LICENSE.txt
%doc	%{gem_instdir}/[A-CR-Z]*

%{gem_libdir}
%{gem_instdir}/rakelib/
%{gem_spec}

%files	doc
%{gem_instdir}/todo.txt
%{gem_instdir}/doc/
%{gem_docdir}/

%changelog
%autochangelog
