%global source0_hash b6919ba49b9fe98bfdf3e8accae7b9b7f78dc9e71ebbd0b7fef7a45d99324ccb
Name:           perl-Data-Uniqid
Version:        0.12
Release:        1%{?dist}
Summary:        Perl extension for simple generating of unique id's
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-Uniqid
Source0:        https://cpan.metacpan.org/modules/by-module/Data/Data-Uniqid-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(Data::Uniqid)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Data::Uniqid provides three simple routines for generating unique ids.
These ids are coded with a Base62 system to make them short and handy (e.g.
to use it as part of a URL).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Data-Uniqid-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
