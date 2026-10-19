%global source0_hash 80b1e281d8cd3b2b31dac711f5c8a1657a87cd80bbe69af3924bcbeb4e5db077
%bcond_with perl_Sub_Install_enables_optional_test
Name:           perl-Sub-Install
Version:        0.929
Release:        1%{?dist}
Summary:        Install subroutines into packages easily
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Sub-Install
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Sub-Install-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Sub_Install_enables_optional_test} && !%{defined perl_bootstrap}
%endif
Requires:       perl(B)
Provides:       perl(Sub::Install)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module makes it easy to install subroutines into packages without the
unsightly mess of no strict or typeglobs lying about where just anyone
can see them.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Sub-Install-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.929-9
- Prepare for Oreon 11 (RP1)
