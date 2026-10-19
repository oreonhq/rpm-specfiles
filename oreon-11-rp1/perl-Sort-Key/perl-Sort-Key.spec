%global source0_hash ed6a4ccfab094c9cd164f564024e98bd21d94f4312ccac4d6246d22b34081acf
Name:           perl-Sort-Key
Version:        1.33
Release:        1%{?dist}
Summary:        Fastest way to sort anything in Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Sort-Key
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SALVA/Sort-Key-%{version}.tar.gz
%{?perl_default_filter}
Provides:       perl(Sort::Key)
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(constant)
BuildRequires:  perl(integer)
BuildRequires:  perl(locale)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Sort::Key provides a set of functions to sort lists of values by some
calculated key value.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Sort-Key-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
