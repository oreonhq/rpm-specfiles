%global source0_hash 3b004e3714f9e174a01987c13977452e6ae65d0083a35a334639289fccd2a091

%global vagrant_plugin_name vagrant-digitalocean

Name: vagrant-digitalocean
Version: 0.9.0
Release: 20%{?dist}
Summary: Vagrant plugin for having Digital Ocean as an provider
License: MIT
URL: https://github.com/devopsgroup-io/vagrant-digitalocean
Source0: https://rubygems.org/gems/%{vagrant_plugin_name}-%{version}.gem
Requires: vagrant >= 1.9.1
Requires: rubygem-highline
Requires: rubygem-faraday
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildRequires: vagrant >= 1.9.1
BuildArch: noarch
Provides: vagrant(vagrant-digitalocean) = %{version}

%description
It is a Vagrant provider plugin that supports the management of DigitalOcean
droplets (instances).

%package doc
Summary: Documentation for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildArch: noarch

Provides: bundled(lato-fonts)
# Using OFL license https://www.google.com/fonts/specimen/Source+Code+Pro
Provides: bundled(sourcecodepro-fonts)

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}
%setup -q -D -T -n  %{vagrant_plugin_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{vagrant_plugin_name}.gemspec

%build
gem build %{name}.gemspec
# Despite having install in the name, this macro builds the docs among other
# things, so it belongs here.
%vagrant_plugin_install

%install
# We don't ship the test suite
rm -rf .%{vagrant_plugin_dir}/gems/%{vagrant_plugin_name}-%{version}/test

mkdir -p %{buildroot}%{vagrant_plugin_dir}
cp -a .%{vagrant_plugin_dir}/* \
       %{buildroot}%{vagrant_plugin_dir}/

%files
%license %{vagrant_plugin_instdir}/LICENSE.txt
%exclude %{vagrant_plugin_cache}
%dir %{vagrant_plugin_instdir}
%exclude %{vagrant_plugin_instdir}/.gitignore
%{vagrant_plugin_instdir}/locales
%{vagrant_plugin_libdir}
%{vagrant_plugin_spec}
%{vagrant_plugin_instdir}/box*

%files doc
%license %{vagrant_plugin_instdir}/LICENSE.txt
%doc %{vagrant_plugin_docdir}
%doc %{vagrant_plugin_instdir}/README.md
%{vagrant_plugin_instdir}/Gemfile
%{vagrant_plugin_instdir}/Rakefile
%{vagrant_plugin_instdir}/%{vagrant_plugin_name}.gemspec
%{vagrant_plugin_instdir}/box/*

%changelog
%autochangelog
