%global source0_hash dfba394a6166a5a5e35ce763f408f97788047cc39ce5acad802e281432c88011

Name:           perl-Net-Jabber
Version:        2.0
Release:        57%{?dist}
Summary:        Jabber Perl Library
License:        ( GPL-1.0-or-later OR Artistic-1.0-Perl ) OR LGPL-2.0-or-later
URL:            https://metacpan.org/release/Net-Jabber
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REATMON/Net-Jabber-%{version}.tar.gz
Source1:        LICENSING.correspondance
Patch0:         Net-Jabber-2.0-timezone.patch
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-doc
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  %{_bindir}/perldoc
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Net::XMPP) >= 1.0
BuildRequires:  perl(Net::XMPP::Client)
BuildRequires:  perl(Net::XMPP::Connection)
BuildRequires:  perl(Net::XMPP::Debug)
BuildRequires:  perl(Net::XMPP::IQ)
BuildRequires:  perl(Net::XMPP::JID)
BuildRequires:  perl(Net::XMPP::Message)
BuildRequires:  perl(Net::XMPP::Namespaces)
BuildRequires:  perl(Net::XMPP::Presence)
BuildRequires:  perl(Net::XMPP::Stanza)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::Timezone)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
Requires:  perl(Time::Timezone)

%description
Net::Jabber provides a Perl user with access to the Jabber Instant
Messaging protocol.

For more information about Jabber visit:

    http://www.jabber.org

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-Jabber-%{version}
%patch -P0 -p1
cp %{SOURCE1} .
# generate our other two licenses...
perldoc perlgpl > LICENSE.GPL
perldoc perlartistic > LICENSE.Artistic
# we really don't want executable examples...
chmod -x examples/*

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} %{buildroot}/*
# fix wonky execute permissions
find %{buildroot} -type f -exec chmod -x '{}' ';'

%check
# Disable tests which will fail under mock
rm t/protocol_definenamespace.t
rm t/protocol_muc.t
rm t/protocol_rpc.t
make test

%files
%license LICENSE.* LICENSING.*
%doc CHANGES README examples
%{perl_vendorlib}/Net/*
%{_mandir}/man3/Net::Jabber*.3*

%changelog
%autochangelog
