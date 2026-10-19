%global source0_hash bebde91c42298ed6ec8e6c82b21433a1b49aa39412c247f3905b80f955acf77b
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond_with apache
%bcond_without perl_Plack_enables_Devel_StackTrace_WithLexicals
%bcond_without perl_Plack_enables_fcgi
%bcond_without perl_Plack_enables_HTTP_Parser_XS
%bcond_with perl_Plack_enables_httpd1
%bcond_without perl_Plack_enables_httpd2
%bcond_without perl_Plack_enables_ipv6
%bcond_without perl_Plack_enables_log4perl
%bcond_without perl_Plack_enables_log_test
%bcond_without perl_Plack_enables_ssl
Name:           perl-Plack
Version:        1.0051
Release:        1%{?dist}
Summary:        Perl Superglue for Web frameworks and Web Servers (PSGI toolkit)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Plack
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Plack-%{version}.tar.gz
Patch0:         Plack-1.0047-Update-Apache-2-handler-tests-to-httpd-2.4.patch
BuildArch:      noarch
%if %{with perl_Plack_enables_httpd1}
%endif
%if %{with perl_Plack_enables_httpd2}
%endif
%if %{with perl_Plack_enables_Devel_StackTrace_WithLexicals}
%endif
%if %{with perl_Plack_enables_fcgi}
%endif
%if %{with perl_Plack_enables_HTTP_Parser_XS}
%endif
%if %{with perl_Plack_enables_log_test} && %{with perl_Plack_enables_log4perl}
%endif
%if %{with perl_Plack_enables_fcgi}
%endif
%if %{with perl_Plack_enables_fcgi}
%endif
%if %{with perl_Plack_enables_log_test}
%endif
%if %{with perl_Plack_enables_httpd2}
%endif
%if %{with perl_Plack_enables_fcgi}
%endif
Requires:       perl(Apache::LogFormat::Compiler) >= 0.33
Requires:       perl(CGI::Compile) >= 0.03
Requires:       perl(CGI::Emulate::PSGI) >= 0.10
Requires:       perl(Cookie::Baker) >= 0.07
Requires:       perl(Devel::StackTrace) >= 1.23
Requires:       perl(Devel::StackTrace::AsHTML) >= 0.11
%if %{with perl_Plack_enables_Devel_StackTrace_WithLexicals}
Suggests:       perl(Devel::StackTrace::WithLexicals) >= 0.8
%endif
Requires:       perl(File::Basename)
Requires:       perl(Filesys::Notify::Simple)
Requires:       perl(Getopt::Long)
Requires:       perl(Hash::MultiValue) >= 0.05
Requires:       perl(HTTP::Entity::Parser) >= 0.17
Requires:       perl(HTTP::Headers) >= 5.814
Requires:       perl(HTTP::Headers::Fast) >= 0.18
%if %{with perl_Plack_enables_HTTP_Parser_XS}
Recommends:     perl(HTTP::Parser::XS)
%endif
Requires:       perl(HTTP::Tiny) >= 0.03
%if %{with perl_Plack_enables_ssl}
Suggests:       perl(IO::Socket::SSL)
%endif
%if %{with perl_Plack_enables_ipv6}
Recommends:     perl(IO::Socket::IP)
%endif
Requires:       perl(lib)
Requires:       perl(Pod::Usage) >= 1.36
Requires:       perl(Stream::Buffered) >= 0.02
Requires:       perl(URI) >= 1.59
Requires:       perl(WWW::Form::UrlEncoded) >= 0.23
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Apache::LogFormat::Compiler|CGI::Compile|CGI::Emulate::PSGI|Cookie::Baker|Devel::StackTrace|Devel::StackTrace::AsHTML|File::ShareDir|Hash::MultiValue|HTTP::Entity::Parser|HTTP::Headers|HTTP::Headers::Fast|HTTP::Tiny|Stream::Buffered|Test::More|Test::TCP|URI|WWW::Form::UrlEncoded)\\)$
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  /usr/bin/perl
BuildRequires:  /usr/sbin/httpd
BuildRequires:  mod_perl
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(APR::Table)
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(Apache2::Const)
BuildRequires:  perl(Apache2::Log)
BuildRequires:  perl(Apache2::RequestIO)
BuildRequires:  perl(Apache2::RequestRec)
BuildRequires:  perl(Apache2::RequestUtil)
BuildRequires:  perl(Apache2::Response)
BuildRequires:  perl(Apache::LogFormat::Compiler)
BuildRequires:  perl(Authen::Simple::Passwd)
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Compile)
BuildRequires:  perl(CGI::Emulate::PSGI)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cookie::Baker)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Devel::StackTrace::AsHTML)
BuildRequires:  perl(Devel::StackTrace::WithLexicals)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(DirHandle)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Filesys::Notify::Simple)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Entity::Parser)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Headers::Fast)
BuildRequires:  perl(HTTP::Parser::XS)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Request::AsCGI)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(Hash::MultiValue)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Handle::Util)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(LWP::Protocol::http10)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Log::Dispatch)
BuildRequires:  perl(Log::Dispatch::Array)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::Types)
BuildRequires:  perl(Module::Refresh)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Stream::Buffered)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::TCP)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(WWW::Form::UrlEncoded)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
# /oreon:deps
%description
Plack is a set of tools for using the PSGI stack. It contains middleware
components, a reference server and utilities for Web application
frameworks. Plack is like Ruby's Rack or Python's Paste for WSGI.

