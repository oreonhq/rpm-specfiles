%global source0_hash 0bb895cd6f8d0a072f466972dff38743248c68df1dec9398bd944f002dbeeb60

Name:           perl-Gtk2-Ex-PodViewer
Version:        0.18
Release:        49%{?dist}
Summary:        Gtk2 widget for displaying Plain Old Documentation (POD)
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Gtk2-Ex-PodViewer
Source0:        https://cpan.metacpan.org/authors/id/G/GB/GBROWN/Gtk2-Ex-PodViewer-%{version}.tar.gz
# Allow bulding the package without run-time depenencies because of no tests
Patch0:         Gtk2-Ex-PodViewer-0.18-Do-not-insist-on-run-time-dependencies-when-building.patch
# Remove "use lib" from podviewer, CPAN RT#115717
Patch1:         Gtk2-Ex-PodViewer-0.18-Do-not-search-modules-in-relative-paths.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.8.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
# No tests exist
## Run-time:
# perl(base)
# perl(bytes)
# perl(Carp)
# perl(Data::Dumper)
# perl(Exporter)
# perl(File::Basename)
# perl(Gtk2)
# perl(Gtk2::Ex::Simple::List)
# perl(Gtk2::Gdk::Keysyms)
# perl(Gtk2::Pango)
# perl(IO::Scalar)
# perl(lib)
# perl(Pod::Parser)
# perl(Pod::Simple::Search)
# perl(vars)
## Optional run-time:
# perl(Locale::gettext)
Recommends:     perl(Locale::gettext)

%description
This is a Perl Gtk2 widget for displaying Plain Old Documentation (POD) files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Gtk2-Ex-PodViewer-%{version}
%patch -P0 -p1
%patch -P1 -p1
find . -type f -exec chmod a-x {} +

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
