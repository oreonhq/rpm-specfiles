%global source0_hash d318a85bb29ee3c770e6b888585692a6f1a0173faf001be995e97481212536bf

Name:           perl-Devel-SimpleTrace
Version:        0.08
Release:        27%{?dist}
Summary:        See where you code warns and dies using stack traces
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-SimpleTrace
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SAPER/Devel-SimpleTrace-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(Data::Dumper)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test::Distribution)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 0.08
BuildRequires:  perl(Test::Portability::Files)
Requires:       perl(Data::Dumper)

%description
This Perl module can be used to more easily spot the place where a program or a
module generates errors.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Devel-SimpleTrace-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}

%check
make test

%files
%license LICENSE LICENSE.Artistic LICENSE.GPL
# eg directory is not helpful
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
