%global source0_hash 555b4f1308939bb3141ea4570ad12e04e27c23329c302c9dc8725409e1049111
Name:           perl-Glib-Object-Introspection
Version:        0.052
Release:        1%{?dist}
Summary:        Dynamically create Perl language bindings
License:        LGPL-2.1-or-later
URL:            https://metacpan.org/release/Glib-Object-Introspection
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/Glib-Object-Introspection-%{version}.tar.gz
Patch1:         perl-Glib-Object-Introspection_lib_pattern.patch
Patch2:         Glib-Object-Introspection-0.050-Use-CFLAGS-and-LDFLAGS-from-the-envirnoment-for-buil.patch
Requires:       perl(Glib) >= 1.320
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Glib\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^(libgimarshallingtests|libregress).so\\(\\)
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Glib::Object::Introspection::Install::Files\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Cairo::GObject)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Glib)
BuildRequires:  perl(Glib::MakeHelper)
BuildRequires:  perl(Glib::Object::Subclass)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libffi)
# /oreon:deps
%description
Glib::Object::Introspection uses the gobject-introspection and libffi projects
to dynamically create Perl bindings for a wide variety of libraries.  Examples
include gtk+, webkit, libsoup and many more.

%package -n perli11ndoc
Summary:        GObject Introspection documentation viewer
Requires:       %{name} = %{version}-%{release}
Recommends:     perl(Gtk3)
Requires:       perl(Text::Wrap)
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

export LANG=C.UTF-8
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a build t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:build
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles perli11ndoc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
LANG=C.UTF-8 make test
%files -f %{oreon_filedir}/main.list
%files -n perli11ndoc -f %{oreon_filedir}/perli11ndoc.list
%files -n perl-Glib-Object-Introspection-tests -f %{oreon_filedir}/perl-Glib-Object-Introspection-tests.list

%changelog

%autochangelog
