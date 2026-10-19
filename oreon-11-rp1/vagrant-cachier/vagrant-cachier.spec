%global source0_hash 093a9476b390c468d63838b08cec11494074556993a94f2ab75378d184b3216c
%global vagrant_plugin_name vagrant-cachier
Name: %{vagrant_plugin_name}
Version: 1.2.1
Release:        19%{?dist}
Summary:        Vagrant plugin to cache packages
License: MIT
URL: https://github.com/fgrehm/vagrant-cachier
Source0:        https://rubygems.org/gems/%{name}-%{version}.gem
Requires: vagrant >= 1.9.1
BuildArch: noarch
Provides: vagrant(%{vagrant_plugin_name}) = %{version}
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  vagrant
# /oreon:deps
%description
A Vagrant plugin that helps you reduce the amount of coffee you drink
while waiting for boxes to be provisioned by sharing a common package
cache among similar VM instances. Kinda like vagrant-apt_cache or
this magical snippet but targeting multiple package managers and
Linux distros.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n  %{vagrant_plugin_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{vagrant_plugin_name}.gemspec

%build

gem build %{vagrant_plugin_name}.gemspec
%vagrant_plugin_install
%install
mkdir -p %{buildroot}%{vagrant_plugin_dir}
cp -a .%{vagrant_plugin_dir}/* \
        %{buildroot}%{vagrant_plugin_dir}/
sed -i -e '1d' %{buildroot}%{vagrant_plugin_instdir}/spec/acceptance/sanity_check.bats
sed -i -e '1d' %{buildroot}%{vagrant_plugin_instdir}/development/Cheffile
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n vagrant-cachier-doc -f %{oreon_filedir}/vagrant-cachier-doc.list

%changelog

%autochangelog
