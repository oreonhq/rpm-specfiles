%global source0_hash 0640e5570872aafefd79867901deeeeb40b0c9875a36b983d85f54fb7381c47c
%global	gem_name	rspec-support
%global	mainver	3.13.7
%undefine	prever
%global	baserelease	1
%global	prerpmver	%(echo "%{?prever}" | sed -e 's|\\.||g')
%bcond_with bootstrap
%undefine __brp_mangle_shebangs
Name:		rubygem-%{gem_name}
Version:	%{mainver}
Release:        1%{?dist}
Summary:        Common functionality to Rspec series
License:	MIT
URL:		https://rspec.info
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	rubygem-%{gem_name}-%{version}-full.tar.gz
Source2:        rspec-related-create-full-tarball.sh
Patch0:	rubygem-rspec-support-3.13.3-diff_spec-format-revert.patch
Patch100:	rubygem-rspec-support-3.2.1-callerfilter-searchpath-regex.patch
%if %{without bootstrap}
%endif
BuildArch:		noarch
# oreon:deps
BuildRequires:  git
BuildRequires:  rubygem(bigdecimal)
BuildRequires:  rubygem(rake)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(thread_order)
BuildRequires:  rubygems-devel
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{without bootstrap}
LANG=C.UTF-8
FAILFILE=()
FAILTEST=()
for ((i = 0; i < ${#FAILFILE[@]}; i++)) {
	sed -i \
		-e "\@${FAILTEST[$i]}@s|do$|, :broken => true do|" \
		${FAILFILE[$i]}
}
export RUBYLIB=$(pwd)/lib
rspec spec/ || rspec --tag ~broken
%endif
%files -f %{oreon_filedir}/main.list
%files -n rubygem-rspec-support-doc -f %{oreon_filedir}/rubygem-rspec-support-doc.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.13.7-1
- Import
