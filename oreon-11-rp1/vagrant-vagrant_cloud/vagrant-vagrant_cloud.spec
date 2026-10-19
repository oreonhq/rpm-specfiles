%global source0_hash 6ba87f548cb8963b946ebda63607257d2d57f1d2aaab58a206232826336ae05a
%global vagrant_plugin_name vagrant_cloud
Name: vagrant-%{vagrant_plugin_name}
Version: 3.0.5
Release:        10%{?dist}
Summary:        Vagrant Cloud API Library
License: MIT
URL: https://github.com/hashicorp/vagrant_cloud
Source0:        %{vagrant_plugin_name}-%{version}.gem
Source1: %{vagrant_plugin_name}-%{version}-spec.txz
Requires: vagrant
BuildArch: noarch
Provides: vagrant(%{vagrant_plugin_name}) = %{version}
# oreon:deps
BuildRequires:  rubygem(excon)
BuildRequires:  rubygem(rdoc)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(webmock)
BuildRequires:  vagrant
# /oreon:deps
%description
Ruby library for the HashiCorp Vagrant Cloud API.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{vagrant_plugin_name}-%{version} -b1

%build

gem build ../%{vagrant_plugin_name}-%{version}.gemspec
%vagrant_plugin_install
%install
mkdir -p %{buildroot}%{vagrant_plugin_dir}
cp -a .%{vagrant_plugin_dir}/* \
        %{buildroot}%{vagrant_plugin_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{vagrant_plugin_instdir}
ln -s %{_builddir}/spec .
rspec spec
popd
%files -f %{oreon_filedir}/main.list
%files -n vagrant-vagrant_cloud-doc -f %{oreon_filedir}/vagrant-vagrant_cloud-doc.list

%changelog

%autochangelog
