%global source0_hash 6c3c64450a5de34314867cfbb505a5837729a2639fa88885cde634cb76750a33

%global gem_name puppet-resource_api

Name: rubygem-%{gem_name}
Version: 2.0.1
Release: 1%{?dist}
Summary: This library provides a simple way to write new native resources for puppet
License: Apache-2.0
URL: https://github.com/puppetlabs/puppet-resource_api
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
Requires: puppet
BuildArch: noarch

%description
This library provides a simple way to write new native resources for puppet.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

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
rm -rf %{buildroot}%{gem_instdir}/{.gitignore,.rubocop.yml,.travis.yml,appveyor.yml,codecov.yml}

# %%check can't run since it requires puppet, but puppet requires this package

%files
%license %{gem_instdir}/LICENSE
%license %{gem_instdir}/NOTICE
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/docs
%{gem_instdir}/puppet-resource_api.gemspec

%changelog
%autochangelog
