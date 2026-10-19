%global source1_hash d884bb53f5bb8cccfcd8722df41187dffe744f5fdd9813cded8ddf2f32c144f7
%global source0_hash 699dcde817ae0e98826606e5f8537eb3755d0f97c75806ee9193319a606ebede
%global gem_name cucumber-wire
%bcond_with bootstrap
Name: rubygem-%{gem_name}
Version: 6.2.1
Release:        1%{?dist}
Summary:        Wire protocol for Cucumber
License: MIT
URL: http://cucumber.io
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/cucumber/cucumber-ruby-wire/archive/refs/tags/v6.2.1.tar.gz
Patch0: rubygem-cucumber-wire-7.0.0-Support-quote-in-backtrace-for-Ruby-3-4.patch
%if %{without bootstrap}
%endif
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
# /oreon:deps
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
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{without bootstrap}
%check

pushd .%{gem_instdir}
rspec -Ilib spec
ln -s %{_builddir}/features features
RUBYOPT="-I$(pwd)/lib" cucumber --format progress --publish-quiet
popd
%endif
%files -f %{oreon_filedir}/main.list
%files -n rubygem-cucumber-wire-doc -f %{oreon_filedir}/rubygem-cucumber-wire-doc.list

%changelog

%autochangelog
