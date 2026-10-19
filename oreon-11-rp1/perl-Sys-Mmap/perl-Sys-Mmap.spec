%global source0_hash 1820ce2c89f1ab7357644f8db0f49f142f54526250fb1e235db10aa80f15e2cf
Name:           perl-Sys-Mmap
Version:        0.20
Release:        1%{?dist}
Summary:        Use mmap to map in a file as a Perl variable
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Sys-Mmap
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/Sys-Mmap-%{version}.tar.gz
Requires:       perl(Carp)
Requires:       perl(XSLoader)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The Mmap module lets you use mmap to map in a file as a perl variable rather
than reading the file into dynamically allocated memory.  Multiple programs may
map the same file into memory, and immediately see changes by each other.
Memory may be allocated not attached to a file, and shared with sub-processes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Sys-Mmap-%{version}
%oreon_prep
%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%make_build
%install
%make_build pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
find %{buildroot} -type d -empty -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

%make_build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
