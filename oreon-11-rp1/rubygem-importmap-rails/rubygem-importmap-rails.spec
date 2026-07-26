%global source0_hash 1d2df835ac0e2429a0495e3776af928ef3b8f37793763d0626812ff78665ef1a

# Generated from importmap-rails-1.0.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name importmap-rails

Name: rubygem-%{gem_name}
Version: 1.0.3
Release: 12%{?dist}
Summary: Manage modern JavaScript in Rails without transpiling or bundling
License: MIT
URL: https://github.com/rails/importmap-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# To get the test suite:
# git clone https://github.com/rails/importmap-rails.git --no-checkout
# git -C importmap-rails archive -v -o importmap-rails-1.0.3-tests.txz v1.0.3 test/
Source1: %{gem_name}-%{version}%{?prerelease}-tests.txz

BuildRequires: ruby
BuildRequires: ruby(release)
# Used for sample app
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(minitest-mock)
BuildRequires: rubygem(mutex_m)
BuildRequires: rubygem(rails)
BuildRequires: rubygem(sqlite3)
BuildRequires: rubygems-devel
BuildArch: noarch
# Bundles ES Module Shims
# app/assets/javascripts/es-module-shims.js
Provides: bundled(es-module-shims) = 1.4.1

%description
Use ESM with importmap to manage modern JavaScript in Rails without
transpiling or bundling.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/test

echo 'gem "minitest-mock"' >> Gemfile
echo 'gem "mutex_m"' >> Gemfile
echo 'gem "rails"' >> Gemfile
echo 'gem "sqlite3"' >> Gemfile

# Test requires network access
mv test/packager_integration_test.rb{,.disable}

export BUNDLE_GEMFILE="$(pwd)/Gemfile"

# Tests require building rails app (currently fails)
echo > test/dummy/config/initializers/assets.rb
mv test/importmap_test.rb{,.disable}

ruby -Ilib:test -rbundler -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/app
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
%autochangelog
