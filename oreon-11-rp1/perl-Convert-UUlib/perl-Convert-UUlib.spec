%global source0_hash 98c314c50fb15bf53f89fcfe47ecaaf2b7bd3a87573638916c8a04cde9a8db3c

# Filter the Perl extension module
%{?perl_default_filter}

%global pkgname Convert-UUlib

Summary:        Perl interface to the uulib library
Name:           perl-Convert-UUlib
Epoch:          3
Version:        1.8
Release:        18%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/%{pkgname}
Source0:        https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/%{pkgname}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Canary::Stability)
BuildRequires:  perl(Carp)
BuildRequires:  perl(common::sense)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%description
A perl interface to the uulib library (a.k.a. uudeview/uuenview).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pkgname}-%{version}

%build
%if 0%{?fedora} > 41 || 0%{?rhel} > 10
export RPM_OPT_FLAGS="$RPM_OPT_FLAGS -std=gnu17"
%endif

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%make_build

%install
%make_install
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%license COPYING*
%doc Changes README doc/*
%{perl_vendorarch}/Convert
%{perl_vendorarch}/auto/Convert
%{_mandir}/man?/Convert::UUlib*

%changelog
%autochangelog
