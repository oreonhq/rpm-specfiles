%global source0_hash 9b1b1c09bff2fe1c4d61e3d17b04f2aaf5abb879a48272c85f4654d8a3fddd8c
%global gem_name puppet-resource_api
Name: rubygem-%{gem_name}
Version: 1.8.18
Release:        1%{?dist}
Summary:        This library provides a simple way to write new native resources for puppet
License: Apache-2.0
URL: https://github.com/puppetlabs/puppet-resource_api
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: puppet
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
# /oreon:deps
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

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
rm -rf %{buildroot}%{gem_instdir}/{.gitignore,.rubocop.yml,.travis.yml,appveyor.yml,codecov.yml}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n rubygem-puppet-resource_api-doc -f %{oreon_filedir}/rubygem-puppet-resource_api-doc.list

%changelog

%autochangelog
