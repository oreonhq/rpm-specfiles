%global source0_hash ef0675e7094b9666bc4552242f5ecc0510e56c332c8ce8151f7be434a59c84fa

# Upstream git:
# https://github.com/rubygems/rubygems.git
#

# Bundled libraries versions
%global rubygems_molinillo_version 0.8.0
%global rubygems_net_http_version 0.7.0
%global rubygems_net_protocol_version 0.2.2
%global rubygems_optparse_version 0.8.0
%global rubygems_resolv_version 0.7.0
%global rubygems_securerandom_version 0.4.1
%global rubygems_timeout_version 0.4.4
%global rubygems_tsort_version 0.2.0
%global rubygems_uri_version 1.1.1

# Requires versions
%global bundler_version 4.0.6
%global psych_version 5.3.1
%global rdoc_version 7.0.3

# The RubyGems library has to stay out of Ruby directory tree, since the
# RubyGems should be share by all Ruby implementations.
%global rubygems_dir %(ruby -e "puts RbConfig::CONFIG['rubygemsdir']")

# TODO: These folders should go into rubygem-filesystem but how to achieve it,
# since noarch package cannot provide arch dependent subpackages?
# http://rpm.org/ticket/78
%global gem_extdir %{_exec_prefix}/lib{,64}/gems

# Executing testsuite (enabling %%check section) will cause dependency loop.
# To avoid dependency loop when necessary, please set the following value to 0
%bcond_with bootstrap

# It cannot be relied on %%{_libdir} for noarch packages. Query Ruby for
# the right value.
# https://fedorahosted.org/rel-eng/ticket/5257
%{!?buildtime_libdir:%global buildtime_libdir $(ruby -rrbconfig -e 'puts RbConfig::CONFIG["libdir"]')}

Summary: The Ruby standard for packaging ruby libraries
Name: rubygems
Version: 4.0.6
Release: 1%{?dist}
# BSD-2-Clause OR Ruby:
#   lib/rubygems/net-http/
#   lib/rubygems/net-protocol/
#   lib/rubygems/optparse/
#   lib/rubygems/resolv/
#   lib/rubygems/securerandom/
#   lib/rubygems/timeout/
#   lib/rubygems/tsort/
#   lib/rubygems/uri/
# MIT: lib/rubygems/package_task.rb
# MIT: lib/rubygems/resolver/molinillo
# Ruby OR BSD-2-Clause OR GPL-1.0-or-later: lib/net/protocol.rb
License: %{shrink:
    (Ruby OR MIT) AND
    BSD-2-Clause AND
    (BSD-2-Clause OR Ruby) AND
    (Ruby OR BSD-2-Clause OR GPL-1.0-or-later) AND
    MIT
}
URL: https://rubygems.org/
Source0: https://rubygems.org/rubygems/%{name}-%{version}.tgz
# Sources from the works by Vít Ondruch <vondruch@redhat.com>
# NOTE: Keep Source1 in sync with ruby.spec.
Source1: operating_system.rb
Source2: %{name}-%{version}-test-missing-files.tar.gz
# %%SOURCE2 is created by $ bash %%SOURCE2 %%version
Source3: rubygems-create-missing-test-files.sh
# http://seclists.org/oss-sec/2013/q3/att-576/check_CVE-2013-4287_rb.bin
# Slightly modified for exit status
Source11: check_CVE-2013-4287.rb
# http://seclists.org/oss-sec/2013/q3/att-621/check_CVE-2013-XXXX_rb.bin
# Slightly modified for exit status,
# Also modified to match:
# http://seclists.org/oss-sec/2013/q3/605
Source12: check_CVE-2013-4363.rb
# Fix ruby_version abuse.
# https://bugs.ruby-lang.org/issues/11002
# NOTE: Keep this patch in sync with ruby.spec.
Patch0: ruby-2.3.0-ruby_version.patch

Requires:   ruby(release)
Recommends: rubygem(bundler) >= 4.0
Recommends: rubygem(rdoc) >= %{rdoc_version}
Recommends: rubygem(io-console)
Requires:   rubygem(psych) >= %{psych_version}
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
%if %{without bootstrap}
# For mkmf.rb
BuildRequires: ruby-devel
BuildRequires: rubygem(test-unit)
BuildRequires: %{_bindir}/cmake
BuildRequires: %{_bindir}/git
BuildRequires: %{_bindir}/gcc
BuildRequires: rubygem(rake)
BuildRequires: rubygem(webrick)
BuildRequires: rubygem(test-unit-ruby-core)
%endif
Provides:   gem = %{version}-%{release}
Provides:   ruby(rubygems) = %{version}-%{release}
# https://github.com/rubygems/rubygems/pull/1189#issuecomment-121600910
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
# Nothing

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
# No longer needed
rmdir %{buildroot}%{rubygems_dir}/lib

