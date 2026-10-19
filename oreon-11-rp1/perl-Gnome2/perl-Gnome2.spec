%global source0_hash 64fcc382714abd8d57692ac376328c3a20c6cbc8bcd732b007d14cbf9a282ddd
Name:           perl-Gnome2
Version:        1.048
Release:        19%{?dist}
Summary:        Perl interface to the 2.x series of the GNOME libraries (deprecated)
License:        LGPL-2.1-or-later
URL:            https://metacpan.org/release/Gnome2
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/Gnome2-%{version}.tar.gz
Patch0:         Gnome2-1.048-Adapt-to-perl-5.40.0.patch
Requires:       perl(Gnome2::Canvas) >= 1.00
Requires:       perl(Gnome2::VFS) >= 1.00
Requires:       perl(Gtk2) >= 1.00
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Gnome2::Canvas|Gnome2::VFS|Glib|Gtk2)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libgnomeui-devel
BuildRequires:  make
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Glib)
BuildRequires:  perl(Glib::GenPod)
BuildRequires:  perl(Glib::MakeHelper)
BuildRequires:  perl(Gnome2::Canvas)
BuildRequires:  perl(Gnome2::VFS)
BuildRequires:  perl(Gtk2)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The Gnome2 module allows a Perl developer to use the GNOME libraries.  Find out
more about GNOME+ at <https://www.gnome.org/>.

This package is deprecated. Users are advised to uninstall it.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Glib) >= 1.04
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Gnome2-%{version}
chmod a+x t/*.t t/GnomeClient t/GnomeHelp t/GnomeScore t/GnomeSound t/GnomeURL

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}
%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Gnome2-tests -f %{oreon_filedir}/perl-Gnome2-tests.list

%changelog

%autochangelog
