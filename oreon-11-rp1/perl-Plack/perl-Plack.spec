%global source0_hash bebde91c42298ed6ec8e6c82b21433a1b49aa39412c247f3905b80f955acf77b

# Build with apache2 tests enabled
# - works in local mocks, but fails in Fedora's koji.
# - requires customized apache setup with apache >= 2.4.
# Default to not testing apache2.
%bcond_with apache

# Use Devel::StackTrace::WithLexicals for catching exceptions.
%bcond_without perl_Plack_enables_Devel_StackTrace_WithLexicals

# Build with FCGI support
%bcond_without perl_Plack_enables_fcgi

# Use XS HTTP parser. This can be disabled with PLACK_HTTP_PARSER_PP=1
# environment variable at run time.
%bcond_without perl_Plack_enables_HTTP_Parser_XS

# Build with mod_perl support for Apache HTTP server version 1.
# Abandoned/Unsupported in Fedora.
%bcond_with perl_Plack_enables_httpd1

# Build with mod_perl support for Apache HTTP server version 2.
# Abandoned/Unsupported in Fedora.
%bcond_without perl_Plack_enables_httpd2

# Recommends IPv6 support to HTTP::Server::PSGI embedded web server
%bcond_without perl_Plack_enables_ipv6

# Build with support for logging through Log::Log4perl
%bcond_without perl_Plack_enables_log4perl

# Test log middleware for Log::Log4perl and Log::Dispatch
%bcond_without perl_Plack_enables_log_test

# Suggest SSL support to HTTP::Server::PSGI embedded web server
%bcond_without perl_Plack_enables_ssl

Name:           perl-Plack
Version:        1.0051
Release:        7%{?dist}
Summary:        Perl Superglue for Web frameworks and Web Servers (PSGI toolkit)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Plack
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Plack-%{version}.tar.gz
# Adapt tests to Fedora's httpd 2.4
Patch0:         Plack-1.0047-Update-Apache-2-handler-tests-to-httpd-2.4.patch
BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  %{__perl}

BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.12.0
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(File::ShareDir::Install) >= 0.06
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
%if %{with perl_Plack_enables_httpd1}
BuildRequires:  perl(Apache::Constants)
BuildRequires:  perl(Apache::Request)
%endif
BuildRequires:  perl(Apache::LogFormat::Compiler) >= 0.33
%if %{with perl_Plack_enables_httpd2}
BuildRequires:  perl(Apache2::Const)
BuildRequires:  perl(Apache2::Log)
BuildRequires:  perl(Apache2::RequestIO)
BuildRequires:  perl(Apache2::RequestRec)
BuildRequires:  perl(Apache2::RequestUtil)
BuildRequires:  perl(Apache2::Response)
BuildRequires:  perl(APR::Table)
%endif
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(CGI::Compile) >= 0.03
BuildRequires:  perl(CGI::Emulate::PSGI) >= 0.10
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cookie::Baker) >= 0.07
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Devel::StackTrace) >= 1.23
BuildRequires:  perl(Devel::StackTrace::AsHTML) >= 0.11
%if %{with perl_Plack_enables_Devel_StackTrace_WithLexicals}
BuildRequires:  perl(Devel::StackTrace::WithLexicals) >= 0.8
%endif
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(DirHandle)
BuildRequires:  perl(Exporter)
%if %{with perl_Plack_enables_fcgi}
# FCGI not used at tests
# FCGI::ProcManager not used at tests
%endif
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::ShareDir) >= 1.00
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(Filesys::Notify::Simple)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Hash::MultiValue) >= 0.05
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Entity::Parser) >= 0.25
# HTTP::Headers version from HTTP::Message in META
BuildRequires:  perl(HTTP::Headers) >= 5.814
BuildRequires:  perl(HTTP::Headers::Fast) >= 0.18
%if %{with perl_Plack_enables_HTTP_Parser_XS}
BuildRequires:  perl(HTTP::Parser::XS)
%endif
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(HTTP::Tiny) >= 0.03
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket::INET)
# IO::Socket::IP not used at tests
# IO::Socket::SSL not used at tests
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
%if %{with perl_Plack_enables_log_test} && %{with perl_Plack_enables_log4perl}
BuildRequires:  perl(Log::Log4perl)
%endif
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Refresh)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(Pod::Usage) >= 1.36
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
%if %{with perl_Plack_enables_fcgi}
# Server::Starter not used at tests
%endif
BuildRequires:  perl(Socket)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Stream::Buffered) >= 0.02
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::TCP) >= 2.15
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI) >= 1.59
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(WWW::Form::UrlEncoded) >= 0.23

