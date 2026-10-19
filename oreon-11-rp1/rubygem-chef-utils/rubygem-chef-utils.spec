%global source1_hash 6f6f0b770941baaf68a6ecb6c0451c02f26fe2df36e51ae93d1b1f19c13f28fd
%global source0_hash 7c69ad7a8e6e1632c21d8026fbae7ae2363ee7fd9810b102fa00908d0f66fc65
%global gem_name chef-utils
Summary:        Run external commands on Unix or Windows
Name: rubygem-%{gem_name}
Version: 19.1.164
Release:        1%{?dist}
License: Apache-2.0
URL: https://github.com/chef/chef/tree/main/chef-utils
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/chef/chef/archive/refs/tags/v19.1.164.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  grep
BuildRequires:  procps
BuildRequires:  rubygem(concurrent-ruby)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
BuildRequires:  tar
# /oreon:deps
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
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

%gem_install -n %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
tar zxvf %{SOURCE1}
grep -l fauxhai spec/unit/dsl/* | xargs rm -f
rspec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-chef-utils-doc -f %{oreon_filedir}/rubygem-chef-utils-doc.list

%changelog

%autochangelog
