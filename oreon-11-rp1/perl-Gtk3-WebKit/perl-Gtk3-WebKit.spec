%global source0_hash 3b5cde67885961fd4522dd124a5ba4c4d1ef3dbda7166d97aa40fdfe32554606

%global use_x11_tests 1
Name:           perl-Gtk3-WebKit
Version:        0.06
Release:        35%{?dist}
Summary:        WebKit bindings for Perl
License:        LGPL-2.1-only OR Artistic-2.0
URL:            https://metacpan.org/release/Gtk3-WebKit
Source0:        https://cpan.metacpan.org/authors/id/P/PO/POTYL/Gtk3-WebKit-%{version}.tar.gz
# Use webkit2gtk3, bug #1373410, CPAN RT#122598
Patch0:         Gtk3-WebKit-0.06-Port-to-webkitgtk4.patch
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Glib::Object::Introspection)
BuildRequires:  perl(Gtk3)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NeedsDisplay)
BuildRequires:  perl(warnings)
# Typelib for WebKit2-4.1
BuildRequires:  webkit2gtk4.1
%if %{use_x11_tests}
# X11 tests:
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  xorg-x11-xinit
BuildRequires:  font(:lang=en)
%endif
# Typelib for WebKit2-4.1
Requires:       webkit2gtk4.1

# Do not scan documentation for dependencies
%{?perl_default_filter}

%description
This module provides the Perl bindings for the Gtk3 port of WebKit.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Gtk3-WebKit-%{version}
%patch -P0 -p1

%build
%if %{use_x11_tests}
    xvfb-run %{__perl} Makefile.PL INSTALLDIRS=vendor
%else
    %{__perl} Makefile.PL INSTALLDIRS=vendor
%endif
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
%if %{use_x11_tests}
    xvfb-run -a make test
%else
    make test
%endif

%files
%doc Changes COPYING README examples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
