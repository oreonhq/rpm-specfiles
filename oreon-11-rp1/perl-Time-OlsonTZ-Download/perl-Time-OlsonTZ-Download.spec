%global source0_hash 311d23c914215e2f8eef921fc0b234a1cb167c107f9a7bd8d3298b044983466c
Name:           perl-Time-OlsonTZ-Download
Version:        0.009
Release:        1%{?dist}
Summary:        Olson time zone database from source
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Time-OlsonTZ-Download
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Time-OlsonTZ-Download-%{version}.tar.gz
Patch0:         Time-OlsonTZ-Download-0.008-Use-gpgv2-from-GnuPG-2.patch
BuildArch:      noarch
Requires:       coreutils
Requires:       gnupg2
Requires:       gzip
Requires:       lzip
Requires:       make
Requires:       tar
%{?perl_default_filter}
# oreon:deps
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Dir)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IPC::Filter)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Net::FTP)
BuildRequires:  perl(Params::Classify)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
