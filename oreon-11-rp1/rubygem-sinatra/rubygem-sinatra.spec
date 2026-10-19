%global source1_hash 0a0b5a3de3b5e7af0554e062879bf6899bdddf7625abf3e26a1f2f0e49bf30d4
%global source0_hash b7aeb9b11d046b552972ade834f1f9be98b185fa8444480688e3627625377080
%global gem_name sinatra
%bcond_with bootstrap
%bcond_without tilt_integration_tests
Name: rubygem-%{gem_name}
Version: 4.2.1
Release:        1%{?dist}
Summary:        Ruby-based web application framework
License: MIT
URL: http://sinatrarb.com/
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/sinatra/sinatra/archive/refs/tags/v4.2.1.tar.gz
Patch0: rubygem-sinatra-4.2.1-Fix-RDoc-6-16-compatibility-by-relaxing-the-check.patch
Patch1: rubygem-sinatra-4.2.1-minitest6.patch
%if %{without bootstrap}
%if %{with tilt_integration_tests}
%endif
%endif
Epoch: 1
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Sinatra is a DSL for quickly creating web applications in Ruby with minimal
effort.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{gem_name}-%{version} -b 1
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

( cd %{builddir}
%patch 0 -p1
%patch 1 -p1
)

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
sed -i -e 's|^#!/usr/bin/env ruby|#!/usr/bin/ruby|' \
  %{buildroot}%{gem_instdir}/examples/*.rb
chmod a+x %{buildroot}%{gem_instdir}/examples/*.rb
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{without bootstrap}
%check

pushd .%{gem_instdir}
cp -a %{builddir}/test test
sed -i '/active_support/ s/^/#/' test/test_helper.rb
mv test/integration_test.rb{,.disabled}
mv test/integration_async_test.rb{,.disabled}
mv test/integration_start_test.rb{,.disabled}
ruby -e 'Dir.glob "./test/*_test.rb", &method(:require)'
popd
%endif
%files -f %{oreon_filedir}/main.list
%files -n rubygem-sinatra-doc -f %{oreon_filedir}/rubygem-sinatra-doc.list

%changelog

%autochangelog
