%global source1_hash 727719e34ca4c9056ede02abe5efc8ca57d02a6e68a3c5a646e70b63d330bf50
%global source0_hash 005a36692c306ac0b4a9350355ee080fd09ddef1148a5f8b2ac636c720f5c463
%global gem_name rack-test
Name: rubygem-%{gem_name}
Version: 2.2.0
Release:        1%{?dist}
Summary:        Simple testing API built on Rack
License: MIT
URL: https://github.com/rack/rack-test
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/rack/rack-test/archive/refs/tags/v2.2.0.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(minitest-global_expectations)
BuildRequires:  rubygem(rack)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Rack::Test is a small, simple testing API for Rack apps. It can be used on its
own or as a reusable starting point for Web frameworks and testing libraries
to build on.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n  %{gem_name}-%{version} -b 1
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

( cd .%{gem_instdir}
cp -a %{builddir}/spec spec
ruby -Ispec -e 'Dir.glob "./spec/**/*_spec.rb", &method(:require)'
)
%files -f %{oreon_filedir}/main.list
%files -n rubygem-rack-test-doc -f %{oreon_filedir}/rubygem-rack-test-doc.list

%changelog

%autochangelog
