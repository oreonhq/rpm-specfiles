%global source0_hash ccda29f3c93176ad0fdfff4dd6f5e4ac90b370cba4b028386b7343bf64139bde

Name:           perl-Heap
Version:        0.80
Release:        49%{?dist}
Summary:        Perl extension for keeping data partially sorted

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Heap
Source0:        https://cpan.metacpan.org/authors/id/J/JM/JMM/Heap-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76 
# Run-time
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)

Provides:       perl(Heap)
Provides:       perl(Heap::Elem)
Provides:       perl(Heap::Fibonacci)
Provides:       perl(Heap::Elem)
Provides:       perl(Heap::Fibonacci)
%description
The Heap collection of modules provide routines that manage a heap of 
elements. A heap is a partially sorted structure that is always able to 
easily extract the smallest of the elements in the structure (or the 
largest if a reversed compare routine is provided).

If the collection of elements is changing dynamically, the heap has less 
overhead than keeping the collection fully sorted.

The elements must be objects as described in "Heap::Elem" and all 
elements inserted into one heap must be mutually compatible - either 
the same class exactly or else classes that differ only in ways unrelated 
to the Heap::Elem interface.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Heap-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*


%changelog
%autochangelog
