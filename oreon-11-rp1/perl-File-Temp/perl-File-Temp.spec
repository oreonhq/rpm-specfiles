%global cpan_version 0.2312
Name:           perl-File-Temp
Epoch:          1
# Normalized version, compete with perl.spec
Version:        0.231.200
Release:        2%{?dist}
Summary:        Return name and handle of a temporary file safely
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-Temp
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/File-Temp-%{cpan_version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 6fa961d955cf84d5b87f2f219a723cf77cb44b79282793f6819ccb19e8d0b884
%global source0_file File-Temp-0.2312.tar.gz
# oreon url source checksums end
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
# Keep Carp::Heavy optional
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(Fcntl) >= 1.03
BuildRequires:  perl(File::Path) >= 2.06
BuildRequires:  perl(File::Spec) >= 0.8
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Seekable)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent) >= 0.221
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
# Symbol not needed
# VMS::Stdio not needed
# Tests:
BuildRequires:  perl(FileHandle)
# Symbol not needed
BuildRequires:  perl(Test::More)
Requires:       perl(POSIX)

# Filter unused dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Symbol|VMS::Stdio\\)

%description
File::Temp can be used to create and open temporary files in a safe way.
There is both a function interface and an object-oriented interface. The
File::Temp constructor or the tempfile() function can be used to return the
name and the open file handle of a temporary file. The tempdir() function
can be used to create a temporary directory.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/File-Temp-0.2312.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "6fa961d955cf84d5b87f2f219a723cf77cb44b79282793f6819ccb19e8d0b884" || { echo "oreon: Source0 SHA256 mismatch for File-Temp-0.2312.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n File-Temp-%{cpan_version}
chmod -x misc/benchmark.pl
perl -MConfig -p -i -e 's|\A#!/usr/local/bin/perl\b|$Config{startperl}|' \
    misc/benchmark.pl

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
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into temporary files/directories.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
# Omit CONTRIBUTING (first half is not relevant to a binary package, second
# half is already presented in POD)
%doc Changes misc README
%{perl_vendorlib}/File*
%{_mandir}/man3/File::Temp*

%files tests
%{_libexecdir}/%{name}

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:0.231.200-2
- Import
