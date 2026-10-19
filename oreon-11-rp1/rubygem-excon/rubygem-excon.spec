%global source1_hash 69c1f90a667ac6355b5176dacb64c199d94f58472b13c3c4092902490df8135a
%global source0_hash 3b3917dbdf0c65b8d872039fe2b37bf423da2f245ef05b0af07423027c4cfde5
%global gem_name excon
%bcond_with certificate_refresh
Name: rubygem-%{gem_name}
Version: 1.2.7
Release:        1%{?dist}
Summary:        Speed, persistence, http(s)
License: MIT
URL: https://github.com/excon/excon
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/excon/excon/archive/refs/tags/v1.2.7.tar.gz
Patch0:  excon-GH892-ractor-usage-ruby40.patch
%{?with_certificate_refresh:BuildRequires: %{_bindir}/openssl}
BuildArch: noarch
# oreon:deps
BuildRequires:  /usr/bin/rackup
BuildRequires:  /usr/bin/shindont
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(activesupport)
BuildRequires:  rubygem(delorean)
BuildRequires:  rubygem(eventmachine)
BuildRequires:  rubygem(open4)
BuildRequires:  rubygem(puma)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(sinatra)
BuildRequires:  rubygem(webrick)
BuildRequires:  rubygems-devel
# /oreon:deps
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
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;
(
cd %{_builddir}
%patch -P0 -p1
)

# Use system crypto policies.
# https://fedoraproject.org/wiki/Packaging:CryptoPolicies
sed -i "/ciphers:/ s/'.*'/'PROFILE=SYSTEM'/" lib/excon/constants.rb

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
rm -rf %{buildroot}%{gem_instdir}/data
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ln -s %{_builddir}/spec spec
ln -s %{_builddir}/tests tests
sed -i '/if plugin == :unicorn/ i\  before { skip("until #{plugin} is in Fedora") } if plugin == :unicorn' spec/support/shared_contexts/test_server_context.rb
sed -i '/with_unicorn/ s/^/  pending\n\n/' tests/{basic_tests.rb,proxy_tests.rb}
sed -i "/it 'passes the dns_timeouts to Resolv::DNS::Config' do/a\
    skip 'DNS resolution is disabled in Mock'" spec/requests/dns_timeout_spec.rb
sed -i "/it 'resolv_resolver config reaches Resolv::DNS::Config' do/a\
    skip 'DNS resolution is disabled in Mock'" spec/requests/resolv_resolver_spec.rb
rspec spec
sed -i "/'bundler\/setup'/ s/^/#/" tests/test_helper.rb
sed -i '/redirecting_with_cookie.ru/,/^  end/ s/^/#/' tests/middlewares/capture_cookies_tests.rb
ruby -e 'require "rackup/handler/webrick"' || (
  sed -i 's/ackup/ack/' tests/rackups/ssl*.ru
)
%if %{with certificate_refresh}
openssl req -subj '/CN=excon/O=excon' -new -newkey rsa:2048 -sha256 -days 3650 -nodes -x509 -keyout tests/data/excon.cert.key -out tests/data/excon.cert.crt
openssl req -subj '/CN=127.0.0.1/O=excon' -new -newkey rsa:2048 -sha256 -days 3650 -nodes -x509 -keyout tests/data/127.0.0.1.cert.key -out tests/data/127.0.0.1.cert.crt
%endif
shindont
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-excon-doc -f %{oreon_filedir}/rubygem-excon-doc.list

%changelog

%autochangelog
