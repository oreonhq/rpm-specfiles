%global source1_hash 45799fc4f79b4d0479508332433e44700775588619da4659d4069877087c146e
%global source0_hash 3fe08aa83a23cddce42f4ba412040c08f890d7ff04c175c0ee59119371245be6
%global gem_name fog-core
Name: rubygem-%{gem_name}
Version: 2.6.0
Release:        5%{?dist}
Summary:        Shared classes and tests for fog providers and services
License: MIT
URL: https://github.com/fog/fog-core
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/fog/fog-core/archive/refs/tags/v2.6.0.tar.gz
Patch0:  %{gem_name}-2.6.0-minitest6.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(excon)
BuildRequires:  rubygem(formatador)
BuildRequires:  rubygem(mime-types)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(minitest-mock)
BuildRequires:  rubygem(minitest-stub-const)
BuildRequires:  rubygems-devel
# /oreon:deps
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
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;
(
cd %{_builddir}
%patch -P0 -p1
)

# Test suite passes with Excon 0.100.0 just fine. Relax the dependency for now
# so we don't need to bump excon ATM.
%gemspec_remove_dep -g excon "~> 1.0"
%gemspec_add_dep -g excon [">= 0.100.0", "< 2"]

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
ln -s %{builddir}/spec spec
ruby -Ispec -e 'Dir.glob "./spec/**/*_spec.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-fog-core-doc -f %{oreon_filedir}/rubygem-fog-core-doc.list

%changelog

%autochangelog
