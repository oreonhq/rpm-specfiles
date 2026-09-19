%global source0_hash 9bb940467b016574115c8ca5a8935c99d783f597afd6b92784d7acab2fb29995

# Generated from minitest-global_expectations-1.0.2.gem by gem2rpm -*- rpm-spec -*-
%global	gem_name	minitest-global_expectations

Name:		rubygem-%{gem_name}
Version:	1.0.2
Release:	2%{?dist}

Summary:	Support minitest expectation methods for all objects
License:	MIT
URL:		https://github.com/jeremyevans/minitest-global_expectations
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	%{gem_name}-%{version}-tests.tar.gz
# Source1 is created by $ bash %%{SOURCE1} %%{version}
Source2:	%{gem_name}-create-missing-test-files.sh

BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	rubygem(minitest)
BuildArch:		noarch

%description
minitest-global_expectations allows you to keep using simple code in your
minitest specs, without having to wrap every single object you are calling
an expectation method on with an underscore.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

rm -f %{buildroot}%{gem_cache}

%check
export RUBYLIB=$(pwd)/lib
ruby ./test/minitest_global_expectations_test.rb

%files
%dir %{gem_instdir}
%license	%{gem_instdir}/MIT-LICENSE
%doc	%{gem_instdir}/README.rdoc

%{gem_libdir}
%{gem_spec}

%files doc
%doc	%{gem_docdir}
%doc	%{gem_instdir}/CHANGELOG

%changelog
%autochangelog
