%global source0_hash e1e9b06d40311cd0f499d257c6b675dd4e4c936693da4cb7c25783af77cc5c9d

# Run optional tests
%{bcond_without perl_MooX_Struct_enables_optional_test}

Name:           perl-MooX-Struct
Version:        0.020
Release:        17%{?dist}
Summary:        Record structure-like Moo classes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooX-Struct
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/MooX-Struct-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(B::Hooks::EndOfScope)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::Printer::Filter)
BuildRequires:  perl(Exporter::Tiny) >= 0.044
BuildRequires:  perl(IO::Handle)
# Moo 1.006 for tests from META
BuildRequires:  perl(Moo) >= 1.006
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(namespace::autoclean) >= 0.19
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Object::ID)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Types::Standard) >= 1.000
BuildRequires:  perl(Types::TypeTiny) >= 1.000
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(if)
BuildRequires:  perl(Test::More) >= 0.61
%if %{with perl_MooX_Struct_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Data::Printer) >= 0.36
%endif
Requires:       perl(B::Deparse)
Requires:       perl(Data::Dumper)
Requires:       perl(Data::Printer) >= 0.36
Requires:       perl(Data::Printer::Filter)
Requires:       perl(Exporter::Tiny) >= 0.044
Requires:       perl(IO::Handle)
Requires:       perl(Moo::Role)
Requires:       perl(namespace::autoclean) >= 0.19
Requires:       perl(Object::ID)
Requires:       perl(Term::ANSIColor)

%description
MooX::Struct allows you to create cheap struct-like classes for your data
using Moo.

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Exporter::Tiny|namespace::autoclean)\\)$

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooX-Struct-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes COPYRIGHT CREDITS NEWS README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
