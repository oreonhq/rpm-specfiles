%global source0_hash 555b4f1308939bb3141ea4570ad12e04e27c23329c302c9dc8725409e1049111

Name:           perl-Glib-Object-Introspection
Version:        0.052
Release:        2%{?dist}
Summary:        Dynamically create Perl language bindings
License:        LGPL-2.1-or-later
URL:            https://metacpan.org/release/Glib-Object-Introspection
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/Glib-Object-Introspection-%{version}.tar.gz
Patch1:         perl-Glib-Object-Introspection_lib_pattern.patch
# Use system-wide compiler flags when building test libraries. It silents
# annocheck gating tests, CPAN RT#147466, proposed to the upstream.
Patch2:         Glib-Object-Introspection-0.050-Use-CFLAGS-and-LDFLAGS-from-the-envirnoment-for-buil.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::Depends) >= 0.3
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::PkgConfig) >= 1
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Glib::MakeHelper)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.10.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.0.0
BuildRequires:  pkgconfig(libffi) >= 3.0.0
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Glib) >= 1.320
BuildRequires:  perl(overload)
# Text::Wrap not used at tests
BuildRequires:  perl(XSLoader)
# Optional run-time
# Gtk3 not used at tests
# Tests
BuildRequires:  perl(Glib::Object::Subclass)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
# Optional tests
BuildRequires:  perl(Cairo::GObject)
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(gio-2.0)
Requires:       perl(Glib) >= 1.320

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Glib\\)$
# Remove private libraries
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^(libgimarshallingtests|libregress).so\\(\\)
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Glib::Object::Introspection::Install::Files\\)

%description
Glib::Object::Introspection uses the gobject-introspection and libffi projects
to dynamically create Perl bindings for a wide variety of libraries.  Examples
include gtk+, webkit, libsoup and many more.

%package -n perli11ndoc
Summary:        GObject Introspection documentation viewer
Requires:       %{name} = %{version}-%{release}
Recommends:     perl(Gtk3)
Requires:       perl(Text::Wrap)
# Subpackaged from perl-Glib-Object-Introspection-0.048-2.fc33, bug #1749126
Conflicts:      perl-Glib-Object-Introspection < 0.048-3
BuildArch:      noarch

%description -n perli11ndoc
This is a documentation viewer for GObject Introspection (GIR) files. With
perl(Gtk3), it provides an interactive graphical browser.

%package tests
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Glib-Object-Introspection-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t t/inc/setup.pl; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
# If LANG is not set to UTF-8, then when later running the test
# suite, you will see multiple failures handling UTF-8 data
export LANG=C.UTF-8
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a build t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:build
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
LANG=C.UTF-8 make test

%files
%doc NEWS README.md
%license LICENSE
%dir %{perl_vendorarch}/auto/Glib
%dir %{perl_vendorarch}/auto/Glib/Object
%{perl_vendorarch}/auto/Glib/Object/Introspection
%dir %{perl_vendorarch}/Glib
%dir %{perl_vendorarch}/Glib/Object
%{perl_vendorarch}/Glib/Object/Introspection
%{perl_vendorarch}/Glib/Object/Introspection.pm
%{_mandir}/man3/Glib::Object::Introspection.*

%files -n perli11ndoc
%{_bindir}/perli11ndoc
%{_mandir}/man1/perli11ndoc.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
