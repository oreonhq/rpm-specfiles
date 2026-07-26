%global source0_hash 924f43113a64fecb53bec4a8aef797d2e33b16b36fb985138129fc182213b2a1

%global gem_name mocha

Name: rubygem-%{gem_name}
Version: 2.6.1
Release: 6%{?dist}
Summary: Mocking and stubbing library
License: Ruby OR BSD-2-Clause OR MIT
URL: https://mocha.jamesmead.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/freerange/mocha.git && cd mocha
# git archive -v -o mocha-2.6.1-test.tar.gz v2.6.1 test/
Source1: %{gem_name}-%{version}-test.tar.gz
# Use single quote instead of backtick for Ruby 3.4 compatibility
# https://github.com/freerange/mocha/pull/688
Patch0: rubygem-mocha-2.6.1-Support-single-quote-instead-of-backtick-for-Ruby-3.4.patch
# Use URI instead of CGI for ruby3_5
# https://github.com/freerange/mocha/pull/755
Patch1: mocha-pr755-replace-CGI-with-URI.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(introspection)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(test-unit)
BuildArch: noarch

%global __requires_exclude ruby2_keywords

%description
Mocking and stubbing library with JMock/SchMock syntax, which allows mocking
and stubbing of methods on real (non-mock) classes.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1

%patch 1 -p1
pushd %{builddir}
%patch 0 -p1
popd

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/test .

# Each part of test suite must be run separately, otherwise the test suite fails.
# https://github.com/freerange/mocha/issues/121
for kind in unit acceptance; do
  ruby -e "Dir.glob('./test/$kind/**/*_test.rb').each {|t| require t}"
done

MOCHA_RUN_INTEGRATION_TESTS=minitest ruby -rminitest -e "Dir.glob('./test/integration/**/minitest_test.rb').each {|t| require t}"
MOCHA_RUN_INTEGRATION_TESTS=test-unit ruby -rtest/unit -e "Dir.glob('./test/integration/**/test_unit_test.rb').each {|t| require t}"
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/COPYING.md
%license %{gem_instdir}/MIT-LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/RELEASE.md
%{gem_instdir}/Rakefile
%{gem_instdir}/gemfiles/
%{gem_instdir}/mocha.gemspec

%changelog
%autochangelog
