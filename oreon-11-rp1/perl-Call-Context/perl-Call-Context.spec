%global source0_hash 3d39c14096ecbfcd679ae9e0c216e61bd41dba3511d4ebee25f2f2ee00864ac5
Name:           perl-Call-Context
Version:        0.05
Release:        1%{?dist}
Summary:        Sanity-check calling context
License:        MIT
URL:            https://metacpan.org/dist/Call-Context
Source0:        https://cpan.metacpan.org/authors/id/F/FE/FELIPE/Call-Context-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  /usr/bin/chmod
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
If your function only expects to return a list, then a call in some
other context is, by definition, an error. The problem is that,
depending on how the function is written, it may actually do something
expected in testing, but then in production act differently.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Call-Context-%{version}
%oreon_prep
%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
