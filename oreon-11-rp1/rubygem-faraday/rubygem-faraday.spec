%global source0_hash 1882247e6766615c8220b4392bf1d27f6ebb63d8e28267587cef1fb0bf37f278

# Generated from faraday-0.8.7.gem by gem2rpm -*- rpm-spec -*-
%global gem_name faraday

Name: rubygem-%{gem_name}
Version: 2.14.3
Release: 1%{?dist}
Summary: HTTP/REST API client library
License: MIT
URL: https://lostisland.github.io/faraday
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Since we don't have multipart-parser in Fedora, include the essential part
# just for testing purposes.
# https://github.com/danabr/multipart-parser/blob/master/lib/multipart_parser/parser.rb
Source1: https://raw.githubusercontent.com/danabr/multipart-parser/master/lib/multipart_parser/parser.rb
# https://github.com/danabr/multipart-parser/blob/master/lib/multipart_parser/reader.rb
Source2: https://raw.githubusercontent.com/danabr/multipart-parser/master/lib/multipart_parser/reader.rb
# Fix Rack 2.1+ test compatibility.
# https://github.com/lostisland/faraday/pull/1171
Patch0: rubygem-faraday-1.0.1-Properly-fix-test-failure-with-Rack-2.1.patch
# Extracted from:
# https://github.com/lostisland/faraday/commit/687108bb4ddc2511aeaae7449dd401fe62dd5ceb
Patch1: faraday-1.0.1-net-http-persistent-3-error-kind.patch
# "undefined method" error message changed with ruby 3.3
# https://github.com/lostisland/faraday/pull/1523
# https://github.com/ruby/ruby/pull/6950
Patch2: faraday-pr1523-testsuite-undefined-method-change.patch
# ruby3.4 backtrace quoting change
# https://github.com/lostisland/faraday/pull/1560
Patch3: faraday-pr1560-ruby34-backtrace-change.patch
# ruby3.4 Hash#inspect formatting change
# https://github.com/lostisland/faraday/pull/1604
Patch4: faraday-pr1604-ruby34-hash-inspect-formatting-change.patch
# https://github.com/lostisland/faraday-rack/pull/13
# https://github.com/lostisland/faraday-rack/commit/a590bc34e40b62484440dcd4ab5147c0c02bb425
# Patch for rack 3.1 wrt env['rack.input'] is optional
Patch5: faraday-rack-pr13-rack31-rack_input.patch
# https://github.com/lostisland/faraday/pull/1549
# https://github.com/lostisland/faraday/commit/66551ecc79f5d3d5bca1a2523bd8736db8c2220c.patch
# Unescape the result of Rack::Utils.build_nested_query for rack 3.1
Patch6: faraday-pr1549-unespace-rack-utils-query-result.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.3
BuildRequires: rubygem(multipart-post)
BuildRequires: rubygem(rack)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(webmock)
# Adapter test dependencies, might be optionally disabled.
BuildRequires: rubygem(em-http-request)
BuildRequires: rubygem(excon)
BuildRequires: rubygem(httpclient)
BuildRequires: rubygem(net-http-persistent)
BuildRequires: rubygem(rack-test)
BuildRequires: rubygem(typhoeus)
BuildArch: noarch

%description
HTTP/REST API client library.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

mkdir -p multipart_parser/multipart_parser
cp %{SOURCE1} %{SOURCE2} multipart_parser/multipart_parser

%autosetup -n %{gem_name}-%{version} -p1

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
# We don't care about code coverage.
sed -i "/simplecov/ s/^/#/" spec/spec_helper.rb
sed -i "/coveralls/ s/^/#/" spec/spec_helper.rb
sed -i "/SimpleCov/,/^end$/ s/^/#/" spec/spec_helper.rb

# We don't need Pry.
sed -i "/pry/ s/^/#/" spec/spec_helper.rb

# We don't have {patron,em-synchrony} available in Fedora.
mv spec/faraday/adapter/em_synchrony_spec.rb{,.disabled}
mv spec/faraday/adapter/patron_spec.rb{,.disabled}

# This needs http-net-persistent 3.0+.
sed -i '/allows to set min_version in SSL settings/a\      skip' \
  spec/faraday/adapter/net_http_persistent_spec.rb

rspec -I%{_builddir}/multipart_parser -rspec_helper -r%{SOURCE1} spec -f d
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
%{gem_instdir}/spec

%changelog
%autochangelog
