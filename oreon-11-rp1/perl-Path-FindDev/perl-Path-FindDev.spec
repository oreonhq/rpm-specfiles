%global source0_hash beb465d3060ad7d71d338d48ade5798a96d3cd2bc40a3d619b940372038808b9
%global cpan_version v0.5.3
Name:           perl-Path-FindDev
Version:        %(echo '%{cpan_version}' | tr -d 'v')
Release:        1%{?dist}
Summary:        Find a development path somewhere in an upper hierarchy
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Path-FindDev
Source0:        https://cpan.metacpan.org/authors/id/K/KE/KENTNL/Path-FindDev-%{cpan_version}.tar.gz
BuildArch:      noarch
Requires:       perl(Carp)
Requires:       perl(File::Spec)
Requires:       perl(Path::IsDev) >= 0.2.2
Requires:       perl(Path::IsDev::Object)
Requires:       perl(Path::Tiny)
Requires:       perl(Scalar::Util)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Tiny)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Path::IsDev)
BuildRequires:  perl(Path::IsDev::Object)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
