%global source0_hash 3c8d8c95c6b65c237db9e889c79edb2bb808bf37c084abdfbbd9859fef7787cc
Name:           perl-Gnome2-VFS
Version:        1.084
Release:        1%{?dist}
Summary:        Perl interface to the 2.x series of the GNOME VFS library (deprecated)
License:        LGPL-2.1-or-later
URL:            https://metacpan.org/release/Gnome2-VFS
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/Gnome2-VFS-%{version}.tar.gz
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Glib)
BuildRequires:  perl(Glib::CodeGen)
BuildRequires:  perl(Glib::MakeHelper)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(gnome-vfs-2.0)
# /oreon:deps
%description
This module allows you to interface with the GNOME Virtual File System
library. It provides the means to transparently access files on all kinds of
file systems.

This package is deprecated. Users are advised to migrate to Glib::IO Perl
module.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Gnome2-VFS-%{version} 

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

TMPHOME=$(mktemp -d)
mkdir "$TMPHOME"/.gnome
HOME="$TMPHOME" make test
rm -rf "$TMPHOME"
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
