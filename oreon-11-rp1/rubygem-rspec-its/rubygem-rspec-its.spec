%global source0_hash a88e8bc38149f2835e93533591ec4f5c829aacbfd41269a2e6f9f5b82f5260df

%global gem_name rspec-its

Name: rubygem-%{gem_name}
Version: 2.0.0
Release: 1%{?dist}
Summary: Provides "its" method formerly part of rspec-core
License: MIT
URL: https://github.com/rspec/rspec-its
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Ruby 3.4 changes backticks to single quotes, which breaks test suite.
# https://github.com/rspec/rspec-its/pull/96
Patch0: rubygem-cucumber-1.3.1-Ruby-3-4-replaces-initial-backtick-by-single-quote.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(cucumber)
BuildRequires: rubygem(aruba)
BuildRequires: rubygem(rspec-core)
BuildRequires: rubygem(rspec-expectations)
BuildRequires: rubygem(matrix)
BuildArch: noarch

%description
RSpec extension gem for attribute matching.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

%patch 0 -p1

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

export RUBYOPT="-I${PWD}/lib"
# Exclude the pre RSpec 3.9 test cases.
cucumber --tags 'not @pre-3-9'
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Changelog.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/features
%{gem_instdir}/rspec-its.gemspec
%{gem_instdir}/script
%{gem_instdir}/spec

%changelog
%autochangelog
