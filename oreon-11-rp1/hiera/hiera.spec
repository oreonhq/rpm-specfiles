%global source2_hash 4d5a9c73f97235eebe8c69f728aa2efcc8e1ee02282f972efdbbbd3a430be454
%global source1_hash d3ce0a0d4c074cfe37d361b8e86f17e80eb9bcefd34f0ebc84f2b55af3e4f4ae
%global source0_hash 1c258f6b290f0884f6b6e892985b58d0dd24f389b42f5911c83f392030c403e1
Name:           hiera
Version:        3.12.0
Release:        1%{?dist}
Summary:        A simple hierarchical database supporting plugin data sources
License:        Apache-2.0
URL:            https://github.com/puppetlabs/hiera
Source0:        https://downloads.puppetlabs.com/hiera/%{name}-%{version}.tar.gz
Source1:        https://downloads.puppetlabs.com/%{name}/%{name}-%{version}.tar.gz.asc
Source2:        https://downloads.puppetlabs.com/puppet-gpg-signing-key-20250406.pub
Patch0:         fix-puppetlab-paths.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  gnupg2
BuildRequires:  ruby-devel
BuildRequires:  rubygem(json)
BuildRequires:  rubygem(mocha)
BuildRequires:  rubygem(rspec)
# /oreon:deps
%description
A simple hierarchical database supporting plugin data sources.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q
%patch -P0 -p1

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_vendorlibdir}
mkdir -p %{buildroot}%{_sysconfdir}/puppet
mkdir -p %{buildroot}%{_bindir}
cp -pr lib/hiera %{buildroot}%{ruby_vendorlibdir}
cp -pr lib/hiera.rb %{buildroot}%{ruby_vendorlibdir}
install -p -m0755 bin/hiera %{buildroot}%{_bindir}
install -p -m0644 ext/hiera.yaml %{buildroot}%{_sysconfdir}/puppet
mkdir -p %{buildroot}%{_sharedstatedir}/hiera
%oreon_autofiles main

%check

rspec -Ilib spec
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
