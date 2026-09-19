%global source0_hash daf26d3c96e482c1ff1785a0478b543c555eef456e4e08b4c253cfeaa584e837

Name:           perl-Mail-Box-IMAP4
Version:        4.01
Release:        2%{?dist}
Summary:        Handle IMAP4 folders as client
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mail-Box-IMAP4
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/Mail-Box-IMAP4-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(Digest::HMAC_MD5)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Log::Report) >= 1.42
BuildRequires:  perl(Mail::Box::Manage::User) >= 4
BuildRequires:  perl(Mail::Box::Net) >= 4
BuildRequires:  perl(Mail::Box::Net::Message)
BuildRequires:  perl(Mail::Box::Parser::Perl)
BuildRequires:  perl(Mail::Box::Search) >= 4
BuildRequires:  perl(Mail::IMAPClient)
BuildRequires:  perl(Mail::Message::Head)
BuildRequires:  perl(Mail::Message::Head::Complete) >= 4
BuildRequires:  perl(Mail::Message::Head::Delayed) >= 4
BuildRequires:  perl(Mail::Transport::Receive) >= 4
BuildRequires:  perl(parent)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(Mail::Box::Identity)
BuildRequires:  perl(Mail::Box::MH)
BuildRequires:  perl(Mail::Box::Test) >= 4
BuildRequires:  perl(Mail::Message) >= 4
BuildRequires:  perl(Mail::Message::Body::Lines) >= 4
BuildRequires:  perl(Test::More)
Requires:       perl(Mail::Box) >= 4
Requires:       perl(Mail::Box::Net) >= 4
Requires:       perl(Mail::IMAPClient) >= 3.42
Requires:       perl(Mail::Message::Body::Lines) >= 4
Requires:       perl(Mail::Message::Head::Complete) >= 4
Requires:       perl(Mail::Message::Head::Delayed) >= 4
Requires:       perl(Mail::Transport::Receive) >= 4

Conflicts:      perl-Mail-Box < 4

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Mail::Box::Manage::User\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Mail::IMAPClient\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Mail::Box::(Net|Search|Test)\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Mail::Message(::Body::Lines|::Head::Complete|::Head::Delayed|)\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Mail::(Server|Transport::Receive)\\)$

%description
Maintain a folder which has its messages stored on a remote server. The
communication between the client application and the server is implemented
using the IMAP4 protocol.

%package -n perl-Mail-Server-IMAP4
Summary:        IMAP4 server implementation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Requires:       perl(Mail::Box::Manage::User) >= 4
Requires:       perl(Mail::Box::Search) >= 4
Requires:       perl(Mail::Server) >= 4

%description -n perl-Mail-Server-IMAP4
This module is a place-holder, which can be used to grow code which is
needed to implement a full IMAP4 server.
The server implementation is not completed.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Mail-Server-IMAP4 = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Mail::Box::Test) >= 4
Requires:       perl(Mail::Message) >= 4
Requires:       perl(Mail::Message::Body::Lines) >= 4

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Mail-Box-IMAP4-%{version}
# Remove tests that are always skipped
for F in t/10client-read.t t/11client-write.t; do
    rm "$F"
    perl -i -ne 'print $_ unless m{\Q'"$F"'\E}' MANIFEST
done
# Correct shebangs
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
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc ChangeLog README.md
%dir %{perl_vendorlib}/Mail
%{perl_vendorlib}/Mail/Box
%{perl_vendorlib}/Mail/Transport
%{_mandir}/man3/Mail::Box::*
%{_mandir}/man3/Mail::Transport::*

%files -n perl-Mail-Server-IMAP4
%dir %{perl_vendorlib}/Mail
%dir %{perl_vendorlib}/Mail/Server
%{perl_vendorlib}/Mail/Server/IMAP4*
%{_mandir}/man3/Mail::Server::IMAP4*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
