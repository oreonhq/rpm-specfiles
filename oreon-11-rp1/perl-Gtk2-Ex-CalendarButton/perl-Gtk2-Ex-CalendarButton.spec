%global source0_hash a7fb65d0cd2a6ef2606f38435691d34dc27ea612e0933046778622fa2db54527

Name:           perl-Gtk2-Ex-CalendarButton
Version:        0.01
Release:        52%{?dist}
Summary:        Gtk2::Ex::CalendarButton Perl module
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Gtk2-Ex-CalendarButton
Source0:        https://cpan.metacpan.org/authors/id/O/OF/OFEYAIKON/Gtk2-Ex-CalendarButton-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Glib)
BuildRequires:  perl(Gtk2)
# Tests:
BuildRequires:  font(:lang=en)
BuildRequires:  perl(Gtk2::TestHelper)
BuildRequires:  perl(Test::More)
BuildRequires:  xorg-x11-server-Xvfb

%description
I realized that I was constantly re-creating a simple widget that will pop-up
a Gtk2::Calendar when clicked. Just like the date-time display on your
desktop taskbar. This package is my attempt to extract the portion of code
required to create a button-click-calendar.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Gtk2-Ex-CalendarButton-%{version}
find t/ -type f -exec \
    perl -MConfig -pi -e 's|\r||; s|^#!perl|$Config{startperl}|' {} +

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}/*

%check
xvfb-run -a make test

%files
# Package tests as documentation because the offical documentation is brief
%doc Changes README t/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
