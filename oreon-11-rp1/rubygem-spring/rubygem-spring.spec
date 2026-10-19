%global source1_hash 7f63794447f1e42c8ba794c6b82f679324f36bd11946ef58c753f6528709100c
%global source0_hash 1d240116fde0af4979dd0c9501fde96114e07599ca012fb34e8c95342edf6df3
%global gem_name spring
Name: rubygem-%{gem_name}
Version: 4.1.1
Release:        7%{?dist}
Summary:        Rails application preloader
License: MIT
URL: https://github.com/rails/spring
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/rails/spring/archive/refs/tags/v4.1.1.tar.gz
Requires: %{_bindir}/ps
BuildArch: noarch
Provides: bundled(okjson) = 43
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(activesupport)
BuildRequires:  rubygem(bundler)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Spring is a Rails application preloader. It speeds up development by keeping
your application running in the background so you don't need to boot it every
time you run a test, rake task or migration.

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
mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ln -s %{_builddir}/test test
ruby -Ilib -e 'Dir.glob "./test/unit/**/*_test.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-spring-doc -f %{oreon_filedir}/rubygem-spring-doc.list

%changelog

%autochangelog
