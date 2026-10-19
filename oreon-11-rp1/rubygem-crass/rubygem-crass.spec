%global source0_hash d1e156128a69a165b79c5f05fec7a6a8d7a7dd824c776abd7c2f71f98cfffd2e
%global gem_name crass
Name: rubygem-%{gem_name}
Version: 1.0.4
Release:        1%{?dist}
Summary:        CSS parser based on the CSS Syntax Level 3 spec
License: MIT
URL: https://github.com/rgrove/crass/
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: rubygem-crass-1.0.6-Fix-compatibility-with-Minitest-5.19.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Crass is a pure Ruby CSS parser based on the CSS Syntax Level 3 spec.

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
%files -n rubygem-crass-doc -f %{oreon_filedir}/rubygem-crass-doc.list

%changelog

%autochangelog
