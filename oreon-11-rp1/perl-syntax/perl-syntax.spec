%global source0_hash fe19b6da8a8f43a5aa2ee571441bc0e339fb156d0081c157a1a24e9812c7d365
Name:           perl-syntax
Version:        0.004
Release:        1%{?dist}
Summary:        Activate syntax extensions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/syntax
Source0:        https://cpan.metacpan.org/authors/id/P/PH/PHAYLON/syntax-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(syntax)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::OptList)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl-generators
# /oreon:deps
%description
This module activates community provided syntax extensions to Perl. You
pass it a feature name, and optionally a scalar with arguments, and the
dispatching system will load and install the extension in your package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n syntax-%{version}

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
