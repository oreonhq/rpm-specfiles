%global source1_hash 8f3640a703c23c9668d44ce64cf18c82be5622aa0b4e956bbf26b3e10fedf075
%global source0_hash 88fc26a40083a51015faa2ba02cbdc3605cb59f183cf0868f4fb3ac02900148f
%global gem_name backports
Name: rubygem-%{gem_name}
Version: 3.23.0
Release:        1%{?dist}
Summary:        Backports of Ruby features for older Ruby
License: MIT
URL: http://github.com/marcandre/backports
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/marcandre/backports/archive/refs/tags/v3.23.0.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Essential backports that enable many of the nice features of Ruby for earlier
versions.

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
mv test/ractor_extra_test.rb{,.skip}
ruby -Ilib -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
mv test/ractor_extra_test.rb{.skip,}
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-backports-doc -f %{oreon_filedir}/rubygem-backports-doc.list

%changelog

%autochangelog
