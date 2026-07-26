%global source0_hash 83ced3a3d7f95f67de958d2ce41b1874e83c8d94fe2ddbff50c8b4b82323563a

%global enable_checks 1

# Generated from deep_merge-1.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name deep_merge

Name: rubygem-%{gem_name}
Version: 1.2.2
Release: 11%{?dist}
Summary: Merge Deeply Nested Hashes
License: MIT
URL: https://github.com/danielsdeleo/deep_merge
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(rubygems) 
BuildRequires: rubygems-devel 
BuildRequires: ruby 
%if 0%{?enable_checks}
BuildRequires: rubygem(minitest) >= 5
BuildRequires: rubygem(test-unit)
%endif

BuildArch: noarch

%description
Recursively merge hashes. 

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
%if 0%{?enable_checks}
ruby -Ilib test/test_deep_merge.rb
%endif

%files
%dir %{gem_instdir}

%{gem_libdir}
%exclude %{gem_cache} 
%exclude %{gem_instdir}/CHANGELOG
%exclude %{gem_instdir}/test
%exclude %{gem_instdir}/Rakefile
%{gem_spec}
%doc %{gem_instdir}/LICENSE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md 

%changelog
%autochangelog
