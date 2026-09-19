%global source0_hash 70dc4bf2aa74981c79e15fd298d998e05a92eba4811f1ad5c9f1f4de37737acc

%global use_x11_tests 1
%if 0%{?rhel} && 0%{?rhel} < 10
%global use_wayland_tests 0
%else
%global use_wayland_tests 1
%endif

Name:           perl-Gtk3
Version:        0.038
Release:        19%{?dist}
Summary:        Perl interface to the 3.x series of the GTK+ toolkit
License:        LGPL-2.1-or-later
URL:            https://metacpan.org/release/Gtk3
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/Gtk3-%{version}.tar.gz
# Fix the tests to pass from a read-only location, CPAN RT#147461,
# proposed to an upstream.
Patch0:         Gtk3-0.038-Create-temporary-files-for-tests-in-HOME.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  gtk3
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Cairo::GObject) >= 1.000
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
# Glib::Object::Introspection version for
# Glib::Object::Introspection:convert_flags_to_sv(), CPAN RT#122761
BuildRequires:  perl(Glib::Object::Introspection) >= 0.043
BuildRequires:  perl(overload)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
# Tests
# Config used only on FreeBSD
BuildRequires:  perl(constant)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Glib)
BuildRequires:  perl(Glib::Object::Subclass)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
%if 0%{?fedora} >= 41 || 0%{?rhel} >= 10
# XPM loading for tests:
BuildRequires:  gdk-pixbuf2-modules-extra
%endif
%if %{use_x11_tests}
# X11 tests:
%if 0%{?rhel} >= 10
BuildRequires:  mutter
BuildRequires:  xwayland-run
%else
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  font(:lang=en)
%endif
%endif
%if %{use_wayland_tests}
# Wayland tests:
BuildRequires:  mutter
BuildRequires:  xwayland-run
%endif
Requires:       gtk3
Requires:       perl(Cairo::GObject) >= 1.000
# Glib::Object::Introspection version for
# Glib::Object::Introspection:convert_flags_to_sv(), CPAN RT#122761
Requires:       perl(Glib::Object::Introspection) >= 0.043
Requires:       perl(POSIX)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Cairo::GObject|Glib::Object::Introspection)\\)$

%description
The Gtk3 module allows a Perl developer to use the GTK+ graphical user
interface library. Find out more about GTK+ at <http://www.gtk.org/>.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if 0%{?fedora} >= 41 || 0%{?rhel} >= 10
# XPM loading for tests:
Requires:       gdk-pixbuf2-modules-extra
%endif
%if %{use_x11_tests}
# X11 tests:
%if 0%{?rhel} >= 10
Requires:       mutter
Requires:       xwayland-run
%else
Requires:       xorg-x11-server-Xvfb
Requires:       font(:lang=en)
%endif
%endif
%if %{use_wayland_tests}
# Wayland tests:
Requires:       mutter
Requires:       xwayland-run
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Gtk3-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t t/inc/setup.pl; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_install}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
set -e
cd %{_libexecdir}/%{name}
%if %{use_x11_tests}
%if 0%{?rhel} >= 10
xwfb-run -c mutter -- prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
%else
xvfb-run -d prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
%endif
%else
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
%endif
%if %{use_wayland_tests}
wlheadless-run -c mutter -- prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
%endif
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
%if %{use_x11_tests}
%if 0%{?rhel} >= 10
    # Tests fail with default weston compositor
    xwfb-run -c mutter -- make test
%else
    xvfb-run -d make test
%endif
%else
    make test
%endif
%if %{use_wayland_tests}
    # Tests fail with default weston compositor
    wlheadless-run -c mutter -- make test
%endif

%files
%license LICENSE
%doc NEWS README
%{perl_vendorlib}/Gtk3.pm
%{_mandir}/man3/Gtk3.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
