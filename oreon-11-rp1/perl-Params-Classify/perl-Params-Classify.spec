# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Params_Classify_enables_optional_test
%else
%bcond_with perl_Params_Classify_enables_optional_test
%endif

Name:           perl-Params-Classify
Version:        0.015
Release:        28%{?dist}
Summary:        Argument type classification
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Params-Classify
Source0:        https://cpan.metacpan.org/modules/by-module/Params/Params-Classify-%{version}.tar.gz
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.15
BuildRequires:  perl(ExtUtils::ParseXS) >= 3.30
BuildRequires:  perl(Module::Build)
# Module Runtime
BuildRequires:  perl(Devel::CallChecker) >= 0.003
BuildRequires:  perl(Exporter)
BuildRequires:  perl(parent)
BuildRequires:  perl(Scalar::Util) >= 1.01
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Test Suite
BuildRequires:  perl(Test::More)
%if %{with perl_Params_Classify_enables_optional_test}
# Optional Tests
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
%endif
# Dependencies
Requires:       perl(Devel::CallChecker) >= 0.003
Requires:       perl(Exporter)
Requires:       perl(Scalar::Util) >= 1.01
Requires:       perl(XSLoader)

# Don't "provide" private Perl libs
%{?perl_default_filter}

%description
This module provides various type-testing functions. These are intended
for functions that, unlike most Perl code, care what type of data they
are operating on. For example, some functions wish to behave
differently depending on the type of their arguments (like overloaded
functions in C++).

%prep
%setup -q -n Params-Classify-%{version}

%build
perl Build.PL --installdirs=vendor --optimize="%{optflags}"
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%doc Changes README
%{perl_vendorarch}/auto/Params/
%{perl_vendorarch}/Params/
%{_mandir}/man3/Params::Classify.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.015-28
- Prepare for Oreon 11 (RP1)
