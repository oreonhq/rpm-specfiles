%global source0_hash 6dfda79d91bb3b949b947ecc5919f042ef2f399b904013eb3ef6d20dd3a4082e

%global gem_name xpath

Name: rubygem-%{gem_name}
Version: 3.2.0
Release: 12%{?dist}
Summary: Generate XPath expressions from Ruby
License: MIT
URL: https://github.com/teamcapybara/xpath
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec-core)
BuildRequires: rubygem(rspec-expectations)
BuildRequires: rubygem(nokogiri)
BuildArch: noarch

%description
XPath is a Ruby DSL for generating XPath expressions.

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
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
sed -i "/^require 'pry'$/ s/^/#/" spec/spec_helper.rb

rspec spec
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/README.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/spec

%changelog
%autochangelog
