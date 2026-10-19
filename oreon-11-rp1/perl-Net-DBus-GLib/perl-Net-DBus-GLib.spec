%global source0_hash 72f7e94c72927c3004846ac103a6c228feafcbbb3242d509304d65f0d15e95fc
Name:           perl-Net-DBus-GLib
Version:        0.33.0
Release:        1%{?dist}
Summary:        Perl extension for the DBus GLib bindings
License:        GPL-2.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-DBus-GLib
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DANBERR/Net-DBus-GLib-%{version}.tar.gz
Requires:       perl(Net::DBus) >= 0.33.0
Requires:       perl(XSLoader)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Net::DBus\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  dbus-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Glib)
BuildRequires:  perl(Net::DBus)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
