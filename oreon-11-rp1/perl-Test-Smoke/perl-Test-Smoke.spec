%global source0_hash 798ad2673957df9d1bcde0f51b0436eed9dd995308912e77775467de9bef4cd3

Name:           perl-Test-Smoke
Version:        1.84
Release:        3%{?dist}
Summary:        Perl core test smoke suite
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Smoke
Source0:        https://cpan.metacpan.org/authors/id/C/CO/CONTRA/Test-Smoke-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Cpanel::JSON::XS)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::ParseWords)
# Run-time
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(autodie)
BuildRequires:  perl(base)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec) >= 0.82
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request)
# HTTP::Tiny is not needed for tests
# LWP::Simple is not needed for tests
BuildRequires:  perl(LWP::UserAgent)
# Mail::Sendmail - optional tests - bundled
# BuildRequires:  perl(MIME::Lite)
# Net::FTP is not needed for tests
BuildRequires:  perl(overload)
BuildRequires:  perl(Path::Tiny)
# Pod::Usage is not needed for tests
BuildRequires:  perl(POSIX)
BuildRequires:  perl(System::Info)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Errno)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Daemon)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::Zlib)
BuildRequires:  perl(JSON)
BuildRequires:  perl(lib)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(subs)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(version)
Requires:       perl(Mail::Sendmail)
Requires:       perl(File::Spec) >= 0.82
Requires:       perl(HTTP::Headers)
Requires:       perl(HTTP::Request)
Requires:       perl(LWP::Simple)

%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(Mail::Sendmail\\)
# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(GitUtils\\)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(TestLib\\)

%description
The perl core test smoke suite is a set of scripts and modules that try to run
the perl core tests on as many configurations as possible and combine the
results into an easy to read report.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Smoke-%{version}

# Ignore output files from find-debuginfo.sh to fix the test 00-manifest.t
echo '.+\.list' >> MANIFEST.SKIP

# Fix shebang for the script
perl -MConfig -i -pe 's{^#!.*perl}{$Config{startperl}}' bin/tsrepostjsn.pl

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
rm -rf %{buildroot}/%{_bindir}/tsw32configure.pl
rm -rf %{buildroot}/%{_mandir}/man1/tsw32configure*
rm -rf %{buildroot}/%{perl_vendorlib}/inc/JSON.pm
rm -rf %{buildroot}/%{perl_vendorlib}/inc/Mail/Sendmail.pm

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/syncer_ftp.t
mkdir -p %{buildroot}%{_libexecdir}/%{name}/lib/Test/Smoke
ln -s %{perl_vendorlib}/Test/Smoke/perlcurrent.cfg %{buildroot}%{_libexecdir}/%{name}/lib/Test/Smoke
rm %{buildroot}%{_libexecdir}/%{name}/t/vms_rl.t
rm %{buildroot}%{_libexecdir}/%{name}/t/win32_error_mode.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into temporary files/directories. The easiest solution
# is to copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I .
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
make test

%files
%doc Changes README.pod
%{_bindir}/tsarchive.pl
%{_bindir}/tsarchivelog.pl
%{_bindir}/tsconfigsmoke.pl
#%%{_bindir}/tshandlequeue.pl
%{_bindir}/tsreport.pl
%{_bindir}/tsrepostjsn.pl
%{_bindir}/tsrunsmoke.pl
%{_bindir}/tssendrpt.pl
%{_bindir}/tssmokeperl.pl
%{_bindir}/tssmokestatus.pl
%{_bindir}/tssysinfo.pl
%{_bindir}/tssynctree.pl
%{perl_vendorlib}/configsmoke*
%{perl_vendorlib}/Test/Smoke*
%{_mandir}/man1/configsmoke*
%{_mandir}/man1/tsconfigsmoke.pl*
%{_mandir}/man1/tssmokestatus.pl*
%{_mandir}/man3/Test::Smoke*
%{_mandir}/man3/configsmoke*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
