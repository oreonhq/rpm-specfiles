%global source0_hash 162499dc0bba1e66d334273a059f207a61981cc8cc69d2ca743594e7886d080f

# Generated from regexp_property_values-1.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name regexp_property_values

Name: rubygem-%{gem_name}
Version: 1.0.0
Release: 18%{?dist}
Summary: Inspect property values supported by Ruby's regex engine
License: MIT
URL: https://github.com/jaynetics/regexp_property_values
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Spec is not packaged with gem
# You can check it like so:
# git clone --no-checkout https://github.com/jaynetics/regexp_property_values.git
# cd regexp_property_values && git archive -v -o regexp_property_values-1.0.0-spec.txz v1.0.0 spec
Source1: %{gem_name}-%{version}-spec.txz

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel >= 2.0.0
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc
BuildRequires: rubygem(rspec)

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

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/spec .

# We don't have the dependency in Fedora
sed -e '/^\s*require..character_set.$/ i skip' \
    -i spec/regexp_property_values/value_spec.rb

# Don't use bundler for tests
sed -i '/^require..bundler./ s/^/#/g' spec/spec_helper.rb
rspec -I$(dirs +1)/%{gem_extdir_mri} spec
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/regexp_property_values.gemspec

%changelog
%autochangelog
