%global source0_hash 3d4864f218d54580dffcf0a97da0af2456cd8aa1d1c35d1944ed021cc032ff36

%global gem_name chef-utils

Summary: Run external commands on Unix or Windows
Name: rubygem-%{gem_name}
Version: 19.1.164
Release: %autorelease
License: Apache-2.0
URL: https://github.com/chef/chef/tree/main/chef-utils
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Tests for this package are not in the gem. To update:
# git clone https://github.com/chef/chef.git && cd chef/chef-utils
# version=<version>
# git checkout v${version?}
# tar czvf ../../rubygem-chef-utils/rubygem-chef-utils-${version?}-specs.tgz spec/
Source1: rubygem-%{gem_name}-%{version}-specs.tgz

BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(concurrent-ruby)
BuildRequires: procps
BuildRequires: tar
BuildRequires: findutils
BuildRequires: coreutils
BuildRequires: grep
BuildArch: noarch

%description
A set of convenience functions for various libraries and utilities in the Chef
ecosystem.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T

%gem_install -n %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
tar zxvf %{SOURCE1}
# A few tests depend on fauxhai which isn't in a packagable state.
#
# Most tests work fine without it, so disable the few tests that require it.
grep -l fauxhai spec/unit/dsl/* | xargs rm -f
rspec
popd

%files
%license %{gem_instdir}/LICENSE
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/spec
%{gem_spec}
%exclude %{gem_instdir}/%{gem_name}.gemspec

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Rakefile

%changelog
%autochangelog
