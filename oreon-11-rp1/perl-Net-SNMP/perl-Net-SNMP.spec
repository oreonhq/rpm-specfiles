%global source0_hash 14c37bc1cbb3f3cdc7d6c13e0f27a859f14cdcfd5ea54a0467a88bc259b0b741
Name:           perl-Net-SNMP
Version:        6.0.1
Release:        1%{?dist}
Summary:        Object oriented interface to SNMP
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-SNMP
Source0:        https://cpan.metacpan.org/authors/id/D/DT/DTOWN/Net-SNMP-v%{version}.tar.gz
Patch0:         Net-SNMP-v6.0.1-Switch_from_Socket6_to_Socket.patch
Patch1:         Net-SNMP-v6.0.1-Simple_rewrite_to_Digest-HMAC-helpers.patch
Patch2:         Net-SNMP-v6.0.1-Split_usm.t_to_two_parts.patch
Patch3:         Net-SNMP-v6.0.1-Add_tests_for_another_usm_scenarios.patch
Patch4:         Net-SNMP-v6.0.1-Rewrite_from_Digest-SHA1-to-Digest-SHA.patch
BuildArch:      noarch
Requires:       perl(Carp)
Requires:       perl(Crypt::DES) >= 2.03
Requires:       perl(Digest::HMAC_MD5) => 1.01
Requires:       perl(Digest::HMAC_SHA1) => 1.03
Requires:       perl(Digest::MD5) >= 2.11
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Crypt::DES|Digest::HMAC_MD5|Digest::HMAC_SHA1|Digest::MD5)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test)
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The Net::SNMP module implements an object oriented interface to the
Simple Network Management Protocol.  Perl applications can use the
module to retrieve or update information on a remote host using the
SNMP protocol.  The module supports SNMP version-1, SNMP version-2c
(Community-Based SNMPv2), and SNMP version-3.  The Net::SNMP module
assumes that the user has a basic understanding of the Simple Network
Management Protocol and related network management concepts.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Net-SNMP-v%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
perl -MConfig -pi -e 's|^#!.*perl|$Config{startperl}|' examples/*.pl

chmod -c a-x examples/*.pl

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Net-SNMP-tests -f %{oreon_filedir}/perl-Net-SNMP-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.0.1-45
- Prepare for Oreon 11 (RP1)
