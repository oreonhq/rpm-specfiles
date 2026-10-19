%global source0_hash 70dc4bf2aa74981c79e15fd298d998e05a92eba4811f1ad5c9f1f4de37737acc
%global use_x11_tests 1
%global use_wayland_tests 1
Name:           perl-Gtk3
Version:        0.038
Release:        1%{?dist}
Summary:        Perl interface to the 3.x series of the GTK+ toolkit
License:        LGPL-2.1-or-later
URL:            https://metacpan.org/release/Gtk3
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/Gtk3-%{version}.tar.gz
Patch0:         Gtk3-0.038-Create-temporary-files-for-tests-in-HOME.patch
BuildArch:      noarch
%if 0%{?fedora} >= 41 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
%endif
Requires:       gtk3
Requires:       perl(Cairo::GObject) >= 1.000
Requires:       perl(Glib::Object::Introspection) >= 0.043
Requires:       perl(POSIX)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Cairo::GObject|Glib::Object::Introspection)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  font(:lang=en)
BuildRequires:  gdk-pixbuf2-modules-extra
BuildRequires:  gtk3
BuildRequires:  make
BuildRequires:  mutter
BuildRequires:  perl(Cairo::GObject)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Glib)
BuildRequires:  perl(Glib::Object::Introspection)
BuildRequires:  perl(Glib::Object::Subclass)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  xwayland-run
# /oreon:deps
%description
The Gtk3 module allows a Perl developer to use the GTK+ graphical user
interface library. Find out more about GTK+ at <http://www.gtk.org/>.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if 0%{?fedora} >= 41 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
Requires:       gdk-pixbuf2-modules-extra
%endif
Requires:       xorg-x11-server-Xvfb
Requires:       font(:lang=en)
Requires:       mutter
Requires:       xwayland-run
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
cd %{_libexecdir}/%{name}
xvfb-run -d prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
wlheadless-run -c mutter -- prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
    xvfb-run -d make test
    wlheadless-run -c mutter -- make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Gtk3-tests -f %{oreon_filedir}/perl-Gtk3-tests.list

%changelog

%autochangelog
