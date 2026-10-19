%global source0_hash b48424f9c73f326a87aafaaa2517945c489a1d3b2248b1c7dd475ded75f7a3c3
%global gem_name ruby-dbus
Name: rubygem-%{gem_name}
Version: 0.22.1
Release:        1%{?dist}
Summary:        Ruby module for interaction with D-Bus
License: LGPL-2.1-or-later AND MIT
URL: https://github.com/mvidner/ruby-dbus
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0:  %{gem_name}-pr145-support-ruby34-backtrace-formatting.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  /usr/bin/dbus-daemon
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(logger)
BuildRequires:  rubygem(nokogiri)
BuildRequires:  rubygem(ostruct)
BuildRequires:  rubygem(rexml)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Pure Ruby module for interaction with D-Bus IPC system.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
%patch -P0 -p1

# Rakefile should not be executable.
sed -i '1d' Rakefile
chmod a-x Rakefile

# Fix shebangs.
find {examples,spec} -type f -executable -exec sed -i 's|env ||' '{}' \;
find {examples,spec} -type f -executable -exec sed -r -i 's|#!.?/bin|#!/usr/bin|' '{}' \;

# https://github.com/mvidner/ruby-dbus/pull/147
%gemspec_add_dep -g logger
%gemspec_add_dep -g ostruct

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
spec/tools/test_env rspec spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-ruby-dbus-doc -f %{oreon_filedir}/rubygem-ruby-dbus-doc.list

%changelog

%autochangelog
