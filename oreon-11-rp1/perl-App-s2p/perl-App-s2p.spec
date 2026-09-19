%global source0_hash c4493ddcb845f062bcf7984d2ed425663ef26f52aae30217c9d16393e9fd8a2d

Name:           perl-App-s2p
Version:        1.003
Release:        17%{?dist}
Summary:        Convert sed script to Perl program
License:        CC-BY-SA-3.0
URL:            https://metacpan.org/release/App-s2p
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/App-s2p-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Config)
BuildRequires:  perl(integer)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(blib)
%if !%{defined perl_bootstrap}
BuildRequires:  perl(Devel::FindPerl) >= 0.009
BuildRequires:  perl(File::Copy)
%endif
BuildRequires:  perl(IO::Handle)
%if !%{defined perl_bootstrap}
BuildRequires:  perl(IPC::Open2)
%endif
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)
Conflicts:      perl < 4:5.18.2-300

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

%check
make test

%files
%license LICENSE
%doc Changes README
%{_bindir}/*
%{_mandir}/man1/*

%changelog
%autochangelog
