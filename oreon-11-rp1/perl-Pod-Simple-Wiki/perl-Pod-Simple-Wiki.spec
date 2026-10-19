%global source0_hash 49a4f72ac709f2a9d4a0410331b475e8399a4731a76c28d6880ff1a2805cd4b9
Name:           perl-Pod-Simple-Wiki
Version:        0.20
Release:        1%{?dist}
Summary:        Utility and perl classes for converting POD to Wiki text
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-Simple-Wiki
Source0:        https://cpan.metacpan.org/authors/id/J/JM/JMCNAMARA/Pod-Simple-Wiki-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Pod::Simple)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Pod::Simple)
BuildRequires:  perl(Test::More)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The Pod::Simple::Wiki module is used for converting Pod text to Wiki text.
It currently contains the following output filters: Confluence, Kwiki,
Mediawiki, Moinmoin, Template, Tiddlywiki, Twiki and Usemod.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Pod-Simple-Wiki-%{version}

iconv -f latin1 -t utf-8 README > README.utf-8
mv README.utf-8 README

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
