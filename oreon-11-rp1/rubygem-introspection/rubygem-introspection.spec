%global source0_hash 8abd4f906cc644aa39bf879f28ec9a0267452342c5689d6c75f40336655c56f8

# Generated from introspection-0.0.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name introspection

Name: rubygem-%{gem_name}
Version: 0.0.4
Release: 21%{?dist}
Summary: Dynamic inspection of the hierarchy of method definitions on a Ruby object
# https://github.com/floehopper/introspection/issues/1
License: MIT
URL: http://jamesmead.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(metaclass) => 0.0.1
BuildRequires: rubygem(metaclass) < 0.1
# There is no #assert_nothing_raised in minitest 5.x
BuildRequires: rubygem(minitest)
BuildArch: noarch

%description
Dynamic inspection of the hierarchy of method definitions on a Ruby object.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T
%gem_install -n %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# Disable Bundler.
sed -i '/bundler\/setup/ s/^/#/' test/test_helper.rb

# Drop BlankSlate test case. There should be no need for BlankSlate, when
# there is BasicObject available for years.
# https://github.com/floehopper/introspection/issues/11
sed -i -e '/require.*blankslate/ s/^/#/' \
  -e '/def test_should_cope_with_blankslate_object$/a\\    skip' \
  test/snapshot_test.rb

ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%license %{gem_instdir}/COPYING.txt
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/introspection.gemspec
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_instdir}/README.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/samples
%{gem_instdir}/test
%doc %{gem_docdir}

%changelog
%autochangelog
