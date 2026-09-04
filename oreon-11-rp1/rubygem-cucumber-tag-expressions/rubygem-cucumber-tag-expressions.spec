%global source0_hash ead62a1c6bb613de1f5469975a9dd11ba2ced7322a6c8837cdde9db33dcbeac5

# Generated from cucumber-tag-expressions-4.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name cucumber-tag-expressions

Name: rubygem-%{gem_name}
Version: 11.0.1
Release: 1%{?dist}
Summary: Cucumber tag expressions for ruby
License: MIT
URL: https://cucumber.io/docs/cucumber/api/#tag-expressions
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.9.3
BuildRequires: rubygem(rspec)
BuildArch: noarch

Provides: rubygem-cucumber-tag_expressions = %{version}-%{release}
Obsoletes: rubygem-cucumber-tag_expressions < 2.0.2-10

%description
Cucumber tag expressions for ruby.

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
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
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
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/spec

%changelog
%autochangelog
