%global source0_hash abecb1783385f001d35ae769408ba4e7113d2f91bddbefb3eee0e4f327b59992

Name:           perl-NetPacket
Version:        1.8.0
Release:        1%{?dist}
Summary:        Assemble/disassemble network packets at the protocol level
# lib/NetPacket.pm:     Artistic-2.0
# lib/NetPacket/IPX.pm: GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/NetPacket/SLL.pm  Artistic-2.0
# lib/NetPacket/SLL2.pm:    Artistic-2.0
# lib/NetPacket/USBMon.pm:  GPL-1.0-or-later OR Artistic-1.0-Perl
# LICENSE:      Artistic-2.0 text
## Not in any binary package
# repackage.sh:     GPL-2.0-or-later
## Stripped from the source archive
# CODE_OF_CONDUCT.md:   CC-BY ???
#                       "adapted from
#                       <https://www.contributor-covenant.org/version/2/0/code_of_conduct.html>"
#                       Probaly Hippocratic License 3.0
#                       <https://github.com/EthicalSource/contributor_covenant/blob/release/LICENSE.md>.
#                       FIXME: License clarification requested
#                       <https://github.com/EthicalSource/contributor_covenant/issues/1583>?
#                       FIXME: waiting on SPDX
#                       <https://github.com/spdx/license-list-XML/issues/2931> and
#                       on Fedora legal approval
#                       <https://gitlab.com/fedora/legal/fedora-license-data/-/issues/717>
#                       FIXME: A copy of the license is missing
#                       <https://github.com/yanick/netpacket/issues/19>
License:        Artistic-2.0 AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
SourceLicense:  %{license} AND GPL-2.0-or-later
URL:            https://metacpan.org/release/NetPacket
# Upstream URL <https://cpan.metacpan.org/authors/id/Y/YA/YANICK/NetPacket-%%{version}.tar.gz>
# Repackaged with "./repackage.sh %%{version}" because of CODE_OF_CONDUCT.md.
Source0:        NetPacket-%{version}_repackaged.tar.gz
Source1:        repackage.sh
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
# Net::Pcap and Net::PcapUtils are nowhere used.
BuildRequires:  perl(parent)
BuildRequires:  perl(Socket) >= 1.87
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test2::Bundle::More)
# Optional tests:
# CPAN::Meta not helpful
# CPAN::Meta::Prereqs not helpful

%description
NetPacket provides a base class for a cluster of modules related to decoding
and encoding of network protocols. Each NetPacket descendant module knows how
to encode and decode packets for the network protocol it implements. Consult
the documentation for the module in question for protocol-specific
implementation.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n NetPacket-%{version}
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
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset AUTHOR_TESTING PERL_COMPILE_TEST_DEBUG
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING PERL_COMPILE_TEST_DEBUG
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING.md README SECURITY.md
%{perl_vendorlib}/NetPacket
%{perl_vendorlib}/NetPacket.pm
%{_mandir}/man3/NetPacket.*
%{_mandir}/man3/NetPacket::*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
