%global source0_hash a1be9df1e5d787f62ff89e5a96c9a78e2e3b989cef7bf698f22cd5efd699d391
%global gem_name cucumber-cucumber-expressions
Name: rubygem-%{gem_name}
Version: 17.1.0
Release:        5%{?dist}
Summary:        A simpler alternative to Regular Expressions
License: MIT
URL: https://github.com/cucumber/cucumber-expressions
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: LICENSE
BuildArch: noarch
Provides: rubygem-cucumber-expressions = %{version}-%{release}
Obsoletes: rubygem-cucumber-expressions < 6.0.1-10
# oreon:deps
BuildRequires:  /usr/bin/rspec
BuildRequires:  ruby(release)
BuildRequires:  rubygem(rspec-expectations)
BuildRequires:  rubygem-bigdecimal
BuildRequires:  rubygems-devel
# /oreon:deps
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
sed -i -e '/attr_reader :name, :type/ a    alias :prefer_for_regexp_match? :prefer_for_regexp_match' \
       -e '/attr_reader :name, :type/ a    alias :use_for_snippets? :use_for_snippets' \
          .%{gem_libdir}/cucumber/cucumber_expressions/parameter_type.rb
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
rspec spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-cucumber-cucumber-expressions-doc -f %{oreon_filedir}/rubygem-cucumber-cucumber-expressions-doc.list

%changelog

%autochangelog
