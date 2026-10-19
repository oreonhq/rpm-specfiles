%global source0_hash 00cc5a454f733367403dcdbba21966047f920c5abc5f03e6847d2f53e0c57996
Name:           perl-IO-Prompt-Tiny
Version:        0.003
Release:        1%{?dist}
Summary:        Prompt for user input with a default option
License:        Apache-2.0
URL:            https://metacpan.org/release/IO-Prompt-Tiny
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/IO-Prompt-Tiny-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is an extremely simple prompting module, based on the extremely simple
prompt offered by ExtUtils::MakeMaker.In many cases, that's all you need and
this module gives it to you without all the overhead of ExtUtils::MakeMaker just
to prompt for input.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IO-Prompt-Tiny-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
