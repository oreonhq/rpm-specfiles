Name:           perl-Devel-StackTrace
Summary:        Perl module implementing stack trace and stack trace frame objects
Version:        2.05
Epoch:          1
Release:        7%{?dist}
License:        Artistic-2.0
URL:            https://metacpan.org/release/Devel-StackTrace
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Devel-StackTrace-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 63cb6196e986a7e578c4d28b3c780e7194835bfc78b68eeb8f00599d4444888c
%global source0_file Devel-StackTrace-2.05.tar.gz
# oreon url source checksums end
BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  %{__perl}
BuildRequires:  %{__make}

BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(overload)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%description
The Devel::StackTrace module contains two classes, Devel::StackTrace
and Devel::StackTraceFrame.  The goal of this object is to encapsulate
the information that can found through using the caller() function, as
well as providing a simple interface to this data.

The Devel::StackTrace object contains a set of Devel::StackTraceFrame
objects, one for each level of the stack.  The frames contain all the
data available from caller() as of Perl 5.6.0.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Devel-StackTrace-2.05.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "63cb6196e986a7e578c4d28b3c780e7194835bfc78b68eeb8f00599d4444888c" || { echo "oreon: Source0 SHA256 mismatch for Devel-StackTrace-2.05.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Devel-StackTrace-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes
%license LICENSE
%{perl_vendorlib}/Devel
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.05-7
- Prepare for Oreon 11 (RP1)
