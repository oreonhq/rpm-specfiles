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
Requires:       perl(Archive::Zip) >= 1
Requires:       perl(Compress::Zlib) >= 1.3
Requires:       perl(File::Temp) >= 0.05
Requires:       perl(Getopt::ArgvFile) >= 1.07
Requires:       perl(IO::Compress::Gzip)
Requires:       perl(Module::ScanDeps) >= 1.21
Requires:       perl(PAR) >= 1.020
Requires:       perl(PAR::Dist) >= 0.22
Requires:       perl(:VERSION) = %(eval "`perl -V:version`"; echo ${version:-0})
Provides:       bundled(libperl) = %(eval "`perl -V:version`"; echo ${version:-0})
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Archive::Zip|File::Temp|Getopt::ArgvFile|Module::ScanDeps|PAR\\)\\s*$
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::ArgvFile)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Compress::Gzip)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::ScanDeps)
BuildRequires:  perl(Module::Signature)
BuildRequires:  perl(PAR)
BuildRequires:  perl(PAR::Dist)
BuildRequires:  perl(PAR::SetupTemp)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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

DEBUG=1 perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%global _smp_build_ncpus 1
%{make_build}
%install
%{make_install}
ln -sf %{_mandir}/man3/pp.3pm %{buildroot}%{_mandir}/man1/pp.1
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
%{SOURCE1} < script/tkpp | convert gif:- tkpp.png
install -m644 -D tkpp.png \
    %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/tkpp.png
desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-PAR-Packer-Tk -f %{oreon_filedir}/perl-PAR-Packer-Tk.list

%changelog

%autochangelog
