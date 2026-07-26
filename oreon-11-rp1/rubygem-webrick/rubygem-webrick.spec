%global source0_hash b42d3c94f166f3fb73d87e9b359def9b5836c426fc8beacf38f2184a21b2a989

# Generated from webrick-1.7.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name webrick

Name: rubygem-%{gem_name}
Version: 1.9.1
Release: 3%{?dist}
Summary: HTTP server toolkit
License: Ruby AND BSD-2-Clause
URL: https://github.com/ruby/webrick
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Test suite is not packaged with the gem, you may check out it like so:
# git clone --no-checkout https://github.com/ruby/webrick
# cd webrick && git archive -v -o webrick-1.9.1-tests.txz v1.9.1 test
Source1: %{gem_name}-%{version}-tests.txz
# https://github.com/ruby/webrick/pull/181
# https://github.com/ruby/webrick/issues/179
# ruby4_0 removes IO#nread
Patch0:  webrick-pr181-ruby40-IO-nread-removal.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.4.0
BuildRequires: rubygem(test-unit)
BuildRequires: rubygem(test-unit-ruby-core)
BuildArch: noarch

%description
WEBrick is an HTTP server toolkit that can be configured as an HTTPS server, a
proxy server, and a virtual-host server.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1
%patch -P0 -p1

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# Symlink the test suite.
ln -s %{_builddir}/test .

# Use --verbose to set $VERBOSE to true. `test_sni` in test/webrick/test_https.rb
# relies on output in $stderr from lib/webrick/ssl.rb that is only written there
# if $VERBOSE is true.
# https://github.com/ruby/webrick/pull/158
ruby --verbose           \
     -Ilib:test:test/lib \
     -rhelper            \
     -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/sig
%{gem_instdir}/webrick.gemspec

%changelog
%autochangelog
