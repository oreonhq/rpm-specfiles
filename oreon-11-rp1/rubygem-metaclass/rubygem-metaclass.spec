%global source0_hash 8569685c902108b1845be4e5794d646f2a8adcb0280d7651b600dab0844fe942

# Generated from metaclass-0.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name metaclass

Summary: Adds a metaclass method to all Ruby objects
Name: rubygem-%{gem_name}
Version: 0.0.4
Release: 22%{?dist}
# https://github.com/floehopper/metaclass/issues/1
License: MIT
URL: http://github.com/floehopper/metaclass
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Make the test suite support MiniTest 5.x.
# https://github.com/floehopper/metaclass/commit/cff40cbace639d3b66d7913d99e74e56f91905b8
Patch0: rubygem-metaclass-0.0.4-Move-to-Minitest-5.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildArch: noarch

%description
Adds a metaclass method to all Ruby objects

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T
%gem_install -n %{SOURCE0}

pushd .%{gem_instdir}
%patch 0 -p1
popd

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# test_helper.rb currently references bundler, so it is easier to avoid
# its usage at all.
sed -i '/require "bundler\/setup"/ d' test/test_helper.rb

ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/COPYING.txt
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/metaclass.gemspec
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
%autochangelog
