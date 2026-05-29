%global source0_hash none

%global	majorver	3.13.8
#%%global	preminorver	.rc6
%global	rpmminorver	.%(echo %preminorver | sed -e 's|^\\.\\.*||')
%global	fullver	%{majorver}%{?preminorver}

%global	baserelease	1

%global	gem_name	rspec-mocks

%bcond_with bootstrap

%undefine __brp_mangle_shebangs

Summary:	RSpec's 'test double' framework (mocks and stubs)
Name:		rubygem-%{gem_name}
Version:	%{majorver}
Release:	%{?preminorver:0.}%{baserelease}%{?preminorver:%{rpmminorver}}%{?dist}

# SPDX confirmed
License:	MIT
URL:		https://rspec.info
Source0:        https://rubygems.org/gems/rspec-mocks-3.13.8%{?preminorver}.gem
# %%{SOURCE2} %%{name} %%{version}
Source1:	rubygem-%{gem_name}-%{version}-full.tar.gz
Source2:	rspec-related-create-full-tarball.sh
# https://github.com/rspec/rspec/pull/282/commits/939c4799993b7ff7e524fac701ae6490772ca6de
# Skip mock for ruby4_0 Kernel#inspect
Patch0:	rspec-mocks-pr282-skip-mock-for-ruby4_0-inspect.patch

BuildRequires:	rubygems-devel
%if %{without bootstrap}
# rspec
BuildRequires:	rubygem(rspec)
BuildRequires:	rubygem(rake)
%if %{undefined rhel} || 0%{?oreon}
# cucumber
BuildRequires:	rubygem(aruba)
BuildRequires:	rubygem(cucumber)
BuildRequires:	rubygem(minitest)
%endif
BuildRequires:	git
%endif
BuildArch:	noarch

%description
rspec-mocks provides a test-double framework for rspec including support
for method stubs, fakes, and message expectations.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version} -b 1
%patch -P0 -p2

# Cucumber 7 syntax change
sed -i cucumber.yml -e "s|~@wip|not @wip|"
sed -i features/support/disallow_certain_apis.rb -e "s|~@allow-old-syntax|not @allow-old-syntax|"

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
# Don't do actual check
exit 0
%endif

%if %{defined rhel} || 0%{?oreon}
# avoid aruba dep on RHEL, but tests fail if files are removed entirely
echo -n > spec/integration/rails_support_spec.rb
echo -n > spec/support/aruba.rb
%else
# Don't call bundler
sed -i spec/integration/rails_support_spec.rb \
	-e 's|bundle exec rspec|rspec|'
%endif

# library_wide_checks.rb needs UTF-8
LANG=C.UTF-8
export RUBYLIB=$(pwd)/lib
rspec spec/

%if 0%{?rhel} || 0%{?oreon}
# Don't do cucumber test
exit 0
%endif
export CUCUMBER_PUBLISH_QUIET=true
cucumber

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
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.13.8-1
- Import
