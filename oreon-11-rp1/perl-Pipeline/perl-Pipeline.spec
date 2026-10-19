%global source0_hash c3e242f675b61dc0a3dec670fbcbe3ff5b0bbe952333377cb3acb86796b3de01
Name:           perl-Pipeline
Version:        3.12
Release:        1%{?dist}
Summary:        Generic pipeline interface
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pipeline
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/Pipeline-%{version}.tar.gz
Patch0:         Pipeline-3.12-Fix-POD-to-obey-stricter-Pod-Parser-1.51.patch
BuildArch:      noarch
Requires:       perl(Class::ISA) >= 0.01
Requires:       perl(Data::UUID) >= 0.01
Requires:       perl(Error) >= 0.15
Requires:       perl(File::Spec)
Requires:       perl(Scalar::Util) >= 0.01
Requires:       perl(Storable)
Requires:       perl(threads)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Class::ISA\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Data::UUID\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Error\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Scalar::Util\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Class::ISA)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::Structure::Util)
BuildRequires:  perl(Data::UUID)
BuildRequires:  perl(Error)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Null)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(Pod::Checker)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Pipelines are a mechanism to process data. They are designed to be plugged
together to make fairly complex operations act in a fairly straightforward
manner, cleanly, and simply.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Pipeline-%{version}
%patch -P0 -p1

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
