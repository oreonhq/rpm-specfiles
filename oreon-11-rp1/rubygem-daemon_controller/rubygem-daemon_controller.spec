%global source0_hash 6d4b4589f7f8ed2201e857a9f0c80a5c3c19548c5b7b5df55794299fd981aa0b
%define gem_name daemon_controller
Name: rubygem-%{gem_name}
Version: 1.2.0
Release:        26%{?dist}
Summary:        A library for implementing daemon management capabilities
License: MIT
URL: https://github.com/FooBarWidget/daemon_controller
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: rubygem-daemon_controller-1.2.0-upgrade-to-RSpec3.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(benchmark)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
A library for robust daemon management.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n  %{gem_name}-%{version}

%patch 0 -p1

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
rm -rf %{buildroot}%{gem_instdir}/debian.template
rm -rf %{buildroot}%{gem_instdir}/rpm
rm -rf %{buildroot}%{gem_instdir}/Rakefile
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
sed -i 's/localhost/127.0.0.1/g' spec/daemon_controller_spec.rb
rspec spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-daemon_controller-doc -f %{oreon_filedir}/rubygem-daemon_controller-doc.list

%changelog

%autochangelog
