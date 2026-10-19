%global source0_hash e7aaf0df0d6e6d440f8340d187e134ec501dfd07181f0990f905587b208c863a
%global vagrant_plugin_name vagrant-sshfs
Name: %{vagrant_plugin_name}
Version: 1.3.7
Release:        13%{?dist}
Summary:        A Vagrant synced folder plugin that mounts folders via SSHFS
License: GPL-2.0-only
URL: https://github.com/dustymabe/vagrant-sshfs
Source0:        https://rubygems.org/gems/%{name}-%{version}.gem
Requires: vagrant >= 1.9.1
Recommends: /usr/bin/fusermount
Recommends: /usr/bin/sshfs
BuildArch: noarch
Provides: vagrant(%{vagrant_plugin_name}) = %{version}
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygem(rdoc)
BuildRequires:  rubygems-devel
BuildRequires:  vagrant
# /oreon:deps
%description
A Vagrant synced folder plugin that mounts folders via SSHFS. 
This is the successor to Fabio Kreusch's implementation:
https://github.com/fabiokr/vagrant-sshfs.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -b 0 -q -n %{vagrant_plugin_name}-%{version}

# remove dependencies on windows libraries (needed for windows, not linux)
%gemspec_remove_dep -s ../%{vagrant_plugin_name}-%{version}.gemspec -g win32-process

%build

gem build ../%{vagrant_plugin_name}-%{version}.gemspec
%vagrant_plugin_install
%install
mkdir -p %{buildroot}%{vagrant_plugin_dir}
cp -a .%{vagrant_plugin_dir}/* \
        %{buildroot}%{vagrant_plugin_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n vagrant-sshfs-doc -f %{oreon_filedir}/vagrant-sshfs-doc.list

%changelog

%autochangelog
