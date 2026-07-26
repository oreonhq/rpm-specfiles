%global source0_hash 5da9c3b7674d851e25e8ccefc08d0c20831e383c46234f544e0fa89d16b83494

# Generated from rackup-2.2.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rackup

Name: rubygem-%{gem_name}
Version: 2.2.1
Release: 6%{?dist}
Summary: A general server command for Rack applications
License: MIT
URL: https://github.com/rack/rackup
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/rack/rackup.git && cd rackup
# git archive -v -o rackup-2.2.1-tests.tar.gz v2.2.1 test/
Source1: %{gem_name}-%{version}-tests.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.5
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(minitest-global_expectations)
BuildRequires: rubygem(rack)
BuildRequires: rubygem(webrick)
BuildArch: noarch

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

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
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

%check
( cd .%{gem_instdir}
cp -a %{builddir}/test .

ruby -Ilib:test -e 'Dir.glob "./test/**/spec_*.rb", &method(:require)'
)

%files
%dir %{gem_instdir}
%{_bindir}/rackup
%{gem_instdir}/bin
%{gem_libdir}
%license %{gem_instdir}/license.md
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/readme.md
%doc %{gem_instdir}/releases.md
%doc %{gem_instdir}/security.md

%changelog
%autochangelog
