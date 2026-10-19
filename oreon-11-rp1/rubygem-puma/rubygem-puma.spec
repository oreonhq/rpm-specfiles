%global source0_hash 3eb41999d00733280be3faeb00d610331b6965a537a8cd3d905f316c38575b44
%global gem_name puma
%bcond_without ragel
%bcond_without help2man
%global __requires_exclude_from ^%{gem_instdir}/docs/jungle.*$
Name: rubygem-%{gem_name}
Version: 6.4.2
Release:        1%{?dist}
Summary:        A simple, fast, threaded, and highly concurrent HTTP 1.1 server
License: BSD-3-Clause AND MIT
URL: https://puma.io
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: %{gem_name}-%{version}-tests.txz
Source3: %{gem_name}-%{version}-examples.txz
Patch2: rubygem-puma-3.6.0-fedora-crypto-policy-cipher-list.patch
Patch3: rubygem-puma-6.4.2-test-helper-rb-allow-to-run-with-new-and-old-Minitest.patch
Patch4: rubygem-puma-6.4.2-Ran-ruby-examples-puma-chain-cert-generate-chain-test-rb-.patch
Patch5: rubygem-puma-6.4.2-Renewed-test-certificates.patch
Patch6: rubygem-puma-6.4.2-Update-all-certs.patch
Patch7: rubygem-puma-3.4.2-CI-Ruby-head-changed-odd-backtick-in-error-messages-to.patch
Patch8: rubygem-puma-pr3743-update-all-certs.patch
Patch9: rubygem-puma-pr3615-ruby40-OpenSSL-set_minmax_proto_version-removal.patch
Patch10: rubygem-puma-6.4.2-minitest6.patch
%if %{with ragel}
%endif
%if %{with help2man}
%endif
Provides: bundled(rubygem-sd_notify) = 0.1.1
# oreon:deps
BuildRequires:  //bin/rackup
BuildRequires:  //bin/ragel
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  openssl-devel
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(minitest-mock)
BuildRequires:  rubygem(minitest-stub-const)
BuildRequires:  rubygem(nio4r)
BuildRequires:  rubygem(rack)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Puma is a simple, fast, threaded, and highly parallel HTTP 1.1 server for
Ruby/Rack applications. Puma is intended for use in both development and
production environments. It's great for highly parallel Ruby implementations
such as Rubinius and JRuby as well as as providing process worker support to
support CRuby well.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n  %{gem_name}-%{version} -b 1 -b 3

%patch 2 -p1

pushd %{builddir}
%patch 3 -p1
%patch 4 -p1
%patch 5 -p1
%patch 6 -p1
%patch 7 -p1
%patch 8 -p1
%patch 9 -p1
%patch 10 -p1
popd

%if %{with ragel}
# Regenarate the parser.
# https://fedoraproject.org/wiki/Packaging:Guidelines#Use_of_pregenerated_code
rm -f ext/puma_http11/http11_parser.c
ragel ext/puma_http11/http11_parser.rl -G2 -I ext/puma_http11 \
  -o ext/puma_http11/http11_parser.c
%endif

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{gem_extdir_mri}/puma
cp -a .%{gem_extdir_mri}/gem.build_complete %{buildroot}%{gem_extdir_mri}/
cp -a .%{gem_extdir_mri}/puma/*.so %{buildroot}%{gem_extdir_mri}/puma
rm -rf %{buildroot}%{gem_instdir}/ext/
mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x
find %{buildroot}%{gem_instdir}/bin -type f | \
  xargs sed -i 's|^#!/usr/bin/env ruby$|#!/usr/bin/ruby|'
%if %{with help2man}
export RUBYOPT="-I%{buildroot}%{gem_extdir_mri}:%{buildroot}%{gem_libdir}"
mkdir -p %{buildroot}%{_mandir}/man1
help2man --no-discard-stderr -N -s1 -o %{buildroot}%{_mandir}/man1/%{gem_name}.1 \
    %{buildroot}/usr/share/gems/gems/%{gem_name}-%{version}/bin/%{gem_name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%check

pushd .%{gem_instdir}
cp -a %{_builddir}/test .
ln -s %{_builddir}/examples .
sed -i -e '/require..minitest\/proveit./ s/^/#/' test/helper.rb
sed -i '/prove_it!/ s/^/#/' test/helper.rb
mv test/test_url_map.rb{,.disable}
mv test/test_preserve_bundler_env.rb{,.disable}
mv test/test_worker_gem_independence.rb{,.disable}
sed -i -e '/^\s*def test_prune_bundler_with_multiple_workers$/a\
    skip_if :no_bundler' test/test_integration_pumactl.rb
mv test/test_puma_localhost_authority.rb{,.disable}
sed -i '/def test_ssl_self_signed_configuration_from_DSL/a\
    skip "Missing localhost gem"' test/test_config.rb
sed -i '/def test_ssl_run_with_localhost_authority/a\
    skip "Missing localhost gem"' test/test_integration_ssl.rb
mv test/test_integration_single.rb{,.disable}
mv test/test_integration_cluster.rb{,.disable}
mv test/test_plugin_systemd.rb{,.disable}
sed -i '/^  def test_plugin$/a\
    skip "Flaky test case"' test/test_plugin.rb
sed -i '/^  def test_multiple_requests_waiting_on_less_busy_worker$/a\
    skip "Flaky test case"' test/test_busy_worker.rb
sed -i '/^  def test_refork_cluster$/a\
    skip "Flaky test case"' test/test_integration_pumactl.rb
sed -i '/^  def test_sighup_redirects_io_cluster$/a\
    skip "Flaky test case"' test/test_redirect_io.rb
env -u NOTIFY_SOCKET \
TEST_CASE_TIMEOUT=300 \
RUBYOPT="-Ilib:$(dirs +1 -l)%{gem_extdir_mri}" \
ruby -e 'Dir.glob "./test/**/test_*.rb", &method(:require)' - -v
%if %{with help2man}
export RUBYOPT="-I%{buildroot}%{gem_extdir_mri}:%{buildroot}%{gem_libdir}"
%{buildroot}/usr/share/gems/gems/%{gem_name}-%{version}/bin/%{gem_name} --help 2> /dev/null \
  | grep -q '^puma <options> <rackup file>'
%endif
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-puma-doc -f %{oreon_filedir}/rubygem-puma-doc.list

%changelog

%autochangelog
