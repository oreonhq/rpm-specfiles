%global source0_hash 0fc063e448e34f7cb5c69c6be5b2258f7150187b33140dedabd53a2c34ca3cba

Name:           perl-PAR-Packer
Version:        1.064
Release:        4%{?dist}
Summary:        PAR Packager
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PAR-Packer
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSCHUPP/PAR-Packer-%{version}.tar.gz
Source1:        extract_icon
Source2:        tkpp.desktop
BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  ImageMagick
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# myldr/Makefile.PL, myldr/file2c.pl is executed
BuildRequires:  perl(inc::Module::Install) >= 0.92
BuildRequires:  perl(Compress::Zlib) >= 1.3
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Compress::Gzip)
BuildRequires:  perl(lib)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Archive::Zip) >= 1
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp) >= 0.05
BuildRequires:  perl(Getopt::ArgvFile) >= 1.07
BuildRequires:  perl(Module::ScanDeps) >= 1.21
BuildRequires:  perl(PAR) >= 1.020
BuildRequires:  perl(PAR::Dist) >= 0.22
BuildRequires:  perl(vars)
# Optional run-time:
BuildRequires:  perl(Module::Signature)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(IPC::Run3) >= 0.048
BuildRequires:  perl(PAR::SetupTemp)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
Requires:       perl(Archive::Zip) >= 1
Requires:       perl(Compress::Zlib) >= 1.3
Requires:       perl(File::Temp) >= 0.05
Requires:       perl(Getopt::ArgvFile) >= 1.07
Requires:       perl(IO::Compress::Gzip)
Requires:       perl(Module::ScanDeps) >= 1.21
Requires:       perl(PAR) >= 1.020
Requires:       perl(PAR::Dist) >= 0.22
# This package bundles libperl.so into %%{_bindir}/parl and when executing it
# after upgrading Perl, Perl version checks in Config fail. Thus we need to
# require the same version used when building this package. Bug #1470542.
Requires:       perl(:VERSION) = %(eval "`perl -V:version`"; echo ${version:-0})
Provides:       bundled(libperl) = %(eval "`perl -V:version`"; echo ${version:-0})

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Archive::Zip|File::Temp|Getopt::ArgvFile|Module::ScanDeps|PAR\\)\\s*$

%description
This module implements the App::Packer::Backend interface, for generating
stand-alone executables, perl scripts and PAR files.

%package Tk
Summary:        Front-end to pp written in Perl/Tk
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       perl(ExtUtils::MakeMaker)
Requires:       perl(File::Temp)
Requires:       perl(Tk::ColoredButton)
Requires:       perl(Tk::EntryCheck)
Requires:       perl(Tk::Getopt)
Requires:       perl(Tk::Pod)

%description Tk
Tkpp is a GUI front-end to pp, which can turn perl scripts into standalone
PAR files, perl scripts or executables.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n PAR-Packer-%{version}
# Remove bundled modules
rm -rf inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST

%build
# DEBUG variable needed to disable stripping binary
DEBUG=1 perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
# The Makefile is not parallel-safe.
%global _smp_build_ncpus 1
%{make_build}

%install
%{make_install}
# Ensure pp(1) manpage points to the documentation from pp.pm
ln -sf %{_mandir}/man3/pp.3pm %{buildroot}%{_mandir}/man1/pp.1
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
# Install desktop file
%{SOURCE1} < script/tkpp | convert gif:- tkpp.png
install -m644 -D tkpp.png \
    %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/tkpp.png
desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}

%check
make test

%files
%license LICENSE
%doc AUTHORS Changes README
%{perl_vendorlib}/App*
%{perl_vendorlib}/PAR*
%{perl_vendorlib}/pp*
%{_bindir}/par.pl
%{_bindir}/parl
%{_bindir}/parldyn
%{_bindir}/pp
%{_mandir}/man1/par*.1.*
%{_mandir}/man1/pp*.1.*
%{_mandir}/man3/App::*
%{_mandir}/man3/PAR::*
%{_mandir}/man3/pp*

%files Tk
%{_bindir}/tkpp
%{_mandir}/man1/tkpp.1.*
%{_datadir}/applications/tkpp.desktop
%{_datadir}/icons/hicolor/32x32/apps/tkpp.png

%changelog
%autochangelog
