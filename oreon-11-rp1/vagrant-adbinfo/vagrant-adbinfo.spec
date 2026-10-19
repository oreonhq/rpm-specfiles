%global source0_hash 22c21fd1f3862512a34939ab7656b7326a9fc93b1146fa83ac5c5c3c92ba218c
%global vagrant_plugin_name vagrant-adbinfo
Name: %{vagrant_plugin_name}
Version: 0.1.0
Release:        1%{?dist}
Summary:        Connection and configuration for a Docker daemon
License: GPL-2.0-only
URL: https://github.com/projectatomic/vagrant-adbinfo
Source0:        https://rubygems.org/gems/%{name}-%{version}.gem
Requires: vagrant >= 1.9.1
BuildArch: noarch
Provides: vagrant(%{vagrant_plugin_name}) = %{version}
# oreon:deps
BuildRequires:  rubygem(rdoc)
BuildRequires:  vagrant
# /oreon:deps
%description
Vagrant plugin that provides the IP address:port and TLS certificate file
location for a Docker daemon.

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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{vagrant_plugin_instdir}
popd
%files -f %{oreon_filedir}/main.list
%files -n vagrant-adbinfo-doc -f %{oreon_filedir}/vagrant-adbinfo-doc.list

%changelog

%autochangelog
