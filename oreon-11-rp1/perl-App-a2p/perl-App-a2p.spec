%global source0_hash 9257f182e957c5b3d036a3e89b0d4cbb5a4849593a12bb491df96c1becf14e8b

Name:           perl-App-a2p
Version:        1.013
Release:        16%{?dist}
Summary:        Awk to Perl translator
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/App-a2p
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/App-a2p-%{version}.tar.gz
# Current code will fail test tests if the code will run for more than 5
# seconds. This is not much portable test.
Patch0:         App-a2p-1.007-Remove-alarm-call-from-test.patch

# Fix BZ#1177672
# - Add a2p.y from https://github.com/Leont/app-a2p/a2p.y
Patch1:         App-a2p-1.007-a2p-y.patch

# Required for App-a2p-1.009-Check-for-n-argument-length.patch
Patch2:         App-a2p-1.009-Capture-stderr-in-tests.patch

# Fix a buffer overflow when parsing long enough -n argument, CPAN RT#100361
Patch3:         App-a2p-1.009-Check-for-n-argument-length.patch

BuildRequires:  byacc
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More) >= 0.89
Conflicts:      perl < 4:5.18.2-300

%description
This package delivers a2p tool which takes an awk script specified on the
command line and produces a comparable Perl script.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n App-a2p-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
# Regenerate a2p.c from a2p.y
byacc -o a2p.c a2p.y

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" \
    NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*

%changelog
%autochangelog
