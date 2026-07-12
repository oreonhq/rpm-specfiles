%global source0_hash 499bb1b482db24fda277a51525596ad092c2bd51dd508fa8fec2e9f849097402

Name:		perl-Params-Util
Version:	1.102
Release:	20%{?dist}
Summary:	Simple standalone parameter-checking functions
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Params-Util
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REHSACK/Params-Util-%{version}.tar.gz

Requires:	perl(Scalar::Util) >= 1.18
Requires:       perl(XSLoader) >= 0.22

BuildRequires:  %{__perl}
BuildRequires:  %{__make}
BuildRequires:  gcc

BuildRequires:	perl-interpreter
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Config::AutoConf)
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.52
BuildRequires:	perl(File::Spec) >= 0.82
BuildRequires:	perl(strict)
BuildRequires:  perl(inc::latest)

# Run-time:
BuildRequires:	perl(Exporter)
BuildRequires:	perl(overload)
BuildRequires:	perl(Scalar::Util) >= 1.18
BuildRequires:  perl(XSLoader) >= 0.22
BuildRequires:	perl(vars)
# Tests:
BuildRequires:	perl(Test::More) >= 0.47
BuildRequires:	perl(File::Spec::Functions)

%{?perl_default_filter}

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Scalar::Util\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(XSLoader\\)$

Provides:       perl(Params::Util)
%description
Params::Util provides a basic set of importable functions that 
makes checking parameters a hell of a lot easier.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Params-Util-%{version}
rm -rf inc/latest* inc/inc_*

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{__make} test AUTOMATED_TESTING=1

%files
%doc Changes
%license LICENSE
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Params

%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.102-20
- Prepare for Oreon 11 (RP1)
