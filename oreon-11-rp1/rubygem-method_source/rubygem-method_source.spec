%global source0_hash 181301c9c45b731b4769bc81e8860e72f9161ad7d66dd99103c9ab84f560f5c5

# Generated from method_source-0.7.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name method_source

Name: rubygem-%{gem_name}
Version: 1.1.0
Release: 4%{?dist}
Summary: Retrieve the source code for a method
License: MIT
URL: https://github.com/banister/method_source/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Fix compatibility with Prism parser in Ruby 3.4
# https://github.com/banister/method_source/pull/84
Patch0: rubygem-method_source-1.1.0-Update-error-message-expectations-to-work-on-MRI-with-Prism.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildArch: noarch

%description
Retrieve the source code for a method.

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
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
rspec spec
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.markdown
%{gem_instdir}/Rakefile
%{gem_instdir}/method_source.gemspec
%{gem_instdir}/spec

%changelog
%autochangelog
