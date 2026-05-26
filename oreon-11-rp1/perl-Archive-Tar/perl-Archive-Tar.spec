# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Archive_Tar_enables_optional_test
%else
%bcond_with perl_Archive_Tar_enables_optional_test
%endif

Name:           perl-Archive-Tar
Version:        3.04
Release:        522%{?dist}
Summary:        A module for Perl manipulation of .tar files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Archive-Tar
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Archive-Tar-%{version}.tar.gz
# Remove annoying sleep after warnings in the build script
Patch0:         Archive-Tar-2.02-Do-not-sleep-in-Makefile.PL.patch
# oreon url source checksums begin
%global source0_sha256 ba6b8addbedc43a463edcddf7b93accb7676c7b79c40f425b619d99545c4cb8c
%global source0_file Archive-Tar-3.04.tar.gz
# oreon url source checksums end
BuildArch:      noarch
# Most of the BRS are needed only for tests, compression support at run-time
# is optional soft dependency.
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# File::Copy not used
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec) >= 0.82
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Zlib) >= 1.01
BuildRequires:  perl(Pod::Usage)
# Time::Local not used on Linux
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Optional run-time:
BuildRequires:  perl(IO::Compress::Bzip2) >= 2.015
%if !%{defined perl_bootstrap}
BuildRequires:  perl(IO::Compress::Xz)
%endif
# IO::String not used if perl supports useperlio which is true
# Use Compress::Zlib's version for IO::Uncompress::Bunzip2
BuildRequires:  perl(IO::Uncompress::Bunzip2) >= 2.015
%if !%{defined perl_bootstrap}
BuildRequires:  perl(IO::Uncompress::UnXz)
BuildRequires:  perl(Text::Diff)
%endif
# Tests:
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Harness) >= 2.26
BuildRequires:  perl(Test::More)
# Optional tests:
%if %{with perl_Archive_Tar_enables_optional_test} && !%{defined perl_bootstrap}
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Test::Pod) >= 0.95
%endif
Requires:       perl(IO::Zlib) >= 1.01
# Optional run-time:
Requires:       perl(IO::Compress::Bzip2) >= 2.015
%if !%{defined perl_bootstrap}
Requires:       perl(IO::Compress::Xz)
%endif
# IO::String not used if perl supports useperlio which is true
# Use Compress::Zlib's version for IO::Uncompress::Bunzip2
Requires:       perl(IO::Uncompress::Bunzip2) >= 2.015
%if !%{defined perl_bootstrap}
Requires:       perl(IO::Uncompress::UnXz)
Requires:       perl(Text::Diff)
%endif

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(IO::Zlib\\)$

%description
Archive::Tar provides an object oriented mechanism for handling tar
files.  It provides class methods for quick and easy files handling
while also allowing for the creation of tar file objects for custom
manipulation.  If you have the IO::Zlib module installed, Archive::Tar
will also support compressed or gzipped tar files.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(ExtUtils::MakeMaker)
Requires:       perl(IPC::Cmd)
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Archive-Tar-3.04.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ba6b8addbedc43a463edcddf7b93accb7676c7b79c40f425b619d99545c4cb8c" || { echo "oreon: Source0 SHA256 mismatch for Archive-Tar-3.04.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Archive-Tar-%{version}
%patch -P0 -p1

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/99_pod.t
mkdir -p %{buildroot}%{_libexecdir}/%{name}/bin
for F in ptar ptardiff ptargrep; do
    ln -s %{_bindir}/"$F" %{buildroot}%{_libexecdir}/%{name}/bin
done
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into temporary files/directories. The easiest solution
# is to copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test

%check
make test

%files
%doc CHANGES README
%{_bindir}/ptar*
%{perl_vendorlib}/Archive/
%{_mandir}/man3/Archive::Tar*.3*
%{_mandir}/man1/ptar*.1*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.04-522
- Prepare for Oreon 11 (RP1)
