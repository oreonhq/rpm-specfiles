%global source0_hash 48218d981c63ebd565938ef6a89adc5850d23a8eab0964f5b2597dfd08878e2c
Name:           perl-Kwiki-Archive-Rcs
Version:        0.16
Release:        1%{?dist}
Summary:        Kwiki Page Archival Using RCS
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Kwiki-Archive-Rcs
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Kwiki-Archive-Rcs-%{version}.tar.gz
Patch0:         Kwiki-Archive-Rcs-0.16-Fix-unescaped-left-brace-in-regex.patch
BuildArch:      noarch
Requires:       perl(Kwiki) >= 0.38
Requires:       rcs
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Date::Manip)
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Kwiki::Archive)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
