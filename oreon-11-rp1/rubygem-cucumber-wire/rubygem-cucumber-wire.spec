%global source0_hash 699dcde817ae0e98826606e5f8537eb3755d0f97c75806ee9193319a606ebede

# Generated from cucumber-wire-0.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name cucumber-wire

%bcond_with bootstrap

Name: rubygem-%{gem_name}
Version: 6.2.1
Release: 6%{?dist}
Summary: Wire protocol for Cucumber
License: MIT
URL: http://cucumber.io
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone --no-checkout https://github.com/cucumber/cucumber-ruby-wire.git
# git -C cucumber-ruby-wire archive -v -o rubygem-cucumber-wire-6.2.1-features.txz v6.2.1 features/
Source1: %{name}-%{version}-features.txz
# Support quote in backtrace for Ruby 3.4
# https://github.com/cucumber/cucumber-ruby-wire/pull/72
Patch0: rubygem-cucumber-wire-7.0.0-Support-quote-in-backtrace-for-Ruby-3-4.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
%if %{without bootstrap}
# Dependencies for %%check
BuildRequires: rubygem(aruba)
BuildRequires: rubygem(cucumber)
BuildRequires: rubygem(rspec)
%endif
BuildArch: noarch

%description
Wire protocol for Cucumber.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1

(
cd %{builddir}
%patch 0 -p1
)

# Relax the dependency.
%gemspec_remove_dep -g cucumber-cucumber-expressions "~> 14.0", ">= 14.0.0"
%gemspec_add_dep -g cucumber-cucumber-expressions ">= 14.0"

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%if %{without bootstrap}
%check
pushd .%{gem_instdir}

rspec -Ilib spec

ln -s %{_builddir}/features features

# Ensure the current version of cucumber-wire is used in place of system one,
# pulled in as a Cucumber dependency.
RUBYOPT="-I$(pwd)/lib" cucumber --format progress --publish-quiet

popd
%endif

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%license %{gem_instdir}/LICENSE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/spec

%changelog
%autochangelog
