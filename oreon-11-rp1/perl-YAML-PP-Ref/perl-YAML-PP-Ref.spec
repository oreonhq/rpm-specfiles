%global source0_hash eb2fa65c2b4cdadeed4ef29c57638c5a8839fa209d1babdfafab2dbbba933cdb

Name:           perl-YAML-PP-Ref
Version:        0.02
Release:        11%{?dist}
Summary:        Generated Reference Parser backend for YAML::PP
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/YAML-PP-Ref
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TINITA/YAML-PP-Ref-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.14.0
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Scalar::Util) >= 1.07
BuildRequires:  perl(YAML::Parser)
BuildRequires:  perl(YAML::PP) >= 0.027
BuildRequires:  perl(YAML::PP::Common)
BuildRequires:  perl(YAML::PP::Parser)
# Tests
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(utf8)

%description
The https://yaml.org/ YAML Specification can be used to generate a YAML
Parser from it.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n YAML-PP-Ref-%{version}

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
%doc Changes examples README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
