%global source0_hash 19696653af577117374873479d029d43f3bb033e1e33ec1870a06bf481147daf

Name:           perl-Tk-Stderr
Version:        1.2
Release:        52%{?dist}
Summary:        Capture standard error output, display in separate window for Perl::Tk

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/Tk-Stderr
Source0:        http://cpan.org/modules/by-module/Tk/Tk-Stderr-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Tk)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  xorg-x11-server-Xvfb, xorg-x11-fonts-misc

%description
This module captures that standard error of a program and redirects it
to a read only text widget, which doesn't appear until necessary. When
it does appear, the user can close it; it'll appear again when there is
more output.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Tk-Stderr-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w %{buildroot}/*

%check
# disabled by default because it needs an x screen
%{?_with_tests:make test}

%files
%doc README
%{perl_vendorlib}/Tk
%{_mandir}/man3/Tk*.3*

%changelog
%autochangelog
