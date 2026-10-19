%global source0_hash a66532dc9745ce50f7ad75f0b635a4d010d2dce03e94da1b985b161d07586902
Name:		perl-HTTP-Server-Simple-Static
Version:	0.14
Release:        1%{?dist}
Summary:        Serve static files with HTTP::Server::Simple
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/HTTP-Server-Simple-Static
Source0:        https://cpan.metacpan.org/authors/id/S/SJ/SJQUINNEY/HTTP-Server-Simple-Static-%{version}.tar.gz
BuildArch:	noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::LibMagic)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Server::Simple)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
rm -rf $RPM_BUILD_ROOT%{perl_vendorlib}/HTTP/Server/Simple/example.pl
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
