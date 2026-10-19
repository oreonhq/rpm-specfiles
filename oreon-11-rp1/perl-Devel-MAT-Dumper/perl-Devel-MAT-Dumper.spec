%global source0_hash e8dfd5dc2dfada33c20237a260ecb6d586ce582d49bbfa06d2f3b5736f2007c0
Name:           perl-Devel-MAT-Dumper
Version:        0.51
Release:        1%{?dist}
Summary:        Write a heap dump file for later analysis
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Devel-MAT-Dumper
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Devel-MAT-Dumper-%{version}.tar.gz
%{?perl_default_filter}
Provides:       perl(Devel::MAT::Dumper)
Provides:       perl(Devel::MAT::Dumper::Helper)
Provides:       perl(Devel::MAT::Dumper)
Provides:       perl(Devel::MAT::Dumper::Helper)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
