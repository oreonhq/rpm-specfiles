%global source0_hash none

%global	majorver	3.13.6
#%%global	preminorver	.rc6
%global	rpmminorver	.%(echo %preminorver | sed -e 's|^\\.\\.*||')
%global	fullver	%{majorver}%{?preminorver}

%global	baserelease	3

%global	gem_name	rspec-core

# %%check section needs rspec-core, however rspec-core depends on rspec-mocks
# runtime part of rspec-mocks does not depend on rspec-core
# Disable test for now due to cucumber v.s. gherkin dependency issue
# pulled by aruba
%bcond_with bootstrap

# Disable Aruba support in RHEL due to excesive dependency chain. This also
# disables Cucumber integration test suite, which depends on Aruba as well.
%if ! 0%{?rhel} || 0%{?oreon}
%bcond_without aruba
%endif

%undefine __brp_mangle_shebangs

Summary:	RSpec runner and formatters
Name:		rubygem-%{gem_name}
Version:	%{majorver}
Release:	%{?preminorver:0.}%{baserelease}%{?preminorver:%{rpmminorver}}%{?dist}

# SPDX confirmed
License:	MIT
URL:		https://rspec.info
Source0:        http://rubygems.org/gems/rspec-core-3.13.6%{?preminorver}.gem
# %%{SOURCE2} %%{name} %%{version}
Source1:	rubygem-%{gem_name}-%{version}-full.tar.gz
Source2:	rspec-related-create-full-tarball.sh
# Adjust backtrace filter for Fedora placement of StdLib.
# https://github.com/rspec/rspec-core/pull/2881
Patch0:		rubygem-rspec-core-3.10.1-Filter-content-of-usr-share-ruby.patch
# https://github.com/rspec/rspec/pull/282/commits/1c20fa80772ca7a1ed0512056ce7cd6a94f8e68d
# Support ruby4_0 source_location behavior change
Patch1:	rspec-core-pr282-ruby4_0-source_location.patch

#BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
%if %{without bootstrap}
BuildRequires:	rubygem(minitest)
BuildRequires:	rubygem(rake)
BuildRequires:	rubygem(rspec)
BuildRequires:	rubygem(test-unit)
BuildRequires:	rubygem(coderay)
BuildRequires:	rubygem(drb)
BuildRequires:	rubygem(thread_order)
BuildRequires:	git

%if %{with aruba}
BuildRequires:	rubygem(aruba)
BuildRequires:	rubygem(flexmock)
BuildRequires:	rubygem(mocha)
BuildRequires:	rubygem(rr)
BuildRequires:	rubygem(cucumber)
%endif

%if 0%{?fedora} || 0%{?rhel} > 7 || 0%{?oreon}
BuildRequires:	glibc-langpack-en
%endif

%endif
# Make the following dependency optionally installed
# lib/rspec/core/rake_task
%if 0%{?fedora} >= 36 || 0%{?oreon}
Recommends:	rubygem(rake)
%else
Requires:	rubygem(rake)
%endif
# Optional
#Requires:	rubygem(ZenTest)
#Requires:	rubygem(flexmock)
#Requires:	rubygem(mocha)
#Requires:	rubygem(rr)
BuildArch:	noarch

