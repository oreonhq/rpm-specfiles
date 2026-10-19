%global source1_hash b793df8394d3305b7f9d855e6494fa27091bb9962af05dd8c1ba30aa1bb38bb8
%global source0_hash 195036135e28b0cb7aad555bfda4b53b3b2fa27064425369c8544597a93cc602
%global gem_name mocha
Name: rubygem-%{gem_name}
Version: 2.6.1
Release:        1%{?dist}
Summary:        Mocking and stubbing library
License: Ruby OR BSD-2-Clause OR MIT
URL: https://mocha.jamesmead.org
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/freerange/mocha/archive/refs/tags/v2.6.1.tar.gz
Patch0: rubygem-mocha-2.6.1-Support-single-quote-instead-of-backtick-for-Ruby-3.4.patch
Patch1: mocha-pr755-replace-CGI-with-URI.patch
BuildArch: noarch
%global __requires_exclude ruby2_keywords
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(introspection)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
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
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ln -s %{_builddir}/test .
for kind in unit acceptance; do
  ruby -e "Dir.glob('./test/$kind/**/*_test.rb').each {|t| require t}"
done
MOCHA_RUN_INTEGRATION_TESTS=minitest ruby -rminitest -e "Dir.glob('./test/integration/**/minitest_test.rb').each {|t| require t}"
MOCHA_RUN_INTEGRATION_TESTS=test-unit ruby -rtest/unit -e "Dir.glob('./test/integration/**/test_unit_test.rb').each {|t| require t}"
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-mocha-doc -f %{oreon_filedir}/rubygem-mocha-doc.list

%changelog

%autochangelog
