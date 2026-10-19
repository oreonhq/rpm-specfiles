%global source1_hash fa162f81890e03e6b56da10c0e0bf2857f04854a7b4809c3f25c2b7e527fd608
%global source0_hash 162499dc0bba1e66d334273a059f207a61981cc8cc69d2ca743594e7886d080f
%global gem_name regexp_property_values
Name: rubygem-%{gem_name}
Version: 1.0.0
Release:        1%{?dist}
Summary:        Inspect property values supported by Ruby's regex engine
License: MIT
URL: https://github.com/jaynetics/regexp_property_values
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/jaynetics/regexp_property_values/archive/refs/tags/v1.0.0.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
This small library lets you see which property values are supported by the
regular expression engine of the Ruby version you are running, and what they
match.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{gem_extdir_mri}/%{gem_name}
cp -a .%{gem_extdir_mri}/gem.build_complete %{buildroot}%{gem_extdir_mri}/
cp -a .%{gem_extdir_mri}/%{gem_name}/*.so %{buildroot}%{gem_extdir_mri}/%{gem_name}/
rm -rf %{buildroot}%{gem_instdir}/ext/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ln -s %{_builddir}/spec .
sed -e '/^\s*require..character_set.$/ i skip' \
    -i spec/regexp_property_values/value_spec.rb
sed -i '/^require..bundler./ s/^/#/g' spec/spec_helper.rb
rspec -I$(dirs +1)/%{gem_extdir_mri} spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-regexp_property_values-doc -f %{oreon_filedir}/rubygem-regexp_property_values-doc.list

%changelog

%autochangelog
