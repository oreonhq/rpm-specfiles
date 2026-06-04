%global source0_hash none

%global	gem_name	rspec-support

%global	mainver	3.13.7
%undefine	prever

%global	baserelease	1
%global	prerpmver	%(echo "%{?prever}" | sed -e 's|\\.||g')

%bcond_with bootstrap

%undefine __brp_mangle_shebangs

Name:		rubygem-%{gem_name}
Version:	%{mainver}
Release:	%{?prever:0.}%{baserelease}%{?prever:.%{prerpmver}}%{?dist}

Summary:	Common functionality to Rspec series
# SPDX confirmed
License:	MIT
URL:		https://rspec.info
Source0:        https://rubygems.org/gems/%{gem_name}-%{mainver}%{?prever}.gem
# %%{SOURCE2} %%{name} %%{version}
Source1:	rubygem-%{gem_name}-%{version}-full.tar.gz
Source2:        rspec-related-create-full-tarball.sh
# Workaround tests wrt diff/lcs diff format
# Partially revert 3.13.2 -> 3.13.3 change
Patch0:	rubygem-rspec-support-3.13.3-diff_spec-format-revert.patch
Patch100:	rubygem-rspec-support-3.2.1-callerfilter-searchpath-regex.patch

#BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
%if %{without bootstrap}
BuildRequires:	rubygem(rspec)
BuildRequires:	rubygem(thread_order)
BuildRequires:	rubygem(bigdecimal)
# spec/rspec/support/spec/shell_out_spec.rb -> lib/rspec/support/spec/library_wide_checks.rb
# -> rake (%%check)
BuildRequires:	rubygem(rake)
BuildRequires:	git
%endif

BuildArch:		noarch

%description
`RSpec::Support` provides common functionality to `RSpec::Core`,
`RSpec::Expectations` and `RSpec::Mocks`. It is considered
suitable for internal use only at this time.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
Documentation for %{name}

%global	version_orig	%{version}
%global	version	%{version_orig}%{?prever}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -T -n %{gem_name}-%{version} -b 1
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%patch -P0 -p1
%patch -P100 -p1

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

%check
%if %{without bootstrap}
# UTF-8 is needed
LANG=C.UTF-8

# Test failure needs investigation...
FAILFILE=()
FAILTEST=()
%if 0
FAILFILE+=("spec/rspec/support/differ_spec.rb")
FAILTEST+=("copes with encoded strings")
%endif

for ((i = 0; i < ${#FAILFILE[@]}; i++)) {
	sed -i \
		-e "\@${FAILTEST[$i]}@s|do$|, :broken => true do|" \
		${FAILFILE[$i]}
}

export RUBYLIB=$(pwd)/lib
rspec spec/ || rspec --tag ~broken
%endif

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/LICENSE.md
%doc	%{gem_instdir}/Changelog.md
%doc	%{gem_instdir}/README.md

%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc	%{gem_docdir}

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.13.7-1
- Import
