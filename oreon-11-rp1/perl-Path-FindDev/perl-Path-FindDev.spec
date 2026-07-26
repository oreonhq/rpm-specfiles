%global source0_hash beb465d3060ad7d71d338d48ade5798a96d3cd2bc40a3d619b940372038808b9

%global cpan_version v0.5.3
Name:           perl-Path-FindDev
Version:        %(echo '%{cpan_version}' | tr -d 'v')
Release:        26%{?dist}
Summary:        Find a development path somewhere in an upper hierarchy
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Path-FindDev
Source0:        https://cpan.metacpan.org/authors/id/K/KE/KENTNL/Path-FindDev-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Tiny) >= 0.010
BuildRequires:  perl(Path::IsDev) >= 0.2.2
BuildRequires:  perl(Path::IsDev::Object)
BuildRequires:  perl(Path::Tiny) >= 0.054
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter)
# Tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More) >= 1.001002
Requires:       perl(Carp)
Requires:       perl(File::Spec)
Requires:       perl(Path::IsDev) >= 0.2.2
Requires:       perl(Path::IsDev::Object)
Requires:       perl(Path::Tiny)
Requires:       perl(Scalar::Util)

%description
This package is mostly a glue layer around Path::IsDev with a few directory
walking tricks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Path-FindDev-%{cpan_version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
