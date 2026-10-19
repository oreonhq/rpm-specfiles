%global source1_hash 1ef35c71775d8ec7ed5573d478a5c508ed2f40434d45c6fffa5a787ba6f8fcba
%global source0_hash 700e6413ad4bb954bb63547fa098dddf7b0ebe75b40cc6f93b8d54255b173844
%global gem_name useragent
Name: rubygem-%{gem_name}
Version: 0.16.11
Release:        1%{?dist}
Summary:        HTTP User Agent parser
License: MIT
URL: https://github.com/gshutler/useragent
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/gshutler/useragent/archive/refs/tags/v0.16.11.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(ostruct)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
HTTP User Agent parser.

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
ln -s %{builddir}/spec .
rspec spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-useragent-doc -f %{oreon_filedir}/rubygem-useragent-doc.list

%changelog

%autochangelog
