%global source0_hash e2c3997023445856cae788dec4cd54726d9bd97c9c81fac03221925ad047482c
%global rubygems_molinillo_version 0.8.0
%global rubygems_net_http_version 0.7.0
%global rubygems_net_protocol_version 0.2.2
%global rubygems_optparse_version 0.8.0
%global rubygems_resolv_version 0.7.0
%global rubygems_securerandom_version 0.4.1
%global rubygems_timeout_version 0.4.4
%global rubygems_tsort_version 0.2.0
%global rubygems_uri_version 1.1.1
%global bundler_version 4.0.21
%global psych_version 5.3.1
%global rdoc_version 7.0.3
%global rubygems_dir %(ruby -e "puts RbConfig::CONFIG['rubygemsdir']")
%global gem_extdir %{_exec_prefix}/lib{,64}/gems
%bcond_with bootstrap
%{!?buildtime_libdir:%global buildtime_libdir $(ruby -rrbconfig -e 'puts RbConfig::CONFIG["libdir"]')}
Summary:        The Ruby standard for packaging ruby libraries
Name: rubygems
Version: 4.0.21
Release:        1%{?dist}
License: %{shrink:
    (Ruby OR MIT) AND
    BSD-2-Clause AND
    (BSD-2-Clause OR Ruby) AND
    (Ruby OR BSD-2-Clause OR GPL-1.0-or-later) AND
    MIT
}
URL: https://rubygems.org/
Source0:        https://rubygems.org/rubygems/%{name}-%{version}.tgz
Source1: operating_system.rb
Source2: %{name}-%{version}-test-missing-files.tar.gz
Source3: rubygems-create-missing-test-files.sh
Source11: check_CVE-2013-4287.rb
Source12: check_CVE-2013-4363.rb
Patch0: ruby-2.3.0-ruby_version.patch
Requires:   ruby(release)
Recommends: rubygem(bundler) >= 4.0
Recommends: rubygem(rdoc) >= %{rdoc_version}
Recommends: rubygem(io-console)
Requires:   rubygem(psych) >= %{psych_version}
%if %{without bootstrap}
%endif
Provides:   gem = %{version}-%{release}
Provides:   ruby(rubygems) = %{version}-%{release}
Provides:   bundled(rubygem-molinillo) = %{rubygems_molinillo_version}
Provides:   bundled(rubygem-net-http) = %{rubygems_net_http_version}
Provides:   bundled(rubygem-net-protocol) = %{rubygems_net_protocol_version}
Provides:   bundled(rubygem-optparse) = %{rubygems_optparse_version}
Provides:   bundled(rubygem-resolv) = %{rubygems_resolv_version}
Provides:   bundled(rubygem-securerandom) = %{rubygems_securerandom_version}
Provides:   bundled(rubygem-timeout) = %{rubygems_timeout_version}
Provides:   bundled(rubygem-tsort) = %{rubygems_tsort_version}
Provides:   bundled(rubygem-uri) = %{rubygems_uri_version}
BuildArch:  noarch
# oreon:deps
BuildRequires:  /usr/bin/cmake
BuildRequires:  /usr/bin/gcc
BuildRequires:  /usr/bin/git
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(rake)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygem(test-unit-ruby-core)
BuildRequires:  rubygem(webrick)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
RubyGems is the Ruby standard for publishing and managing third party
libraries.

%package    doc
Summary:    Documentation for %{name}
License:    Ruby or MIT
Requires:   ruby(%{name}) = %{version}-%{release}
BuildArch:  noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -b 2

%patch 0 -p1

%build

%install
mkdir -p %{buildroot}{%{rubygems_dir},%{gem_dir}}/
GEM_HOME=%{buildroot}%{gem_dir} \
    ruby setup.rb \
    --document rdoc,ri \
    --prefix=/ \
    --backtrace \
    --no-regenerate-binstubs \
    --destdir=%{buildroot}%{rubygems_dir}/
