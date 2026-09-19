%global source0_hash 66ea4a9425bcf198bc1e5e5a225f370699597901d3d502ad2d93eb45b7c429ba

%global vagrant_plugin_name vagrant-hostmanager

Name: vagrant-hostmanager
Version: 1.8.10
Release: %autorelease
BuildArch: noarch

License: MPL-2.0
Summary: Vagrant plugin to manage /etc/hosts
URL:     https://github.com/devopsgroup-io/vagrant-hostmanager
Source0: https://rubygems.org/gems/%{vagrant_plugin_name}-%{version}.gem

BuildRequires: ruby(release)
BuildRequires: ruby
BuildRequires: rubygem(rdoc)
BuildRequires: vagrant >= 1.9.1

Requires: vagrant >= 1.9.1

Provides: vagrant(vagrant-hostmanager) = %{version}

%description
vagrant-hostmanager is a Vagrant plugin that manages the /etc/hosts file
on guest machines (and optionally the host). Its goal is to enable
resolution of multi-machine environments deployed with a cloud provider
where IP addresses are not known in advance.

%package doc
BuildArch: noarch
Summary: Documentation for %{name}

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
%license %{vagrant_plugin_instdir}/LICENSE
%exclude %{vagrant_plugin_cache}
%dir %{vagrant_plugin_instdir}
%exclude %{vagrant_plugin_instdir}/.gitignore
%{vagrant_plugin_instdir}/locales
%{vagrant_plugin_libdir}
%{vagrant_plugin_spec}

%files doc
%license %{vagrant_plugin_instdir}/LICENSE
%doc %{vagrant_plugin_docdir}
%doc %{vagrant_plugin_instdir}/CHANGELOG.md
%doc %{vagrant_plugin_instdir}/README.md
%{vagrant_plugin_instdir}/Gemfile
%{vagrant_plugin_instdir}/Rakefile
%{vagrant_plugin_instdir}/%{vagrant_plugin_name}.gemspec

%changelog
%autochangelog
