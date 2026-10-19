%global source1_hash 120d15e068293cacca9de4d5ac130c299b82cb8de45ac641eb37f90baf6a0437
%global source0_hash 403bc5d598353821e94d4c870e7927dbd61731de38bdeb75741cbb4f18c47bf9
%global gem_name rack-cache
Name: rubygem-%{gem_name}
Version: 1.14.0
Release:        7%{?dist}
Summary:        HTTP Caching for Rack
License: MIT
URL: https://github.com/rack/rack-cache
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/rack/rack-cache/archive/refs/tags/v1.14.0.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(minitest-global_expectations)
BuildRequires:  rubygem(mocha)
BuildRequires:  rubygem(rack)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Rack::Cache is suitable as a quick drop-in component to enable HTTP caching
for Rack-based applications that produce freshness (expires, cache-control)
and/or validation (last-modified, etag) information.

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
ln -s %{_builddir}/test .
sed -i '/bundler/ s/^/#/' test/test_helper.rb
sed -i '/global_must/ s/global_must/global_expectations/' test/test_helper.rb
sed -i 's/maxitest/minitest/' test/test_helper.rb
mv test/meta_store_test.rb{,.disabled}
ruby -Ilib -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-rack-cache-doc -f %{oreon_filedir}/rubygem-rack-cache-doc.list

%changelog

%autochangelog
