%global source0_hash fd6ca2c8075f8085065dffcee0805c5b3f88d643d5c954acdc3282f463a9ad58
%global gem_name mixlib-log
Name: rubygem-%{gem_name}
Version: 3.0.9
Release:        1%{?dist}
Summary:        A gem that provides a simple mixin for log functionality
License: Apache-2.0
URL: https://github.com/chef/mixlib-log
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: rubygem-mixlib-log-%{version}-specs.tar.gz
Patch0:  mixlib-log-pr74-ruby33-Logger-support.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(logger)
BuildRequires:  rubygem-rspec
BuildRequires:  rubygems-devel
# /oreon:deps
%description
A gem that provides a simple mixin for log functionality.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1
%patch -P0 -p1

# from lib/mixlib/log.rb
%gemspec_add_dep -g logger

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
ln -s %{_builddir}/spec .
rspec spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-mixlib-log-doc -f %{oreon_filedir}/rubygem-mixlib-log-doc.list

%changelog

%autochangelog
