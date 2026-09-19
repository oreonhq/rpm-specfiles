%global source0_hash c3e242f675b61dc0a3dec670fbcbe3ff5b0bbe952333377cb3acb86796b3de01

Name:           perl-Pipeline
Version:        3.12
Release:        52%{?dist}
Summary:        Generic pipeline interface
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pipeline
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/Pipeline-%{version}.tar.gz
# Fix compatibility with Pod-Parser-1.51, CPAN RT #77896
Patch0:         Pipeline-3.12-Fix-POD-to-obey-stricter-Pod-Parser-1.51.patch
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Class::ISA)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::UUID) >= 0.01
BuildRequires:  perl(Error) >= 0.15
BuildRequires:  perl(File::Spec)
# XXX: BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Scalar::Util) >= 0.01
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)
# Tests only
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(IO::Null) >= 0.01
BuildRequires:  perl(IO::String) >= 0.01
BuildRequires:  perl(lib)
BuildRequires:  perl(Pod::Checker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(vars)
# Optional tests only
# XXX: BuildRequires:  perl(Acme::Colour)
BuildRequires:  perl(Data::Structure::Util) >= 0.04
Requires:       perl(Class::ISA) >= 0.01
Requires:       perl(Data::UUID) >= 0.01
Requires:       perl(Error) >= 0.15
Requires:       perl(File::Spec)
Requires:       perl(Scalar::Util) >= 0.01
Requires:       perl(Storable)
Requires:       perl(threads)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Class::ISA\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Data::UUID\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Error\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Scalar::Util\\)$

%description
Pipelines are a mechanism to process data. They are designed to be plugged
together to make fairly complex operations act in a fairly straightforward
manner, cleanly, and simply.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Pipeline-%{version}
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
