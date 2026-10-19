%global source0_hash 3b5cde67885961fd4522dd124a5ba4c4d1ef3dbda7166d97aa40fdfe32554606
%global use_x11_tests 1
Name:           perl-Gtk3-WebKit
Version:        0.06
Release:        1%{?dist}
Summary:        WebKit bindings for Perl
License:        LGPL-2.1-only OR Artistic-2.0
URL:            https://metacpan.org/release/Gtk3-WebKit
Source0:        https://cpan.metacpan.org/authors/id/P/PO/POTYL/Gtk3-WebKit-%{version}.tar.gz
Patch0:         Gtk3-WebKit-0.06-Port-to-webkitgtk4.patch
BuildArch:      noarch
Requires:       webkit2gtk4.1
%{?perl_default_filter}
# oreon:deps
BuildRequires:  font(:lang=en)
BuildRequires:  make
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Glib::Object::Introspection)
BuildRequires:  perl(Gtk3)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NeedsDisplay)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  webkit2gtk4.1
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  xorg-x11-xinit
# /oreon:deps
%description
This module provides the Perl bindings for the Gtk3 port of WebKit.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Gtk3-WebKit-%{version}
%patch -P0 -p1

%build

    xvfb-run %{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

    xvfb-run -a make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
