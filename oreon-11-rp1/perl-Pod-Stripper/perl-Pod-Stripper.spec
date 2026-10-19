%global source0_hash 5a1a8afbb13ed083be44d974f95d2093e541d43ce7bca787d49c0cd3d5aca04d
Name:           perl-Pod-Stripper
Version:        0.22
Release:        1%{?dist}
Summary:        Strip all pod, and output what's left
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-Stripper
Source0:        https://cpan.metacpan.org/authors/id/P/PO/PODMASTER/Pod-Stripper-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Pod::Parser) >= 1.13
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Pod::Parser\\)\s*$
Provides:       perl(Pod::Stripper)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Pod::Parser)
BuildRequires:  perl(Test)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
This be Pod::Stripper, a subclass of Pod::Parser. It parses perl files,
stripping out the pod, and dumping the rest (presumably code) to wherever
you point it to (like you do with Pod::Parser).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Pod-Stripper-%{version}
sed -i 's/\r//' Changes README podstrip

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
