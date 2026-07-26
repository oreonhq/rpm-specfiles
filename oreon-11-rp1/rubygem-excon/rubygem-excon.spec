%global source0_hash af9bcc81527fd007bf88ff914e15c9f7d069886b98d8f0a4ee98d036c746f68d

%global gem_name excon

# The certificate refresh is broken by:
# https://github.com/excon/excon/pull/810
# Upstream hit this issue as well:
# https://github.com/excon/excon/pull/823/commits/06659d6408faa4f7c17b90f1b3e204fc00448311
%bcond_with certificate_refresh

Name: rubygem-%{gem_name}
Version: 1.2.7
Release: 4%{?dist}
Summary: Speed, persistence, http(s)
License: MIT
URL: https://github.com/excon/excon
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/excon/excon.git --no-checkout && cd excon
# git archive -v -o excon-1.2.7-tests.tar.gz v1.2.7 tests/ spec/
Source1: %{gem_name}-%{version}-tests.tar.gz
# https://github.com/excon/excon/commit/fbe4748d49ac87504ee8d3e7352da0de3485144c
# https://github.com/excon/excon/issues/892
# adjust ractor usage for Ruby 3.5+
Patch0:  excon-GH892-ractor-usage-ruby40.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
%{?with_certificate_refresh:BuildRequires: %{_bindir}/openssl}
BuildRequires: %{_bindir}/rackup
BuildRequires: %{_bindir}/shindont
BuildRequires: rubygem(activesupport)
BuildRequires: rubygem(delorean)
BuildRequires: rubygem(eventmachine)
BuildRequires: rubygem(open4)
BuildRequires: rubygem(puma)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(sinatra)
BuildRequires: rubygem(webrick)
BuildArch: noarch

%description
EXtended http(s) CONnections.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1
(
cd %{_builddir}
%patch -P0 -p1
)

# Use system crypto policies.
# https://fedoraproject.org/wiki/Packaging:CryptoPolicies
sed -i "/ciphers:/ s/'.*'/'PROFILE=SYSTEM'/" lib/excon/constants.rb

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

# Kill bundled cacert.pem
rm -rf %{buildroot}%{gem_instdir}/data

%check
pushd .%{gem_instdir}

# Move the tests into place
ln -s %{_builddir}/spec spec
ln -s %{_builddir}/tests tests

# Unicorn is not available in Fedora yet (rhbz#1065685).
sed -i '/if plugin == :unicorn/ i\  before { skip("until #{plugin} is in Fedora") } if plugin == :unicorn' spec/support/shared_contexts/test_server_context.rb
sed -i '/with_unicorn/ s/^/  pending\n\n/' tests/{basic_tests.rb,proxy_tests.rb}

# DNS resolution does not work on Koji
sed -i "/it 'passes the dns_timeouts to Resolv::DNS::Config' do/a\
    skip 'DNS resolution is disabled in Mock'" spec/requests/dns_timeout_spec.rb
sed -i "/it 'resolv_resolver config reaches Resolv::DNS::Config' do/a\
    skip 'DNS resolution is disabled in Mock'" spec/requests/resolv_resolver_spec.rb

rspec spec

# Don't use Bundler.
sed -i "/'bundler\/setup'/ s/^/#/" tests/test_helper.rb

# This would require sinatra-contrib.
sed -i '/redirecting_with_cookie.ru/,/^  end/ s/^/#/' tests/middlewares/capture_cookies_tests.rb

# This is required for Rack 2.x compatibility and can be removed as soon as
# Rack 3+ and Rackup gems are in Fedora.
ruby -e 'require "rackup/handler/webrick"' || (
  sed -i 's/ackup/ack/' tests/rackups/ssl*.ru
)

%if %{with certificate_refresh}
# Keep the test certificates fresh.
# https://github.com/excon/excon/blob/fe8ec7b53905c4eb1ffd88c1b507b9ecb5e21226/Rakefile#L53-L54
openssl req -subj '/CN=excon/O=excon' -new -newkey rsa:2048 -sha256 -days 3650 -nodes -x509 -keyout tests/data/excon.cert.key -out tests/data/excon.cert.crt
openssl req -subj '/CN=127.0.0.1/O=excon' -new -newkey rsa:2048 -sha256 -days 3650 -nodes -x509 -keyout tests/data/127.0.0.1.cert.key -out tests/data/127.0.0.1.cert.crt
%endif

shindont
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUT*
%doc %{gem_instdir}/README.md
%{gem_instdir}/excon.gemspec

%changelog
%autochangelog
