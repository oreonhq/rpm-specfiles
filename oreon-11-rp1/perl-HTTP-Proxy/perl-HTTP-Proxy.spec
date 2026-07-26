%global source0_hash b05290534ec73625c21a0565fc35170890dab163843d95331c292c23f504c69d

%{?perl_default_filter}

Name:           perl-HTTP-Proxy
Version:        0.304
Release:        31%{?dist}
Summary:        A pure Perl HTTP proxy
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-Proxy
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOOK/HTTP-Proxy-%{version}.tar.gz
# Add support for IPv6, bug #1422948, CPAN RT#120275
Patch1:     HTTP-Proxy-0.304-Support-IPv6.patch
# debugging 23connect
Patch2:		HTTP-Proxy-0.303-23connect-logging-debug.patch
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build), perl(Module::Build::Tiny)
BuildRequires:  perl(Test::Pod), perl(Test::Pod::Coverage), perl(HTML::Parser)
BuildRequires:  perl(HTTP::Daemon), perl(LWP::UserAgent), perl(Crypt::SSLeay)
BuildRequires:  perl(File::Spec), perl(Pod::Coverage::TrustPod), perl(Test::CPAN::Meta)
BuildRequires:  perl(Carp), perl(Exporter), perl(ExtUtils::MakeMaker), perl(Fcntl)
BuildRequires:  perl(File::Spec), perl(File::Spec::Functions)
BuildRequires:  perl(File::Find), perl(File::Path), perl(File::Temp), perl(HTTP::Daemon), perl(HTTP::Date)
BuildRequires:  perl(HTTP::Headers), perl(HTTP::Headers::Util), perl(HTTP::Request), perl(HTTP::Request::Common)
BuildRequires:  perl(IO::Handle), perl(IO::Select), perl(IO::Socket::IP)
BuildRequires:  perl(LWP::ConnCache), perl(LWP::UserAgent), perl(POSIX)
BuildRequires:  perl(Socket), perl(Sys::Hostname), perl(Test::More), perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage), perl(URI), perl(base), perl(constant), perl(strict)
BuildRequires:  perl(vars), perl(version), perl(warnings)

%description
Its main use should be to record and/or modify web sessions, so as to
help users create web robots, web testing suites, as well as proxy
systems than can transparently alter the requests to and answers from
an origin server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-Proxy-%{version}
%patch -P1 -p1
%patch -P2 -p1 -b .logging

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}

%check
make test

%files
%doc Changes README eg/
%{perl_vendorlib}/HTTP/
%{_mandir}/man3/*.3pm*

%changelog
%autochangelog
