%global source0_hash 461fe5f6a189e6dc85f8776f7534fdb9821ecb3e04d839268d31353f9b429d7e
%global gnupghome %(mktemp --directory)
Name:           perl-Module-Signature
Version:        0.96
Release:        1%{?dist}
Summary:        CPAN signature management utilities and modules
License:        CC0-1.0
URL:            https://metacpan.org/release/Module-Signature
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TIMLEGGE/Module-Signature-%{version}.tar.gz
BuildArch:      noarch
Requires:       gnupg2
Requires:       perl(Digest::SHA)
Requires:       perl(File::Temp)
Requires:       perl(IO::Socket::INET)
Requires:       perl(Text::Diff)
Requires:       perl(version)
Suggests:       perl(PAR::Dist)
Suggests:       /usr/bin/perldoc
Provides:       perl(Module::Signature)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Diff)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This package contains a command line tool and module for checking and creating
SIGNATURE files for Perl CPAN distributions.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Module-Signature-%{version}

%build

export GNUPGHOME=%{gnupghome}
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

export GNUPGHOME=%{gnupghome}
make test TEST_SIGNATURE=0
%clean
rm -rf %{buildroot} %{gnupghome}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
