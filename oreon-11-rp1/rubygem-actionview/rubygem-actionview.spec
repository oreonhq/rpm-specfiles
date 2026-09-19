%global source0_hash 165207ed307b8ceb1e64332d905ff049b7c1fb36da08d35c416da781d500ef56

%global gem_name actionview

# Circular dependency with rubygem-railties.
%bcond_with bootstrap

Name: rubygem-%{gem_name}
Version: 8.0.3
Release: 3%{?dist}
Summary: Rendering framework putting the V in MVC (part of Rails)
License: MIT
URL: https://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}%{?prerelease}.gem
# The gem doesn't ship with the test suite.
# You may check it out like so
# git clone http://github.com/rails/rails.git && cd rails/actionview
# git archive -v -o actionview-8.0.3-tests.tar.gz v8.0.3 test/
Source1: %{gem_name}-%{version}%{?prerelease}-tests.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
%if %{without bootstrap}
BuildRequires: rubygem(activesupport) = %{version}
BuildRequires: rubygem(activerecord) = %{version}
BuildRequires: rubygem(actionpack) = %{version}
BuildRequires: rubygem(minitest-mock)
BuildRequires: rubygem(railties) = %{version}
BuildRequires: rubygem(capybara)
BuildRequires: rubygem(sqlite3)
BuildRequires: tzdata
%endif
BuildArch: noarch

%description
Simple, battle-tested conventions and helpers for building web pages.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}%{?prerelease} -b1

%build
gem build ../%{gem_name}-%{version}%{?prerelease}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%if %{without bootstrap}
%check
# This requires activerecord in rails git structure
ln -s %{gem_dir}/gems/activerecord-%{version}%{?prerelease}/ .%{gem_dir}/gems/activerecord

( cd .%{gem_instdir}
cp -a %{builddir}/test .

mkdir ../tools
# Fake test_common.rb. It does not provide any functionality besides
# `force_skip` alias.
touch ../tools/test_common.rb
# Netiher strict_warnings.rb appears to be useful.
touch ../tools/strict_warnings.rb

# Make it sure that we are using fixed library, not
# using library already installed in system path
# (dependency loop)
export RUBYLIB=$(pwd)/lib

# Run separately as we need to avoid superclass mismatch errors
find test -type f -name '*_test.rb' -print0 | \
  sort -z | \
  xargs -0 -n1 -i sh -c "echo '* Test file: {}'; ruby -Itest -- '{}' || exit 255"

)
%endif

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/app
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.rdoc

%changelog
%autochangelog
