%global source0_hash 5322347ad788413d78e7d4211a414bfef3fbf3686f318d91e5a23881765ac474

Name:       perl-Net-DHCP
Version:    0.700
Release:    12%{?dist}
Summary:    Set of classes for basic handling of DHCP packets

License:    MIT
URL:        https://metacpan.org/release/Net-DHCP
Source0:    https://cpan.metacpan.org/authors/id/D/DJ/DJZORT/Net-DHCP-0.7.tar.gz

Buildarch:      noarch

# build requirements
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
# runtime requirements
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)

%{?perl_default_filter}

%description
Net::DHCP is a DHCP set of classes designed to handle basic DHCP
handling. It can be used to develop either client, server or relays.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-DHCP-0.7
# Fix permissions
find examples -type f -exec chmod 644 {} 2>/dev/null \;
chmod 644 README
chmod 644 Changes
# Some tests require Net::Frame::Simple and Net::Frame::Dump
# which are under the Artistic 1.0 license and cannot be
# packaged for Fedora.
rm -f t/10*.t

%build
/usr/bin/perl Build.PL installdirs=vendor
./Build
# See README
rm -rf docs

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
# Permissions
find %{buildroot} -type f -exec chmod 644 {} 2>/dev/null \;

%check
./Build test

%files
%license LICENSE
%doc README examples/ Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
