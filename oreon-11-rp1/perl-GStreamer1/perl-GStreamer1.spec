%global source0_hash 4cf0ecfaefd425ac6f171fff5430e770efc3ea161475ee8856ccd23a974502dc

# spec file for perl-GStreamer1
#
# Copyright (c) 2015 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries

Name:           perl-GStreamer1
Version:        0.003
Release:        34%{?dist}
Summary:        Perl binding for GStreamer 1.x
# lib/GStreamer1.pm:                BSD
# lib/GStreamer1/Caps/Simple.pm:    BSD
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://metacpan.org/release/GStreamer1
Source0:        https://cpan.metacpan.org/authors/id/T/TM/TMURRAY/GStreamer1-%{version}.tar.gz
# Remove useless dependency on gstreamer1-devel
Patch0:         GStreamer1-0.003-Remove-a-useless-check-for-gstreamer1-library.patch
# Remove bogus shell bangs from the documentation
Patch1:         GStreamer1-0.003-Remove-shebangs-from-examples.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Devel::CheckLib) >= 0.9
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# gstreamer1 for Gst-1.0.typelib, GstBase-1.0.typelib and GstController-1.0.typelib
BuildRequires:  gstreamer1
# gstreamer1-plugins-base for GstApp-1.0.typelib
BuildRequires:  gstreamer1-plugins-base
BuildRequires:  perl(:VERSION) >= 5.12
BuildRequires:  perl(Glib::Object::Introspection) >= 0.009
# Tests:
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
# gstreamer1 for Gst-1.0.typelib, GstBase-1.0.typelib and GstController-1.0.typelib
Requires:       gstreamer1
# gstreamer1-plugins-base for GstApp-1.0.typelib
Requires:       gstreamer1-plugins-base
Requires:       perl(Glib::Object::Introspection) >= 0.009

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Glib::Object::Introspection\\)$

%description
GStreamer1 implements a framework that allows for processing and encoding
of multimedia sources in a manner similar to a shell pipeline. This package
provides the Perl language bindings.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n GStreamer1-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc CHANGELOG dist.ini examples
%{perl_vendorlib}/GStreamer1*
%{_mandir}/man3/GStreamer1*

%changelog
%autochangelog
