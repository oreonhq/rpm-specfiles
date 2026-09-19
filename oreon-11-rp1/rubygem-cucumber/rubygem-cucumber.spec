%global source0_hash f9566e5e3050066ef22e19c9b43758787b71427235ea192ffdccc41e2a0fa2f5

%global gem_name cucumber

%bcond_with bootstrap

Name: rubygem-%{gem_name}
Version: 7.1.0
Release: 15%{?dist}
Summary: Tool to execute plain-text documents as functional tests
License: MIT
URL: https://cucumber.io/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone --no-checkout https://github.com/cucumber/cucumber-ruby.git
# git -C cucumber-ruby archive -v -o rubygem-cucumber-7.1.0-spec.txz v7.1.0 spec/ cucumber.yml
Source1: %{name}-%{version}-spec.txz
# git clone --no-checkout https://github.com/cucumber/cucumber-ruby.git
# git -C cucumber-ruby archive -v -o rubygem-cucumber-7.1.0-features.txz v7.1.0 features/
Source2: %{name}-%{version}-features.txz
# Fix Ruby 3.4 compatibility due to `Hash.new` now accepting `:capacity`
# keyword option.
# https://github.com/cucumber/cucumber-ruby/pull/1757/commits/87a375822f0f1d76fa464423f9743e36c5036713
Patch0: rubygem-cucumber-9.2.0-Pass-hash-through-as-explicit-hash-to-avoid-unknown-keyword.patch
# Fix Ruby 3.4 backtrace formatting compatibility.
# https://github.com/cucumber/cucumber-ruby/pull/1771/commits/398eb7080936481b6b8c4921ff59aea7a8951883
Patch1: rubygem-cucumber-9.2.0-Fix-error-backtrace-formatting-on-Ruby-3-4.patch
# Fix Ruby 3.4 Hash#inspect compatibility.
# https://github.com/cucumber/cucumber-ruby/pull/1771/commits/b9065c96098b893c75fcbb41b7558332b3bfd23b
Patch2: rubygem-cucumber-9.2.0-CI-support-Ruby-3-4-Hash-inspect.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
# Aruba has circular dependency with Cucumber.
%if %{without bootstrap}
BuildRequires: rubygem(aruba)
%endif
BuildRequires: rubygem(base64)
BuildRequires: rubygem(builder)
BuildRequires: rubygem(cucumber-core)
BuildRequires: rubygem(cucumber-wire)
BuildRequires: rubygem(cucumber-create-meta)
BuildRequires: rubygem(multi_test)
BuildRequires: rubygem(mime-types)
BuildRequires: rubygem(webrick)
BuildRequires: rubygem(nokogiri)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(rake)
BuildArch: noarch

%description
Cucumber lets software development teams describe how software should behave
in plain text. The text is written in a business-readable domain-specific
language and serves as documentation, automated tests and development-aid.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1 -b 2

%patch 0 -p1
%patch 1 -p1

(
cd %{builddir}
%patch 2 -p1
)

# The rubygem-cucumber-html-formatter is currently not packaged in Fedora.
%gemspec_remove_dep -g cucumber-html-formatter

# Relax requires.
%gemspec_remove_dep -g diff-lcs "~> 1.4", ">= 1.4.4"
%gemspec_add_dep -g diff-lcs ">= 1.3"

%gemspec_remove_dep -g cucumber-gherkin "~> 22.0", ">= 22.0.0"
%gemspec_add_dep -g cucumber-gherkin ">= 20.0"

%gemspec_remove_dep -g cucumber-cucumber-expressions "~> 14.0", ">= 14.0.0"
%gemspec_add_dep -g cucumber-cucumber-expressions ">= 12.1"

%gemspec_remove_dep -g cucumber-messages "~> 17.1", ">= 17.1.1"
%gemspec_add_dep -g cucumber-messages ">= 17.0"

%gemspec_add_dep -g base64 ">= 0.2.0"

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
# Cucumber.yml is needed for both test suites.
# Used as fixture for rspec and options for cucumber.
ln -s %{_builddir}/cucumber.yml cucumber.yml

ln -s %{_builddir}/spec spec
# We don't need Pry.
sed -i '/require.*pry/ s/^/#/' spec/spec_helper.rb

rspec -Ilib spec

%if %{without bootstrap}
ln -s %{_builddir}/features features

# Skip the test that requires rubygem-cucumber-html-formatter,
# which is currently not packaged in Fedora.
sed -i -e '/^  Scenario: output html to stdout$/i @skip' \
    features/docs/formatters/html.feature

# Use RUBYOPT to make sure that the Cucumber from current directory has
# precedence over system Cucumber, which is pulled in as Aruba dependency.
RUBYOPT=-Ilib cucumber --tags 'not @skip'
%endif
popd

%files
%dir %{gem_instdir}
%{_bindir}/cucumber
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CHANGELOG.md

%changelog
%autochangelog
