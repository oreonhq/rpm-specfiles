%global source0_hash 51e7a47ae594cf55f66c0762f669215486e7d8b3460bdadfe79350ccf26daf38

Name:           perl-Crypt-DH-GMP
Version:        0.00012
Release:        38%{?dist}
Summary:        Crypt::DH Using GMP Directly
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-DH-GMP
Source0:        https://cpan.metacpan.org/authors/id/D/DM/DMAKI/Crypt-DH-GMP-%{version}.tar.gz
Patch0:         Crypt-DH-GMP-0.00012-Fix-building-on-Perl-with-bundled-library.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gmp-devel
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
%if ! (0%{?rhel})
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::AuthorTests)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Module::Install::XSUtil)
%else
BuildRequires:  gcc
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Devel::CheckLib)
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(FindBin)
%endif
# Run-time
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(Config)
BuildRequires:  perl(Crypt::DH)
BuildRequires:  perl(Math::BigInt::GMP)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(threads)
Requires:       perl(XSLoader)

%{?perl_default_filter}

%description
Crypt::DH::GMP is a (somewhat) portable replacement to Crypt::DH,
implemented mostly in C.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Crypt-DH-GMP-%{version}

%if ! (0%{?rhel})
# Remove bundled libraries
rm -r inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
%else
%patch -P0 -p1
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Crypt*
%{_mandir}/man3/*

%changelog
%autochangelog
