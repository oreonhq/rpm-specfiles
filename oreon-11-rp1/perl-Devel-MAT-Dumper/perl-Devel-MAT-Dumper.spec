%global source0_hash e8dfd5dc2dfada33c20237a260ecb6d586ce582d49bbfa06d2f3b5736f2007c0

Name:           perl-Devel-MAT-Dumper
Version:        0.51
Release:        1%{?dist}
Summary:        Write a heap dump file for later analysis
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/dist/Devel-MAT-Dumper
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Devel-MAT-Dumper-%{version}.tar.gz

# build requirements
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(ExtUtils::CBuilder)
# runtime requirements
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(Config)
BuildRequires:  perl(Test::More) >= 0.88

%{?perl_default_filter}

Provides:       perl(Devel::MAT::Dumper)
Provides:       perl(Devel::MAT::Dumper::Helper)
Provides:       perl(Devel::MAT::Dumper)
Provides:       perl(Devel::MAT::Dumper::Helper)
%description
This module provides the memory-dumping function that creates a heap dump
file which can later be read by Devel::MAT::Dumpfile. It provides a single
function which is not exported, which writes a file to the given path.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Devel-MAT-Dumper-%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
/usr/bin/find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes doc README
%license LICENSE
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Devel*
%{_mandir}/man3/*

%changelog
%autochangelog
