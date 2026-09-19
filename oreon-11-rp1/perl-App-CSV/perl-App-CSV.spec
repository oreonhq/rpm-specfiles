%global source0_hash f14c91135160fe8fe6d1e66a1ffffc0114e48765fb7480d93a30e10ab995c002

Name:           perl-App-CSV
Version:        0.08
Release:        35%{?dist}
Summary:        App::CSV Perl module
License:        MIT
URL:            https://metacpan.org/release/App-CSV
Source0:        https://cpan.metacpan.org/authors/id/G/GA/GAAL/App-CSV-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Getopt)
BuildRequires:  perl(Text::CSV)
# Tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(Test::More)
# Optional tests
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::TempDir)

Requires:       perl(MooseX::Getopt)

%description
App::CSV Perl module

%package -n csv
Summary: A CSV command line Tool

%description -n csv
A command-line tool to manipulate CSV (and other delimited, line-based) files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n App-CSV-%{version}

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
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files -n csv
%{_bindir}/csv
%{_mandir}/man1/csv.1*

%changelog
%autochangelog