# Kill bundled certificates, as they should be part of ca-certificates.
rm %{buildroot}%{rubygems_dir}/rubygems/ssl_certs/rubygems.org/GlobalSign.pem
rmdir %{buildroot}%{rubygems_dir}/rubygems/ssl_certs/rubygems.org/

# Install custom operating_system.rb.
mkdir -p %{buildroot}%{rubygems_dir}/rubygems/defaults
install -cpm 0644 %{SOURCE1} %{buildroot}%{rubygems_dir}/rubygems/defaults/

# Create gem folders.
mkdir -p %{buildroot}%{gem_dir}/{cache,gems,specifications,extensions,doc,plugins}
mkdir -p %{buildroot}%{gem_extdir}/ruby

# Create below
mkdir -p %{buildroot}%{gem_dir}/specifications/default

# Remove bundled bundler
rm -vr %{buildroot}%{rubygems_dir}/bundler*
rm -vr %{buildroot}%{rubygems_dir}/gems/bundler*
rm %{buildroot}%{rubygems_dir}/specifications/default/bundler-*.gemspec
rmdir %{buildroot}%{rubygems_dir}/specifications/default/
rmdir %{buildroot}%{rubygems_dir}/specifications/

# Remove unneeded .document file
rm %{buildroot}%{rubygems_dir}/rubygems/ssl_certs/.document
rm %{buildroot}%{rubygems_dir}/rubygems/vendor/.document

%check
# Create an empty operating_system.rb, so that the system's one doesn't get used,
# otherwise the test suite fails.
mkdir -p lib/rubygems/defaults
touch lib/rubygems/defaults/operating_system.rb

# Check Bundler version.
RUBYOPT=-Ibundler/lib ruby -rbundler/version -e " \
  puts '%%{bundler_version}: %{bundler_version}' ; \
  puts %Q[Bundler::VERSION: #{Bundler::VERSION}] ; \
  exit 1 if Bundler::VERSION != '%{bundler_version}' ; \
"

# Check Rubygems bundled dependencies versions.

# Molinillo.
RUBYOPT=-Ilib ruby -e " \
  module Gem; class Resolver; end; end; \
  require 'rubygems/vendor/molinillo/lib/molinillo/gem_metadata'; \
  puts '%%{rubygems_molinillo_version}: %{rubygems_molinillo_version}'; \
  puts %Q[Gem::Molinillo::VERSION: #{Gem::Molinillo::VERSION}]; \
  exit 1 if Gem::Molinillo::VERSION != '%{rubygems_molinillo_version}'; \
"

# Net::HTTP.
RUBYOPT=-Ilib ruby -e " \
  module Gem; module Net; end; end; \
  require 'rbconfig'; \
  require 'rubygems/vendor/net-http/lib/net/http'; \
  puts '%%{rubygems_net_http_version}: %{rubygems_net_http_version}'; \
  puts %Q[Gem::Net::HTTP::VERSION: #{Gem::Net::HTTP::VERSION}]; \
  exit 1 if Gem::Net::HTTP::VERSION != '%{rubygems_net_http_version}'; \
"

# Net::Protocol.
RUBYOPT=-Ilib ruby -e " \
  module Gem; module Net; end; end; \
  require 'rubygems/vendor/net-protocol/lib/net/protocol'; \
  puts '%%{rubygems_net_protocol_version}: %{rubygems_net_protocol_version}'; \
  puts %Q[Gem::Net::Protocol::VERSION: #{Gem::Net::Protocol::VERSION}]; \
  exit 1 if Gem::Net::Protocol::VERSION != '%{rubygems_net_protocol_version}'; \
"

# OptParse.
RUBYOPT=-Ilib ruby -e " \
  module Gem; end; \
  require 'rubygems/vendor/optparse/lib/optparse'; \
  puts '%%{rubygems_optparse_version}: %{rubygems_optparse_version}'; \
  puts %Q[Gem::OptionParser::Version: #{Gem::OptionParser::Version}]; \
  exit 1 if Gem::OptionParser::Version != '%{rubygems_optparse_version}'; \
"

# Resolv.
RUBYOPT=-Ilib ruby -e " \
  module Gem; end; \
  require 'rbconfig'; \
  require 'rubygems/vendor/resolv/lib/resolv'; \
  puts '%%{rubygems_resolv_version}: %{rubygems_resolv_version}'; \
  puts %Q[Gem::Resolv::VERSION: #{Gem::Resolv::VERSION}]; \
  exit 1 if Gem::Resolv::VERSION != '%{rubygems_resolv_version}'; \
"

