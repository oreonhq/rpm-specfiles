%global source0_hash 0b1617af218dfab911ba0fbd72210529a246efe140332da77fe3e03d11000117

%global pkgname Tie-Function

Name:           perl-Tie-Function
Version:        0.02
Release:        36%{?dist}
Summary:        Wrap functions in tied hash sugar
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tie-Function
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAVIDNICO/handy_tied_functions/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test)
Requires:       perl(warnings)

%description
Tie::Function simplifies wrapping functions in tied hash syntax so they can
be interpolated in double-quoted literals without messy intermediate
variables.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{pkgname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
