%global source0_hash dc9b5f13e8224032a26f81ebc31ba1bb51f8c97652e4c54cb8f7a419838d9b3d

Name:           perl-Catalyst-Manual
Summary:        Catalyst web framework manual
Epoch:          1
Version:        5.9013
Release:        5%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Catalyst-Manual-%{version}.tar.gz
URL:            https://metacpan.org/release/Catalyst-Manual
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
This is the manual to the Catalyst web framework.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Catalyst-Manual-%{version}

#remove extraneous .gitignore
find -name .gitignore -print0 | xargs -0 rm -f

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor --skipdeps NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%doc Changes README t/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