# tests
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(Authen::Simple::Passwd)
BuildRequires:  perl(CGI)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Request::AsCGI) >= 1.2
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle::Util)
%if %{with perl_Plack_enables_fcgi}
BuildRequires:  perl(IO::Socket)
%endif
%if %{with perl_Plack_enables_log_test}
BuildRequires:  perl(Log::Dispatch) >= 2.25
BuildRequires:  perl(Log::Dispatch::Array) >= 1.001
%endif
BuildRequires:  perl(LWP::Protocol::http10)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MIME::Types)
# Test::Pod 1.41 not used
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(utf8)
# FCGI::Client not used

%if %{with perl_Plack_enables_httpd2}
# For mod_perl.so
BuildRequires:  mod_perl >= 2

# For httpd tests
BuildRequires:  /usr/sbin/httpd
%endif

%if %{with perl_Plack_enables_fcgi}
# For lighttpd tests, not used, RELEASE_TESTING only
# /usr/sbin/lighttpd
# lighttpd-fastcgi
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
# HTTP::Headers version from HTTP::Message in META
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

# Remove under-specified dependenics
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Apache::LogFormat::Compiler|CGI::Compile|CGI::Emulate::PSGI|Cookie::Baker|Devel::StackTrace|Devel::StackTrace::AsHTML|File::ShareDir|Hash::MultiValue|HTTP::Entity::Parser|HTTP::Headers|HTTP::Headers::Fast|HTTP::Tiny|Stream::Buffered|Test::More|Test::TCP|URI|WWW::Form::UrlEncoded)\\)$

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
# FCGI handler needs FCGI::ProcManager by default
Requires:   perl(FCGI::ProcManager)
# Server::Starter is used only of Plack is executed from Server::Starter. No
# need for declaring the dependency.
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

%check
unset AUTHOR_TESTING PLACK_HTTP_PARSER_PP RELEASE_TESTING
export TEST_APACHE1=0%{?with_perl_Plack_enables_httpd1:1}
export TEST_APACHE2=0%{?with_perl_Plack_enables_httpd2:1}
%if ! %{with apache}
export TEST_APACHE1=0
export TEST_APACHE2=0
%endif
%{__make} test

%files
%doc Changes README
%{_bindir}/plackup
%{_mandir}/man1/plackup.*
%{perl_vendorlib}/Plack
%{perl_vendorlib}/Plack.pm
%{perl_vendorlib}/HTTP
# Abandoned/Unsupported in Fedora: Apache1
%exclude %{perl_vendorlib}/Plack/Handler/Apache1.pm
%exclude %{_mandir}/man3/Plack::Handler::Apache1.3pm*
# Packaged separately in perl-Plack-Handler-Apache2
%exclude %{perl_vendorlib}/Plack/Handler/Apache2*
%exclude %{_mandir}/man3/Plack::Handler::Apache2*
# Packaged separately in perl-Plack-Handler-FCGI
%exclude %{perl_vendorlib}/Plack/Handler/FCGI.pm
%exclude %{_mandir}/man3/Plack::Handler::FCGI.3pm*
# Packaged separatelt in perl-Plack-Middleware-Log4perl
%exclude %{perl_vendorlib}/Plack/Middleware/Log4perl.pm
%exclude %{_mandir}/man3/Plack::Middleware::Log4perl.3pm*
# Packaged separately in perl-Plack-Test
%exclude %{perl_vendorlib}/Plack/Test
%exclude %{perl_vendorlib}/Plack/Test.pm
%exclude %{perl_vendorlib}/auto/*
%exclude %{_mandir}/man3/Plack::Test*

%{_mandir}/man3/*

%if %{with perl_Plack_enables_httpd1}
%files Handler-Apache1
%{perl_vendorlib}/Plack/Handler/Apache1.pm
%{_mandir}/man3/Plack::Handler::Apache1.3pm*
%endif

%if %{with perl_Plack_enables_httpd2}
%files Handler-Apache2
%{perl_vendorlib}/Plack/Handler/Apache2*
%{_mandir}/man3/Plack::Handler::Apache2*
%endif

%if %{with perl_Plack_enables_fcgi}
%files Handler-FCGI
%{perl_vendorlib}/Plack/Handler/FCGI.pm
%{_mandir}/man3/Plack::Handler::FCGI.3pm*
%endif

%if %{with perl_Plack_enables_log4perl}
%files Middleware-Log4perl
%{perl_vendorlib}/Plack/Middleware/Log4perl.pm
%{_mandir}/man3/Plack::Middleware::Log4perl.3pm*
%endif

%files Test
%{_mandir}/man3/Plack::Test*
%dir %{perl_vendorlib}/Plack
%{perl_vendorlib}/Plack/Test
%{perl_vendorlib}/Plack/Test.pm
# Used by Plack/Test/Suite.pm
%{perl_vendorlib}/auto/*

%changelog
%autochangelog
