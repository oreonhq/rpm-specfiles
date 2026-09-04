%global source0_hash 9c079dbc513dfc8833ab59c0c2d8f230fa28499cc5efb4b8dd276cf931457cd1

# Generated from hashdiff-0.3.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name hashdiff

Name: rubygem-%{gem_name}
Version: 1.2.1
Release: 1%{?dist}
Summary: Hashdiff is a diff lib to compute the smallest difference between two hashes
License: MIT
URL: https://github.com/liufengyun/hashdiff
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.8.7
BuildRequires: rubygem(rspec)
BuildArch: noarch

%description
Hashdiff is a diff lib to compute the smallest difference between two hashes.

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

# Run the test suite
%check
pushd .%{gem_instdir}
rspec spec
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE
# Exclude this file, since it is not the original one.
%exclude %{gem_instdir}/hashdiff.gemspec
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/changelog.md
%{gem_instdir}/spec

%changelog
%autochangelog
