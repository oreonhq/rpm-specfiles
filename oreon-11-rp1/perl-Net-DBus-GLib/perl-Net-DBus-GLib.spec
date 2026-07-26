%global source0_hash 72f7e94c72927c3004846ac103a6c228feafcbbb3242d509304d65f0d15e95fc

Name:           perl-Net-DBus-GLib
Version:        0.33.0
Release:        52%{?dist}
Summary:        Perl extension for the DBus GLib bindings
License:        GPL-2.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-DBus-GLib
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DANBERR/Net-DBus-GLib-%{version}.tar.gz
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  dbus-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  perl(Glib)
BuildRequires:  perl(Net::DBus) >= 0.33.0
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests only
BuildRequires:  perl(Test::More)
# Optional tests only
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
Requires:       perl(Net::DBus) >= 0.33.0
Requires:       perl(XSLoader)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Net::DBus\\)$

%description
Net::DBus::GLib provides an extension to the Net::DBus module allowing
integration with the GLib mainloop. To integrate with the main loop, simply
get a connection to the bus via the methods in Net::DBus::GLib rather than
the usual Net::DBus module. That's it - every other API remains the same.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-DBus-GLib-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc AUTHORS CHANGES README examples/
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Net*
%{_mandir}/man3/*

%changelog
%autochangelog
