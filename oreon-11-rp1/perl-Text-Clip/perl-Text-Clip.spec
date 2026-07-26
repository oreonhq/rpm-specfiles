%global source0_hash 6f5b134a96a22ac9f314a996188955f4c631eecae5057e187330b4b1727adb4f

Name:           perl-Text-Clip
Version:        0.0014
Release:        34%{?dist}
Summary:        Clip and extract text in clipboard-like way
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-Clip
Source0:        https://cpan.metacpan.org/authors/id/R/RO/ROKR/Text-Clip-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  perl-generators
BuildRequires:  perl(Any::Moose)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Most)

%description
Text::Clip allows you to mark/slice up a piece of text. String matching (by
regular expression, etc.) is used to place marks. The first mark lets you
access the text preceding and following the mark. Subsequent marks allow
you to slurp up the text "clipped" between the marks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-Clip-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
