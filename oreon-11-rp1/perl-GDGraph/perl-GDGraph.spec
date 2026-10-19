%global source0_hash 6f49cc4e59015480db9c9b6b18afd8c50be30886687b69411513d06f38971113
Name:           perl-GDGraph
Epoch:          1
Version:        1.56
Release:        1%{?dist}
Summary:        Graph generation package for Perl
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND GPL-2.0-or-later
URL:            https://metacpan.org/release/GDGraph
Source0:        https://cpan.metacpan.org/modules/by-module/GD/GDGraph-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Data::Dumper)
Requires:       perl(GD) >= 1.18
Requires:       perl(GD::Text) >= 0.80
Requires:       perl(Text::ParseWords)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(GD\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(GD)
BuildRequires:  perl(GD::Text)
BuildRequires:  perl(GD::Text::Align)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n GDGraph-%{version}

# Fix shellbangs
perl -pi -e 's{^#!/usr/local/bin/perl\b}{#!%{__perl}}' \
  samples/sample1A.pl \
  samples/make_index.pl

# Fix line endings
perl -pi -e 's/\r\n/\n/' samples/sample64.pl

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
