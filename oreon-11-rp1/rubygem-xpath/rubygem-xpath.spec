%global source0_hash 6dfda79d91bb3b949b947ecc5919f042ef2f399b904013eb3ef6d20dd3a4082e
%global gem_name xpath
Name: rubygem-%{gem_name}
Version: 3.2.0
Release:        12%{?dist}
Summary:        Generate XPath expressions from Ruby
License: MIT
URL: https://github.com/teamcapybara/xpath
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygem(nokogiri)
BuildRequires:  rubygem(rspec-core)
BuildRequires:  rubygem(rspec-expectations)
BuildRequires:  rubygems-devel
# /oreon:deps
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

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
sed -i "/^require 'pry'$/ s/^/#/" spec/spec_helper.rb
rspec spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-xpath-doc -f %{oreon_filedir}/rubygem-xpath-doc.list

%changelog

%autochangelog
