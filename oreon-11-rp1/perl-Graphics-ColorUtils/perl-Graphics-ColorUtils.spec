%global source0_hash 3cd61bac56a9cf78fc132941df876292db70b872a7220ccde6eefcb36ed63604
Name:           perl-Graphics-ColorUtils
Version:        0.17
Release:        1%{?dist}
Summary:        Easy-to-use color space conversions and more
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Graphics-ColorUtils
Source0:        https://cpan.metacpan.org/authors/id/J/JA/JANERT/Graphics-ColorUtils-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This modules provides some utility functions to handle colors and color space
conversions.

The interface has been kept simple, so that most functions can be called
"inline" when making calls to graphics libraries such as GD, Tk, or when
generating HTML/CSS.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Graphics-ColorUtils-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
make %{?_smp_mflags}
%install
%make_install
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
