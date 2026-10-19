%global source1_hash b241820a823384f9e509b65d3164a59be6bb4856f9106f111e2c626d0426615e
%global source0_hash e059eabb5cbd4e6d68589adf2ad380520bee6a8d0c7309755b6450c8b44a0949
%global gem_name test_declarative
Name: rubygem-%{gem_name}
Version: 0.0.6
Release:        9%{?dist}
Summary:        Simply adds a declarative test method syntax to test/unit
License: MIT
URL: http://github.com/svenfuchs/test_declarative
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/svenfuchs/test_declarative/archive/refs/tags/v0.0.6.tar.gz
Patch0: rubygem-test_declarative-0.0.6-Use-Minitest-Test-as-a-test-runner.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
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
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

pushd %{_builddir}
%patch 0 -p1
popd

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ln -s %{_builddir}/test test
BUNDLE_GEMFILE=Gemfile ruby -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
BUNDLE_GEMFILE=Gemfile.unit-test ruby -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-test_declarative-doc -f %{oreon_filedir}/rubygem-test_declarative-doc.list

%changelog

%autochangelog
