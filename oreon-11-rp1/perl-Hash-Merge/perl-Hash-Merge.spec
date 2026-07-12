%global source0_hash ae0522f76539608b61dde14670e79677e0f391036832f70a21f31adde2538644

Name:           perl-Hash-Merge
Version:        0.302
Release:        16%{?dist}
Summary:        Merges arbitrary deep hashes into a single hash
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Hash-Merge
Source0:        https://cpan.metacpan.org/modules/by-module/Hash/Hash-Merge-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clone)
BuildRequires:  perl(Clone::Choose) >= 0.008
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Scalar::Util)
# Tests
BuildRequires:  perl(Test::More)
# Optional tests
BuildRequires:  perl(Clone::PP)
BuildRequires:  perl(Storable)
# Dependencies
# required but not detected automatically
Requires:       perl(Clone)

Provides:       perl(Hash::Merge)
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Hash-Merge-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README.md
%{perl_vendorlib}/Hash/
%{_mandir}/man3/Hash::Merge.3*

%changelog
%autochangelog
