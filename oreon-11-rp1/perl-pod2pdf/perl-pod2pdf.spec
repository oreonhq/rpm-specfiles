%global source0_hash dbc7451758d52194d3c740fdcb20ac5b858bc2921fa7ec2c39f0ee00bc3fb770

Name:           perl-pod2pdf
Version:        0.42
Release:        39%{?dist}
Summary:        Converts Pod to PDF format
License:        Artistic-2.0
URL:            https://metacpan.org/release/pod2pdf
Source0:        https://cpan.metacpan.org/authors/id/J/JO/JONALLEN/pod2pdf-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Type)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::ArgvFile)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Image::Size)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Paper::Specs) >= 0.10
BuildRequires:  perl(PDF::API2) >= 0.6
BuildRequires:  perl(Pod::Escapes)
BuildRequires:  perl(Pod::ParseLink)
BuildRequires:  perl(Pod::Parser)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
# Tests
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.00
Requires:       perl(File::Type)
Requires:       perl(Image::Size)
Requires:       perl(Paper::Specs) >= 0.10

Provides:       perl(App::pod2pdf)
Provides:       perl(pod2pdf)
%description
pod2pdf converts documents written in Perl's POD (Plain Old Documentation)
format to PDF files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n pod2pdf-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test

%files
%license artistic-2_0.txt
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_bindir}/*

%changelog
%autochangelog
