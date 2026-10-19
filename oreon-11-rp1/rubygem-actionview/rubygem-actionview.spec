%global source1_hash 0419bf47f7357e6d3da85ff4ad797a3609dcf36ff44be496162ffbc901ff4232
%global source0_hash 5171946ff07d1e95bf3d805ad9425a89040a013dea11bb1f4cf604f108b1ce66
%global gem_name actionview
%bcond_with bootstrap
Name: rubygem-%{gem_name}
Version: 8.0.3
Release:        1%{?dist}
Summary:        Rendering framework putting the V in MVC (part of Rails)
License: MIT
URL: https://rubyonrails.org
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/rails/rails/archive/refs/tags/v8.0.3.tar.gz
%if %{without bootstrap}
%endif
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Simple, battle-tested conventions and helpers for building web pages.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}%{?prerelease} -b1
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

%build

gem build ../%{gem_name}-%{version}%{?prerelease}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{without bootstrap}
%check

ln -s %{gem_dir}/gems/activerecord-%{version}%{?prerelease}/ .%{gem_dir}/gems/activerecord
( cd .%{gem_instdir}
cp -a %{builddir}/test .
mkdir ../tools
touch ../tools/test_common.rb
touch ../tools/strict_warnings.rb
export RUBYLIB=$(pwd)/lib
find test -type f -name '*_test.rb' -print0 | \
  sort -z | \
  xargs -0 -n1 -i sh -c "echo '* Test file: {}'; ruby -Itest -- '{}' || exit 255"
)
%endif
%files -f %{oreon_filedir}/main.list
%files -n rubygem-actionview-doc -f %{oreon_filedir}/rubygem-actionview-doc.list

%changelog

%autochangelog
