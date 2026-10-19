%global source1_hash 51ab53c21a89a97570d8d2633732eb6937c458bb49bbedc379c57515c47bbba0
%global source0_hash 1d2df835ac0e2429a0495e3776af928ef3b8f37793763d0626812ff78665ef1a
%global gem_name importmap-rails
Name: rubygem-%{gem_name}
Version: 1.0.3
Release:        12%{?dist}
Summary:        Manage modern JavaScript in Rails without transpiling or bundling
License: MIT
URL: https://github.com/rails/importmap-rails
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/rails/importmap-rails/archive/refs/tags/v1.0.3.tar.gz
BuildArch: noarch
Provides: bundled(es-module-shims) = 1.4.1
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(bundler)
BuildRequires:  rubygem(minitest-mock)
BuildRequires:  rubygem(mutex_m)
BuildRequires:  rubygem(rails)
BuildRequires:  rubygem(sqlite3)
BuildRequires:  rubygems-devel
# /oreon:deps
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
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

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
ln -s %{_builddir}/test
echo 'gem "minitest-mock"' >> Gemfile
echo 'gem "mutex_m"' >> Gemfile
echo 'gem "rails"' >> Gemfile
echo 'gem "sqlite3"' >> Gemfile
mv test/packager_integration_test.rb{,.disable}
export BUNDLE_GEMFILE="$(pwd)/Gemfile"
echo > test/dummy/config/initializers/assets.rb
mv test/importmap_test.rb{,.disable}
ruby -Ilib:test -rbundler -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-importmap-rails-doc -f %{oreon_filedir}/rubygem-importmap-rails-doc.list

%changelog

%autochangelog
