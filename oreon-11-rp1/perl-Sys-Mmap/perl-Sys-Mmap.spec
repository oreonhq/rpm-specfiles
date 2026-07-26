%global source0_hash 1820ce2c89f1ab7357644f8db0f49f142f54526250fb1e235db10aa80f15e2cf

Name:           perl-Sys-Mmap
Version:        0.20
Release:        22%{?dist}
Summary:        Use mmap to map in a file as a Perl variable
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Sys-Mmap
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/Sys-Mmap-%{version}.tar.gz

BuildRequires: make
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) 
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# Carp is not used at tests
# DynaLoader is not used if XSLoader is available
BuildRequires:  perl(Exporter)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Errno)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)

Requires:       perl(Carp)
Requires:       perl(XSLoader)
%{?perl_default_filter}

%description
The Mmap module lets you use mmap to map in a file as a perl variable rather
than reading the file into dynamically allocated memory.  Multiple programs may
map the same file into memory, and immediately see changes by each other.
Memory may be allocated not attached to a file, and shared with sub-processes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Sys-Mmap-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%make_build

%install
%make_build pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
find %{buildroot} -type d -empty -delete

%{_fixperms} %{buildroot}/*

%check
%make_build test

%files
%license Copying Artistic
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Sys*
%{_mandir}/man3/*

%changelog
%autochangelog
