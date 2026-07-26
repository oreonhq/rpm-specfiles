%global source0_hash 46756461c24ce7666b8108ddb96dbab612699df3012c80ef11016619fe1554f7

Name:           perl-CGI-Session
Version:        4.48
Release:        35%{?dist}
Summary:        Persistent session data in CGI applications
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CGI-Session
Source0:        https://cpan.metacpan.org/modules/by-module/CGI/CGI-Session-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(CGI) >= 3.26
Requires:       perl(File::Path)
Requires:       perl(Text::Abbrev)

BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::Wrap)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(CGI) >= 3.26
BuildRequires:  perl(Class::Struct)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBD::Pg)
BuildRequires:  perl(DB_File)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
# File::Path not used at tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FreezeThaw)
BuildRequires:  perl(overload)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Abbrev)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Env)

%description
CGI-Session is a Perl5 library that provides an easy, reliable and modular
session management system across HTTP requests. Persistency is a key
feature for such applications as shopping carts, login/authentication
routines, and application that need to carry data across HTTP requests.
CGI::Session does that and many more.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CGI-Session-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
chmod 644 examples/*

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes examples README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