mkdir -p %{buildroot}%{_bindir}
mv %{buildroot}%{rubygems_dir}/bin/gem %{buildroot}%{_bindir}/.
rm -rf %{buildroot}%{rubygems_dir}/bin
mv %{buildroot}/%{rubygems_dir}/lib/* %{buildroot}%{rubygems_dir}/.
rmdir %{buildroot}%{rubygems_dir}/lib
rm %{buildroot}%{rubygems_dir}/rubygems/ssl_certs/rubygems.org/GlobalSign.pem
rmdir %{buildroot}%{rubygems_dir}/rubygems/ssl_certs/rubygems.org/
mkdir -p %{buildroot}%{rubygems_dir}/rubygems/defaults
install -cpm 0644 %{SOURCE1} %{buildroot}%{rubygems_dir}/rubygems/defaults/
mkdir -p %{buildroot}%{gem_dir}/{cache,gems,specifications,extensions,doc,plugins}
mkdir -p %{buildroot}%{gem_extdir}/ruby
mkdir -p %{buildroot}%{gem_dir}/specifications/default
rm -vr %{buildroot}%{rubygems_dir}/bundler*
rm -vr %{buildroot}%{rubygems_dir}/gems/bundler*
rm %{buildroot}%{rubygems_dir}/specifications/default/bundler-*.gemspec
rmdir %{buildroot}%{rubygems_dir}/specifications/default/
rmdir %{buildroot}%{rubygems_dir}/specifications/
rm %{buildroot}%{rubygems_dir}/rubygems/ssl_certs/.document
rm %{buildroot}%{rubygems_dir}/rubygems/vendor/.document
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

mkdir -p lib/rubygems/defaults
touch lib/rubygems/defaults/operating_system.rb
RUBYOPT=-Ibundler/lib ruby -rbundler/version -e " \
  puts '%%{bundler_version}: %{bundler_version}' ; \
  puts %Q[Bundler::VERSION: #{Bundler::VERSION}] ; \
  exit 1 if Bundler::VERSION != '%{bundler_version}' ; \
"
RUBYOPT=-Ilib ruby -e " \
  module Gem; class Resolver; end; end; \
  require 'rubygems/vendor/molinillo/lib/molinillo/gem_metadata'; \
  puts '%%{rubygems_molinillo_version}: %{rubygems_molinillo_version}'; \
  puts %Q[Gem::Molinillo::VERSION: #{Gem::Molinillo::VERSION}]; \
  exit 1 if Gem::Molinillo::VERSION != '%{rubygems_molinillo_version}'; \
"
RUBYOPT=-Ilib ruby -e " \
  module Gem; module Net; end; end; \
  require 'rbconfig'; \
  require 'rubygems/vendor/net-http/lib/net/http'; \
  puts '%%{rubygems_net_http_version}: %{rubygems_net_http_version}'; \
  puts %Q[Gem::Net::HTTP::VERSION: #{Gem::Net::HTTP::VERSION}]; \
  exit 1 if Gem::Net::HTTP::VERSION != '%{rubygems_net_http_version}'; \
"
RUBYOPT=-Ilib ruby -e " \
  module Gem; module Net; end; end; \
  require 'rubygems/vendor/net-protocol/lib/net/protocol'; \
  puts '%%{rubygems_net_protocol_version}: %{rubygems_net_protocol_version}'; \
  puts %Q[Gem::Net::Protocol::VERSION: #{Gem::Net::Protocol::VERSION}]; \
  exit 1 if Gem::Net::Protocol::VERSION != '%{rubygems_net_protocol_version}'; \
"
RUBYOPT=-Ilib ruby -e " \
  module Gem; end; \
  require 'rubygems/vendor/optparse/lib/optparse'; \
  puts '%%{rubygems_optparse_version}: %{rubygems_optparse_version}'; \
  puts %Q[Gem::OptionParser::Version: #{Gem::OptionParser::Version}]; \
  exit 1 if Gem::OptionParser::Version != '%{rubygems_optparse_version}'; \
"
RUBYOPT=-Ilib ruby -e " \
  module Gem; end; \
  require 'rbconfig'; \
  require 'rubygems/vendor/resolv/lib/resolv'; \
  puts '%%{rubygems_resolv_version}: %{rubygems_resolv_version}'; \
  puts %Q[Gem::Resolv::VERSION: #{Gem::Resolv::VERSION}]; \
  exit 1 if Gem::Resolv::VERSION != '%{rubygems_resolv_version}'; \
"
RUBYOPT=-Ilib ruby -e " \
  module Gem; module Random; end; end; \
  require 'rubygems/vendor/securerandom/lib/securerandom'; \
  puts '%%{rubygems_securerandom_version}: %{rubygems_securerandom_version}'; \
  puts %Q[Gem::SecureRandom::VERSION: #{Gem::SecureRandom::VERSION}]; \
  exit 1 if Gem::SecureRandom::VERSION != '%{rubygems_securerandom_version}'; \
"
RUBYOPT=-Ilib ruby -e " \
  module Gem; end; \
  require 'rubygems/vendor/timeout/lib/timeout'; \
  puts '%%{rubygems_timeout_version}: %{rubygems_timeout_version}'; \
  puts %Q[Gem::Timeout::VERSION: #{Gem::Timeout::VERSION}]; \
  exit 1 if Gem::Timeout::VERSION != '%{rubygems_timeout_version}'; \
"
RUBYOPT=-Ilib ruby -e " \
  module Gem; end; \
  require 'rubygems/vendor/tsort/lib/tsort'; \
  puts '%%{rubygems_tsort_version}: %{rubygems_tsort_version}'; \
  puts %Q[Gem::TSort::VERSION: #{Gem::TSort::VERSION}]; \
  exit 1 if Gem::TSort::VERSION != '%{rubygems_tsort_version}'; \
"
RUBYOPT=-Ilib ruby -e " \
  module Gem; end; \
  require 'rubygems/vendor/uri/lib/uri/version'; \
  puts '%%{rubygems_uri_version}: %{rubygems_uri_version}'; \
  puts %Q[Gem::URI::VERSION: #{Gem::URI::VERSION}]; \
  exit 1 if Gem::URI::VERSION != '%{rubygems_uri_version}'; \
"
%if %{without bootstrap}
mv test/test_changelog_generator.rb{,.disabled}
export RUBYOPT="-I$(ruby -e 'size = $LOAD_PATH.size; %w(rake test-unit rdoc webrick core_assertions).each {|r| require r}; puts $LOAD_PATH[...-size].join ?:')"
GEM_COMMAND="skip test_realworld_{default_gem,upgraded_default_gem}" \
  ruby -Itest:bundler/lib:lib -e 'Dir.glob "./test/**/test_*.rb", &method(:require)' - \
ruby %{SOURCE11}
ruby %{SOURCE12}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rubygems-doc -f %{oreon_filedir}/rubygems-doc.list

%changelog

%autochangelog
