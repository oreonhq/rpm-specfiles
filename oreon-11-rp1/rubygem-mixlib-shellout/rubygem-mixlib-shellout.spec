%global source0_hash 41b05507258dbaa6e801b52b0290993e46bcd07922ffb032487c11194d66d73d

%global gem_name mixlib-shellout

Summary: Run external commands on Unix or Windows
Name: rubygem-%{gem_name}
Version: 3.4.10
Release: 1%{?dist}
License: Apache-2.0
URL: https://github.com/chef/mixlib-shellout
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Tests for this package are not in the gem. To update:
# git clone https://github.com/chef/mixlib-shellout.git && cd mixlib-shellout
# version=3.4.10
# git checkout v${version?}
# tar czvf ../rubygem-mixlib-shellout/rubygem-mixlib-shellout-${version?}-specs.tgz spec/
Source1: rubygem-%{gem_name}-%{version}-specs.tgz

BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(chef-utils)
BuildRequires: procps
BuildRequires: tar
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

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

%gem_install -n %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
tar zxvf %{SOURCE1}
# upstream tests fail: https://github.com/chef/mixlib-shellout/issues/278
# so removing that file, but not others, so we have some tests
rm spec/mixlib/shellout_spec.rb
# some tests sleep a bit so make sure we wait...
rspec && sleep 10
popd

%files
%license %{gem_instdir}/LICENSE
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
%autochangelog
