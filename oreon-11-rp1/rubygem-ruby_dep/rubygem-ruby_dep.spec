%global source0_hash c5bfbc7c53f9b40d287f426846d0b5765b3d0d197aca60e766b3a678129d2bb0
%bcond_with tests
%global gem_name ruby_dep
Name: rubygem-%{gem_name}
Version: 1.5.0
Release:        19%{?dist}
Summary:        Extracts supported Ruby versions from Travis file
License: MIT
URL: https://github.com/e2/ruby_dep
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: ruby_dep-spec-4e79416.tgz
%if %{with tests}
%endif
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygem(gem_isolater)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
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
%gem_install
cp -a ./spec ./%{gem_instdir}
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
pushd .%{gem_instdir}
rspec spec
popd
%endif
%files -f %{oreon_filedir}/main.list
%files -n rubygem-ruby_dep-doc -f %{oreon_filedir}/rubygem-ruby_dep-doc.list

%changelog

%autochangelog