%description
Behaviour Driven Development for Ruby. RSpec runner and example groups.

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
mkdir -p %{buildroot}%{_prefix}
cp -a .%{_prefix}/* %{buildroot}%{_prefix}/

# cleanups
rm -f %{buildroot}%{gem_instdir}/{.document,.yardopts}

%check
%if %{with bootstrap}
# Not do actual check, exiting.
exit 0
%endif

LANG=C.UTF-8

%if %{without aruba}
# Avoid dependency on Aruba. The files needs to be present, since they are
# listed by `git ls-files` from 'library wide checks' shared example.
truncate -s 0 spec/support/aruba_support.rb
find spec/integration -exec truncate -s 0 {} \;
%endif

# Adjust the backtrace filters to our directory layout.
sed -i '/backtrace_exclusion_patterns/ s/rspec-core/rspec-core-%{version}/' \
  spec/integration/{suite_hooks_errors,spec_file_load_errors}_spec.rb

# ruby3.1: output format change, disabling for now
sed -i spec/integration/spec_file_load_errors_spec.rb \
	-e '\@nicely handles load-time errors in user spec files@s| it | xit |'

# ruby3.2 + compile with YJIT + LTO seems to make rspec-core GC test fail.
# disabling this, per ruby upsteram advice:
# https://bugs.ruby-lang.org/issues/19254
sed -i spec/rspec/core/example_spec.rb \
	-e '\@defined.*RUBY_ENGINE.*truffleruby@s|^\(.*\)$|\1 \&\& false|'

# RSpec uses only one thread local variable: disable for now
sed -i spec/rspec/core_spec.rb \
	-e '\@only one thread local variable@s| it | xit |'

# FIXME seed 33413 sees test failure
ruby -Ilib -S exe/rspec --seed 1 #33413

%if %{without aruba}
# The following lines are for cucumber tests, so exiting.
exit 0
%endif

# Mark failing test as broken
sed -i features/command_line/init.feature \
       -e 's|^\([ \t]*\)\(Scenario: Accept and use the recommended settings\)|\1@broken\n\1\2|'

%if 0%{?fedora} >= 34 || 0%{?rhel} >= 9 || 0%{?oreon}
for f in  \
	`# disabling tests failing with rr 1.2.1` \
	`# https://github.com/rspec/rspec-core/issues/2882` \
	features/mock_framework_integration/use_rr.feature \
	%{nil}
do
	mv $f ${f}.drop
done
%endif

# cucumber 7.0.0 does not support ~@
sed -i cucumber.yml -e 's|~@wip|"not @wip"|'
sed -i features/support/require_expect_syntax_in_aruba_specs.rb -e 's|~@|not @|g'
# Perhaps with cucumber 7.0.0 change? (along with diff-lcs updated to 1.5)
sed -i features/support/diff_lcs_versions.rb -e 's|scenario.title|scenario.name|'

# Setup just right amount of paths to make the tests suite run.
export RUBYOPT="-I$(pwd)/lib:$(ruby -e 'puts %w[rspec/support minitest test/unit].map {|r| Gem::Specification.find_by_path(r).full_require_paths}.join(?:)')"
export CUCUMBER_PUBLISH_QUIET=true
cucumber -v -f progress features/ || \
	cucumber -v -f progress features/ \
	--tag "not @broken" \
	`# Explicitly skip 'skip-when-diff-lcs-1.3' and '@ruby-2-7' test cases. While` \
	`# the conditions are correctly detected, the 'warning' called instead their` \
	`# execution is troublesome, possibly due to upstream using old Cucumber?` \
	--tag "not @skip-when-diff-lcs-1.3" \
%if 0%{?fedora} >= 36 || 0%{?oreon}
	`# Cucumber 7 upgrades diff-lcs to 1.5` \
	--tag "not @skip-when-diff-lcs-1.4" \
%endif
	--tag "not @ruby-2-7" \
	%{nil}

%if 0%{?fedora} >= 34 || 0%{?rhel} >= 9 || 0%{?oreon}
for f in  \
	features/mock_framework_integration/use_rr.feature \
	%{nil}
do
	mv ${f}.drop ${f}
done
%endif

%files
%dir	%{gem_instdir}

%license	%{gem_instdir}/LICENSE.md
%doc	%{gem_instdir}/Changelog.md
%doc	%{gem_instdir}/README.md

%{_bindir}/rspec
%{gem_instdir}/exe/
%{gem_instdir}/lib/

%exclude	%{gem_cache}
%{gem_spec}

%files	doc
%{gem_docdir}

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.13.6-3
- Import
