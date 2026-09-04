%global source0_hash 6cc4b5880ba1c3991292579d0451af0f44814f5a1a13d7823317a09705eb15d4

# Generated from cucumber-expressions-6.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name cucumber-cucumber-expressions

Name: rubygem-%{gem_name}
Version: 20.1.0
Release: 1%{?dist}
Summary: A simpler alternative to Regular Expressions
License: MIT
URL: https://github.com/cucumber/cucumber-expressions
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Upstream removed LICENSE file from packages.
# https://github.com/cucumber/cucumber-expressions/issues/292
# Taken from:
# https://github.com/cucumber/cucumber-expressions/blob/v17.1.0/LICENSE
Source1: LICENSE
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: %{_bindir}/rspec
BuildRequires: rubygem(rspec-expectations)
BuildRequires: rubygem-bigdecimal
BuildArch: noarch

# Provides: can be removed in F36+2, i.e. F38
Provides: rubygem-cucumber-expressions = %{version}-%{release}
Obsoletes: rubygem-cucumber-expressions < 6.0.1-10

%description
Cucumber Expressions - a simpler alternative to Regular Expressions.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install

install -m 644 %{SOURCE1} .%{gem_instdir}/LICENSE

# The methods with question marks were replaced with attr_reader(s) in 17.0.0.
# They were getters already. To keep compatibility with cucumber v7.
# simply aliasing the methods on the correct place is enough.
# Related: https://github.com/cucumber/cucumber-expressions/pull/234
sed -i -e '/attr_reader :name, :type/ a    alias :prefer_for_regexp_match? :prefer_for_regexp_match' \
       -e '/attr_reader :name, :type/ a    alias :use_for_snippets? :use_for_snippets' \
          .%{gem_libdir}/cucumber/cucumber_expressions/parameter_type.rb

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
rspec spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%{gem_spec}

%exclude %{gem_instdir}/.*
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/VERSION
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/cucumber-cucumber-expressions.gemspec
%{gem_instdir}/spec

%changelog
%autochangelog
