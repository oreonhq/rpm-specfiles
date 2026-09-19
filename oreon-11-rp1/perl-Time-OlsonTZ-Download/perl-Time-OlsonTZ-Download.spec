%global source0_hash 311d23c914215e2f8eef921fc0b234a1cb167c107f9a7bd8d3298b044983466c

Name:           perl-Time-OlsonTZ-Download
Version:        0.009
Release:        25%{?dist}
Summary:        Olson time zone database from source
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Time-OlsonTZ-Download
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Time-OlsonTZ-Download-%{version}.tar.gz
# Use GnuPG2 instead of GnuPG1, CPAN RT#124132
Patch0:         Time-OlsonTZ-Download-0.008-Use-gpgv2-from-GnuPG-2.patch
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# coreutils for cp, sha512sum, not used at tests
# gnupg2 for gpgv2, not used at tests
# gzip for gunzip, not used at tests
# lzip not used at tests
# make not used at tests
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode) >= 1.75
BuildRequires:  perl(File::Path) >= 2.07
BuildRequires:  perl(File::Temp) >= 0.22
BuildRequires:  perl(IO::Dir) >= 1.03
BuildRequires:  perl(IO::File) >= 1.03
BuildRequires:  perl(IPC::Filter) >= 0.002
BuildRequires:  perl(Net::FTP) >= 3.07
BuildRequires:  perl(Params::Classify)
BuildRequires:  perl(utf8)
# tar not used at tests
# Tests:
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
# coreutils for cp, sha512sum
Requires:       coreutils
# gnupg2 for gpgv2
Requires:       gnupg2
# gzip for gunzip
Requires:       gzip
Requires:       lzip
Requires:       make
Requires:       tar

%{?perl_default_filter}

%description
An object of this Perl class represents a local copy of the source of the
Olson time zone database, possibly used to build binary tzfiles. The source
copy always begins by being downloaded from the canonical repository of the
Olson database. This class provides methods to help with extracting useful
information from the source.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Time-OlsonTZ-Download-%{version}
%patch -P0 -p1

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
