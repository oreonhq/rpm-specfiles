%global source0_hash 13a8fc3921ce4df8e04fb65f1037251decb08d74757b41163688bd1c1feccd39

# Generated from connection_pool-2.2.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name connection_pool

Name: rubygem-%{gem_name}
Version: 2.2.5
Release: 13%{?dist}
Summary: Generic connection pool for Ruby
License: MIT
URL: https://github.com/mperham/connection_pool
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Fix compatibility with minitest 6
Patch0:  %{gem_name}-2.2.5-minitest6.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(minitest-mock)
BuildArch: noarch

%description
Generic connection pool for Ruby.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
%patch -P0 -p1

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
  ruby -Ilib -e 'Dir.glob "./test/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/Changes.md
%{gem_libdir}
%{gem_spec}
%license %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}
%exclude %{gem_instdir}/connection_pool.gemspec

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/test
%{gem_instdir}/Gemfile

%changelog
%autochangelog
