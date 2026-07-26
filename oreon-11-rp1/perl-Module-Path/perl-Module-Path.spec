%global source0_hash b33179ce4dd73dfcde7d46808804b9ffbb11db0245fe455a7d001747562feaca

Name:           perl-Module-Path
Version:        0.19
Release:        32%{?dist}
Summary:        Get the full path to a locally installed module
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Path
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Module-Path-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Pod::Usage)
# Tests:
BuildRequires:  perl(Devel::FindPerl)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(FindBin) >= 0.05
BuildRequires:  perl(Test::More) >= 0.88

%description
This Module::Path Perl module provides a single function, module_path(), which
takes a module name and finds the first directory in your @INC path where the
module is installed locally. It returns the full path to that file, resolving
any symbolic links.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Path-%{version}
sed -i -e '1s|^#!.*|#!perl|' bin/mpath

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README TODO.md
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
%autochangelog
