%global source0_hash 0114ef39b65f49f8968283ab47719d7e88f98d7360fe3649be331c7f53d5832c
%bcond_with perl_Archive_Tar_enables_optional_test
Name:           perl-Archive-Tar
Version:        3.12
Release:        1%{?dist}
Summary:        A module for Perl manipulation of .tar files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Archive-Tar
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Archive-Tar-%{version}.tar.gz
Patch0:         Archive-Tar-2.02-Do-not-sleep-in-Makefile.PL.patch
BuildArch:      noarch
%if !%{defined perl_bootstrap}
%endif
%if !%{defined perl_bootstrap}
%endif
%if %{with perl_Archive_Tar_enables_optional_test} && !%{defined perl_bootstrap}
%endif
Requires:       perl(IO::Zlib) >= 1.01
Requires:       perl(IO::Compress::Bzip2) >= 2.015
%if !%{defined perl_bootstrap}
Requires:       perl(IO::Compress::Xz)
%endif
Requires:       perl(IO::Uncompress::Bunzip2) >= 2.015
%if !%{defined perl_bootstrap}
Requires:       perl(IO::Uncompress::UnXz)
Requires:       perl(Text::Diff)
%endif
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(IO::Zlib\\)$
Provides:       perl(Archive::Tar)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(IO::Compress::Bzip2)
BuildRequires:  perl(IO::Compress::Xz)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Uncompress::Bunzip2)
BuildRequires:  perl(IO::Uncompress::UnXz)
BuildRequires:  perl(IO::Zlib)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Diff)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/99_pod.t
mkdir -p %{buildroot}%{_libexecdir}/%{name}/bin
for F in ptar ptardiff ptargrep; do
    ln -s %{_bindir}/"$F" %{buildroot}%{_libexecdir}/%{name}/bin
done
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Archive-Tar-tests -f %{oreon_filedir}/perl-Archive-Tar-tests.list

%changelog

%autochangelog
