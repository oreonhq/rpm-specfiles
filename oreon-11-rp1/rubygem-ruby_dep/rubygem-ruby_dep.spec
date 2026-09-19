%global source0_hash 25f7379de54d35730559cb499b118338443f4b9b59a6a8fe638e9ca32e41e381

# Circular dependency with rubygem-gem_isolater for tests
%bcond_with tests

# Generated from ruby_dep-1.5.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ruby_dep

Name: rubygem-%{gem_name}
Version: 1.5.0
Release: 19%{?dist}
Summary: Extracts supported Ruby versions from Travis file
License: MIT
URL: https://github.com/e2/ruby_dep
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Source1 is tar of spec directory of tests from upstream
Source1: ruby_dep-spec-4e79416.tgz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
%if %{with tests}
BuildRequires: rubygem(gem_isolater)
%endif
BuildArch: noarch

%description
Creates a version constraint of supported Rubies,suitable for a gemspec file.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n  %{gem_name}-%{version} -a 1

%build
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

# build spec tests from Source1
cp -a ./spec ./%{gem_instdir}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
%if %{with tests}
pushd .%{gem_instdir}
rspec spec
popd
%endif

%files
%dir %{gem_instdir}
%{gem_instdir}/spec
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/.rspec
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
