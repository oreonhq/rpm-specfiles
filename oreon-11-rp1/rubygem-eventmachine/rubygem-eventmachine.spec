%global source0_hash 994016e42aa041477ba9cff45cbe50de2047f25dd418eba003e84f0d16560972

%global gem_name eventmachine

# This enables to run full test suite, where network connection is available.
# However, it must be disabled for Koji build.
%{!?network: %global network 0}

Name: rubygem-%{gem_name}
Version: 1.2.7
Release: 33%{?dist}
Summary: Ruby/EventMachine library
# Automatically converted from old format: GPLv2 or Ruby - review is highly recommended.
License: GPL-2.0-only OR Ruby
URL: http://rubyeventmachine.com
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Fix compatibility with OpenSSL 1.1.1.
# https://github.com/eventmachine/eventmachine/pull/789
Patch0: rubygem-eventmachine-1.2.7-OpenSSL-1.1.0-test-updates.patch
# https://github.com/eventmachine/eventmachine/pull/867/commits/0904385936ef4ecae4519f4f7b8f829a3608afcd
Patch1: rubygem-eventmachine-1.2.7-Update-runtime-files-for-TLS13-no-SSL-OpenSSL-lib-info.patch
# https://github.com/eventmachine/eventmachine/pull/867/commits/fc95df7a31ae5694f6a762c0c3d4f5c79c3ee40b
Patch2: rubygem-eventmachine-1.2.7-Move-console-SSL-Info-code-to-em_test_helper.patch
# https://github.com/eventmachine/eventmachine/pull/867/commits/dd6cec8d5278e11f2a1752aa7b4a712d53b1f1d3
Patch3: rubygem-eventmachine-1.2.7-Openssl-1.1.1-updates.patch
# Extend certificate length.
# https://github.com/eventmachine/eventmachine/pull/923
Patch4: rubygem-eventmachine-1.2.7-Increase-certificate-length.patch
# Fix `test_case_insensitivity(TestSslProtocols)` test case.
# This small change is part of big upstream commit:
# https://github.com/eventmachine/eventmachine/pull/868/commits/a7da18ed78a60f25162c944f497154f7769f08f0
Patch5: rubygem-eventmachine-1.2.7-Bump-TLS-version.patch
# Fix intermittent tests.
# https://github.com/eventmachine/eventmachine/pull/870
Patch6: rubygem-eventmachine-1.2.7-Fix-intermittent-tests.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc-c++
# Enables SSL support.
BuildRequires: openssl-devel
BuildRequires: rubygem(ostruct)
BuildRequires: rubygem(test-unit)

%description
EventMachine implements a fast, single-threaded engine for arbitrary network
communications. It's extremely easy to use in Ruby. EventMachine wraps all
interactions with IP sockets, allowing programs to concentrate on the
implementation of network protocols. It can be used to create both network
servers and clients. To create a server or client, a Ruby program only needs
to specify the IP address and port, and provide a Module that implements the
communications protocol. Implementations of several standard network protocols
are provided with the package, primarily to serve as examples. The real goal
of EventMachine is to enable programs to easily interface with other programs
using TCP/IP, especially if custom protocols are required.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

# Make the package compliant with Fedora's crypto policies.
# https://fedoraproject.org/wiki/Packaging:CryptoPolicies
sed -i '/SSL_CTX_set_cipher_list/ s/".*"/"PROFILE=SYSTEM"/' ext/ssl.cpp

%patch 0 -p1
%patch 1 -p1
%patch 2 -p1
%patch 3 -p1
%patch 4 -p1
%patch 5 -p1
%patch 6 -p1

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

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

%check
pushd .%{gem_instdir}

ruby -Ilib:$(dirs +1)%{gem_extdir_mri}:tests -e "Dir.glob './tests/**/test_*.rb', &method(:require)" -- \
  --verbose \
  --ignore-name /^test_.*v3.*$/ \
  --ignore-name /^test_no_ecdh_curve$/ \
  --ignore-name=/^test_cookie$/ \
  --ignore-name=/^test_http_client$/ \
  --ignore-name=/^test_http_client_1$/ \
  --ignore-name=/^test_http_client_2$/ \
  --ignore-name=/^test_version_1_0$/ \
  --ignore-name=/^test_https_get$/ \
  --ignore-name=/^test_get$/ \
  --ignore-name=/^test_get_pipeline$/ \
  --ignore-name=/^test_ipv6_udp_local_server$/ \
  `# Ruby 3.0 related test failure` \
  `# https://github.com/eventmachine/eventmachine/issues/941` \
  --ignore-name=/^test_em_system_pid$/ \
%if 0%{network} < 1
  --ignore-name=/^test_a$/ \
  --ignore-name=/^test_a_pair$/ \
  --ignore-name=/^test_bad_host$/ \
  --ignore-name=/^test_failure_timer_cleanup$/ \
  --ignore-name=/^test_timer_cleanup$/ \
  --ignore-name=/^test_nameserver$/ \
  --ignore-name=/^test_invalid_address_bind_connect_dst$/ \
  --ignore-name=/^test_invalid_address_bind_connect_src$/ \
%endif

# TODO: This fails on ppc64 :/
# Moreover it appears abandoned upstream:
# https://github.com/eventmachine/eventmachine/issues/924
#EM_PURE_RUBY=true ruby -Ilib:tests -e "(Dir.glob('./tests/**/test_pure*.rb') + Dir.glob('./tests/**/test_ssl*.rb')).each {|f| require f}" -- \
#   --verbose \
#   --ignore-name /^test_.*v3.*$/ \
#   --ignore-name /^test_no_ecdh_curve$/ \
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%license %{gem_instdir}/GNU
%license %{gem_instdir}/LICENSE

%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/docs
%{gem_instdir}/examples
# TODO: Hmm, we can build also JRuby bindigs.
%{gem_instdir}/java
%{gem_instdir}/rakelib
%{gem_instdir}/tests

%changelog
%autochangelog
