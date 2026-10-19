%global source0_hash 01153de4535343bd150129bf90d7de3408249a1aedb0922e6441727fc20aab7a
%bcond_without perl_Mail_DMARC_enables_optional_test
Name:           perl-Mail-DMARC
Version:        1.20260306
Release:        1%{?dist}
Summary:        Perl implementation of DMARC
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND MPL-2.0
URL:            https://metacpan.org/dist/Mail-DMARC
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSIMERSON/Mail-DMARC-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Mail_DMARC_enables_optional_test}
%endif
Requires:       perl(DBD::SQLite) >= 1.31
Requires:       perl(DBIx::Simple) >= 1.35
Requires:       perl(Email::Sender::Simple) >= 1.300032
Requires:       perl(File::ShareDir) >= 1.00
Recommends:     perl(GeoIP2::Database::Reader)
Requires:       perl(Mail::DKIM::PrivateKey)
Requires:       perl(Mail::DKIM::Signer)
Requires:       perl(Mail::DKIM::TextWrap)
Recommends:     perl(Net::HTTP)
Requires:       perl(Net::IMAP::Simple)
Requires:       perl(Socket6) >= 0.23
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((File::ShareDir|DBIx::Simple|Email::Sender::Simple|Socket6)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(CGI)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Config::Tiny)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBIx::Simple)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Email::MIME)
BuildRequires:  perl(Email::Sender)
BuildRequires:  perl(Email::Sender::Simple)
BuildRequires:  perl(Email::Sender::Transport::Failable)
BuildRequires:  perl(Email::Sender::Transport::SMTP)
BuildRequires:  perl(Email::Sender::Transport::SMTP::Persistent)
BuildRequires:  perl(Email::Sender::Transport::Test)
BuildRequires:  perl(Email::Simple)
BuildRequires:  perl(Encode)
BuildRequires:  perl(English)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(IO::Compress::Gzip)
BuildRequires:  perl(IO::Compress::Zip)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(IO::Uncompress::Gunzip)
BuildRequires:  perl(IO::Uncompress::Unzip)
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Mail::DKIM::PrivateKey)
BuildRequires:  perl(Mail::DKIM::Signer)
BuildRequires:  perl(Mail::DKIM::TextWrap)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Net::DNS::Resolver)
BuildRequires:  perl(Net::DNS::Resolver::Mock)
BuildRequires:  perl(Net::HTTP)
BuildRequires:  perl(Net::IDN::Encode)
BuildRequires:  perl(Net::IMAP::Simple)
BuildRequires:  perl(Net::IP)
BuildRequires:  perl(Net::Server::HTTP)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Socket6)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Sys::Syslog)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::File::ShareDir)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(URI)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(XML::SAX::ParserFactory)
BuildRequires:  perl(XML::Validator::Schema)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This Perl module is a suite of tools for implementing DMARC. It adheres to the
2013 DMARC draft.

%package HTTP
Summary:        Web server for DMARC validation and report viewing
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(File::ShareDir) >= 1.00
%description HTTP
Mail::DMARC::HTTP Perl module and dmarc_httpd tool for viewing DMARC reports.
This package is has intentionally left out jqgrid JavaScript and CSS files
because of missing their source code.

%package Test
Summary:        Perl modules for testing Mail::DMARC framework
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
%description Test
Public Perl modules of Mail::DMARC framework which have no other use than
performing internal tests.

%package tests
Summary:        Tests for %{name}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-HTTP = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-Test = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
%if %{with perl_Mail_DMARC_enables_optional_test}
Requires:       perl(XML::SAX::ParserFactory)
Requires:       perl(XML::Validator::Schema)
%endif
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Mail-DMARC-%{version}
%if %{without perl_Mail_DMARC_enables_optional_test}
rm t/17.Report.Aggregate.Schema.t
perl -i -ne 'print $_ unless m{\Qt/17.Report.Aggregate.Schema.t\E}' MANIFEST
%endif
# Correct shebangs and help generators to recognize Perl scripts
for F in bin/dmarc_sqlite_to_mysql.pl t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
ln -s -r %{buildroot}%{perl_vendorlib}/auto/share/dist/Mail-DMARC \
    %{buildroot}%{_libexecdir}/%{name}/share
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
cp -a --dereference %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
unset HTTP_ACCEPT_ENCODING MAIL_DMARC_CONFIG_FILE
prove -I .
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset HTTP_ACCEPT_ENCODING MAIL_DMARC_CONFIG_FILE
export HARNESS_OPTIONS=j1
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Mail-DMARC-HTTP -f %{oreon_filedir}/perl-Mail-DMARC-HTTP.list
%files -n perl-Mail-DMARC-Test -f %{oreon_filedir}/perl-Mail-DMARC-Test.list
%files -n perl-Mail-DMARC-tests -f %{oreon_filedir}/perl-Mail-DMARC-tests.list

%changelog

%autochangelog
