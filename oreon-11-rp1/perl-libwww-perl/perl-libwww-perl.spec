%global source0_hash e75f0fa9d3c6f0daf5a5a72fa9f8b1c9c0d23e3a84a8522ccb4f835232b95505
%bcond_without perl_libwww_perl_enables_optional_test
%bcond_with perl_libwww_perl_enables_internet_test
Name:           perl-libwww-perl
Version:        6.83
Release:        1%{?dist}
Summary:        A Perl interface to the World-Wide Web
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/libwww-perl
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/libwww-perl-%{version}.tar.gz
Patch0:         libwww-perl-6.39-Normalize-shebangs-in-examples.patch
BuildArch:      noarch
%if %{with perl_libwww_perl_enables_internet_test}
%endif
%if %{with perl_libwww_perl_enables_internet_test}
%if %{with perl_libwww_perl_enables_optional_test}
%endif
%endif
Requires:       perl(Authen::NTLM) >= 1.02
Suggests:       perl(CPAN::Config)
Requires:       perl(Encode) >= 2.12
Requires:       perl(File::Spec)
Requires:       perl(File::Listing) >= 6
Suggests:       perl(HTML::FormatPS)
Suggests:       perl(HTML::FormatText)
Requires:       perl(HTML::Entities)
Requires:       perl(HTML::HeadParser)
Suggests:       perl(HTML::Parse)
Requires:       perl(HTTP::Config)
Requires:       perl(HTTP::Cookies) >= 6
Requires:       perl(HTTP::Date) >= 6
Requires:       perl(HTTP::Headers::Util)
Requires:       perl(HTTP::Negotiate) >= 6
Requires:       perl(HTTP::Request) >= 6.18
Requires:       perl(HTTP::Request::Common) >= 6.18
Requires:       perl(HTTP::Response) >= 6.18
Requires:       perl(HTTP::Status) >= 6.18
Requires:       perl(LWP::MediaTypes) >= 6
Suggests:       perl(LWP::Protocol::https) >= 6.02
Requires:       perl(MIME::Base64) >= 2.1
Requires:       perl(Net::FTP) >= 2.58
Requires:       perl(Net::HTTP) >= 6.18
Requires:       perl(URI) >= 1.10
Requires:       perl(URI::Escape)
Requires:       perl(WWW::RobotRules) >= 6
Provides:       perl(LWP::Debug::TraceHTTP::Socket) = %{version}
Provides:       perl(LWP::Protocol::http::Socket) = %{version}
Provides:       perl(LWP::Protocol::http::SocketMethods) = %{version}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Authen::NTLM|Encode|File::Listing|HTTP::Cookies|HTTP::Daemon|HTTP::Date|HTTP::Negotiate|HTTP::Request|HTTP::Response|HTTP::Status|LWP::MediaTypes|MIME::Base64|Net::FTP|Net::HTTP|Test::More|URI|WWW::RobotRules)\\)$
Provides:       perl(LWP)
Provides:       perl(LWP::Protocol::http)
Provides:       perl(LWP::RobotUA)
Provides:       perl(LWP::Simple)
Provides:       perl(LWP::UserAgent)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Locale)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::HeadParser)
BuildRequires:  perl(HTTP::Config)
BuildRequires:  perl(HTTP::CookieJar::LWP)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Daemon)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Headers::Util)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(LWP::MediaTypes)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Net::HTTP)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(WWW::RobotRules)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The libwww-perl collection is a set of Perl modules which provides a simple and
consistent application programming interface to the World-Wide Web.  The main
focus of the library is to provide classes and functions that allow you to
write WWW clients. The library also contain modules that are of more general
use and even classes that help you implement simple HTTP servers.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(HTTP::Cookies) >= 6
Requires:       perl(HTTP::CookieJar::LWP)
Requires:       perl(HTTP::Daemon) >= 6.01
Requires:       perl(HTTP::Request) >= 6.18
Requires:       perl(HTTP::Response) >= 6.18
Requires:       perl(Net::HTTP) >= 6.18
Requires:       perl(Test::More) >= 0.96
%if %{with perl_libwww_perl_enables_internet_test} && %{with perl_libwww_perl_enables_optional_test}
Requires:       perl(Test::LeakTrace)
%endif
Requires:       perl(URI) >= 1.10
Suggests:       perl(JSON::PP) => 2.27300
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n libwww-perl-%{version} 
%patch -P 0 -p1
%if !%{with perl_libwww_perl_enables_internet_test}
rm t/base/protocols/nntp.t t/leak/no_leak.t t/redirect.t
perl -i -ne 'print $_ unless m{^(?:t/base/protocols/nntp\.t|t/leak/no_leak\.t|t/redirect\.t)}' MANIFEST
%endif
# Help generators to recognize a Perl code
for F in $(find t -name '*.t') talk-to-ourself; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*\bperl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 --aliases < /dev/null
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t talk-to-ourself %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
unset COVERAGE PERL_LWP_ENV_HTTP_TEST_SERVER_TIMEOUT PERL_LWP_ENV_HTTP_TEST_URL
prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset COVERAGE PERL_LWP_ENV_HTTP_TEST_SERVER_TIMEOUT PERL_LWP_ENV_HTTP_TEST_URL
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-libwww-perl-tests -f %{oreon_filedir}/perl-libwww-perl-tests.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.83-1
- Import
