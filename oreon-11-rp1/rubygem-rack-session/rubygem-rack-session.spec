%global source1_hash 017498e6e0cdabae278256aac18043342b191110e4684a1971bbe295acdf180a
%global source0_hash 0b6dc07dea7e4b583f58a48e8b806d4c9f1c6c9214ebc202ec94562cbea2e4e9
%global gem_name rack-session
Name: rubygem-%{gem_name}
Version: 2.1.1
Release:        1%{?dist}
Summary:        A session implementation for Rack
License: MIT
URL: https://github.com/rack/rack-session
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0:  rack-session-2.1.1-minitest6.patch
Source1: https://github.com/rack/rack-session/archive/refs/tags/v2.1.1.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(base64)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(minitest-global_expectations)
BuildRequires:  rubygem(minitest-mock)
BuildRequires:  rubygem(rack)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
A session implementation for Rack.

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
( cd %{builddir}/test
%patch -P0 -p2
)

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
cp -a %{builddir}/test .
ruby -Itest -e 'Dir.glob "./test/**/spec_*.rb", &method(:require)'
)
%files -f %{oreon_filedir}/main.list
%files -n rubygem-rack-session-doc -f %{oreon_filedir}/rubygem-rack-session-doc.list

%changelog

%autochangelog
