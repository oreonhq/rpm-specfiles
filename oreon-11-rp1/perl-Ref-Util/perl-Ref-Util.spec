%global source0_hash 415fa73dbacf44f3d5d79c14888cc994562720ab468e6f71f91cd1f769f105e1
%bcond_with perl_Ref_Util_enables_optional_test
Name:		perl-Ref-Util
Version:	0.204
Release:        1%{?dist}
Summary:        Utility functions for checking references
License:	MIT
URL:		https://metacpan.org/release/Ref-Util
Source0:        https://cpan.metacpan.org/modules/by-module/Ref/Ref-Util-%{version}.tar.gz
BuildArch:	noarch
%if %{with perl_Ref_Util_enables_optional_test}
%endif
Requires:	perl(Ref::Util::XS)
Provides:       perl(Ref::Util)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IPC::Open2)
BuildRequires:  perl(Ref::Util::XS)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Ref::Util introduces several functions to help identify references in a faster
and smarter way.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Ref-Util-%{version}

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

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.204-24
- Prepare for Oreon 11 (RP1)
