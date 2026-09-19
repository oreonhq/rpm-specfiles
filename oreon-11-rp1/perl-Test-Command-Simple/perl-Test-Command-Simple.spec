%global source0_hash 4d9dc422f03a620d0c441279f8366d1acf017da9acfdebe68b5a0e5c39c629da

Name:           perl-Test-Command-Simple
Version:        0.05
Release:        18%{?dist}
Summary:        Test external commands (nearly) as easily as loaded modules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Test-Command-Simple
Source0:        https://cpan.metacpan.org/authors/id/D/DM/DMCBRIDE/Test-Command-Simple-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(warnings)

%description
This test module is intended to simplify testing of external commands. It does
so by running the command under IPC::Open3, closing the stdin immediately, and
reading everything from the command's stdout and stderr. It then makes the
output available to be tested.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Test-Command-Simple-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/Test::Command::Simple*.*

%changelog
%autochangelog
