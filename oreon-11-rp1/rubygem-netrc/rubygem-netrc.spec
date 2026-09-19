%global source0_hash de1ce33da8c99ab1d97871726cba75151113f117146becbe45aa85cb3dabee3f

# Generated from netrc-0.7.gem by gem2rpm -*- rpm-spec -*-
%global gem_name netrc

Name: rubygem-%{gem_name}
Version: 0.11.0
Release: 20%{?dist}
Summary: Library to read and write netrc files
License: MIT
URL: https://github.com/geemus/netrc
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Fix `TestNetrc#test_missing_environment` test case.
# https://github.com/heroku/netrc/pull/47
Patch0: rubygem-netrc-0.11.0-missing-HOME-relevant-only-w-o-passwd-pw_dir.patch
# https://github.com/heroku/netrc/pull/53
Patch1: rubygem-netrc-0.11.0-augment-Dir-home-to-read-password-database-by-uid.patch
# https://github.com/heroku/netrc/pull/45
# Fix compatibility with minitest 6
Patch2: rubygem-netrc-pr45-minitest6.patch
# This is installed by default in Ruby upstream, but we need to require
# it explicitly.
# https://github.com/heroku/netrc/pull/16
Requires: rubygem(io-console)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildArch: noarch

%description
This library can read and update netrc files, preserving formatting including
comments and whitespace.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

%patch 0 -p1
%patch 1 -p1
%patch 2 -p1

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

%check
pushd .%{gem_instdir}
ruby -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Readme.md
%doc %{gem_instdir}/changelog.txt
%{gem_instdir}/data
%{gem_instdir}/test

%changelog
%autochangelog
