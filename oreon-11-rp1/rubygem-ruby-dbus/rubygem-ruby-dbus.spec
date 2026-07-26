%global source0_hash b48424f9c73f326a87aafaaa2517945c489a1d3b2248b1c7dd475ded75f7a3c3

# Generated from ruby-dbus-0.7.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ruby-dbus

Name: rubygem-%{gem_name}
Version: 0.22.1
Release: 9%{?dist}
Summary: Ruby module for interaction with D-Bus
# MIT: lib/dbus/core_ext/*
License: LGPL-2.1-or-later AND MIT
URL: https://github.com/mvidner/ruby-dbus
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Support ruby3.4 backtrace formatting change
# https://github.com/mvidner/ruby-dbus/pull/145
Patch0:  %{gem_name}-pr145-support-ruby34-backtrace-formatting.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
# ReXML as well as Nokogiri are necessary to pass the test suite.
# https://github.com/mvidner/ruby-dbus/issues/137
BuildRequires: rubygem(nokogiri)
BuildRequires: rubygem(rexml)
# https://github.com/mvidner/ruby-dbus/pull/147
BuildRequires: rubygem(logger)
BuildRequires: rubygem(ostruct)
BuildRequires: %{_bindir}/dbus-daemon
BuildArch: noarch

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
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
spec/tools/test_env rspec spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/COPYING
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/.rspec
%doc %{gem_instdir}/NEWS.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/VERSION
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/doc
%{gem_instdir}/examples
%{gem_instdir}/ruby-dbus.gemspec
%{gem_instdir}/spec

%changelog
%autochangelog
