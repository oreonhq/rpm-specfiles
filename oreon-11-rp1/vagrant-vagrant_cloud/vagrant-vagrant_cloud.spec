%global source0_hash 6ba87f548cb8963b946ebda63607257d2d57f1d2aaab58a206232826336ae05a

# Generated from vagrant_cloud-2.0.1.gem by gem2rpm -*- rpm-spec -*-
%global vagrant_plugin_name vagrant_cloud

Name: vagrant-%{vagrant_plugin_name}
Version: 3.0.5
Release: 10%{?dist}
Summary: Vagrant Cloud API Library
License: MIT
URL: https://github.com/hashicorp/vagrant_cloud
Source0: %{vagrant_plugin_name}-%{version}.gem
# Upstream gem doesn't ship tests, pull it from upstream
# git clone --no-checkout https://github.com/hashicorp/vagrant_cloud.git
# git -C vagrant_cloud archive -v -o vagrant_cloud-3.0.5-spec.txz v3.0.5 spec
Source1: %{vagrant_plugin_name}-%{version}-spec.txz
Requires: vagrant
BuildRequires: vagrant
BuildRequires: rubygem(rdoc)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(webmock)
BuildRequires: rubygem(excon)
BuildArch: noarch
Provides: vagrant(%{vagrant_plugin_name}) = %{version}

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

%check
pushd .%{vagrant_plugin_instdir}
ln -s %{_builddir}/spec .

rspec spec
popd

%files
%dir %{vagrant_plugin_instdir}
%license %{vagrant_plugin_instdir}/LICENSE
%{vagrant_plugin_libdir}
%exclude %{vagrant_plugin_cache}
%{vagrant_plugin_spec}

%files doc
%doc %{vagrant_plugin_docdir}
%doc %{vagrant_plugin_instdir}/README.md

%changelog
%autochangelog
