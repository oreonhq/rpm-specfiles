%global source0_hash 38473d0c1c2633d469e117df10bfb8ea21adbc97c83cabe49e1b68bf2c4a4a8b

# Generated from cucumber-core-1.4.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name cucumber-core

Name: rubygem-%{gem_name}
Version: 19.0.0
Release: 1%{?dist}
Summary: Core library for the Cucumber BDD app
License: MIT
URL: https://cucumber.io
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/cucumber/cucumber-ruby-core/pull/299/
# https://github.com/cucumber/cucumber-ruby-core/pull/302/commits/6f157ae0a5d2dac850f3d0d6982dd00b5c25b1d9
# Discard the extraneous arguments from Method#source_location
# ruby3_5 now returns 5 elements from source_location:
# https://github.com/ruby/ruby/pull/12539
Patch0:  cucumber-ruby-core-pr299-default-source-location-fix.patch
Patch1:  cucumber-ruby-core-pr302-remove-source_location-extra-args.patch
# Fix compatibilty with cucumber-messages 25+. Roughly equivalent to:
# https://github.com/cucumber/gherkin/pull/259
Patch2: rubygem-cucumber-core-15.0.0-Fix-compatibility-with-cucumber-messages-25.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(cucumber-gherkin)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(kramdown-parser-gfm)
BuildRequires: rubygem(cucumber-tag-expressions)
BuildRequires: rubygem(cucumber-messages)
# BuildRequires: rubygem(unindent)
BuildArch: noarch

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

%check
pushd .%{gem_instdir}

# unindent is not available in Fedora => avoid the requires.
for file in $(grep -Rl unindent spec); do
  sed -i "/require 'unindent'/ s/^/#/" "${file}"
  sed -i '/^ *expect.*unindent$/ i \pending' "${file}"
done

LANG=C.UTF-8 rspec -rkramdown/parser/gfm spec
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/spec

%changelog
%autochangelog
