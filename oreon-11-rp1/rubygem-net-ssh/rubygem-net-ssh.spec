%global source1_hash 312f7aebe197a63c7ca8d5fce8a5dbdc668dcc9747c582003c5a9b1f250c90c3
%global source0_hash 172076c4b30ce56fb25a03961b0c4da14e1246426401b0f89cba1a3b54bf3ef0
%global gem_name net-ssh
Name: rubygem-%{gem_name}
Version: 7.3.0
Release:        5%{?dist}
Summary:        Net::SSH: a pure-Ruby implementation of the SSH2 client protocol
License: MIT
URL: https://github.com/net-ssh/net-ssh
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/net-ssh/net-ssh/archive/refs/tags/v7.3.0.tar.gz
Recommends: rubygem(bcrypt_pbkdf)
Recommends: rubygem(ed25519)
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(base64)
BuildRequires:  rubygem(bcrypt_pbkdf)
BuildRequires:  rubygem(ed25519)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(mocha)
BuildRequires:  rubygems-devel
# /oreon:deps
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
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

%gemspec_add_dep -g openssl

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ln -s %{_builddir}/test test
mv test/transport/kex/test_curve25519_sha256.rb{,.disable}
sed -i 's;\[false, :standard\].each do |compress|;[false].each do |compress|;g' test/transport/test_packet_stream.rb
OPENSSL_CONF="$PWD/test/openssl3.conf" \
OPENSSL_ENABLE_SHA1_SIGNATURES=1 \
  ruby -Ilib:test test/test_all.rb
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-net-ssh-doc -f %{oreon_filedir}/rubygem-net-ssh-doc.list

%changelog

%autochangelog
