%global source0_hash 542530f9930d5874de51e3105239ff472c20972ead49e6949dc21564f9f8a4f8
Name:           perl-ORLite-Mirror
Version:        1.24
Release:        1%{?dist}
Summary:        Extend ORLite to support remote SQLite databases
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/ORLite-Mirror
Source0:        https://cpan.metacpan.org/authors/id/A/AD/ADAMK/ORLite-Mirror-%{version}.tar.gz
Patch0:         ORLite-Mirror-1.24-Remove-using-of-MI-DSL.patch
BuildArch:      noarch
Requires:       perl(IO::Uncompress::Bunzip2) >= 2.008
Requires:       perl(IO::Uncompress::Gunzip) >= 2.008
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Remove)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(IO::Compress::Bzip2)
BuildRequires:  perl(IO::Compress::Gzip)
BuildRequires:  perl(IO::Uncompress::Bunzip2)
BuildRequires:  perl(IO::Uncompress::Gunzip)
BuildRequires:  perl(LWP::Online)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Share)
BuildRequires:  perl(Module::Install::With)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(ORLite)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::file)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
ORLite provides a read-only ORM API when it loads a read-only SQLite database
from your local system. By combining this capability with LWP, ORLite::Mirror
goes one step better and allows you to load a SQLite database from any
arbitrary URI in read-only form as well.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ORLite-Mirror-%{version}
%patch -P0 -p1
# Remove bundled libraries
rm -r inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name stub.db -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
