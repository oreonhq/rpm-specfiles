%global source1_hash bb71da71f11488706c769adeeee8104f8768eff45845f1af832830640dd6bb35
%global source0_hash fdcfcfa33cc52e93c4308d40e4090a5d4ea279e160a7f6af988260fa970e0bee
%global gem_name marcel
Name: rubygem-%{gem_name}
Version: 1.1.0
Release:        1%{?dist}
Summary:        Simple mime type detection using magic numbers, file names, and extensions
License: MIT AND Apache-2.0
URL: https://github.com/rails/marcel
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/rails/marcel/archive/refs/tags/v1.1.0.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(rack)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Simple mime type detection using magic numbers, file names, and extensions.

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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

( cd .%{gem_instdir}
ln -s %{builddir}/test .
ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
)
%files -f %{oreon_filedir}/main.list
%files -n rubygem-marcel-doc -f %{oreon_filedir}/rubygem-marcel-doc.list

%changelog

%autochangelog
