%global source0_hash 0d85a8513677e7923697bce42cdbb33d2b57af915abde1d0671e7ae80b2ef0b4
Name:         stow
Version:      2.4.1
Release:        1%{?dist}
License:      GPL-3.0-or-later
URL:          https://www.gnu.org/software/stow/stow.html
Summary:        Manage the installation of software packages from source
Source0:        https://ftp.gnu.org/gnu/stow/stow-%{version}.tar.bz2
BuildArch:    noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  gawk
BuildRequires:  grep
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
GNU Stow is a program for managing the installation of software packages,
keeping them separate (/usr/local/stow/emacs vs. /usr/local/stow/perl, for
example) while making them appear to be installed in the same place
(/usr/local). Software to ease the keeping track of software built from
source, making it easy to install, delete, move etc.

%package doc
Summary:    Documentation for Stow
Requires:   %{name} = %{version}-%{release}
%description doc
This package contains the documentation for GNU Stow.

%global moredocs %{_defaultdocdir}/stow-doc-%{version}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --docdir=%{moredocs} --with-pmdir=%{perl_vendorlib}
%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
cd $RPM_BUILD_ROOT%{moredocs}/
rm -f ChangeLog* README.md INSTALL.md version.texi
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make check
%files -f %{oreon_filedir}/main.list
%files -n stow-doc -f %{oreon_filedir}/stow-doc.list

%changelog

%autochangelog
