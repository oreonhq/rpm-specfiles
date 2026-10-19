%global source0_hash 5b80b7d5e709d34393bcba88971864a17b44a5bf0f9e4bcee383d029e7d2d5c3
Name:           perl-Text-Iconv
Version:        1.7
Release:        1%{?dist}
Summary:        Perl interface to iconv() codeset conversion function
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-Iconv
Source0:        https://cpan.metacpan.org/authors/id/M/MP/MPIOTR/Text-Iconv-%{version}.tar.gz
%{?perl_default_filter}
Provides:       perl(Text::Iconv)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The Text::Iconv module provides a Perl interface to the iconv()
function as defined by the Single UNIX Specification. The convert()
method converts the encoding of characters in the input string from
the fromcode codeset to the tocode codeset, and returns the result.
Settings of fromcode and tocode and their permitted combinations are
implementation-dependent. Valid values are specified in the system
documentation.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Text-Iconv-%{version}

# README is ISO-8859-1 encoded
iconv -f iso-8859-1 -t utf8 < README > README.utf8
touch -c -r README README.utf8
mv README.utf8 README

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build
%install
%make_install
chmod -R u+w $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
