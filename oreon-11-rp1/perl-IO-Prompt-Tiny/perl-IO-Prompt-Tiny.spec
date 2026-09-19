%global source0_hash 00cc5a454f733367403dcdbba21966047f920c5abc5f03e6847d2f53e0c57996

Name:           perl-IO-Prompt-Tiny
Version:        0.003
Release:        29%{?dist}
Summary:        Prompt for user input with a default option
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://metacpan.org/release/IO-Prompt-Tiny
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/IO-Prompt-Tiny-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.17
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
# Tests:
BuildRequires:  perl(Capture::Tiny) >= 0.12
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More) >= 0.96

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

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING.mkdn README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
