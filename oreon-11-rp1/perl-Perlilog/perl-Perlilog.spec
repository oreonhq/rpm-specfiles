%global source0_hash 2d6132042de7055851a6a35a702076655e7c0269799339a9c3c3a9e79a44d980
Name:           perl-Perlilog
Version:        1.0
Release:        1%{?dist}
Summary:        Verilog environment and IP core handling in Perl
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/Perlilog
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BILLAUER/Perlilog-%{version}.tar.gz
BuildArch:      noarch
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(PL_const\\)
%global __provides_exclude %__provides_exclude|perl\\(PL_hardroot\\)$
%global __provides_exclude %__provides_exclude|perl\\(PL_settable\\)$
%global __provides_exclude %__provides_exclude|perl\\(UNIVERSAL\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
Perlilog is a command-line tool which generates Verilog
modules from a set of files, which come in several other
formats. It was originally designed to integrate Verilog IP cores.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Perlilog-%{version}

# rpmlint : line endings
affected=`find examples/ -type f -name "*.*"`
for i in license.txt $affected ; do
  echo "Fixing wrong-file-end-of-line-encoding : $i"
  sed 's/\r//' $i > $i.rpmlint
  touch -r $i $i.rpmlint;
  mv $i.rpmlint $i
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
