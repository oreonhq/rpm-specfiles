%global source0_hash 414ca1446ef8292d91bd2ad7f39ac9d6ce78a7fc4f22101c86b63b227d93ca0c

# Generated from fog-libvirt-0.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name fog-libvirt

Name: rubygem-%{gem_name}
Version: 0.13.1
Release: 4%{?dist}
Summary: Module for the 'fog' gem to support libvirt
License: MIT
URL: http://github.com/fog/fog-libvirt
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: %{_bindir}/shindo
BuildRequires: rubygem(ruby-libvirt)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(fog-core)
BuildRequires: rubygem(fog-xml)
BuildRequires: rubygem(fog-json)
BuildArch: noarch

%description
This library can be used as a module for 'fog' or as standalone libvirt
provider.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Run the test suite
%check
pushd .%{gem_instdir}
FOG_MOCK=true shindo tests
ruby -Iminitests -e "Dir.glob './minitests/**/*_test.rb', &method(:require)"
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTORS.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/fog-libvirt.gemspec
%{gem_instdir}/tests
%{gem_instdir}/minitests

%changelog
%autochangelog
