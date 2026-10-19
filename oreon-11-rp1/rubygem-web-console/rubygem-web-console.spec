%global source1_hash 85140749adc3c0e67ec98a52ad98c362f042619c0243abd12a94e9bdafc397b0
%global source0_hash e8f05057a83d6d305d5941fb828d13a25e9aa9b0f3a550f01c308711885433c3
%global gem_name web-console
Name: rubygem-%{gem_name}
Version: 4.2.0
Release:        1%{?dist}
Summary:        A debugging tool for your Ruby on Rails applications
License: MIT
URL: https://github.com/rails/web-console
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/rails/web-console/archive/refs/tags/v4.2.0.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(activemodel)
BuildRequires:  rubygem(bindex)
BuildRequires:  rubygem(mocha)
BuildRequires:  rubygem(railties)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
A debugging tool for your Ruby on Rails applications.

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

pushd .%{gem_instdir}
ln -s %{_builddir}/test test
sed -i '/[Ss]imple[Cc]ov/ s/^/#/' test/test_helper.rb
sed -i '/^Bundler.require/ s/^/#/' test/dummy/config/application.rb
ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-web-console-doc -f %{oreon_filedir}/rubygem-web-console-doc.list

%changelog

%autochangelog
