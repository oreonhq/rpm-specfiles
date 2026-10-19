%global source0_hash 6e185c59f778d40c56023adfa9321623952f2cad474016e1d85addce4bd6d9ee
Name:           perl-Devel-CallParser
Version:        0.004
Release:        1%{?dist}
Summary:        Custom parsing attached to subroutines
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-CallParser
Source0:        https://cpan.metacpan.org/authors/id/L/LN/LNATION/Devel-CallParser-%{version}.tar.gz
Requires:       perl(Devel::CallChecker) >= 0.002
Requires:       perl(DynaLoader)
Requires:       perl(DynaLoader::Functions) >= 0.001
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Devel::CallChecker\\)
Provides:       perl(Devel::CallParser)
Provides:       perl(Devel::CallParser)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Devel::CallChecker)
BuildRequires:  perl(Devel::Declare)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(DynaLoader::Functions)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::ParseXS)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Lexical::Sub)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(indirect)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
