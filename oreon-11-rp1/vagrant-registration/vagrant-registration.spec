%global source0_hash 8bba83e280ebbce8abef4614f1a27ae3c3cc53737e870c7541b0074af538ce97

# Generated from vagrant-registration-0.0.7.gem by gem2rpm -*- rpm-spec -*-
%global vagrant_plugin_name vagrant-registration

Name: %{vagrant_plugin_name}
Version: 1.3.1
Release: 20%{?dist}
Summary: Automatic guest registration for Vagrant
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: https://github.com/projectatomic/adb-vagrant-registration
Source0: https://rubygems.org/gems/%{vagrant_plugin_name}-%{version}.gem
Requires: vagrant >= 1.9.1
BuildRequires: vagrant >= 1.9.1
BuildRequires: rubygem(rdoc)
BuildArch: noarch
Provides: vagrant(%{vagrant_plugin_name}) = %{version}

%description
Enables guests to be registered automatically which is especially useful
for RHEL or SLES guests.

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
%vagrant_plugin_install

chmod 644 .%{vagrant_plugin_instdir}/resources/rhn_unregister.py
sed -i 's/^#!\/usr\/bin\/python$//' .%{vagrant_plugin_instdir}/resources/rhn_unregister.py

%install
mkdir -p %{buildroot}%{vagrant_plugin_dir}
cp -a .%{vagrant_plugin_dir}/* \
        %{buildroot}%{vagrant_plugin_dir}/

# We can't run test suite because it requires virtualization
%check
pushd .%{vagrant_plugin_instdir}

popd

%files
%dir %{vagrant_plugin_instdir}
%license %{vagrant_plugin_instdir}/LICENSE
%{vagrant_plugin_libdir}
%{vagrant_plugin_instdir}/locales
%{vagrant_plugin_instdir}/plugins
%{vagrant_plugin_instdir}/resources
%exclude %{vagrant_plugin_cache}
%{vagrant_plugin_spec}

%files doc
%doc %{vagrant_plugin_docdir}
%doc %{vagrant_plugin_instdir}/CHANGELOG.adoc
%{vagrant_plugin_instdir}/Gemfile
%doc %{vagrant_plugin_instdir}/README.adoc
%{vagrant_plugin_instdir}/Rakefile
%{vagrant_plugin_instdir}/vagrant-registration.gemspec

%changelog
%autochangelog
