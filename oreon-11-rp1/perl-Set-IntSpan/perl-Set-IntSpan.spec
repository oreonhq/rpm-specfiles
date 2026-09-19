%global source0_hash 11b7549b13ec5d87cc695dd4c777cd02983dd5fe9866012877fb530f48b3dfd0

Name:           perl-Set-IntSpan
Version:        1.19
Release:        37%{?dist}
Summary:        Perl module for managing sets of integers

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Set-IntSpan
Source0:        https://cpan.metacpan.org/authors/id/S/SW/SWMCD/Set-IntSpan-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
Set::IntSpan manages sets of integers. It is optimized for sets that
have long runs of consecutive integers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Set-IntSpan-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%{perl_vendorlib}/Set/
%{_mandir}/man3/Set::IntSpan.3*

%changelog
%autochangelog
