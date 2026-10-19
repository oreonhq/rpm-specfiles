%global source0_hash ccda29f3c93176ad0fdfff4dd6f5e4ac90b370cba4b028386b7343bf64139bde
Name:           perl-Heap
Version:        0.80
Release:        1%{?dist}
Summary:        Perl extension for keeping data partially sorted
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Heap
Source0:        https://cpan.metacpan.org/authors/id/J/JM/JMM/Heap-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(Heap)
Provides:       perl(Heap::Elem)
Provides:       perl(Heap::Fibonacci)
Provides:       perl(Heap::Elem)
Provides:       perl(Heap::Fibonacci)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
