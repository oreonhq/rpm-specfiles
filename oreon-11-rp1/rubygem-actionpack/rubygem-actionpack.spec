%global source0_hash d63c21cb109e0529d785ffdb657a092928890327c5c8ea2e46f63b6751be5ad3

# Generated from actionpack-1.13.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name actionpack

# Circular dependency with rubygem-{actverecord,railties}.
%bcond_with bootstrap

Name: rubygem-%{gem_name}
Epoch: 1
Version: 8.0.3
Release: 2%{?dist}
Summary: Web-flow and rendering framework putting the VC in MVC (part of Rails)
License: MIT
URL: https://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}%{?prerelease}.gem
# git clone http://github.com/rails/rails.git && cd rails/actionpack
# git archive -v -o actionpack-8.0.3-tests.tar.gz v8.0.3 test/
Source1: %{gem_name}-%{version}%{?prerelease}-tests.tar.gz

# Let's keep Requires and BuildRequires sorted alphabeticaly
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 3.2.0
%if %{without bootstrap}
BuildRequires: rubygem(activemodel) = %{version}
BuildRequires: rubygem(activesupport) = %{version}
BuildRequires: rubygem(actionview) = %{version}
BuildRequires: rubygem(launchy)
BuildRequires: rubygem(msgpack)
BuildRequires: rubygem(railties) = %{version}
BuildRequires: rubygem(rack)
BuildRequires: rubygem(rack-cache)
BuildRequires: rubygem(rack-test)
BuildRequires: rubygem(capybara) >= 3.26
BuildRequires: rubygem(selenium-webdriver)
BuildRequires: rubygem(useragent)
BuildRequires: rubygem(zeitwerk)
BuildRequires: chromedriver chromium chromium-headless
# Chromium availability is limited:
# https://src.fedoraproject.org/rpms/chromium/blob/0d9761748509bb12051ab149d28c1052cd834f87/f/chromium.spec#_800
# and chrome-headless even more:
# https://src.fedoraproject.org/rpms/chromium/blob/0d9761748509bb12051ab149d28c1052cd834f87/f/chromium.spec#_46-48
ExclusiveArch: x86_64 aarch64 noarch
%endif
BuildArch: noarch

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

%build
gem build ../%{gem_name}-%{version}%{?prerelease}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%if %{without bootstrap}
%check
( cd .%{gem_instdir}
cp -a %{builddir}/test .

mkdir ../tools
# Fake test_common.rb. It does not provide any functionality besides
# `force_skip` alias.
touch ../tools/test_common.rb
# Netiher strict_warnings.rb appears to be useful.
touch ../tools/strict_warnings.rb

# Use `:remote` option to surpres preload of Selenium drivers.
sed -i '/driven_by/ s/$/, :options => {browser: :remote}/' \
  test/abstract_unit.rb

# Required on various palces such as:
# https://github.com/rails/rails/blob/3235827585d87661942c91bc81f64f56d710f0b2/actionpack/test/dispatch/system_testing/driver_test.rb#L34
# https://github.com/rails/rails/blob/3235827585d87661942c91bc81f64f56d710f0b2/actionpack/test/dispatch/system_testing/driver_test.rb#L53
mkdir bin
touch bin/test
chmod a+x bin/test

sed -r -i '/driver = ActionDispatch::SystemTesting::Driver.new\(:selenium, .*using: :(headless_)?firefox.*\)/i \
    skip "gecko driver is not available on Fedora"' \
  test/dispatch/system_testing/driver_test.rb

# `"binary" => "/usr/bin/chromium-browser"` entry randomly appears in result.
# It is not clear how this instability happens, but it might be caused by the
# `:remote` option used above. Or it might be due to `selenium-manager`.
# https://github.com/rails/rails/issues/54740
sed -r -i '/capabilities.slice\(\*expected_capabilities\.keys\)$/ s/$/.tap {|h| h["goog:chromeOptions"].delete("binary")}/' \
  test/dispatch/system_testing/driver_test.rb

# Tests need to run in isolation
find test -type f -name '*_test.rb' -print0 | \
  sort -z | \
  xargs -0 -n1 -i sh -c "
    echo '* Test file: {}'
    ruby -Ilib:test -- '{}' || exit 255
  "

)
%endif

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.rdoc

%changelog
%autochangelog
