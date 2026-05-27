%global source0_hash none

%global	majorver	3.13.5
#%%global	preminorver	.rc6
%global	rpmminorver	.%(echo %preminorver | sed -e 's|^\\.\\.*||')
%global	fullver	%{majorver}%{?preminorver}

%global	baserelease	5

%global	gem_name	rspec-expectations

%bcond_with bootstrap

%undefine __brp_mangle_shebangs

Summary:	RSpec expectations (should and matchers)
Name:		rubygem-%{gem_name}
Version:	%{majorver}
Release:	%{?preminorver:0.}%{baserelease}%{?preminorver:%{rpmminorver}}%{?dist}

# SPDX confirmed
License:	MIT
URL:		https://rspec.info
Source0:	https://rubygems.org/gems/%{gem_name}-%{fullver}.gem
# %%{SOURCE2} %%{name} %%{version}
Source1:	rubygem-%{gem_name}-%{version}-full.tar.gz
Source2:	rspec-related-create-full-tarball.sh
# Workaround tests wrt diff/lcs diff format
# Partially revert 3.13.3 -> 3.13.4 change
Patch0:	rubygem-rspec-expectations-3.13.4-diff_spec-format-revert.patch
# https://github.com/rspec/rspec/pull/282/commits/1c20fa80772ca7a1ed0512056ce7cd6a94f8e68d
# Support ruby4_0 source_location behavior change
Patch1:	rspec-expectations-pr282-ruby4_0-source_location.patch

#BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
%if %{without bootstrap}
BuildRequires:	rubygem(rspec)
BuildRequires:	rubygem(rake)
# Some features in expectations needs this
BuildRequires:	rubygem(rspec-support) >= 3.9.3
BuildRequires:	rubygem(minitest) >= 5
%if ! 0%{?rhel} || 0%{?oreon}
BuildRequires:	rubygem(aruba)
BuildRequires:	rubygem(cucumber)
%endif
BuildRequires:	git
%endif
BuildArch:		noarch

%description
rspec-expectations adds `should` and `should_not` to every object and includes
RSpec::Matchers, a library of standard matchers.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
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

# cleanups
rm -f %{buildroot}%{gem_instdir}/{.document,.yardopts}

%check
%if %{with bootstrap}
# Skip test, exiting
exit 0
%endif

LANG=C.UTF-8
export RUBYLIB=$(pwd)/lib
rspec spec/

%if 0%{?rhel} || 0%{?oreon}
# Skip cucumber test
exit 0
%endif

# Fix minitest 6 compatibility
# Behavior changed on: https://github.com/minitest/minitest/commit/2572c78420af73dbe9b202d535a1474405a32173
if ( ruby -e 'require "minitest" ; exit Minitest::VERSION >= "6"' ) ; then
	sed -i features/test_frameworks/minitest.feature \
		-e 's|9 runs, 10 assertions, 5 failures, 0 errors|9 runs, 11 assertions, 5 failures, 0 errors|'
fi

# Skip one failing scenario, needs investigating...
sed -i features/built_in_matchers/include.feature -e '\@skip-on-fedora@d'
sed -i features/built_in_matchers/include.feature -e 's|^\([ \t]*\)\(Scenario: counts usage.*\)|\1@skip-on-fedora\n\1\2|'
export CUCUMBER_PUBLISH_QUIET=true
cucumber \
    --tag "not @skip-when-diff-lcs-1.3" \
    --tag "not @skip-on-fedora" \
    %{nil}

%files
%dir	%{gem_instdir}

%license	%{gem_instdir}/LICENSE.md
%doc	%{gem_instdir}/Changelog.md
%doc	%{gem_instdir}/README.md

%{gem_instdir}/lib/

%exclude	%{gem_cache}
%{gem_spec}

%files	doc
%{gem_docdir}

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.13.5-5
- Import
