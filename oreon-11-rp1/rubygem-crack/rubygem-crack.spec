%global source1_hash 69f390141028d7397a3031aa712ba8236cb4ce81e6d73de6afc908d217daeae0
%global source0_hash ff4a10390cd31d66440b7524eb1841874db86201d5b70032028553130b6d4c7e
%global gem_name crack
Name: rubygem-%{gem_name}
Version: 1.0.1
Release:        1%{?dist}
Summary:        Really simple JSON and XML parsing, ripped from Merb and Rails
License: MIT
URL: https://github.com/jnunemaker/crack
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/jnunemaker/crack/archive/refs/tags/v1.0.1.tar.gz
BuildArch: noarch
Epoch: 1
# oreon:deps
BuildRequires:  rubygem(bigdecimal)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(rexml)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Really simple JSON and XML parsing, ripped from Merb and Rails.

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
ln -s %{builddir}/test test
ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
)
%files -f %{oreon_filedir}/main.list
%files -n rubygem-crack-doc -f %{oreon_filedir}/rubygem-crack-doc.list

%changelog

%autochangelog
