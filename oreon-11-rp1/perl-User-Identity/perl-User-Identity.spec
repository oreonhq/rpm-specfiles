%global source0_hash 46ec55c4b2c158fb9e3bd5c63aaa10695fee8508ef4ec958774dd8eaccab3847
Name:           perl-User-Identity
Version:        4.00
Release:        1%{?dist}
Summary:        Maintains info about a physical person
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/User-Identity
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/User-Identity-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Geography::Countries)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Geography::Countries)
BuildRequires:  perl(Hash::Ordered)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Log::Report)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
A module designed to store and maintain a set of informational objects that
are related to one user.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n User-Identity-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
