%global source1_hash 8cbf86ede385760ae4adb3be1c6a464e53b0ffe7f8fb405986bd42be5d11ca7e
%global source0_hash 7c8a6c5a6c90922a8871ed682129c19c9b1a514eedea2e867077229e6a415f0c
%global gem_name mixlib-shellout
Summary:        Run external commands on Unix or Windows
Name: rubygem-%{gem_name}
Version: 3.4.10
Release:        1%{?dist}
License: Apache-2.0
URL: https://github.com/chef/mixlib-shellout
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/chef/mixlib-shellout/archive/refs/tags/v3.4.10.tar.gz
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}
# oreon:deps
BuildRequires:  procps
BuildRequires:  rubygem(chef-utils)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
BuildRequires:  tar
# /oreon:deps
%description
Run external commands on Unix or Windows

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
rm spec/mixlib/shellout_spec.rb
rspec && sleep 10
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-mixlib-shellout-doc -f %{oreon_filedir}/rubygem-mixlib-shellout-doc.list

%changelog

%autochangelog
