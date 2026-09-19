%global source0_hash 8ffcf85a7f6213e5e94140adcc2b179ed02498eadc84309457e904dec93f7f92

Name:           perl-IO-Digest
Version:        0.11
Release:        38%{?dist}
Summary:        Calculate digests while reading or writing
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IO-Digest
Source0:        https://cpan.metacpan.org/modules/by-module/IO/IO-Digest-%{version}.tar.gz
BuildArch:      noarch
Patch0:         IO-Digest-0.11-Fix-building-on-Perl-without-dot-in-INC.patch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Digest)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(PerlIO::via::dynamic) >= 0.10
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)

%description
This module allows you to calculate digests while reading or writing file
handles. This avoids the case you need to reread the same content to
compute the digests after written a file.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IO-Digest-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null \;

chmod -R u+rwX,go+rX,go-w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
