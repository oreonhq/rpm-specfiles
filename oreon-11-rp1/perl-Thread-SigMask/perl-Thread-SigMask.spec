%global source0_hash f4baa4841b990b1fff742d3256dd1a91885603e3fdaf134337dd9dd13408113a

Name:           perl-Thread-SigMask
Version:        0.004
Release:        42%{?dist}
Summary:        Thread specific signal masks
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Thread-SigMask
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/Thread-SigMask-%{version}.tar.gz

BuildRequires:  perl-interpreter >= 0:5.006
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(blib)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)

%description
This module provides per-thread signal masks. On non-threaded perls it will
be effectively the same as POSIX::sigprocmask. The interface works exactly
the same as sigprocmask.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Thread-SigMask-%{version}

%build
%{__perl} Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%license LICENSE
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Thread*
%{_mandir}/man3/*

%changelog
%autochangelog
