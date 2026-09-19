%global source0_hash a66532dc9745ce50f7ad75f0b635a4d010d2dce03e94da1b985b161d07586902

Name:		perl-HTTP-Server-Simple-Static
Version:	0.14
Release:	25%{?dist}
Summary:	Serve static files with HTTP::Server::Simple
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/HTTP-Server-Simple-Static
Source0:	https://cpan.metacpan.org/authors/id/S/SJ/SJQUINNEY/HTTP-Server-Simple-Static-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(base)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::LibMagic)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(HTTP::Date)
BuildRequires:	perl(HTTP::Server::Simple)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(strict)
BuildRequires:	perl(URI::Escape)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
BuildRequires:	perl(warnings)

%description
HTTP::Server::Simple::Static adds a method to serve static files from your
HTTP::Server::Simple subclass.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-Server-Simple-Static-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
chmod -R u+w $RPM_BUILD_ROOT/*

# We'll get this as a doc file instead.
rm -rf $RPM_BUILD_ROOT%{perl_vendorlib}/HTTP/Server/Simple/example.pl

%check
make test

%files
%doc Changes example.pl
%{perl_vendorlib}/HTTP/
%{_mandir}/man3/*.3pm*

%changelog
%autochangelog
