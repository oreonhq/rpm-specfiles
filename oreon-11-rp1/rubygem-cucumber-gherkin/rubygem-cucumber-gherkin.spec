%global source0_hash f97293c8a3343db6765ff58811c13143944c3cb22e001830248fed8adbc1c7b7

# Generated from cucumber-gherkin-21.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name cucumber-gherkin

Name: rubygem-%{gem_name}
Version: 22.0.0
Release: 12%{?dist}
Summary: Fast Gherkin lexer/parser
License: MIT
URL: https://github.com/cucumber/gherkin
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone --no-checkout https://github.com/cucumber/gherkin-ruby
# git -C gherkin-ruby archive -v -o rubygem-gherkin-22.0.0-testdata.txz v22.0.0 testdata/
Source1: %{name}-%{version}-testdata.txz
# Fix compatibility with cucumber-messages 25+. Roughly equivalent to:
# https://github.com/cucumber/cucumber-ruby-core/pull/285/files
Patch0: rubygem-cucumber-gherkin-29.0.0-Fix-compatibility-with-cucumber-messages-25.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.3
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(cucumber-messages)
BuildArch: noarch

# Provides are to be removed in F38
Provides: rubygem-gherkin = %{version}-%{release}
Obsoletes: rubygem-gherkin < 5.1.0-100

%description
A fast Gherkin lexer/parser based on the Ragel State Machine Compiler.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1

%patch 0 -p2

%gemspec_remove_dep -g cucumber-messages "~> 17.1", ">= 17.1.1"
%gemspec_add_dep -g cucumber-messages ">= 17.0"

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
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/testdata testdata
rspec spec
popd

%files
%dir %{gem_instdir}
%{_bindir}/gherkin-ruby
%{_bindir}/gherkin
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/spec

%changelog
%autochangelog
