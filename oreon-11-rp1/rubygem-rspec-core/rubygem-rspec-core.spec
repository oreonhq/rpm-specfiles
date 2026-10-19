%global source0_hash a8823c6411667b60a8bca135364351dda34cd55e44ff94c4be4633b37d828b2d
%global source1_hash none
%global	majorver	3.13.6
%global	rpmminorver	.%(echo %preminorver | sed -e 's|^\\.\\.*||')
%global	fullver	%{majorver}%{?preminorver}
%global	baserelease	3
%global	gem_name	rspec-core
%bcond_with bootstrap
%if ! 0%{?rhel} || (0%{?oreon} >= 11)
%bcond_without aruba
%endif
%undefine __brp_mangle_shebangs
Summary:        RSpec runner and formatters
Name:		rubygem-%{gem_name}
Version:	%{majorver}
Release:        3%{?dist}
License:	MIT
URL:		https://rspec.info
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	rubygem-%{gem_name}-%{version}-full.tar.gz
Source2:        rspec-related-create-full-tarball.sh
Patch0:		rubygem-rspec-core-3.10.1-Filter-content-of-usr-share-ruby.patch
Patch1:	rspec-core-pr282-ruby4_0-source_location.patch
%if %{without bootstrap}
%if %{with aruba}
%endif
%if 0%{?fedora} || 0%{?rhel} > 7 || (0%{?oreon} >= 11)
%endif
%endif
%if 0%{?fedora} >= 36 || (0%{?oreon} >= 11)
Recommends:	rubygem(rake)
%else
Requires:	rubygem(rake)
%endif
BuildArch:	noarch
# oreon:deps
BuildRequires:  git
BuildRequires:  glibc-langpack-en
BuildRequires:  rubygem(aruba)
BuildRequires:  rubygem(coderay)
BuildRequires:  rubygem(cucumber)
BuildRequires:  rubygem(drb)
BuildRequires:  rubygem(flexmock)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(mocha)
BuildRequires:  rubygem(rake)
BuildRequires:  rubygem(rr)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygem(thread_order)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Behaviour Driven Development for Ruby. RSpec runner and example groups.

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
mkdir -p %{buildroot}%{_prefix}
cp -a .%{_prefix}/* %{buildroot}%{_prefix}/
rm -f %{buildroot}%{gem_instdir}/{.document,.yardopts}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with bootstrap}
exit 0
%endif
LANG=C.UTF-8
%if %{without aruba}
truncate -s 0 spec/support/aruba_support.rb
find spec/integration -exec truncate -s 0 {} \;
%endif
sed -i '/backtrace_exclusion_patterns/ s/rspec-core/rspec-core-%{version}/' \
  spec/integration/{suite_hooks_errors,spec_file_load_errors}_spec.rb
sed -i spec/integration/spec_file_load_errors_spec.rb \
	-e '\@nicely handles load-time errors in user spec files@s| it | xit |'
sed -i spec/rspec/core/example_spec.rb \
	-e '\@defined.*RUBY_ENGINE.*truffleruby@s|^\(.*\)$|\1 \&\& false|'
sed -i spec/rspec/core_spec.rb \
	-e '\@only one thread local variable@s| it | xit |'
ruby -Ilib -S exe/rspec --seed 1 #33413
%if %{without aruba}
exit 0
%endif
sed -i features/command_line/init.feature \
       -e 's|^\([ \t]*\)\(Scenario: Accept and use the recommended settings\)|\1@broken\n\1\2|'
%if 0%{?fedora} >= 34 || 0%{?rhel} >= 9 || (0%{?oreon} >= 11)
for f in  \
	`# disabling tests failing with rr 1.2.1` \
	`# https://github.com/rspec/rspec-core/issues/2882` \
	features/mock_framework_integration/use_rr.feature \
	%{nil}
do
	mv $f ${f}.drop
done
%endif
sed -i cucumber.yml -e 's|~@wip|"not @wip"|'
sed -i features/support/require_expect_syntax_in_aruba_specs.rb -e 's|~@|not @|g'
sed -i features/support/diff_lcs_versions.rb -e 's|scenario.title|scenario.name|'
export RUBYOPT="-I$(pwd)/lib:$(ruby -e 'puts %w[rspec/support minitest test/unit].map {|r| Gem::Specification.find_by_path(r).full_require_paths}.join(?:)')"
export CUCUMBER_PUBLISH_QUIET=true
cucumber -v -f progress features/ || \
	cucumber -v -f progress features/ \
	--tag "not @broken" \
	`# Explicitly skip 'skip-when-diff-lcs-1.3' and '@ruby-2-7' test cases. While` \
	`# the conditions are correctly detected, the 'warning' called instead their` \
	`# execution is troublesome, possibly due to upstream using old Cucumber?` \
	--tag "not @skip-when-diff-lcs-1.3" \
%if 0%{?fedora} >= 36 || (0%{?oreon} >= 11)
	`# Cucumber 7 upgrades diff-lcs to 1.5` \
	--tag "not @skip-when-diff-lcs-1.4" \
%endif
	--tag "not @ruby-2-7" \
	%{nil}
%if 0%{?fedora} >= 34 || 0%{?rhel} >= 9 || (0%{?oreon} >= 11)
for f in  \
	features/mock_framework_integration/use_rr.feature \
	%{nil}
do
	mv ${f}.drop ${f}
done
%endif
%files -f %{oreon_filedir}/main.list
%files -n rubygem-rspec-core-doc -f %{oreon_filedir}/rubygem-rspec-core-doc.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.13.6-3
- Import
