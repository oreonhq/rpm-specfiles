%global source0_hash 16d6e0352d02402cdd46bc8d7c426c66cd8488d7066878b250e50a6a34e47b58

Name:           perl-File-ShareDir-Tiny
Version:        0.001
Release:        4%{?dist}
Summary:        Locate per-dist and per-module shared files

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/File-ShareDir-Tiny
Source0:        http://www.cpan.org/authors/id/L/LE/LEONT/File-ShareDir-Tiny-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(blib)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.89
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
Quite often you want or need your Perl module (CPAN or otherwise)
to have access to a large amount of read-only data that is stored
on the file-system at run-time.

On a linux-like system, this would be in a place such as /usr/share,
however Perl runs on a wide variety of different systems, and so
the use of any one location is unreliable.

This module provides a more portable way to have (read-only) data
for your module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-ShareDir-Tiny-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%license LICENSE
%dir %{perl_vendorlib}/File
%dir %{perl_vendorlib}/File/ShareDir
%{perl_vendorlib}/File/ShareDir/Tiny.pm
%{_mandir}/man3/File::ShareDir::Tiny.3pm*

%changelog
%autochangelog
