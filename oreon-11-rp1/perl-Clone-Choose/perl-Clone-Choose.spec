%global source0_hash 5623481f58cee8edb96cd202aad0df5622d427e5f748b253851dfd62e5123632

Name:           perl-Clone-Choose
Version:        0.010
Release:        24%{?dist}
Summary:        Choose appropriate clone utility
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Clone-Choose
Source0:        https://cpan.metacpan.org/modules/by-module/Clone/Clone-Choose-%{version}.tar.gz
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
BuildRequires:  perl(Carp)
# Optional Run-time
BuildRequires:  perl(Clone) >= 0.10
BuildRequires:  perl(Clone::PP)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Storable)
# Tests
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More) >= 0.90
BuildRequires:  perl(Test::Without::Module)
# Dependencies
Recommends:     perl(Module::Runtime)
Requires:       perl(Storable)

Provides:       perl(Clone::Choose)
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Clone-Choose-%{version}

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
%{perl_vendorlib}/Clone/
%{_mandir}/man3/Clone::Choose.3*

%changelog
%autochangelog
