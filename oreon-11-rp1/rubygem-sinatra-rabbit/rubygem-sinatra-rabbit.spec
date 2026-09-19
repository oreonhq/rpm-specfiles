%global source0_hash 3c3045186fe81aded2fed85d79ceb4f8d26130a49c8c6897788c698a14b093ed

%global gem_name sinatra-rabbit

Summary: Ruby DSL for creating restful applications using Sinatra
Name: rubygem-%{gem_name}
Version: 1.1.6
Release: 25%{?dist}
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: https://github.com/mifo/sinatra-rabbit
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems)
Requires: rubygem(sinatra)
Requires: rubygem(haml)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(sinatra)
BuildRequires: rubygem(haml)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(rack-test)
BuildRequires: rubygem(nokogiri)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description

Sinatra::Rabbit is a Sinatra extensions that makes designing a REST API much
easier and more fun.
Rabbit maps REST resources to 'collections'. Every collection then could define
CRUD and other operations to manipulate with resource. Rabbit will handle
parameter validation and capability checks for you, so you can focus on the
structure and design of your REST API.

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
# Tests disabled for now because of bug in Fedora minitest
#
#pushd .%{gem_instdir}
#for test_file in tests/*_test.rb; do
#  testrb $test_file
#done
#popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_instdir}/%{gem_name}.gemspec
%exclude %{gem_instdir}/.yardoc
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/tests

%changelog
%autochangelog
