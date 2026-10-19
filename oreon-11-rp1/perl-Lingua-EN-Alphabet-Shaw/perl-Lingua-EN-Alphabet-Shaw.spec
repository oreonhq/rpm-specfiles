%global source0_hash 6a1a3eabc8f8349dfad92c519992c450b33d0db521d2a24fdc448e8d4a6b10f8
Name:           perl-Lingua-EN-Alphabet-Shaw
Version:        0.64
Release:        1%{?dist}
Summary:        Transliterate the Latin to Shavian alphabets
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Lingua-EN-Alphabet-Shaw
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARNANEL/Lingua-EN-Alphabet-Shaw-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Share)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The Shaw or Shavian alphabet was commissioned by the will of the playwright
George Bernard Shaw in the early 1960s as a replacement for the Latin
alphabet for representing English. It is designed to have a one-to-one
phonemic (not phonetic) mapping with the sounds of English.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Lingua-EN-Alphabet-Shaw-%{version}
# Remove bundled libraries
rm -r inc

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
