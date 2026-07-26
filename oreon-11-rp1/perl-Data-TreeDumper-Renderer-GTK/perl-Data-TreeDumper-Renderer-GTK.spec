%global source0_hash 84047e2e61e86289cf8f097405cadf7994dddda1b70188038fa06b01988db0b5

%global use_x11_tests 1

Name:       perl-Data-TreeDumper-Renderer-GTK
Version:    0.03
Release:    7%{?dist}
# see GTK.pm
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    Gtk3::TreeView renderer for Data::TreeDumper
Source:     https://cpan.metacpan.org/authors/id/N/NK/NKH/Data-TreeDumper-Renderer-GTK-%{version}.tar.gz
Url:        https://metacpan.org/release/Data-TreeDumper-Renderer-GTK
BuildArch:  noarch

BuildRequires: coreutils
BuildRequires: findutils
BuildRequires: make
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires: perl(AutoLoader)
BuildRequires: perl(base)
BuildRequires: perl(Cairo)
BuildRequires: perl(Data::TreeDumper) >= 0.33
BuildRequires: perl(Exporter)
BuildRequires: perl(Glib)
BuildRequires: perl(Gtk3)
# perl(Gtk3::TreeView) is in perl-Gtk3, but not listed in provides
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
%if %{use_x11_tests}
# Tests
BuildRequires: perl(Test)
# X11 tests:
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  font(:lang=en)
%endif

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Gtk3::TreeView\\)

%description
GTK-perl renderer for Data::TreeDumper.

This widget is the GUI equivalent of Data::TreeDumper; it will display a
perl data structure in a TreeView, allowing you to fold and unfold child
data structures and get a quick feel for what's where. Right-clicking
anywhere in the view brings up a context menu, from which the user can
choose to expand or collapse all items.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-TreeDumper-Renderer-GTK-%{version}
find . -type f -exec chmod -c -x {} +

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
find %{buildroot} -type f -name '*.pl' -delete

%check
%if %{use_x11_tests}
    xvfb-run -d make test
%endif

%files
%doc README gtk_test.pl
%{perl_vendorlib}/Data*
%{perl_vendorlib}/auto/Data*
%{_mandir}/man3/Data::TreeDumper*.3*

%changelog
%autochangelog
