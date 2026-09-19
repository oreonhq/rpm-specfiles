%global source0_hash 2c9db069fff990c0765e600ca968114895f7e05aa661a18e59e94b3cd841abaa

Name:           perl-Cache-Mmap
Version:        0.11
Release:        55%{?dist}
Summary:        Shared data cache using memory mapped files
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Cache-Mmap
Source0:        https://cpan.metacpan.org/authors/id/P/PM/PMH/Cache-Mmap-%{version}.tar.gz
# Fixed BZ#1135969, RT#95940
Patch0:         Cache-Mmap-0.11-Avoid-Copy-On-Write-problems-with-Perl-5.20.patch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(integer)
BuildRequires:  perl(IO::Seekable)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(IO::File)
BuildRequires:  perl(open)
BuildRequires:  perl(Test::More)

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

%check
make test

%files
%doc Changes cmmtest README Todo
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Cache*
%{_mandir}/man3/*

%changelog
%autochangelog
