%global source0_hash d72ce76f796c4b61f7fc1a22a39aceab08347aa45de10b0d7c08d468822bc94b
Name:           perl-App-find2perl
Version:        1.005
Release:        1%{?dist}
Summary:        Translate find command lines to Perl code
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/App-find2perl
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/App-find2perl-%{version}.tar.gz
BuildArch:      noarch
%if %{defined perl_bootstrap}
%endif
%if %{defined perl_bootstrap}
%endif
%if !%{defined perl_bootstrap}
%endif
%if !%{defined perl_bootstrap}
%endif
%if !%{defined perl_bootstrap}
%endif
%if !%{defined perl_bootstrap}
%endif
%if !%{defined perl_bootstrap}
%endif
Conflicts:      perl < 4:5.18.2-300
# oreon:deps
BuildRequires:  //bin/find
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Devel::FindPerl)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open2)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Perl::OSType)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(open)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This package delivers find2perl tool which is a little translator to convert
find command lines to equivalent Perl code.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n App-find2perl-%{version}
%if %{defined perl_bootstrap}
rm t/find2perl.t
sed -i -e '/^t\/find2perl.t/d' MANIFEST
%endif

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
