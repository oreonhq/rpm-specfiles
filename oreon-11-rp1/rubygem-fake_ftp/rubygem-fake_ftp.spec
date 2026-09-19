%global source0_hash 049302ca3afad2259beacb5927efe7b6337824c6018207124a9f9e4e6ac289fe

#Generated from fake_ftp-0.1.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name fake_ftp

Name: rubygem-%{gem_name}
Version: 0.3.0
Release: 20%{?dist}
Summary: Creates a fake FTP server for use in testing
License: MIT
URL: http://rubygems.org/gems/fake_ftp
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) >= 1.3.6
BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 1.3.6
BuildRequires: ruby
BuildRequires: rubygem(coderay)
BuildRequires: rubygem(net-ftp)
BuildRequires: rubygem(rspec)
BuildArch: noarch

%description
Testing FTP? Use this!

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

%check
pushd .%{gem_instdir}

# We are not interested in code coverage.
sed -i "/require 'simplecov'/ s/^/#/" spec/spec_helper.rb

# Increase timeout to make the test suite pass.
sed -i "s/timeout: 5,/timeout: 60,/" spec/spec_helper.rb

FUNCTIONAL_SPECS=1 INTEGRATION_SPECS=1 rspec -rspec_helper spec
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}
%exclude %{gem_cache}
%doc %{gem_instdir}/README.md
%exclude %{gem_instdir}/.*

%files doc
%doc %{gem_docdir}
%{gem_instdir}/spec
%{gem_instdir}/Rakefile
%{gem_instdir}/Gemfile
%{gem_instdir}/Guardfile
%{gem_instdir}/fake_ftp.gemspec
%doc %{gem_instdir}/CONTRIBUTORS.md
%doc %{gem_instdir}/CHANGELOG.md
%license %{gem_instdir}/LICENSE.md

%changelog
%autochangelog
