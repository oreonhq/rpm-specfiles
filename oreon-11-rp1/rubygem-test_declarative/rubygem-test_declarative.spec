%global source0_hash a0b0c311fd50f8f0db331740a24eb66b5ee92a8549a7f651a8a5fd7802f1cf51

# Generated from test_declarative-0.0.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name test_declarative

Name: rubygem-%{gem_name}
Version: 0.0.6
Release: 9%{?dist}
Summary: Simply adds a declarative test method syntax to test/unit
License: MIT
URL: http://github.com/svenfuchs/test_declarative
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/svenfuchs/test_declarative.git && cd test_declarative
# git archive -v -o test_declarative-0.0.6-test.tar.gz v0.0.6 test/
Source1: %{gem_name}-%{version}-test.tar.gz
# Fix Minitest 5.19+ compatibility.
# https://github.com/svenfuchs/test_declarative/pull/24
Patch0: rubygem-test_declarative-0.0.6-Use-Minitest-Test-as-a-test-runner.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(test-unit)
BuildArch: noarch

%description
Simply adds a declarative test method syntax to test/unit.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1

pushd %{_builddir}
%patch 0 -p1
popd

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
ln -s %{_builddir}/test test

# Use `BUNDLE_GEMFILE` env variable to trick the test suite to run against
# various test frameworks (and ignore Minitest 4.x).
# https://github.com/svenfuchs/test_declarative/blob/4c0ccc6f649f33f76772a826e6afd367b143cd66/test/test_declarative_test.rb#L10-L37
BUNDLE_GEMFILE=Gemfile ruby -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
BUNDLE_GEMFILE=Gemfile.unit-test ruby -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
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
