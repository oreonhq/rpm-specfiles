%global source0_hash de1ce33da8c99ab1d97871726cba75151113f117146becbe45aa85cb3dabee3f
%global gem_name netrc
Name: rubygem-%{gem_name}
Version: 0.11.0
Release:        1%{?dist}
Summary:        Library to read and write netrc files
License: MIT
URL: https://github.com/geemus/netrc
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: rubygem-netrc-0.11.0-missing-HOME-relevant-only-w-o-passwd-pw_dir.patch
Patch1: rubygem-netrc-0.11.0-augment-Dir-home-to-read-password-database-by-uid.patch
Patch2: rubygem-netrc-pr45-minitest6.patch
Requires: rubygem(io-console)
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygems-devel
# /oreon:deps
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

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ruby -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-netrc-doc -f %{oreon_filedir}/rubygem-netrc-doc.list

%changelog

%autochangelog
