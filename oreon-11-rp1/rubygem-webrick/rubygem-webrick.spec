%global source0_hash b42d3c94f166f3fb73d87e9b359def9b5836c426fc8beacf38f2184a21b2a989
%global gem_name webrick
Name: rubygem-%{gem_name}
Version: 1.9.1
Release:        3%{?dist}
Summary:        HTTP server toolkit
License: Ruby AND BSD-2-Clause
URL: https://github.com/ruby/webrick
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: %{gem_name}-%{version}-tests.txz
Patch0:  webrick-pr181-ruby40-IO-nread-removal.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygem(test-unit-ruby-core)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
WEBrick is an HTTP server toolkit that can be configured as an HTTPS server, a
proxy server, and a virtual-host server.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1
%patch -P0 -p1

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
ruby --verbose           \
     -Ilib:test:test/lib \
     -rhelper            \
     -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-webrick-doc -f %{oreon_filedir}/rubygem-webrick-doc.list

%changelog

%autochangelog
