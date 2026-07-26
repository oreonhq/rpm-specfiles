%global source0_hash 233064e094442f2e449844da9aec9ce0e0ed65a7da7abdb25ec0dc1be454df98

Name:           perl-Class-Field
Version:        0.24
Release:        21%{?dist}
Summary:        Class Field Accessor Generator
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Field
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Class-Field-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  findutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Find)
BuildRequires:  perl(lib)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.41
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
Class::Field exports two subroutines, field and const. These functions are
used to declare fields and constants in your class.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-Field-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Class*
%{_mandir}/man3/Class*

%changelog
%autochangelog
