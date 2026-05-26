# Store keys in a temp directory
%global gnupghome %(mktemp --directory)

Name:           perl-Module-Signature
Version:        0.93
Release:        3%{?dist}
Summary:        CPAN signature management utilities and modules
License:        CC0-1.0
URL:            https://metacpan.org/release/Module-Signature
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TIMLEGGE/Module-Signature-0.93.tar.gz
# oreon url source checksums begin
%global source0_sha256 d0b128ec34152540f05187b8412808ed3661aa57e81c1cf959d06c35295b1f3a
%global source0_file Module-Signature-0.93.tar.gz
# oreon url source checksums end

BuildArch:      noarch
# Module build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
# Module runtime
BuildRequires:  gnupg2
BuildRequires:  perl(constant)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::Diff)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
# Test suite
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
# Dependencies
Requires:       gnupg2
Requires:       perl(Digest::SHA)
Requires:       perl(File::Temp)
Requires:       perl(IO::Socket::INET)
Requires:       perl(Text::Diff)
Requires:       perl(version)
Suggests:       perl(PAR::Dist)
Suggests:       /usr/bin/perldoc

%description
This package contains a command line tool and module for checking and creating
SIGNATURE files for Perl CPAN distributions.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Module-Signature-0.93.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "d0b128ec34152540f05187b8412808ed3661aa57e81c1cf959d06c35295b1f3a" || { echo "oreon: Source0 SHA256 mismatch for Module-Signature-0.93.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Module-Signature-%{version}

%build
export GNUPGHOME=%{gnupghome}
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
export GNUPGHOME=%{gnupghome}
# Don't try to run signature test because it needs access over network to keyserver,
# even if we have the necessary keys already
make test TEST_SIGNATURE=0

%clean
rm -rf %{buildroot} %{gnupghome}

%files
%doc AUTHORS Changes SECURITY.md *.pub
%{_bindir}/cpansign
%{perl_vendorlib}/Module/
%{_mandir}/man1/cpansign.1*
%{_mandir}/man3/Module::Signature.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.93-3
- Prepare for Oreon 11 (RP1)
