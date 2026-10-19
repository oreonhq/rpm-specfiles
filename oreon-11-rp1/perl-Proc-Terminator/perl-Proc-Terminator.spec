%global source0_hash fd3c5773f1504cec2dc1e8f12638c87c9bcdb5d91231c83f8a9805cb231650fb
Name:           perl-Proc-Terminator
Version:        0.05
Release:        1%{?dist}
Summary:        Conveniently terminate processes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Proc-Terminator
Source0:        https://cpan.metacpan.org/authors/id/M/MN/MNUNBERG/Proc-Terminator-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Moo) >= 0.009014
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Moo\\)\\s*$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Moo)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Proc::Terminator provides a convenient way to kill a process, often useful
in utility and startup functions which need to ensure the death of an
external process.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Proc-Terminator-%{version}

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
