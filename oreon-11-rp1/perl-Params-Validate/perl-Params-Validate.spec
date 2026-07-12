%global source0_hash 1bf2518ef2c4869f91590e219f545c8ef12ed53cf313e0eb5704adf7f1b2961e

Summary:        Params-Validate Perl module
Name:           perl-Params-Validate
Version:        1.31
Release:        13%{?dist}
# One file is GPL-1.0-or-later OR Artistic-1.0-Perl (c/ppport.h)
License:        Artistic-2.0 AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/release/Params-Validate
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Params-Validate-%{version}.tar.gz


BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Implementation) >= 0.04
BuildRequires:  perl(Module::Build) >= 0.4227

# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Scalar::Util) >= 1.20
BuildRequires:  perl(warnings)
BuildRequires:  perl(vars)
BuildRequires:  perl(XSLoader)

# Required by the tests
BuildRequires:  perl(base)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(JSON::PP) >= 2.27300
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::Taint) >= 0.02
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Readonly) >= 1.03

Provides:       perl(Params::Validate)
%description
The Params::Validate module allows you to validate method or function
call parameters to an arbitrary level of specificity. At the simplest
level, it is capable of validating the required parameters were given
and that no unspecified additional parameters were passed in. It is
also capable of determining that a parameter is of a specific type,
that it is an object of a certain class hierarchy, that it possesses
certain methods, or applying validation callbacks to arguments.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Params-Validate-%{version}

%build
%{__perl} Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes TODO
%license LICENSE
%{perl_vendorarch}/Params
%{perl_vendorarch}/auto/Params
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.31-13
- Prepare for Oreon 11 (RP1)
