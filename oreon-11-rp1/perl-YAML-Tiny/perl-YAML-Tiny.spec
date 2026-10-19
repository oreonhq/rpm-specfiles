%global source0_hash a8d584394cf069bf8f17cba3dd5099003b097fce316c31fb094f1b1c171c08a3
%{bcond_with perl_YAML_Tiny_enables_JSON_MaybeX_test}
Name:           perl-YAML-Tiny
Version:        1.76
Release:        1%{?dist}
Summary:        Read/Write YAML files with as little code as possible
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/YAML-Tiny
Source0:        https://www.cpan.org/modules/by-module/YAML/YAML-Tiny-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_YAML_Tiny_enables_JSON_MaybeX_test}
%endif
Requires:       perl(Carp)
Requires:       perl(Config)
Requires:       perl(Fcntl)
Provides:       perl(YAML::Tiny)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Dir)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(open)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
YAML::Tiny is a Perl class for reading and writing YAML-style files,
written with as little code as possible, reducing load time and
memory overhead.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n YAML-Tiny-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.76-4
- Prepare for Oreon 11 (RP1)
