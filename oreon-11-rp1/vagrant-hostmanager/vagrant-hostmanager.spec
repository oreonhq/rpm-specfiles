%global source0_hash 66ea4a9425bcf198bc1e5e5a225f370699597901d3d502ad2d93eb45b7c429ba
%global vagrant_plugin_name vagrant-hostmanager
Name: vagrant-hostmanager
Version: 1.8.10
Release:        1%{?dist}
BuildArch: noarch
License: MPL-2.0
Summary:        Vagrant plugin to manage /etc/hosts
URL:     https://github.com/devopsgroup-io/vagrant-hostmanager
Source0:        https://rubygems.org/gems/%{name}-%{version}.gem
Requires: vagrant >= 1.9.1
Provides: vagrant(vagrant-hostmanager) = %{version}
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(rdoc)
BuildRequires:  vagrant
# /oreon:deps
%description
vagrant-hostmanager is a Vagrant plugin that manages the /etc/hosts file
on guest machines (and optionally the host). Its goal is to enable
resolution of multi-machine environments deployed with a cloud provider
where IP addresses are not known in advance.

%package doc
BuildArch: noarch
Summary: Documentation for %{name}
Provides: bundled(lato-fonts)
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
%vagrant_plugin_install
%install
rm -rf .%{vagrant_plugin_dir}/gems/%{vagrant_plugin_name}-%{version}/test
mkdir -p %{buildroot}%{vagrant_plugin_dir}
cp -a .%{vagrant_plugin_dir}/* \
       %{buildroot}%{vagrant_plugin_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n vagrant-hostmanager-doc -f %{oreon_filedir}/vagrant-hostmanager-doc.list

%changelog

%autochangelog
