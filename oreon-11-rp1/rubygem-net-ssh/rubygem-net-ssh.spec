%global source0_hash 379f1328dc88b19cdf8771f8b114188dfae05176efe9c19e979431397bbfeff5

# Generated from net-ssh-2.2.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name net-ssh

Name: rubygem-%{gem_name}
Version: 7.3.0
Release: 5%{?dist}
Summary: Net::SSH: a pure-Ruby implementation of the SSH2 client protocol
License: MIT
URL: https://github.com/net-ssh/net-ssh
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/net-ssh/net-ssh.git --no-checkout
# cd net-ssh && git archive -v --format=tar.gz -o net-ssh-7.3.0-tests.tar.gz v7.3.0 test/
Source1: %{gem_name}-%{version}-tests.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(base64)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(mocha)
# rubygem-ed25519 support
BuildRequires: rubygem(bcrypt_pbkdf)
BuildRequires: rubygem(ed25519)
Recommends: rubygem(bcrypt_pbkdf)
Recommends: rubygem(ed25519)
BuildArch: noarch

%description
Net::SSH: a pure-Ruby implementation of the SSH2 client protocol. It allows
you to write programs that invoke and interact with processes on remote
servers, via SSH2.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1

%gemspec_add_dep -g openssl

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/test test

# This requires rubygem-x25519 which is not yet in Fedora.
mv test/transport/kex/test_curve25519_sha256.rb{,.disable}

# Fedora switched from zlib to zlib-ng -> causes tests with compression to fail
# (compressed data is not same byte-to-byte) -> disable tests with compression
# https://github.com/net-ssh/net-ssh/issues/965
sed -i 's;\[false, :standard\].each do |compress|;[false].each do |compress|;g' test/transport/test_packet_stream.rb

# Use custom upstream OpenSSL config to enable all tested ciphers. There is
# a plan to remove outdated ciphers (see "To remove") which might make this
# unnecessary.
# https://github.com/net-ssh/net-ssh/issues/705
# Use OPENSSL_ENABLE_SHA1_SIGNATURES to enable SHA1 test cases to pass.
# https://github.com/net-ssh/net-ssh/issues/975#issuecomment-3270436202
OPENSSL_CONF="$PWD/test/openssl3.conf" \
OPENSSL_ENABLE_SHA1_SIGNATURES=1 \
  ruby -Ilib:test test/test_all.rb
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/appveyor.yml
%exclude %{gem_instdir}/{D,d}ocker*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGES.txt
%{gem_instdir}/Gemfile*
%doc %{gem_instdir}/ISSUE_TEMPLATE.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Manifest
%doc %{gem_instdir}/THANKS.txt
%{gem_instdir}/Rakefile
%{gem_instdir}/support
%doc %{gem_instdir}/SECURITY.md
%doc %{gem_instdir}/DEVELOPMENT.md
# Required to run tests
%{gem_instdir}/net-ssh.gemspec
%exclude %{gem_instdir}/net-ssh-public_cert.pem

%changelog
%autochangelog
