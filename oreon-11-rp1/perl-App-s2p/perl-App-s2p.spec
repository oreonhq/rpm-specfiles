%global source0_hash c4493ddcb845f062bcf7984d2ed425663ef26f52aae30217c9d16393e9fd8a2d
Name:           perl-App-s2p
Version:        1.003
Release:        1%{?dist}
Summary:        Convert sed script to Perl program
License:        CC-BY-SA-3.0
URL:            https://metacpan.org/release/App-s2p
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/App-s2p-%{version}.tar.gz
BuildArch:      noarch
%if !%{defined perl_bootstrap}
%endif
%if !%{defined perl_bootstrap}
%endif
Conflicts:      perl < 4:5.18.2-300
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(Devel::FindPerl)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open2)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(blib)
BuildRequires:  perl(integer)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This package delivers s2p tool which converts sed scripts to Perl programs.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n App-s2p-%{version}
%if %{defined perl_bootstrap}
rm t/s2p.t
perl -i -ne 'print $_ unless m{^t/s2p.t}' MANIFEST
%endif

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
