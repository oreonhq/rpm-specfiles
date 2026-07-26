%global source0_hash 6d4b4589f7f8ed2201e857a9f0c80a5c3c19548c5b7b5df55794299fd981aa0b

# Generated from daemon_controller-0.2.5.gem by gem2rpm -*- rpm-spec -*-
%define gem_name daemon_controller

Name: rubygem-%{gem_name}
Version: 1.2.0
Release: 26%{?dist}
Summary: A library for implementing daemon management capabilities
License: MIT
URL: https://github.com/FooBarWidget/daemon_controller
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Move to RSpec3.
# https://github.com/FooBarWidget/daemon_controller/commit/c0afb3b2c0df90b69ed76ffacb539856a59cd230
Patch0: rubygem-daemon_controller-1.2.0-upgrade-to-RSpec3.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(benchmark)
BuildArch: noarch

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
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

rm -rf %{buildroot}%{gem_instdir}/debian.template
rm -rf %{buildroot}%{gem_instdir}/rpm
rm -rf %{buildroot}%{gem_instdir}/Rakefile

%check
pushd .%{gem_instdir}
# be explicit so localhost doesn't resolve to an ipv6 address.
sed -i 's/localhost/127.0.0.1/g' spec/daemon_controller_spec.rb

rspec spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%{gem_docdir}
%doc %{gem_instdir}/README.markdown
%{gem_instdir}/*.gemspec
%{gem_instdir}/spec

%changelog
%autochangelog
