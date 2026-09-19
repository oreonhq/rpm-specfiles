%global source0_hash 3c8d8c95c6b65c237db9e889c79edb2bb808bf37c084abdfbbd9859fef7787cc

Name:           perl-Gnome2-VFS
Version:        1.084
Release:        18%{?dist}
Summary:        Perl interface to the 2.x series of the GNOME VFS library (deprecated)
License:        LGPL-2.1-or-later
URL:            https://metacpan.org/release/Gnome2-VFS
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/Gnome2-VFS-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::Depends) >= 0.20
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::PkgConfig) >= 1.03
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Glib) >= 1.120
BuildRequires:  perl(Glib::CodeGen)
BuildRequires:  perl(Glib::MakeHelper)
BuildRequires:  perl(strict)
BuildRequires:  pkgconfig(gnome-vfs-2.0) >= 2.0.0
# Run-time
BuildRequires:  perl(constant)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)

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

%check
TMPHOME=$(mktemp -d)
mkdir "$TMPHOME"/.gnome
HOME="$TMPHOME" make test
rm -rf "$TMPHOME"

%files
%license LICENSE
%doc doctypes NEWS README examples/ t/
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Gnome2*
%{_mandir}/man3/*

%changelog
%autochangelog