%if %{with perl_Plack_enables_httpd1}
%package Handler-Apache1
Summary:    Plack handler for mod_perl in Apache HTTP server version 1
Requires:   perl-Plack = %{version}-%{release}
%description Handler-Apache1
%{summary}.
%endif

%if %{with perl_Plack_enables_httpd2}
%package Handler-Apache2
Summary:    Plack handler for mod_perl in Apache HTTP server version 2
Requires:   perl-Plack = %{version}-%{release}
Requires:   perl(URI) >= 1.59
%description Handler-Apache2
%{summary}.
%endif

%if %{with perl_Plack_enables_fcgi}
%package Handler-FCGI
Summary:    Plack handler for FastCGI
Requires:   perl-Plack = %{version}-%{release}
Requires:   perl(FCGI::ProcManager)
Requires:   perl(URI) >= 1.59
%description Handler-FCGI
%{summary}.
%endif

%if %{with perl_Plack_enables_log4perl}
%package Middleware-Log4perl
Summary:    Plack middleware for logging through Log::Log4perl
Requires:   perl-Plack = %{version}-%{release}
Requires:   perl(Log::Log4perl)
%description Middleware-Log4perl
%{summary}.
%endif

%package Test
Summary:    Test-modules for perl-Plack
Requires:   perl-Plack = %{version}-%{release}
Requires:   perl(File::ShareDir) >= 1.00
Requires:   perl(Test::More) >= 0.88
Requires:   perl(Test::TCP) >= 2.15
%description Test
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Plack-%{version}
%patch -P0 -p1

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install} DESTDIR="$RPM_BUILD_ROOT"
%{_fixperms} "$RPM_BUILD_ROOT"/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset AUTHOR_TESTING PLACK_HTTP_PARSER_PP RELEASE_TESTING
export TEST_APACHE1=0%{?with_perl_Plack_enables_httpd1:1}
export TEST_APACHE2=0%{?with_perl_Plack_enables_httpd2:1}
%if ! %{with apache}
export TEST_APACHE1=0
export TEST_APACHE2=0
%endif
%{__make} test
%files -f %{oreon_filedir}/main.list
%files -n perl-Plack-Handler-Apache2 -f %{oreon_filedir}/perl-Plack-Handler-Apache2.list
%files -n perl-Plack-Handler-FCGI -f %{oreon_filedir}/perl-Plack-Handler-FCGI.list
%files -n perl-Plack-Middleware-Log4perl -f %{oreon_filedir}/perl-Plack-Middleware-Log4perl.list
%files -n perl-Plack-Test -f %{oreon_filedir}/perl-Plack-Test.list

%changelog

%autochangelog
