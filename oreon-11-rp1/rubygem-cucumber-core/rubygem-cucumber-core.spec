%global source0_hash 1b13f9d81708dae89a17a3ee915b3e8e8f2303b480d0978278d61e474001d700
%global gem_name cucumber-core
Name: rubygem-%{gem_name}
Version: 10.1.0
Release:        13%{?dist}
Summary:        Core library for the Cucumber BDD app
License: MIT
URL: https://cucumber.io
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0:  cucumber-ruby-core-pr299-default-source-location-fix.patch
Patch1:  cucumber-ruby-core-pr302-remove-source_location-extra-args.patch
Patch2: rubygem-cucumber-core-15.0.0-Fix-compatibility-with-cucumber-messages-25.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(cucumber-gherkin)
BuildRequires:  rubygem(cucumber-messages)
BuildRequires:  rubygem(cucumber-tag-expressions)
BuildRequires:  rubygem(kramdown-parser-gfm)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Core library for the Cucumber BDD app.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%gemspec_remove_dep -g cucumber-messages "~> 17.1", ">= 17.1.1"
%gemspec_add_dep -g cucumber-messages ">= 17.0"

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
for file in $(grep -Rl unindent spec); do
  sed -i "/require 'unindent'/ s/^/#/" "${file}"
  sed -i '/^ *expect.*unindent$/ i \pending' "${file}"
done
LANG=C.UTF-8 rspec -rkramdown/parser/gfm spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-cucumber-core-doc -f %{oreon_filedir}/rubygem-cucumber-core-doc.list

%changelog

%autochangelog
