%global source1_hash 0a0b5a3de3b5e7af0554e062879bf6899bdddf7625abf3e26a1f2f0e49bf30d4
%global source0_hash cf6e2842df8c55f5e4d1a4be015e603e19e9bc3a7178bae58949ccbb58558bac
%global gem_name rack-protection
%bcond_with bootstrap
Name: rubygem-%{gem_name}
Version: 4.2.1
Release:        1%{?dist}
Summary:        Ruby gem that protects against typical web attacks
License: MIT
URL: https://sinatrarb.com/protection/
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/sinatra/sinatra/archive/refs/tags/v4.2.1.tar.gz
%if %{without bootstrap}
%endif
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Protect against typical web attacks, works with all Rack apps, including
Rails.

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

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{without bootstrap}
%check

pushd .%{gem_instdir}
ln -s %{_builddir}/spec spec
rspec -rspec_helper spec
popd
%endif
%files -f %{oreon_filedir}/main.list
%files -n rubygem-rack-protection-doc -f %{oreon_filedir}/rubygem-rack-protection-doc.list

%changelog

%autochangelog
