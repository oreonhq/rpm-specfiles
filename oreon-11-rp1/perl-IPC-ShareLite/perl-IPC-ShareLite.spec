%global source0_hash 14d406b91da96d6521d0d1a82d22a306274765226b86b0a56e7ffddcf96ae7bf

Name:           perl-IPC-ShareLite
Version:        0.17
Release:        51%{?dist}
Summary:        Lightweight interface to shared memory
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IPC-ShareLite
Source0:        https://cpan.metacpan.org/authors/id/A/AN/ANDYA/IPC-ShareLite-%{version}.tar.gz
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Devel::CheckLib)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
# Runtime
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(subs)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
# Optional tests only
BuildRequires:  perl(Test::Pod) >= 1.14

%description
IPC::ShareLite provides a simple interface to shared memory, allowing
data to be efficiently communicated between processes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IPC-ShareLite-%{version}
# Drop the bundled modules
rm -rf inc && perl -ni -e 'print unless m|^inc/|' MANIFEST
# metafile is broken and we don't need it anyway
perl -ni -e 'print if $. < 50' Makefile.PL

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/IPC*
%{_mandir}/man3/*

%changelog
%autochangelog
