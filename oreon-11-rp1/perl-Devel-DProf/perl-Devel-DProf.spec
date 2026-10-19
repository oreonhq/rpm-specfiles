%global source0_hash b9eec466ab77aa9f6ab48d33134694d1aa5a8cd221b1aa0a00d09c93ab69643c
Name:           perl-Devel-DProf
Version:        20110802.00
Release:        1%{?dist}
Summary:        Deprecated Perl code profiler
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-DProf
Source0:        https://cpan.metacpan.org/authors/id/F/FL/FLORA/Devel-DProf-%{version}.tar.gz
Patch0:         Devel-DProf-20110802.00-Work-around-static-XS_Devel__DProf_END-mismatch.patch
Requires:       perl(deprecate)
Requires:       perl(Pod::Usage)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(deprecate)
BuildRequires:  perl(if)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The Devel::DProf package is a Perl code profiler. This will collect
information on the execution time of a Perl script and of the subs in that
script. This information can be used to determine which subroutines are
using the most time and which subroutines are being called most often. This
information can also be used to create an execution graph of the script,
showing subroutine relationships.

This module is deprecated and new users are advised to use Devel::NYTProf
instead.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Devel-DProf-%{version}
%patch -P0 -p1

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
