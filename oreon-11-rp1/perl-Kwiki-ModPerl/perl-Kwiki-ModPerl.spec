%global source0_hash 5025289a3824fb1ce3991e0d07c6743099d9123c83c1e186989b9da13cf4eefb

Name:           perl-Kwiki-ModPerl
Version:        0.09
Release:        56%{?dist}
Summary:        Enable Kwiki to work under mod_perl
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Kwiki-ModPerl
Source0:        https://cpan.metacpan.org/authors/id/G/GU/GUGOD/Kwiki-ModPerl-%{version}.tar.gz
# Perl 5.18 compatibility, CPAN RT#87450
Patch0:         Kwiki-ModPerl-0.09-Parenthesise-qw-explicitly.patch
Patch1:         Kwiki-ModPerl-0.09-Fix-building-on-Perl-without-dot-in-INC.patch
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Runtime
BuildRequires:  perl(Apache2::Const)
BuildRequires:  perl(Apache2::RequestIO)
BuildRequires:  perl(Apache2::RequestRec)
BuildRequires:  perl(Apache2::RequestUtil)
BuildRequires:  perl(constant)
BuildRequires:  perl(Kwiki) >= 0.32
BuildRequires:  perl(mod_perl2)
# Tests only
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
Requires:       perl(Apache2::Const)
Requires:       perl(Apache2::RequestIO)
Requires:       perl(Apache2::RequestRec)
Requires:       perl(Apache2::RequestUtil)
Requires:       perl(Kwiki) >= 0.32
Requires:       perl(mod_perl2)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Kwiki\\)$

%description
This module allows you to use Kwiki as a mod_perl content handler.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Kwiki-ModPerl-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
