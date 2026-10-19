%global source0_hash 768b7697b4b8d4d372c7507b65e9dd26aa4223f7100183bbb4d3af46d43869b5
Name:		perl-Devel-CheckCompiler
Version:	0.07
Release:        28%{?dist}
Summary:        Check the compiler's availability
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Devel-CheckCompiler
Source0:        https://cpan.metacpan.org/modules/by-module/Devel/Devel-CheckCompiler-%{version}.tar.gz
BuildArch:	noarch
Requires:	perl(File::Temp)
Provides:       perl(Devel::AssertC99)
Provides:       perl(Devel::CheckCompiler)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Devel::CheckCompiler is checker for compiler's availability.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Devel-CheckCompiler-%{version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