# SecureRandom.
RUBYOPT=-Ilib ruby -e " \
  module Gem; module Random; end; end; \
  require 'rubygems/vendor/securerandom/lib/securerandom'; \
  puts '%%{rubygems_securerandom_version}: %{rubygems_securerandom_version}'; \
  puts %Q[Gem::SecureRandom::VERSION: #{Gem::SecureRandom::VERSION}]; \
  exit 1 if Gem::SecureRandom::VERSION != '%{rubygems_securerandom_version}'; \
"

# Timeout.
RUBYOPT=-Ilib ruby -e " \
  module Gem; end; \
  require 'rubygems/vendor/timeout/lib/timeout'; \
  puts '%%{rubygems_timeout_version}: %{rubygems_timeout_version}'; \
  puts %Q[Gem::Timeout::VERSION: #{Gem::Timeout::VERSION}]; \
  exit 1 if Gem::Timeout::VERSION != '%{rubygems_timeout_version}'; \
"

# TSort
RUBYOPT=-Ilib ruby -e " \
  module Gem; end; \
  require 'rubygems/vendor/tsort/lib/tsort'; \
  puts '%%{rubygems_tsort_version}: %{rubygems_tsort_version}'; \
  puts %Q[Gem::TSort::VERSION: #{Gem::TSort::VERSION}]; \
  exit 1 if Gem::TSort::VERSION != '%{rubygems_tsort_version}'; \
"

# URI.
RUBYOPT=-Ilib ruby -e " \
  module Gem; end; \
  require 'rubygems/vendor/uri/lib/uri/version'; \
  puts '%%{rubygems_uri_version}: %{rubygems_uri_version}'; \
  puts %Q[Gem::URI::VERSION: #{Gem::URI::VERSION}]; \
  exit 1 if Gem::URI::VERSION != '%{rubygems_uri_version}'; \
"

%if %{without bootstrap}
# util directory with changelog generator are not shipped in release archive.
mv test/test_changelog_generator.rb{,.disabled}

# Put all required libraries on the `$LOAD_PATH`, where the original Ruby
# `require` can find them. This prevents the RubyGems load machinery from
# running and failing to find `gem.build_complete` files for sytem packages
# and therefore raising warnings such as: "Ignoring json-2.5.1 because its
# extensions are not built. Try: gem pristine json --version 2.5.1".
# https://github.com/rubygems/rubygems/pull/4446
export RUBYOPT="-I$(ruby -e 'size = $LOAD_PATH.size; %w(rake test-unit rdoc webrick core_assertions).each {|r| require r}; puts $LOAD_PATH[...-size].join ?:')"

# Rakefile is not shipped anymore => emulate its content.
# https://github.com/rubygems/rubygems/blob/v3.3.22/Rakefile#L56-L64
# The `test_realworld_{default_gem,upgraded_default_gem}` needs the same
# treatment as the have in Ruby repository. Use `GEM_COMMAND` to skip them.
GEM_COMMAND="skip test_realworld_{default_gem,upgraded_default_gem}" \
  ruby -Itest:bundler/lib:lib -e 'Dir.glob "./test/**/test_*.rb", &method(:require)' - \

# CVE vulnerability check
ruby %{SOURCE11}
ruby %{SOURCE12}
%endif

%files
%doc CHANGELOG.md
%doc CODE_OF_CONDUCT.md
%doc CONTRIBUTING.md
%doc README.md
%doc SECURITY.md
%license MIT.txt LICENSE.txt
%{_bindir}/gem
%dir %{rubygems_dir}
%{rubygems_dir}/rubygems
%{rubygems_dir}/rubygems.rb
%license %{rubygems_dir}/rubygems/vendor/*/{LICENSE.txt,COPYING}

# Explicitly include only RubyGems directory strucure to avoid accidentally
# packaged content.
%dir %{gem_dir}
%dir %{gem_dir}/build_info
%dir %{gem_dir}/cache
%dir %{gem_dir}/doc
%dir %{gem_dir}/extensions
%dir %{gem_dir}/gems
%dir %{gem_dir}/plugins
%dir %{gem_dir}/specifications
%dir %{gem_dir}/specifications/default
%dir %{_exec_prefix}/lib*/gems
%dir %{_exec_prefix}/lib*/gems/ruby

%files	doc
%doc %{gem_dir}/doc/*

%changelog
%autochangelog
