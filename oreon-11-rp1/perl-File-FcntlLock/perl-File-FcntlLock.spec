%global source0_hash 9a9abb2efff93ab73741a128d3f700e525273546c15d04e7c51c704ab09dbcdf

Name:		perl-File-FcntlLock
Version:	0.22
Release:	37%{?dist}
Summary:	Perl module for file locking with fcntl
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/File-FcntlLock
Source0:	https://cpan.metacpan.org/authors/id/J/JT/JTT/File-FcntlLock-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:	perl(POSIX)
# Tests:
BuildRequires:  perl(Test)

%description
FcntlLock is a module to do file locking in an object oriented
fashion using the fcntl(2) system call. This allows locks on parts
of a file as well as on the whole file and overcomes some known
problems with flock(2), on which Perl's flock() function is based.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-FcntlLock-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/File/
%{_mandir}/man3/*.3pm*

%changelog
%autochangelog
