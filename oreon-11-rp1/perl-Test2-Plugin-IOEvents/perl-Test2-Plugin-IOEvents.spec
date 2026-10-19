%global source0_hash a1ccd61ed05dc2bb3e706a01a455969d18d8744d59b71e11bee9c965c9370b72
%bcond_without perl_Test2_Plugin_IOEvents_enables_optional_tests
Name:           perl-Test2-Plugin-IOEvents
%global cpan_version 0.001001
Version:        0.1.1
Release:        1%{?dist}
Summary:        Turn STDOUT and STDERR into Test2 events
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test2-Plugin-IOEvents
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test2-Plugin-IOEvents-%{cpan_version}.tar.gz
BuildArch:      noarch
%if %{with perl_Test2_Plugin_IOEvents_enables_optional_tests}
%endif
Requires:       perl(Test2::API) >= 1.302165
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test2::API\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Test2::API)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This Test2 plugin turns prints to STDOUT and STDERR objects (including warnings)
into the proper Test2 events.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test2-Plugin-IOEvents-%{cpan_version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
