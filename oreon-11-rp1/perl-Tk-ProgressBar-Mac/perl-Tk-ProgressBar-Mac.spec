%global source0_hash 7b62408ce7b618b5d8da9095ad7abd2c02266bd635b9706f0ce8d27fa361179e

Name:           perl-Tk-ProgressBar-Mac
Version:        1.2
Release:        49%{?dist}
Summary:        Mac ProgressBar for Perl::Tk

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tk-ProgressBar-Mac
Source0:        http://cpan.org/modules/by-module/Tk/Tk-ProgressBar-Mac-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Tk)
BuildRequires:  perl(Tk::MMutil)
BuildRequires:  xorg-x11-server-Xvfb, xorg-x11-fonts-misc

%description
This widget provides a dynamic image that looks just like
a Mac OS 9 progress bar.  Packed around it are four
Frames, north, south, east and west, within which you can
stuff additional widgets. For example, see how Tk::Copy::Mac
uses several Labels and a CollapsableFrame widget to create
a reasonable facsimile of a Macintosh copy dialog.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Tk-ProgressBar-Mac-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w %{buildroot}/*

%check
# disabled by default because it needs an x screen
%{?_with_tests:make test}

%files
%doc README
%{perl_vendorlib}/Tk*
%{_mandir}/man3/Tk*.3*

%changelog
%autochangelog
