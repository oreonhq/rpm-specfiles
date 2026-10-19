%global source0_hash 4bf2139ff617d6e59cc0e59cdecd7cb723ecfd28d5ac387afb553ffdc071b860
Name:           perl-Text-Reflow
Version:        1.17
Release:        32%{?dist}
Summary:        Perl module for reflowing text files using Knuth's paragraphing algorithm
License:        GPL-3.0-or-later AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/release/Text-Reflow
Source0:        https://cpan.metacpan.org/authors/id/M/MW/MWARD/Text-Reflow-%{version}.tar.gz
# oreon:deps
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(integer)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
These routines will reflow the paragraphs in the given file, filehandle,
string or array using Knuth's paragraphing algorithm (as used in TeX) to
pick "good" places to break the lines.

%package -n reflow
Summary:        A utility for reflowing text files using Knuth's paragraphing algorithm
License:        GPL-2.0-or-later
BuildArch:      noarch
%description -n reflow
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-Reflow-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles reflow usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n reflow -f %{oreon_filedir}/reflow.list

%changelog

%autochangelog
