%global source0_hash 4cf0ecfaefd425ac6f171fff5430e770efc3ea161475ee8856ccd23a974502dc
Name:           perl-GStreamer1
Version:        0.003
Release:        34%{?dist}
Summary:        Perl binding for GStreamer 1.x
License:        LicenseRef-Callaway-BSD
URL:            https://metacpan.org/release/GStreamer1
Source0:        https://cpan.metacpan.org/authors/id/T/TM/TMURRAY/GStreamer1-%{version}.tar.gz
Patch0:         GStreamer1-0.003-Remove-a-useless-check-for-gstreamer1-library.patch
Patch1:         GStreamer1-0.003-Remove-shebangs-from-examples.patch
BuildArch:      noarch
Requires:       gstreamer1
Requires:       gstreamer1-plugins-base
Requires:       perl(Glib::Object::Introspection) >= 0.009
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Glib::Object::Introspection\\)$
# oreon:deps
BuildRequires:  gstreamer1
BuildRequires:  gstreamer1-plugins-base
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Devel::CheckLib)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Glib::Object::Introspection)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
