%global source0_hash 8ffcf85a7f6213e5e94140adcc2b179ed02498eadc84309457e904dec93f7f92
Name:           perl-IO-Digest
Version:        0.11
Release:        1%{?dist}
Summary:        Calculate digests while reading or writing
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IO-Digest
Source0:        https://cpan.metacpan.org/modules/by-module/IO/IO-Digest-%{version}.tar.gz
BuildArch:      noarch
Patch0:         IO-Digest-0.11-Fix-building-on-Perl-without-dot-in-INC.patch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Digest)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(PerlIO::via::dynamic)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
