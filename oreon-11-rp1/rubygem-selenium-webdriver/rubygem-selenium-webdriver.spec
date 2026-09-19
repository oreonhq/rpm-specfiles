%global source0_hash 132f5b71b53def9f468f10cc61a2e2ef487112cd086fe747c615c7cbcd70e400

%global gem_name selenium-webdriver

%bcond_without spec_integration

Name: rubygem-%{gem_name}
Version: 4.34.0
Release: 3%{?dist}
Summary: Selenium is a browser automation tool for automated testing of webapps and more
License: Apache-2.0
URL: https://selenium.dev
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/SeleniumHQ/selenium && cd selenium
# git archive -v -o selenium-webdriver-4.34.0-spec.tar.gz selenium-4.34.0 rb/spec
Source1: %{gem_name}-%{version}-spec.tar.gz
# Needed for integration `spec/integration`
# git archive -v -o selenium-webdriver-4.34.0-web.tar.gz selenium-4.34.0 common/src/web
Source2: %{gem_name}-%{version}-web.tar.gz
# Make the test suite compatible with Rack 3+.
# https://github.com/SeleniumHQ/selenium/pull/16158
Patch0: rubygem-selenium-webdriver-4.34.0-Use-Rack-Files-for-Rack-3-compatibility.patch
# Enable compatibility with rubyzip v3.
# https://github.com/SeleniumHQ/selenium/pull/16108/commits/b91463c4eb2059da2cbdced3e65f1a7aa2708829
Patch1: rubygem-selenium-webdriver-4.35.0-rb-Allow-to-use-rubyzip-v3.patch

# There is no other driver in Fedora, therefore suggest what we have. This also
# reflescts the `selenium-manager` stub above.
Recommends: chromedriver
Recommends: chromium chromium-headless

Requires: %{_bindir}/selenium-manager
BuildRequires: %{_bindir}/selenium-manager

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(base64)
BuildRequires: rubygem(curb)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(rubyzip)
BuildRequires: rubygem(webmock)
BuildRequires: rubygem(websocket)
%if %{with spec_integration}
BuildRequires: rubygem(rack)
BuildRequires: rubygem(rackup)
BuildRequires: rubygem(webrick)
BuildRequires: chromedriver
BuildRequires: chromium chromium-headless
# Chromium is not available for i686 / s390x
# https://src.fedoraproject.org/rpms/chromium/blob/fcd074b9c31411f795ab402fe88e4513a68c843e/f/chromium.spec#_803
# and on ppc64le
# https://src.fedoraproject.org/rpms/chromium/blob/fcd074b9c31411f795ab402fe88e4513a68c843e/f/chromium.spec#_43-45
ExclusiveArch: x86_64 aarch64
%endif
BuildArch: noarch

%description
Selenium implements the W3C WebDriver protocol to automate popular browsers.
It aims to mimic the behaviour of a real user as it interacts with the
application's HTML. It's primarily intended for web application testing,
but any web-based task can automated.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1 -b2

(
cd %{builddir}
%patch 0 -p1
)

%patch 1 -p2
%gemspec_remove_dep -g rubyzip '< 3.0'

# Drop the original selenium-manager binaries and replace them by symlink to
# selenium-manager binary from the package of the same name.
%gemspec_remove_file Dir.glob('bin/{windows,macos,linux}/selenium-manager{,.exe}')
rm -rf bin

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Create folder for binaries and create symlink to the selenium-manager from repos
mkdir -p %{buildroot}%{gem_instdir}/bin/linux/
ln -sf %{_bindir}/selenium-manager %{buildroot}%{gem_instdir}/bin/linux/

%check
( cd .%{gem_instdir}
cp -a %{builddir}/rb/spec .
cp -a %{builddir}/common ..

mkdir -p ./bin/linux/
ln -sf %{_bindir}/selenium-manager ./bin/linux/

# `DevTools` are part of separate `selenium-devtools` gem.
mv spec/unit/selenium/devtools_spec.rb{,.disable}
mv spec/unit/selenium/devtools/cdp_client_generator_spec.rb{,.disable}
mv spec/integration/selenium/webdriver/devtools_spec.rb{,.disable}

# Require Firefox extensions included in thirdparty directory, available on GH
# not included in gem
sed -i spec/unit/selenium/webdriver/firefox/profile_spec.rb \
    -e '/can install extension/a\          skip' \
    -e '/can install web extension/a\          skip'

# There seems to be wrong stub and when `bin/linux/selenium-manager` exists,
# the test fails.
# https://github.com/SeleniumHQ/selenium/issues/14925
sed -i "/it 'errors if cannot find' do/a\          skip" \
  spec/unit/selenium/webdriver/common/selenium_manager_spec.rb

rspec spec/unit

%if %{with spec_integration}
# This query is not supported by the `selenium` wrapper. But we won't have beta
# version of Chrome anyway.
sed -i -r '/GlobalTestEnv\.beta_chrome_version/ s/exclude: \{.*\},//' \
  spec/integration/selenium/webdriver/network_spec.rb

# Ignore `spec/integration/selenium/server_spec.rb`, which downloads some
# content from internet.
mv spec/integration/selenium/server_spec.rb{,.disable}

# Test passes when it is expected to fail. Maybe Chromium supports this action
# now?
sed -i -r \
  -e "/it 'can minimize the window'/ s/(^\s*)it/\1skip/" \
  spec/integration/selenium/webdriver/window_spec.rb

# This test fails and should likely be guarded by the `headless` flag.
sed -i -r \
  -e "/it 'can maximize the current window'/ s/(^\s*)it/\1skip/" \
  spec/integration/selenium/webdriver/window_spec.rb

HEADLESS=true SE_CHROMEDRIVER=chromedriver rspec spec/integration
%endif
)

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGES
%doc %{gem_instdir}/NOTICE
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/selenium-webdriver.gemspec

%changelog
%autochangelog
