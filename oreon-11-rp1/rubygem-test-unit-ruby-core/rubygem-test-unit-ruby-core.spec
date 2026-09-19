%global source0_hash 679a0dacf4aaf8792016516d24c1a07f43230d99ae25d542cfca2e240ac76ac9

%global	gem_name test-unit-ruby-core

Name:		rubygem-%{gem_name}
Version:	1.0.14
Release:	2%{?dist}

Summary:	Additional test assertions for Ruby standard libraries
# SPDX confirmed
License:	BSD-2-Clause OR Ruby
URL:		https://github.com/ruby/test-unit-ruby-core

Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	%{gem_name}-%{version}-additional.tar.gz
# Source1 is created by $ bash %%SOURCE2 %%version
Source2:	test-unit-ruby-core-create-missing-files.sh
BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel

BuildArch:		noarch

%description
Additional test assertions for Ruby standard libraries.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
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

# Install additional files
cp -a \
	BSDL \
	COPYING \
	README.md \
	%{buildroot}%{gem_instdir}/

rm -f %{buildroot}%{gem_cache}

%check
# No available test suite currently
exit 0

%files
%dir	%{gem_instdir}
%doc	%{gem_instdir}/README.md
%license	%{gem_instdir}/BSDL
%license	%{gem_instdir}/COPYING
%{gem_libdir}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
%autochangelog
