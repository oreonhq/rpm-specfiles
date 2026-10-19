%global source0_hash e21ab942e38822aafa3060152da44af5befbc15d772432f7805f61102899b80e
%global vagrant_plugin_name vagrant-registration
Name: %{vagrant_plugin_name}
Version: 1.3.4
Release:        1%{?dist}
Summary:        Automatic guest registration for Vagrant
License: GPL-2.0-only
URL: https://github.com/projectatomic/adb-vagrant-registration
Source0:        https://rubygems.org/gems/%{name}-%{version}.gem
Requires: vagrant >= 1.9.1
BuildArch: noarch
Provides: vagrant(%{vagrant_plugin_name}) = %{version}
# oreon:deps
BuildRequires:  rubygem(rdoc)
BuildRequires:  vagrant
# /oreon:deps
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

gem build %{vagrant_plugin_name}.gemspec
%vagrant_plugin_install
chmod 644 .%{vagrant_plugin_instdir}/resources/rhn_unregister.py
sed -i 's/^#!\/usr\/bin\/python$//' .%{vagrant_plugin_instdir}/resources/rhn_unregister.py
%install
mkdir -p %{buildroot}%{vagrant_plugin_dir}
cp -a .%{vagrant_plugin_dir}/* \
        %{buildroot}%{vagrant_plugin_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{vagrant_plugin_instdir}
popd
%files -f %{oreon_filedir}/main.list
%files -n vagrant-registration-doc -f %{oreon_filedir}/vagrant-registration-doc.list

%changelog

%autochangelog
