%global source0_hash 65070c045328d19963d24d1ab8da00a8c844513e5645ba079d6729cef82ced33

Name:           perl-Dispatch-Class
Version:        0.04
Release:        3%{?dist}
Summary:        Dispatch on the type (class) of an argument
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Dispatch-Class
Source0:        https://www.cpan.org/modules/by-module/Dispatch/Dispatch-Class-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Exporter::Tiny)
BuildRequires:  perl(parent)
BuildRequires:  perl(Scalar::Util) >= 1
# Tests
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Test::More)
Requires:       perl(Scalar::Util) >= 1

# Remove underspecified dependencies.
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Scalar::Util\\)$

%description
This module offers a (mostly) simple way to check the class of an object
and handle specific cases specially.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dispatch-Class-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Dispatch/*
%{_mandir}/man3/Dispatch::Class.3pm*

%changelog
%autochangelog
