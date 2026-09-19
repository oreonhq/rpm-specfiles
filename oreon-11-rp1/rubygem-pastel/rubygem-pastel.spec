%global source0_hash 481da9fb7d2f6e6b1a08faf11fa10363172dc40fd47848f096ae21209f805a75

# Generated from pastel-0.8.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name pastel

Name: rubygem-%{gem_name}
Version: 0.8.0
Release: 11%{?dist}
Summary: Terminal strings styling with intuitive and clean API
License: MIT
URL: https://ttytoolkit.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.0.0
BuildRequires: rubygem-rspec
BuildArch: noarch

%description
Terminal strings styling with intuitive and clean API.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
rspec spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
