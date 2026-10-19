%global source0_hash a25cb071e214fb89b4450aa4605031eae89b7961e149b0d6e8f491c19c14a90a
Name:           perl-Gtk2-AppIndicator
Version:        0.15
Release:        1%{?dist}
Summary:        Perl extension for libappindicator
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Gtk2-AppIndicator
Source0:        https://cpan.metacpan.org/modules/by-module/Gtk2/Gtk2-AppIndicator-%{version}.tar.gz
Requires:       perl(Gtk2) >= 1.2
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Gtk2\\)$
# oreon:deps
BuildRequires:  findutils
BuildRequires:  font(:lang=en)
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Constant)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Gtk2)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(appindicator-0.1)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
This Perl module gives an interface to libappindicator.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Gtk2-AppIndicator-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

xvfb-run -d make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
