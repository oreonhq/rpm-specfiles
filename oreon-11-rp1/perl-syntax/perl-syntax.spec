%global source0_hash fe19b6da8a8f43a5aa2ee571441bc0e339fb156d0081c157a1a24e9812c7d365

Name:           perl-syntax
Version:        0.004
Release:        38%{?dist}
Summary:        Activate syntax extensions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/syntax
Source0:        https://cpan.metacpan.org/authors/id/P/PH/PHAYLON/syntax-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::OptList) >= 0.104
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(namespace::clean)
# Tests
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.94

Provides:       perl(syntax)
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

%check
make test

%files
%doc Changes LICENSE META.json
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
