%global source0_hash ec7bb718cbe66fe2b247d8ca5e6ba26caed0976d76579d7cb2fadd8dae8b271e
%global gem_name selenium-webdriver
%bcond_without spec_integration
Name: rubygem-%{gem_name}
Version: 4.34.0
Release:        1%{?dist}
Summary:        Selenium is a browser automation tool for automated testing of webapps and more
License: Apache-2.0
URL: https://selenium.dev
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: %{gem_name}-%{version}-spec.tar.gz
Source2: %{gem_name}-%{version}-web.tar.gz
Patch0: rubygem-selenium-webdriver-4.34.0-Use-Rack-Files-for-Rack-3-compatibility.patch
Patch1: rubygem-selenium-webdriver-4.35.0-rb-Allow-to-use-rubyzip-v3.patch
Recommends: chromedriver
Recommends: chromium chromium-headless
Requires: %{_bindir}/selenium-manager
%if %{with spec_integration}
ExclusiveArch: x86_64 aarch64
%endif
BuildArch: noarch
# oreon:deps
BuildRequires:  /usr/bin/selenium-manager
BuildRequires:  chromedriver
BuildRequires:  chromium
BuildRequires:  chromium-headless
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(base64)
BuildRequires:  rubygem(curb)
BuildRequires:  rubygem(rack)
BuildRequires:  rubygem(rackup)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(rubyzip)
BuildRequires:  rubygem(webmock)
BuildRequires:  rubygem(webrick)
BuildRequires:  rubygem(websocket)
BuildRequires:  rubygems-devel
# /oreon:deps
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
mkdir -p %{buildroot}%{gem_instdir}/bin/linux/
ln -sf %{_bindir}/selenium-manager %{buildroot}%{gem_instdir}/bin/linux/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

( cd .%{gem_instdir}
cp -a %{builddir}/rb/spec .
cp -a %{builddir}/common ..
mkdir -p ./bin/linux/
ln -sf %{_bindir}/selenium-manager ./bin/linux/
mv spec/unit/selenium/devtools_spec.rb{,.disable}
mv spec/unit/selenium/devtools/cdp_client_generator_spec.rb{,.disable}
mv spec/integration/selenium/webdriver/devtools_spec.rb{,.disable}
sed -i spec/unit/selenium/webdriver/firefox/profile_spec.rb \
    -e '/can install extension/a\          skip' \
    -e '/can install web extension/a\          skip'
sed -i "/it 'errors if cannot find' do/a\          skip" \
  spec/unit/selenium/webdriver/common/selenium_manager_spec.rb
rspec spec/unit
%if %{with spec_integration}
sed -i -r '/GlobalTestEnv\.beta_chrome_version/ s/exclude: \{.*\},//' \
  spec/integration/selenium/webdriver/network_spec.rb
mv spec/integration/selenium/server_spec.rb{,.disable}
sed -i -r \
  -e "/it 'can minimize the window'/ s/(^\s*)it/\1skip/" \
  spec/integration/selenium/webdriver/window_spec.rb
sed -i -r \
  -e "/it 'can maximize the current window'/ s/(^\s*)it/\1skip/" \
  spec/integration/selenium/webdriver/window_spec.rb
HEADLESS=true SE_CHROMEDRIVER=chromedriver rspec spec/integration
%endif
)
%files -f %{oreon_filedir}/main.list
%files -n rubygem-selenium-webdriver-doc -f %{oreon_filedir}/rubygem-selenium-webdriver-doc.list

%changelog

%autochangelog
