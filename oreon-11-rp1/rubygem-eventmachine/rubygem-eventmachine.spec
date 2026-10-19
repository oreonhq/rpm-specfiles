%global source0_hash 994016e42aa041477ba9cff45cbe50de2047f25dd418eba003e84f0d16560972
%global gem_name eventmachine
%{!?network: %global network 0}
Name: rubygem-%{gem_name}
Version: 1.2.7
Release:        1%{?dist}
Summary:        Ruby/EventMachine library
License: GPL-2.0-only OR Ruby
URL: http://rubyeventmachine.com
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: rubygem-eventmachine-1.2.7-OpenSSL-1.1.0-test-updates.patch
Patch1: rubygem-eventmachine-1.2.7-Update-runtime-files-for-TLS13-no-SSL-OpenSSL-lib-info.patch
Patch2: rubygem-eventmachine-1.2.7-Move-console-SSL-Info-code-to-em_test_helper.patch
Patch3: rubygem-eventmachine-1.2.7-Openssl-1.1.1-updates.patch
Patch4: rubygem-eventmachine-1.2.7-Increase-certificate-length.patch
Patch5: rubygem-eventmachine-1.2.7-Bump-TLS-version.patch
Patch6: rubygem-eventmachine-1.2.7-Fix-intermittent-tests.patch
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(ostruct)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
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

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/
rm -rf %{buildroot}%{gem_instdir}/ext/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

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
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-eventmachine-doc -f %{oreon_filedir}/rubygem-eventmachine-doc.list

%changelog

%autochangelog
