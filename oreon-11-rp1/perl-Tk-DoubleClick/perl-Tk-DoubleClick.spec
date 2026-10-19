%global source0_hash 32c35af57a6bb8bd55ff18508a51d2ca40ab316ef07b042a7c6eec1c71d7acc5
Name:           perl-Tk-DoubleClick
Version:        0.04
Release:        29%{?dist}
Summary:        Correctly handle single-click vs double-click events
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tk-DoubleClick
Source0:        https://cpan.metacpan.org/authors/id/D/DD/DDUMONT/Tk-DoubleClick-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Tk)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Tk::DoubleClick module correctly handle single-click vs double-click
events, calling only the appropriate callback for the given event.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Tk-DoubleClick-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
