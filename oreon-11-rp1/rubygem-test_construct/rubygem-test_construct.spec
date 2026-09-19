%global source0_hash 7e0752ca445bdbe378506a9f20ceb9e822ea1bb1f9ef990dfc241f2a12cf079f

# Generated from test_construct-2.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name test_construct

Name: rubygem-%{gem_name}
Version: 2.0.2
Release: 13%{?dist}
Summary: Creates temporary files and directories for testing
License: MIT
URL: https://github.com/bhb/test_construct
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Fix Mocha 2.0+ compatibility.
# https://github.com/bhb/test_construct/pull/12
Patch0: rubygem-test_construct-2.0.2-Fix-compatibility-with-Mocha-2.0.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(rspec)
BuildArch: noarch

%description
Creates temporary files and directories for testing.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

%patch 0 -p1

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'

# The specs seem to be outdated
#rspec examples
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
%{gem_instdir}/test
%{gem_instdir}/test_construct.gemspec

%changelog
%autochangelog
