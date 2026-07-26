%global source0_hash 4316a39186c4986c12f5a7dfbd7d826e6e2460657f531c41085adaf4a18ac591

Name:           perl-MikroTik-API
Version:        2.0.1
Release:        13%{?dist}
Summary:        Client for the MikroTik RouterOS API
License:        MIT
URL:            https://metacpan.org/dist/MikroTik-API
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARTINGO/MikroTik-API-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Carp)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(Moo)
BuildRequires:  perl(MooX::Types::MooseLike::Base)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Time::Out)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Type::Tiny)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# tests
BuildRequires:  perl(Pod::Coverage) >= 0.18
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08

%description
Perl client for the MikroTik RouterOS API.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MikroTik-API-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
