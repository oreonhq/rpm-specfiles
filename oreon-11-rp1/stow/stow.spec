%global source0_hash 0d85a8513677e7923697bce42cdbb33d2b57af915abde1d0671e7ae80b2ef0b4

Name:         stow
Version:      2.4.1
Release:      %autorelease

License:      GPL-3.0-or-later
URL:          https://www.gnu.org/software/stow/stow.html
Summary:      Manage the installation of software packages from source
Source:       https://ftp.gnu.org/gnu/stow/stow-%{version}.tar.bz2
BuildArch:    noarch

BuildRequires:  coreutils
BuildRequires:  gawk
BuildRequires:  grep
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# Run-time dependencies
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test dependencies
# Data::Dumper no longer provided by base perl in F18+
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(English)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Output)

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

%if 0%{?fedora} >= 20
%global moredocs %{_defaultdocdir}/stow-doc
%else
%global moredocs %{_defaultdocdir}/stow-doc-%{version}
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure --docdir=%{moredocs} --with-pmdir=%{perl_vendorlib}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
# Remove info database, will be generated at install-time by scriptlets
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

# Remove unnecessary documentation
cd $RPM_BUILD_ROOT%{moredocs}/
rm -f ChangeLog* README.md INSTALL.md version.texi

%check
make check

%files
%doc README.md AUTHORS ChangeLog NEWS THANKS TODO
%doc %{_mandir}/man8/stow*
%doc %{_infodir}/stow*
%license COPYING
%{_bindir}/*
%{perl_vendorlib}/Stow.pm
%{perl_vendorlib}/Stow/

%files doc
%docdir %{moredocs}
%dir %{moredocs}
%{moredocs}/manual-single.html
%{moredocs}/manual-split/

%changelog
%autochangelog
