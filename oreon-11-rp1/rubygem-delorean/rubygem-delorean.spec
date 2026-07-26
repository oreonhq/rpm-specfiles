%global source0_hash 5f7e5af9084f0d043cc3e48bfd8e6727186954b47e6aa775550aeff9c7bebba5

%global gem_name delorean

Name: rubygem-%{gem_name}
Version: 2.1.0
Release: 23%{?dist}
Summary: Delorean lets you travel in time with Ruby by mocking Time.now
License: MIT
URL: https://github.com/bebanjo/delorean
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# to get specs:
# git clone https://github.com/bebanjo/delorean.git && cd delorean
# git checkout v2.1.0
# tar -czf rubygem-delorean-2.1.0-spec.tgz spec/
Source1:  %{name}-%{version}-spec.tgz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
# for specs:
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(activesupport)
BuildRequires: rubygem(chronic)
BuildArch: noarch

%description
Delorean lets you travel in time with Ruby by mocking Time.now.

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

%check
pushd .%{gem_instdir}
tar xzf %{SOURCE1}

rspec spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
