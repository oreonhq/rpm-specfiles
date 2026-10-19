%global source0_hash 962a1e8602621118d8b031283cc1220561d166894ce206d9d0ecf0049dd83975
Name:           perl-criticism
Version:        1.02
Release:        1%{?dist}
Summary:        Perl pragma to enforce coding standards and best-practices
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/criticism
Source0:        https://cpan.metacpan.org/authors/id/T/TH/THALJEF/criticism/criticism-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Perl::Critic) >= 1.089
Requires:       perl(Perl::Critic::Violation)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(English)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(Perl::Critic)
BuildRequires:  perl(Perl::Critic::Violation)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This pragma enforces coding standards and promotes best-practices by
running your file through Perl::Critic before every execution. In a
production system, this usually isn't feasible because it adds a lot of
overhead at start-up. If you have a separate development environment, you
can effectively bypass the criticism pragma by not installing Perl::Critic
in the production environment. If Perl::Critic can't be loaded, then
criticism just fails silently.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n criticism-%{version}
chmod 644 lib/*.pm

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
