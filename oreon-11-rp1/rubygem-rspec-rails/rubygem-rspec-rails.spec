%global source0_hash d3e241e80c804da854cbf8adb75595ae0178906f0f435bee235753091dd5ebd9

# Generated from rspec-rails-2.6.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rspec-rails

# Circular dependency with rubygem-ammeter.
%bcond_with bootstrap

Name: rubygem-%{gem_name}
Version: 8.0.1
Release: 3%{?dist}
Summary: RSpec for Rails
License: MIT
URL: https://github.com/rspec/rspec-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/rspec/rspec-rails.git && cd rspec-rails
# git archive -v -o rspec-rails-8.0.1-tests.tar.gz v8.0.1 features/ spec/
Source1: %{gem_name}-%{version}-tests.tar.gz
# Fix Ruby on Rails 7.2+ compatibility. This mainly avoids additional
# dependency on chromedriver.
# https://github.com/rspec/rspec-rails/pull/2856
Patch0: rubygem-rspec-rails-8.0.1-Drop-driven-by-selenium.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
%if %{without bootstrap}
%dnl BuildRequires: rubygem(cucumber)
BuildRequires: rubygem(actionmailbox)
BuildRequires: rubygem(actionmailer)
BuildRequires: rubygem(actioncable)
BuildRequires: rubygem(activerecord)
BuildRequires: rubygem(ammeter)
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(capybara)
BuildRequires: rubygem(railties)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(sqlite3)
%endif
BuildArch: noarch

%description
rspec-rails integrates the Rails testing helpers into RSpec.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1

(
cd %{builddir}
%patch 0 -p1
)

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

%if %{without bootstrap}
%check
pushd .%{gem_instdir}
ln -s %{builddir}/features features
ln -s %{builddir}/spec spec

# Bundler is used to execute two tests, so give him Gemfile.
echo "gem 'rspec', :require => false" > Gemfile

# I have no idea why this is passing upstream, since when RSpec are not supposed
# to be loaded, then RSpec::Support can't exist.
sed -i '/uninitialized constant RSpec::Support/ s/::Support//' spec/sanity_check_spec.rb

# Avoid git dependency. This is not funcitonal test anyway, just style check.
sed -i 's/`git ls-files -z`/""/' spec/rspec/rails_spec.rb

rspec -rspec_helper -rbundler spec

# Needs to generate a rails test application or ship pregenerated one (see
# generate:app rake task). This would be quite fragile.
%dnl cucumber
popd
%endif

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Capybara.md
%doc %{gem_instdir}/Changelog.md
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
