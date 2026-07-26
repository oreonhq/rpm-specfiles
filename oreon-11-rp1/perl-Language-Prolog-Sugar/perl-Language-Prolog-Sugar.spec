%global source0_hash 0f6152ba3a338b16803cb8035ddbd028ba47b65b87e871657aafff7fd407d1cd

Name:           perl-Language-Prolog-Sugar
Version:        0.06
Release:        39%{?dist}
Summary:        Syntactic sugar for Prolog term constructors
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Language-Prolog-Sugar
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SALVA/Language-Prolog-Sugar-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Language::Prolog::Types)
# Tests only
BuildRequires:  perl(Test::More)
# Optional tests
BuildRequires:  perl(Test::Pod) >= 1.00

%description
Language::Prolog::Sugar is able to export to the calling package a set of
subroutines to create Prolog terms as defined in the
Language::Prolog::Types module. Perl programs using these constructors have
the same look as real Prolog programs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Language-Prolog-Sugar-%{version}
for F in README; do
    iconv -f iso8859-1 -t utf-8 < "$F" > "${F}.new"
    touch -r "$F" "${F}.new"
    mv "${F}.new" "$F"
done

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
