%global source0_hash 604e7c3346fedab7834edab16b4be60f411c949cc3f86e0c9894bafc5d4c788d

%global gem_name sinatra

%bcond_with bootstrap
%bcond_without tilt_integration_tests

Name: rubygem-%{gem_name}
Version: 4.2.1
Release: 5%{?dist}
Summary: Ruby-based web application framework
License: MIT
URL: http://sinatrarb.com/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/sinatra/sinatra.git && cd sinatra
# git archive -v -o sinatra-4.2.1-test.tar.gz v4.2.1 test/
Source1: %{gem_name}-%{version}-test.tar.gz
# Fix test failures caused by RDoc 6.16+
# https://github.com/sinatra/sinatra/pull/2132
Patch0: rubygem-sinatra-4.2.1-Fix-RDoc-6-16-compatibility-by-relaxing-the-check.patch
# Fix compatibility with minitest 6
Patch1: rubygem-sinatra-4.2.1-minitest6.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
%if %{without bootstrap}
BuildRequires: rubygem(minitest) > 5
BuildRequires: rubygem(minitest-mock)
BuildRequires: rubygem(mustermann)
BuildRequires: rubygem(rack)
BuildRequires: rubygem(rack-test)
BuildRequires: rubygem(rack-protection) >= %{version}
BuildRequires: rubygem(rack-session)
BuildRequires: rubygem(rackup)
# Tilt is actually required from base_test
BuildRequires: rubygem(tilt)
%if %{with tilt_integration_tests}
BuildRequires: rubygem(asciidoctor)
BuildRequires: rubygem(builder)
BuildRequires: rubygem(erubi)
BuildRequires: rubygem(haml)
BuildRequires: rubygem(kramdown)
BuildRequires: rubygem(nokogiri)
BuildRequires: rubygem(rdiscount)
BuildRequires: rubygem(redcarpet)
BuildRequires: rubygem(slim)
%endif
%endif
Epoch: 1
BuildArch: noarch

%description
Sinatra is a DSL for quickly creating web applications in Ruby with minimal
effort.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1

( cd %{builddir}
%patch 0 -p1
%patch 1 -p1
)

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

# Fix shebangs, though those are examples.
sed -i -e 's|^#!/usr/bin/env ruby|#!/usr/bin/ruby|' \
  %{buildroot}%{gem_instdir}/examples/*.rb
chmod a+x %{buildroot}%{gem_instdir}/examples/*.rb

%if %{without bootstrap}
%check
pushd .%{gem_instdir}
cp -a %{builddir}/test test

# Avoid ActiveSupport dependency, which should not be needed anyway.
sed -i '/active_support/ s/^/#/' test/test_helper.rb

# We can't do integration test
# because we don't ship sinatra-contrib including Sinatra::Runner.
mv test/integration_test.rb{,.disabled}
mv test/integration_async_test.rb{,.disabled}
# These would require additional dependencies, such as Zeitwerk, Puma, etc.
mv test/integration_start_test.rb{,.disabled}

# TODO: Is it worth of testing all the possible template engines integration?
ruby -e 'Dir.glob "./test/*_test.rb", &method(:require)'
popd
%endif

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.yardopts
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/AUTHORS.md
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/MAINTENANCE.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/SECURITY.md
%{gem_instdir}/VERSION
%{gem_instdir}/examples
%{gem_instdir}/sinatra.gemspec

%changelog
%autochangelog
