%global source0_hash 6e185c59f778d40c56023adfa9321623952f2cad474016e1d85addce4bd6d9ee

Name:           perl-Devel-CallParser
Version:        0.004
Release:        1%{?dist}
Summary:        Custom parsing attached to subroutines
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-CallParser
Source0:        https://cpan.metacpan.org/modules/by-module/Devel/Devel-CallParser-%{version}.tar.gz
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.11.2
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.15
BuildRequires:  perl(Module::Build)
# Module
BuildRequires:  perl(Devel::CallChecker) >= 0.002
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(DynaLoader::Functions) >= 0.001
BuildRequires:  perl(Exporter)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::ParseXS)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File) >= 1.03
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
# Optional Tests
#BuildRequires: perl(Data::Alias) >= 1.13          # Retired in Fedora since Fedora 25, could be revived if desired
BuildRequires:  perl(Devel::Declare) >= 0.006004
BuildRequires:  perl(indirect) >= 0.27
BuildRequires:  perl(Lexical::Sub) >= 0.004
#BuildRequires: perl(Sub::StrictDecl) >= 0.001     # Not yet packaged
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
# Dependencies
Requires:       perl(Devel::CallChecker) >= 0.002
Requires:       perl(DynaLoader)
Requires:       perl(DynaLoader::Functions) >= 0.001

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Devel::CallChecker\\)

Provides:       perl(Devel::CallParser)
Provides:       perl(Devel::CallParser)
%description
This module provides a C API, for XS modules, concerned with custom parsing.
It is centered around the function cv_set_call_parser, which allows XS code to
attach a magical annotation to a Perl subroutine, resulting in resolvable
calls to that subroutine having their arguments parsed by arbitrary C code
(this is a more conveniently structured facility than the core's
PL_keyword_plugin API). This module makes cv_set_call_parser and several
supporting functions available.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Devel-CallParser-%{version}

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
%{perl_vendorarch}/auto/Devel/
%{perl_vendorarch}/Devel/
%{_mandir}/man3/Devel::CallParser.3*

%changelog
%autochangelog
