%global source0_hash d715f5a86bcc187075de85e7ae5bc07b0714d6edc196a92da43986efa44e5cbb

# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Glib_enables_optional_test
%else
%bcond_with perl_Glib_enables_optional_test
%endif

Name:           perl-Glib
Version:        1.3294
Release:        9%{?dist}
Summary:        Perl interface to GLib
License:        LGPL-2.1-or-later
URL:            https://metacpan.org/release/Glib
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/Glib-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.0
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::Depends) >= 0.300
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::PkgConfig) >= 1.00
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
# Config not used by tests
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
# Gtk2 not used and optional
BuildRequires:  perl(IO::File)
BuildRequires:  perl(overload)
# POSIX not used by tests
BuildRequires:  perl(Storable)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(Config)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(utf8)
# Optional tests:
%if %{with perl_Glib_enables_optional_test}
BuildRequires:  perl(I18N::Langinfo)
BuildRequires:  perl(Test::ConsistentVersion)
%endif
Requires:       perl(Config)

# Do not export private modules and libraries
%{?perl_default_filter}
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(MY\\)

Provides:       perl(Glib)
%description
This module provides perl access to GLib and GLib's GObject libraries.
GLib is a portability and utility library; GObject provides a generic
type system with inheritance and a powerful signal system.  Together
these libraries are used as the foundation for many of the libraries
that make up the Gnome environment, and are used in many unrelated
projects.

%package devel
Summary:    Development part of Perl interface to GLib
Requires:   %{name} = %{version}-%{release}

%description devel
Development part of package perl-Glib, the Perl module providing interface
to GLib and GObject libraries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Glib-%{version}
for F in AUTHORS; do
    iconv -f ISO-8859-1 -t UTF-8 < "$F" > "${F}.utf8"
    touch -r "$F" "${F}.utf8"
    mv "${F}.utf8" "$F"
done

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" \
    NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc AUTHORS ChangeLog.pre-git NEWS README TODO
%{perl_vendorarch}/auto/Glib/
%{perl_vendorarch}/Glib*
%{_mandir}/man3/*.3pm*
%exclude %{perl_vendorarch}/Glib/*/*.h
%exclude %{perl_vendorarch}/Glib/MakeHelper.pm
%exclude %{perl_vendorarch}/Glib/devel.pod
%exclude %{perl_vendorarch}/Glib/xsapi.pod
%exclude %{_mandir}/man3/Glib::MakeHelper.3pm.gz
%exclude %{_mandir}/man3/Glib::devel.3pm.gz
%exclude %{_mandir}/man3/Glib::xsapi.3pm.gz

%files devel
%{perl_vendorarch}/Glib/*/*.h
%{perl_vendorarch}/Glib/MakeHelper.pm
%{perl_vendorarch}/Glib/devel.pod
%{perl_vendorarch}/Glib/xsapi.pod
%{_mandir}/man3/Glib::MakeHelper.3pm.gz
%{_mandir}/man3/Glib::devel.3pm.gz
%{_mandir}/man3/Glib::xsapi.3pm.gz

%changelog
%autochangelog
