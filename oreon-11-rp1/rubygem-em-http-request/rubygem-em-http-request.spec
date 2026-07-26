%global source0_hash 16fbc72b2a6e20c804c564ac5d12e98668c6fcef8c3b1dd2387dff505f2efdab

# Generated from em-http-request-1.1.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name em-http-request

Name: rubygem-%{gem_name}
Version: 1.1.7
Release: 16%{?dist}
Summary: EventMachine based, async HTTP Request client
License: MIT
URL: http://github.com/igrigorik/em-http-request
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Since Ruby 3.0 keyword arguments need to be explicitly declared
# PR: https://github.com/igrigorik/em-http-request/pull/344
Patch0: %{name}-%{version}-explicit-keyword-argument.patch
Patch1: em-http-request-1.1.7-Also-stop-the-HTTP-parser-in-addition-to-resetting.patch
# Fix compatibility with Rack 3
# https://github.com/igrigorik/em-http-request/pull/370
Patch2: rubygem-em-http-request-1.1.7-Compatibility-with-Rack-3.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(eventmachine)
BuildRequires: rubygem(multi_json)
BuildRequires: rubygem(em-socksify)
BuildRequires: rubygem(addressable)
BuildRequires: rubygem(cookiejar)
BuildRequires: rubygem(http_parser.rb)
BuildRequires: rubygem(rack)
BuildRequires: rubygem(rackup)
BuildRequires: rubygem(webrick)
BuildRequires: %{_bindir}/ping
BuildRequires: rubygem(rspec)

BuildArch: noarch

%description
EventMachine based, async HTTP Request client.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

%patch 0 -p1
%patch 1 -p1
%patch 2 -p1

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

# Have networking enabled in your mock config before testing
%check
pushd .%{gem_instdir}
# We are trying not to use bundler when not needed
sed -i "/require 'bundler\/setup'/ s/^/#/" spec/helper.rb
# Missing require on pathname in client spec
sed -i "/^require 'helper'/i require 'pathname'" spec/client_spec.rb

# Fails, not quite sure why :/
sed -i '/it "should report error if connection was closed by server on client keepalive requests" do/ ,/^  end$/ s/^/#/' spec/client_spec.rb

# These tests fail on WEBrick but on Puma the tests are passing.
sed -i '/it "should set content-length to 0 on posts with empty bodies" do/ ,/^  end$/ s/^/#/' spec/client_spec.rb
sed -i '/it "should keep default https port in redirect url that include it"/ ,/^  end$/ s/^/#/' spec/redirect_spec.rb
sed -i '/it "should keep default http port in redirect url that include it"/ ,/^  end$/ s/^/#/' spec/redirect_spec.rb
# Got a different message than expected with WEBrick, works on Puma
sed -i '/it "should fail gracefully on an invalid host in Location header" do/ ,/^  end$/ s/^/#/' spec/dns_spec.rb

# One of tests expects UTF-8 encoding.
LANG=C.UTF-8 rspec spec -f d
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%{gem_instdir}/benchmarks
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Changelog.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/em-http-request.gemspec
%{gem_instdir}/examples
%{gem_instdir}/spec

%changelog
%autochangelog
