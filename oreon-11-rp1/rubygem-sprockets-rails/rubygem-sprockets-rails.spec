%global source0_hash a9e88e6ce9f8c912d349aa5401509165ec42326baf9e942a85de4b76dbc4119e

# Generated from sprockets-rails-2.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sprockets-rails

Name: rubygem-%{gem_name}
Version: 3.5.2
Release: 4%{?dist}
Summary: Sprockets Rails integration
License: MIT
URL: https://github.com/rails/sprockets-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Get the tests
# git clone --no-checkout https://github.com/rails/sprockets-rails.git && cd sprockets-rails
# git archive -v -o sprockets-rails-3.5.2-tests.tar.gz v3.5.2 test/
Source1: sprockets-rails-%{version}-tests.tar.gz
# Fix compatibility for minitest 6
Patch0:  sprockets-rails-3.5.2-minitest6.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(minitest-mock)
BuildRequires: rubygem(railties) >= 6.1
%dnl BuildRequires: rubygem(rake)
BuildRequires: rubygem(sprockets)
BuildArch: noarch

%description
Provides Sprockets implementation for Rails 4.x (and beyond) Asset Pipeline.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1
(
cd %{_builddir}
%patch -P0 -p1
)

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
( cd .%{gem_instdir}
ln -s %{builddir}/test .

ruby -Ilib -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
)

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
