%global source0_hash 2c9db069fff990c0765e600ca968114895f7e05aa661a18e59e94b3cd841abaa
Name:           perl-Cache-Mmap
Version:        0.11
Release:        1%{?dist}
Summary:        Shared data cache using memory mapped files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Cache-Mmap
Source0:        https://cpan.metacpan.org/authors/id/P/PM/PMH/Cache-Mmap-%{version}.tar.gz
Patch0:         Cache-Mmap-0.11-Avoid-Copy-On-Write-problems-with-Perl-5.20.patch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Seekable)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(integer)
BuildRequires:  perl(open)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module implements a shared data cache, using memory mapped files. If
routines are provided which interact with the underlying data, access to
the cache is completely transparent, and the module handles all the details
of refreshing cache contents, and updating underlying data, if necessary.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Cache-Mmap-%{version}
%patch -P0 -p1
chmod a-x cmmtest

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} +
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
