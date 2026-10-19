%global source0_hash 71a871c717ce4bfdc1dfd98775edb516f21f1805aaa4d8fd519b6446ca99f3ae
%bcond_without perl_Term_Terminfo_enables_optional_test
%bcond_without perl_Term_Terminfo_enables_unibilium
Name:           perl-Term-Terminfo
Version:        0.09
Release:        19%{?dist}
Summary:        Access the terminfo database
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Term-Terminfo
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Term-Terminfo-%{version}.tar.gz
%if %{with perl_Term_Terminfo_enables_unibilium}
%else
%endif
%if %{with perl_Term_Terminfo_enables_optional_test}
%endif
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build::Using::PkgConfig)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(unibilium)
# /oreon:deps
%description
Objects in Term::Terminfo Perl class provide access to the terminfo database
entries.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Term-Terminfo-%{version}
%if !%{with perl_Term_Terminfo_enables_optional_test}
rm t/99pod.t
perl -i -ne 'print $_ unless m{^t/99pod\.t}' MANIFEST
%endif

%build

perl Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build
%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
