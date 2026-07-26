%global source0_hash deac56ed65a2679c2f9375bed1fe9212e4632f2a22710446b3d5f6b0c794bbd2

# Generated from fog-core-1.22.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name fog-core

Name: rubygem-%{gem_name}
Version: 2.6.0
Release: 5%{?dist}
Summary: Shared classes and tests for fog providers and services
License: MIT
URL: https://github.com/fog/fog-core
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/fog/fog-core.git && cd fog-core
# git archive -v -o fog-core-2.6.0-spec.tar.gz v2.6.0 spec/
Source1: %{gem_name}-%{version}-spec.tar.gz
# Fix compatibility with minitest 6
Patch0:  %{gem_name}-2.6.0-minitest6.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(excon)
BuildRequires: rubygem(formatador)
BuildRequires: rubygem(mime-types)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(minitest-mock)
BuildRequires: rubygem(minitest-stub-const)
BuildArch: noarch

%description
Shared classes and tests for fog providers and services.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1
(
cd %{_builddir}
%patch -P0 -p1
)

# Test suite passes with Excon 0.100.0 just fine. Relax the dependency for now
# so we don't need to bump excon ATM.
%gemspec_remove_dep -g excon "~> 1.0"
%gemspec_add_dep -g excon [">= 0.100.0", "< 2"]

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
ln -s %{builddir}/spec spec

ruby -Ispec -e 'Dir.glob "./spec/**/*_spec.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUT*
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/SECURITY.md
%doc %{gem_instdir}/changelog.md
%{gem_instdir}/fog-core.gemspec

%changelog
%autochangelog
