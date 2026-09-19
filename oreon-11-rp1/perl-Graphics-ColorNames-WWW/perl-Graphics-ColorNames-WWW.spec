%global source0_hash d81a96e7dd0a91d3d14dbfd0f0c3c3d27d6efb891452cfdf936eb3eddd7e610c

Name:           perl-Graphics-ColorNames-WWW
Version:        1.14
Release:        21%{?dist}
Summary:        WWW color names and equivalent RGB values
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Graphics-ColorNames-WWW
Source0:        https://cpan.metacpan.org/authors/id/C/CF/CFAERBER/Graphics-ColorNames-WWW-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Graphics::ColorNames)
BuildRequires:  perl(integer)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
This modules defines color names and their associated RGB values from
various WWW specifications and implementations.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Graphics-ColorNames-WWW-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc 
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
