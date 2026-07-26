%global source0_hash 8e82faf7c8125f7c9ce99d8dfbede77369e84fdddd950c4beac8fa4e32b72c47

%global gem_name capybara

Name: rubygem-%{gem_name}
Version: 3.40.0
Release: 5%{?dist}
Summary: Capybara aims to simplify the process of integration testing Rack applications
License: MIT
URL: https://github.com/teamcapybara/capybara
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/teamcapybara/capybara.git --no-checkout && cd capybara
# git archive -v -o capybara-3.40.0-tests.tar.gz 3.40.0 features/
Source1: %{gem_name}-%{version}-tests.tar.gz
# Fix compatibility with Rack::Protection 4.1.0+
# https://github.com/teamcapybara/capybara/pull/2812
Patch0: rubygem-capybara-3.40.0-Disable-Rack-Protection-HostAuthorization-.patch
# Fix compatibility with minitest 6
Patch1: rubygem-capybara-3.40.0-minitest6.patch

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(addressable)
BuildRequires: rubygem(selenium-webdriver)
BuildRequires: rubygem(sinatra)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(launchy)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(puma)
BuildRequires: rubygem(nokogiri)
BuildRequires: rubygem(xpath)
BuildRequires: rubygem(rack-test)
BuildRequires: rubygem(mini_mime)
BuildRequires: rubygem(cucumber)
BuildRequires: rubygem(regexp_parser)
BuildRequires: rubygem(matrix)
BuildArch: noarch

%description
Capybara is an integration testing tool for rack based web applications. It
simulates how a user would interact with a website.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1

%patch 0 -p1
%patch 1 -p1

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
( cd .%{gem_instdir}
# Move the tests into place
ln -s %{_builddir}/features features

# Do not collect statistics
sed -i '/^require..selenium_statistics.$/ s/^/#/' spec/spec_helper.rb
sed -i '/SeleniumStatistics/ s/^/#/g' ./spec/spec_helper.rb

rspec spec

# Bundler is not really needed
sed -i "/^require 'bundler/ s/^/#/g" \
  features/support/env.rb

cucumber
)

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/License.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/spec

%changelog
%autochangelog
