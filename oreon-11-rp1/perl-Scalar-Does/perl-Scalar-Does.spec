%global source0_hash d628b73123e9c6de8f29712d783c9bf2694da288019c564c02940d444433f770

Name:           perl-Scalar-Does
Version:        0.203
Release:        27%{?dist}
Summary:        Check an object implements an interface
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Scalar-Does
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Scalar-Does-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.17
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(B)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter::Tiny) >= 0.026
BuildRequires:  perl(if)
BuildRequires:  perl(lexical::underscore)
BuildRequires:  perl(namespace::clean) >= 0.19
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util) >= 1.24
BuildRequires:  perl(Type::Tiny) >= 0.004
BuildRequires:  perl(Types::Standard) >= 0.004
# UNIVERSAL::DOES not used with perl >= 5.10
BuildRequires:  perl(URI::file)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(feature)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires) >= 0.06
BuildRequires:  perl(URI)
# Optional tests:
BuildRequires:  perl(IO::All)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Path::Tiny)
# Test::NoWarnings used only if List::MoreUtils exists
BuildRequires:  perl(Test::NoWarnings)
Requires:       perl(B)
Requires:       perl(Exporter::Tiny) >= 0.026
Requires:       perl(lexical::underscore)
Requires:       perl(Type::Tiny) >= 0.004

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Exporter::Tiny|Type::Tiny)\\)$

%description
It has long been noted that Perl would benefit from a does() built-in. A
check that ref($thing) eq 'ARRAY' doesn't allow you to accept an object
that uses overloading to provide an array-like interface. This package
delivers Scalar::Does Perl module that can do it.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Scalar-Does-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes COPYRIGHT CREDITS IO-Detect-Changes.txt NEWS README
%doc TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
