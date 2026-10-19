%global source1_hash 3a4524fffcfb9594100e35ce8bc0c3ef2a5e9d34e7f71ad40d97afb9400c2a4e
%global source0_hash 0c3700b10ab6d7c648c4cd554023d8c2b5b07e7f01205f7608f0c511cf686505
%global gem_name rspec-rails
%bcond_with bootstrap
Name: rubygem-%{gem_name}
Version: 8.0.1
Release:        1%{?dist}
Summary:        RSpec for Rails
License: MIT
URL: https://github.com/rspec/rspec-rails
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/rspec/rspec-rails/archive/refs/tags/v8.0.1.tar.gz
Patch0: rubygem-rspec-rails-8.0.1-Drop-driven-by-selenium.patch
%if %{without bootstrap}
%dnl BuildRequires: rubygem(cucumber)
%endif
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
# /oreon:deps
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
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

(
cd %{builddir}
%patch 0 -p1
)

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{without bootstrap}
%check

pushd .%{gem_instdir}
ln -s %{builddir}/features features
ln -s %{builddir}/spec spec
echo "gem 'rspec', :require => false" > Gemfile
sed -i '/uninitialized constant RSpec::Support/ s/::Support//' spec/sanity_check_spec.rb
sed -i 's/`git ls-files -z`/""/' spec/rspec/rails_spec.rb
rspec -rspec_helper -rbundler spec
%dnl cucumber
popd
%endif
%files -f %{oreon_filedir}/main.list
%files -n rubygem-rspec-rails-doc -f %{oreon_filedir}/rubygem-rspec-rails-doc.list

%changelog

%autochangelog
