%global source0_hash fb64c5a823787f6600257918febd9fbc6f0305936fc3287b81a30c099b65633c
%bcond_with perl_Ref_Util_XS_enables_optional_test
Name:		perl-Ref-Util-XS
Version:	0.117
Release:        28%{?dist}
Summary:        Utility functions for checking references
License:	MIT
URL:		https://metacpan.org/release/Ref-Util-XS
Source0:        https://cpan.metacpan.org/modules/by-module/Ref/Ref-Util-XS-%{version}.tar.gz
%if %{with perl_Ref_Util_XS_enables_optional_test}
%endif
%{?perl_default_filter}
Provides:       perl(Ref::Util::XS)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Ref::Util::XS introduces several functions to help identify references in a
faster and smarter way.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Ref-Util-XS-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.117-28
- Prepare for Oreon 11 (RP1)
