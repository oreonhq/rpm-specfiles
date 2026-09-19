%global source0_hash 22c21fd1f3862512a34939ab7656b7326a9fc93b1146fa83ac5c5c3c92ba218c

# Generated from vagrant-adbinfo-0.0.4.gem by gem2rpm -*- rpm-spec -*-
%global vagrant_plugin_name vagrant-adbinfo

Name: %{vagrant_plugin_name}
Version: 0.1.0
Release: 20%{?dist}
Summary: Connection and configuration for a Docker daemon
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: https://github.com/projectatomic/vagrant-adbinfo
Source0: https://rubygems.org/gems/%{vagrant_plugin_name}-%{version}.gem
Requires: vagrant >= 1.9.1
BuildRequires: rubygem(rdoc)
BuildRequires: vagrant >= 1.9.1
BuildArch: noarch
Provides: vagrant(%{vagrant_plugin_name}) = %{version}

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
# Create the gem as gem install only works on a gem file
gem build %{vagrant_plugin_name}.gemspec

# %%vagrant_plugin_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%vagrant_plugin_install

%install
mkdir -p %{buildroot}%{vagrant_plugin_dir}
cp -a .%{vagrant_plugin_dir}/* \
        %{buildroot}%{vagrant_plugin_dir}/

# Run the test suite
%check
pushd .%{vagrant_plugin_instdir}

popd

%files
%dir %{vagrant_plugin_instdir}
%exclude %{vagrant_plugin_instdir}/.*
%license %{vagrant_plugin_instdir}/LICENSE
%{vagrant_plugin_libdir}
%exclude %{vagrant_plugin_cache}
%{vagrant_plugin_spec}

%files doc
%doc %{vagrant_plugin_docdir}
%doc %{vagrant_plugin_instdir}/CHANGELOG.md
%doc %{vagrant_plugin_instdir}/CONTRIBUTING.md
%doc %{vagrant_plugin_instdir}/MAINTAINERS
%{vagrant_plugin_instdir}/Gemfile
%doc %{vagrant_plugin_instdir}/README.md
%{vagrant_plugin_instdir}/Rakefile
%{vagrant_plugin_instdir}/Vagrantfile
%{vagrant_plugin_instdir}/vagrant-adbinfo.gemspec
%{vagrant_plugin_instdir}/vagrant-adbinfo.spec

%changelog
%autochangelog
