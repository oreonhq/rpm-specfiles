%global source1_hash 3d2fb11fa6308edf9c72a854dc656d5e43e30d494a1c42c3cf25f58884ce6119
%global source0_hash f737191fd5c5b348b7f0a4412a3b86383f88c43e13b8217b63d4c8d90b9e798d
%global gem_name rackup
Name: rubygem-%{gem_name}
Version: 2.2.1
Release:        1%{?dist}
Summary:        A general server command for Rack applications
License: MIT
URL: https://github.com/rack/rackup
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/rack/rackup/archive/refs/tags/v2.2.1.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(minitest-global_expectations)
BuildRequires:  rubygem(rack)
BuildRequires:  rubygem(webrick)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
A general server command for Rack applications.

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
find %{buildroot}%{gem_instdir}/bin -type f | \
  xargs sed -i 's|^#!/usr/bin/env ruby$|#!/usr/bin/ruby|'
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

( cd .%{gem_instdir}
cp -a %{builddir}/test .
ruby -Ilib:test -e 'Dir.glob "./test/**/spec_*.rb", &method(:require)'
)
%files -f %{oreon_filedir}/main.list
%files -n rubygem-rackup-doc -f %{oreon_filedir}/rubygem-rackup-doc.list

%changelog

%autochangelog
