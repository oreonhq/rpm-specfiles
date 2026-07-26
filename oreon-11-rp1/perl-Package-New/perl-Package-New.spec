%global source0_hash d1e4814ef2a28302096a6377fff9aa2870ae9a717cd191a1fec2ec656cb29597

Name:           perl-Package-New
Version:        0.10
Release:        3%{?dist}
Summary:        Simple base package from which to inherit
License:        BSD-3-Clause
URL:            https://metacpan.org/release/Package-New
Source0:        https://cpan.metacpan.org/authors/id/M/MR/MRDVT/Package-New-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Devel::Hide)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Simple) >= 0.44
BuildRequires:  perl(warnings)

%description
The Package::New object provides a consistent object constructor for
objects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Package-New-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/Package/
%{_mandir}/man3/Package::New*.3pm*

%changelog
%autochangelog
