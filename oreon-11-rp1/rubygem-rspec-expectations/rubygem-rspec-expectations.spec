%global source0_hash 33a4d3a1d95060aea4c94e9f237030a8f9eae5615e9bd85718fe3a09e4b58836
%global source1_hash none
%global	majorver	3.13.5
%global	rpmminorver	.%(echo %preminorver | sed -e 's|^\\.\\.*||')
%global	fullver	%{majorver}%{?preminorver}
%global	baserelease	5
%global	gem_name	rspec-expectations
%bcond_with bootstrap
%undefine __brp_mangle_shebangs
Summary:        RSpec expectations (should and matchers)
Name:		rubygem-%{gem_name}
Version:	%{majorver}
Release:        1%{?dist}
License:	MIT
URL:		https://rspec.info
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	rubygem-%{gem_name}-%{version}-full.tar.gz
Source2:        rspec-related-create-full-tarball.sh
Patch0:	rubygem-rspec-expectations-3.13.4-diff_spec-format-revert.patch
Patch1:	rspec-expectations-pr282-ruby4_0-source_location.patch
%if %{without bootstrap}
%if ! 0%{?rhel} || (0%{?oreon} >= 11)
%endif
%endif
BuildArch:		noarch
# oreon:deps
BuildRequires:  rubygems-devel
# /oreon:deps
%description
rspec-expectations adds `should` and `should_not` to every object and includes
RSpec::Matchers, a library of standard matchers.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
%description	doc
This package contains documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%setup -q -T -n %{gem_name}-%{version} -b 1

%patch -P0 -p1
%patch -P1 -p2

gem specification %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build

gem build %{gem_name}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
rm -f %{buildroot}%{gem_instdir}/{.document,.yardopts}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with bootstrap}
exit 0
%endif
LANG=C.UTF-8
export RUBYLIB=$(pwd)/lib
rspec spec/
%if 0%{?rhel} || (0%{?oreon} >= 11)
exit 0
%endif
if ( ruby -e 'require "minitest" ; exit Minitest::VERSION >= "6"' ) ; then
	sed -i features/test_frameworks/minitest.feature \
		-e 's|9 runs, 10 assertions, 5 failures, 0 errors|9 runs, 11 assertions, 5 failures, 0 errors|'
fi
sed -i features/built_in_matchers/include.feature -e '\@skip-on-fedora@d'
sed -i features/built_in_matchers/include.feature -e 's|^\([ \t]*\)\(Scenario: counts usage.*\)|\1@skip-on-fedora\n\1\2|'
export CUCUMBER_PUBLISH_QUIET=true
cucumber \
    --tag "not @skip-when-diff-lcs-1.3" \
    --tag "not @skip-on-fedora" \
    %{nil}
%files -f %{oreon_filedir}/main.list
%files -n rubygem-rspec-expectations-doc -f %{oreon_filedir}/rubygem-rspec-expectations-doc.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.13.5-5
- Import
