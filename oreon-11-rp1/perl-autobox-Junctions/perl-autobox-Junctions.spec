%global source0_hash 30f5eac88817a45231f14f8b309162a535cf7c4fe1ebd131c942984134fcb12d

Name:           perl-autobox-Junctions
Version:        0.002
Release:        28%{?dist}
Summary:        Autoboxified junction-style operators
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://metacpan.org/release/autobox-Junctions
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSRCHBOY/autobox-Junctions-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(autobox)
BuildRequires:  perl(parent)
BuildRequires:  perl(Syntax::Keyword::Junction)
# Tests:
BuildRequires:  perl(blib) >= 1.01
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::CheckDeps) >= 0.010
BuildRequires:  perl(Test::More) >= 0.94
# Optional tests:
# CPAN::Meta not helpful

%description
This is a simple autoboxifying wrapper around Syntax::Keyword::Junction Perl
module, that provides array and array references with the functions provided
by that package as methods for arrays: any, all, one, and none.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n autobox-Junctions-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
