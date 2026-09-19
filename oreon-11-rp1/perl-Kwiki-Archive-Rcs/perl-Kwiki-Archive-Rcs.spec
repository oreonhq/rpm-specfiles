%global source0_hash 48218d981c63ebd565938ef6a89adc5850d23a8eab0964f5b2597dfd08878e2c

Name:           perl-Kwiki-Archive-Rcs
Version:        0.16
Release:        46%{?dist}
Summary:        Kwiki Page Archival Using RCS
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Kwiki-Archive-Rcs
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Kwiki-Archive-Rcs-%{version}.tar.gz
Patch0:         Kwiki-Archive-Rcs-0.16-Fix-unescaped-left-brace-in-regex.patch
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(vars)
BuildRequires:  perl(strict)
# Runtime
BuildRequires:  perl(Date::Manip)
BuildRequires:  perl(Kwiki::Archive)
# Tests only
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
Requires:       perl(Kwiki) >= 0.38
Requires:       rcs

%description
Kwiki Page Archival Using RCS.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Kwiki-Archive-Rcs-%{version}
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
