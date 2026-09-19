%global source0_hash 3c5baea113631d1af344c7c2dc87969eb7a7029b9729ac38113f93afd1b5457a

%global gem_name rbvmomi

Name: rubygem-%{gem_name}
Version: 3.0.0
Release: 11%{?dist}
Summary: Ruby interface to the VMware vSphere API
License: MIT
URL: https://github.com/vmware/rbvmomi
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/vmware/rbvmomi.git && cd rbvmomi
# git checkout v1.11.2 && tar czvf rbvmomi-1.11.2-tests.tgz test/
Source1: %{gem_name}-%{version}-tests.tgz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.4.1
BuildRequires: rubygem(base64)
BuildRequires: rubygem(nokogiri)
BuildRequires: rubygem(builder)
BuildRequires: rubygem(test-unit)
BuildArch: noarch

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
%gem_install -n %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

%check
pushd .%{gem_instdir}
tar xzvf %{SOURCE1}

# We don't really care about code coverage.
sed -i "/[sS]imple[cC]ov/ s/^/#/" test/test_helper.rb

ruby -Ilib:test -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}/
%{_bindir}/rbvmomish
%license %{gem_instdir}/LICENSE
%{gem_instdir}/exe
%{gem_libdir}/
%exclude %{gem_instdir}/rbvmomi.gemspec
%{gem_instdir}/vmodl.db
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}/
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
