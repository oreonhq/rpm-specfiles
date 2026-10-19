%global source0_hash 0bb895cd6f8d0a072f466972dff38743248c68df1dec9398bd944f002dbeeb60
Name:           perl-Gtk2-Ex-PodViewer
Version:        0.18
Release:        1%{?dist}
Summary:        Gtk2 widget for displaying Plain Old Documentation (POD)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Gtk2-Ex-PodViewer
Source0:        https://cpan.metacpan.org/authors/id/G/GB/GBROWN/Gtk2-Ex-PodViewer-%{version}.tar.gz
Patch0:         Gtk2-Ex-PodViewer-0.18-Do-not-insist-on-run-time-dependencies-when-building.patch
Patch1:         Gtk2-Ex-PodViewer-0.18-Do-not-search-modules-in-relative-paths.patch
BuildArch:      noarch
Recommends:     perl(Locale::gettext)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
