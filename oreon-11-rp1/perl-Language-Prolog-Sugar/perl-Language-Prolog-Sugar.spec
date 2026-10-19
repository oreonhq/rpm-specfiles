%global source0_hash 0f6152ba3a338b16803cb8035ddbd028ba47b65b87e871657aafff7fd407d1cd
Name:           perl-Language-Prolog-Sugar
Version:        0.06
Release:        1%{?dist}
Summary:        Syntactic sugar for Prolog term constructors
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Language-Prolog-Sugar
Source0:        https://cpan.metacpan.org/authors/id/Z/ZM/ZMUGHAL/Language-Prolog-Sugar-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Language::Prolog::Types)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl-generators
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
