%global source1_hash 029581a9ccbfb8438bda0fdaabab255ec2f652c545e20a57c2ec54e13ff15a80
%global source0_hash c0ed99385f0625415c8f05bcae33fe649ed2952894a95ff8b08f26ca57ea5b3c
%global gem_name rubyzip
Name: rubygem-%{gem_name}
Version: 3.2.2
Release:        1%{?dist}
Summary:        A ruby module for reading and writing zip files
License: Ruby OR BSD-2-Clause
URL: http://github.com/rubyzip/rubyzip
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/rubyzip/rubyzip/archive/refs/tags/v3.2.2.tar.gz
Patch0:  rubyzip-3.2.2-minitest6.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(minitest-mock)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
A ruby module for reading and writing zip files.

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
(
cd %{_builddir}
%patch -P0 -p1
)

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
cp -a %{_builddir}/test .
FULL_ZIP64_TEST=1 ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-rubyzip-doc -f %{oreon_filedir}/rubygem-rubyzip-doc.list

%changelog

%autochangelog
