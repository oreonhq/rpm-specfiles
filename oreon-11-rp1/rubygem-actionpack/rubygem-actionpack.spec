%global source1_hash 0419bf47f7357e6d3da85ff4ad797a3609dcf36ff44be496162ffbc901ff4232
%global source0_hash d63c21cb109e0529d785ffdb657a092928890327c5c8ea2e46f63b6751be5ad3
%global gem_name actionpack
%bcond_with bootstrap
Name: rubygem-%{gem_name}
Epoch: 1
Version: 8.0.3
Release:        2%{?dist}
Summary:        Web-flow and rendering framework putting the VC in MVC (part of Rails)
License: MIT
URL: https://rubyonrails.org
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/rails/rails/archive/refs/tags/v8.0.3.tar.gz
%if %{without bootstrap}
ExclusiveArch: x86_64 aarch64 noarch
%endif
BuildArch: noarch
# oreon:deps
BuildRequires:  chromedriver
BuildRequires:  chromium
BuildRequires:  chromium-headless
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(actionview)
BuildRequires:  rubygem(activemodel)
BuildRequires:  rubygem(activesupport)
BuildRequires:  rubygem(capybara)
BuildRequires:  rubygem(launchy)
BuildRequires:  rubygem(msgpack)
BuildRequires:  rubygem(rack)
BuildRequires:  rubygem(rack-cache)
BuildRequires:  rubygem(rack-test)
BuildRequires:  rubygem(railties)
BuildRequires:  rubygem(selenium-webdriver)
BuildRequires:  rubygem(useragent)
BuildRequires:  rubygem(zeitwerk)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Eases web-request routing, handling, and response as a half-way front,
half-way page controller. Implemented with specific emphasis on enabling easy
unit/integration testing that doesn't require a browser.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}%{?prerelease} -b1
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

%build

gem build ../%{gem_name}-%{version}%{?prerelease}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{without bootstrap}
%check

( cd .%{gem_instdir}
cp -a %{builddir}/test .
mkdir ../tools
touch ../tools/test_common.rb
touch ../tools/strict_warnings.rb
sed -i '/driven_by/ s/$/, :options => {browser: :remote}/' \
  test/abstract_unit.rb
mkdir bin
touch bin/test
chmod a+x bin/test
sed -r -i '/driver = ActionDispatch::SystemTesting::Driver.new\(:selenium, .*using: :(headless_)?firefox.*\)/i \
    skip "gecko driver is not available on Fedora"' \
  test/dispatch/system_testing/driver_test.rb
sed -r -i '/capabilities.slice\(\*expected_capabilities\.keys\)$/ s/$/.tap {|h| h["goog:chromeOptions"].delete("binary")}/' \
  test/dispatch/system_testing/driver_test.rb
find test -type f -name '*_test.rb' -print0 | \
  sort -z | \
  xargs -0 -n1 -i sh -c "
    echo '* Test file: {}'
    ruby -Ilib:test -- '{}' || exit 255
  "
)
%endif
%files -f %{oreon_filedir}/main.list
%files -n rubygem-actionpack-doc -f %{oreon_filedir}/rubygem-actionpack-doc.list

%changelog

%autochangelog
