%global source1_hash 21738b8d51d96c972381930afbf74bd0b4a8bbdc4f2ffa1dd7ac27a07a81833e
%global source0_hash 4fce100c68af588ff91b8ba90a0bb3f0466f06c909f21a32f4962059140ba61b
%global gem_name multi_xml
Name: rubygem-%{gem_name}
Version: 0.7.1
Release:        6%{?dist}
Summary:        A generic swappable back-end for XML parsing
License: MIT
URL: https://github.com/sferik/multi_xml
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/sferik/multi_xml/archive/refs/tags/v0.7.1.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(bigdecimal)
BuildRequires:  rubygem(nokogiri)
BuildRequires:  rubygem(ox)
BuildRequires:  rubygem(rexml)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Provides swappable XML backends utilizing LibXML, Nokogiri, Ox, or REXML.

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

# ref: https://github.com/sferik/multi_xml/issues/72
# ruby4.0 bumps bigdecimal to 4.0
sed -i ../%{gem_name}-%{version}.gemspec \
        -e '\@add_runtime_dependency.*bigdecimal@s|~> 3\.1|>= 3.1|'

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
ln -s %{_builddir}/spec spec
sed -i '/simplecov/,/^end$/ s/^/#/' spec/helper.rb
rspec spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-multi_xml-doc -f %{oreon_filedir}/rubygem-multi_xml-doc.list

%changelog

%autochangelog
