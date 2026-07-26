%global source0_hash 4b45d444094d263d8b664289245ac22f6d12a4713e13143841563662681b48b7

# Generated from sass-3.1.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sass

Name: rubygem-%{gem_name}
Version: 3.7.4
Release: 15%{?dist}
Summary: A powerful but elegant CSS compiler that makes CSS fun again
License: MIT
URL: http://sass-lang.com/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/sass/ruby-sass.git
# cd ruby-sass && git checkout 3.7.4
# tar czvf sass-3.7.4-tests.tgz test/ Rakefile
Source1: %{gem_name}-%{version}-tests.tgz

# Use listen as a depencency instead of sass-listen.
# sass-listen is a fork from original listen v3.0 branch to support Ruby <= 2.1.
# https://github.com/sass/ruby-sass/pull/65
Patch0: rubygem-sass-3.5.6-use-listen.patch
# Note that patches below are not going to be submitted upstream
# because rubygem-sass is obsoleted by the upstream
# Remove warnings for literal string being frozen in ruby3.4
Patch1: rubygem-sass-3.7.4-Remove-warnings-for-literal-string-being-frozen-in-r.patch
# Support caller format change in ruby3.4
Patch2: rubygem-sass-3.7.4-Support-caller-format-change-in-ruby3.4.patch
# Support for method owner in backtrace introduced in Ruby 4.0
# https://bugs.ruby-lang.org/issues/21698
Patch3: rubygem-sass-3.7.4-Backtrace-now-includes-method-owner.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(listen)
BuildRequires: rubygem(minitest)
BuildArch: noarch

%description
Sass makes CSS fun again. Sass is an extension of CSS, adding
nested rules, variables, mixins, selector inheritance, and more.
It's translated to well-formatted, standard CSS using the
command line tool or a web-framework plugin.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -a 1

%gemspec_remove_dep -g sass-listen -s ../%{gem_name}-%{version}.gemspec
%gemspec_add_dep -g listen -s ../%{gem_name}-%{version}.gemspec
%patch 0 -p1
%patch 1 -p2
%patch 2 -p2
%patch 3 -p1

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Fix for rpmlint
find %{buildroot}%{gem_instdir}/bin -type f | \
  xargs sed -i 's|^#!/usr/bin/env ruby|#!/usr/bin/ruby|'

%check
cp -a test/ Rakefile .%{gem_instdir}
pushd .%{gem_instdir}

# Fix Minitest 5.19+ compatibility.
# The fix is not proposed upstream, because this package is deprecated.
grep -Rl MiniTest | xargs sed -i "/MiniTest::Test/ s/MiniTest/Minitest/"

ruby -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{_bindir}/sass
%{_bindir}/sass-convert
%{_bindir}/scss
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/MIT-LICENSE
# Required on runtime from version.rb
%{gem_instdir}/REVISION
%{gem_instdir}/VERSION
%{gem_instdir}/VERSION_DATE
%{gem_instdir}/VERSION_NAME
%{gem_instdir}/bin
%{gem_instdir}/extra
%{gem_instdir}/init.rb
%{gem_libdir}
%{gem_instdir}/rails
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CODE_OF_CONDUCT.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
