%global source1_hash 0173b2e019bac21a33981ea76509e535453c779dd896fa640b46c38faf885480
%global source0_hash 7d2adbd43387c0629c27a37fc5084b4567ac7188a75f55f7f913a9632d603d19
%global gem_name rbvmomi
Name: rubygem-%{gem_name}
Version: 3.0.0
Release:        1%{?dist}
Summary:        Ruby interface to the VMware vSphere API
License: MIT
URL: https://github.com/vmware/rbvmomi
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/vmware/rbvmomi/archive/refs/tags/v3.0.0.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(base64)
BuildRequires:  rubygem(builder)
BuildRequires:  rubygem(nokogiri)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Ruby interface to the VMware vSphere API.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

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
mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
tar xzvf %{SOURCE1}
sed -i "/[sS]imple[cC]ov/ s/^/#/" test/test_helper.rb
ruby -Ilib:test -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-rbvmomi-doc -f %{oreon_filedir}/rubygem-rbvmomi-doc.list

%changelog

%autochangelog
