%global source0_hash 64fcc382714abd8d57692ac376328c3a20c6cbc8bcd732b007d14cbf9a282ddd

Name:           perl-Gnome2
Version:        1.048
Release:        19%{?dist}
Summary:        Perl interface to the 2.x series of the GNOME libraries (deprecated)
# Gnome2.pm:    LGPL-2.1-or-later
# gnome2perl.h: LGPL-2.1-or-later
# LICENSE:      LGPL-2.1 text
# xs/Gnome2.xs: LGPL-2.1-or-later
# xs/GnomeAbout.xs: LGPL-2.1-or-later
# xs/GnomeApp.xs:   LGPL-2.1-or-later
# xs/GnomeAppBar.xs:    LGPL-2.1-or-later
# xs/GnomeAppHelper.xs: LGPL-2.1-or-later
# xs/BonoboDock.xs:     LGPL-2.1-or-later
# xs/BonoboDockItem.xs: LGPL-2.1-or-later
# xs/GnomeClient.xs:    LGPL-2.1-or-later
# xs/GnomeColorPicker.xs:   LGPL-2.1-or-later
# xs/GnomeConfig.xs:    LGPL-2.1-or-later
# xs/GnomeDateEdit.xs:  LGPL-2.1-or-later
# xs/GnomeDruid.xs:     LGPL-2.1-or-later
# xs/GnomeDruidPage.xs: LGPL-2.1-or-later
# xs/GnomeDruidPageEdge.xs: LGPL-2.1-or-later
# xs/GnomeDruidPageStandard.xs: LGPL-2.1-or-later
# xs/GnomeEntry.xs: LGPL-2.1-or-later
# xs/GnomeFileEntry.xs: LGPL-2.1-or-later
# xs/GnomeFontPicker.xs:    LGPL-2.1-or-later
# xs/GnomeGConf.xs: LGPL-2.1-or-later
# xs/GnomeHelp.xs:  LGPL-2.1-or-later
# xs/GnomeHRef.xs:  LGPL-2.1-or-later
# xs/GnomeIconEntry.xs: LGPL-2.1-or-later
# xs/GnomeIconList.xs:  LGPL-2.1-or-later
# xs/GnomeIconLookup.xs:    LGPL-2.1-or-later
# xs/GnomeIconSelection.xs: LGPL-2.1-or-later
# xs/GnomeIconTextItem.xs:  LGPL-2.1-or-later
# xs/GnomeIconTheme.xs: LGPL-2.1-or-later
# xs/GnomeInit.xs:  LGPL-2.1-or-later
# xs/GnomeI18N.xs:  LGPL-2.1-or-later
# xs/GnomeModuleInfo.xs:    LGPL-2.1-or-later
# xs/GnomePasswordDialog.xs:    LGPL-2.1-or-later
# xs/GnomePixmapEntry.xs:   LGPL-2.1-or-later
# xs/GnomePopupMenu.xs:     LGPL-2.1-or-later
# xs/GnomeProgram.xs:       LGPL-2.1-or-later
# xs/GnomeScore.xs: LGPL-2.1-or-later
# xs/GnomeScores.xs:    LGPL-2.1-or-later
# xs/GnomeSound.xs: LGPL-2.1-or-later
# xs/GnomeThumbnail.xs: LGPL-2.1-or-later
# xs/GnomeUIDefs.xs:    LGPL-2.1-or-later
# xs/GnomeURL.xs:   LGPL-2.1-or-later
# xs/GnomeUtil.xs:  LGPL-2.1-or-later
# xs/GnomeWindowIcon.xs:    LGPL-2.1-or-later
# xs/GnomeWindow.xs:    LGPL-2.1-or-later
## Not in any binary package
# Makefile.PL:  LGPL-2.1-or-later
License:        LGPL-2.1-or-later
URL:            https://metacpan.org/release/Gnome2
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/Gnome2-%{version}.tar.gz
# Adapt to Perl 5.40.0, bug #2292164, CPAN RT#153977
Patch0:         Gnome2-1.048-Adapt-to-perl-5.40.0.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libgnomeui-devel
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::Depends) >= 0.20
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::PkgConfig) >= 1.03
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Glib::GenPod)
BuildRequires:  perl(Glib::MakeHelper)
# Gnome2::Canvas is maybe run-time hard checked at build-time
BuildRequires:  perl(Gnome2::Canvas) >= 1.00
# Gnome2::VFS is maybe run-time hard checked at build-time
BuildRequires:  perl(Gnome2::VFS) >= 1.00
# Gtk2 is maybe run-time hard checked at build-time
BuildRequires:  perl(Gtk2) >= 1.00
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(DynaLoader)
# Tests:
BuildRequires:  perl(constant)
# Data::Dumper not used
BuildRequires:  perl(Glib) >= 1.04
BuildRequires:  perl(Test::More)
Requires:       perl(Gnome2::Canvas) >= 1.00
Requires:       perl(Gnome2::VFS) >= 1.00
Requires:       perl(Gtk2) >= 1.00

%{?perl_default_filter}

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Gnome2::Canvas|Gnome2::VFS|Glib|Gtk2)\\)$

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
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc AUTHORS ChangeLog.pre-git examples maps NEWS README TODO
%{perl_vendorarch}/auto/Gnome2
%{perl_vendorarch}/Gnome2
%{perl_vendorarch}/Gnome2.pm
%{_mandir}/man3/Gnome2.*
%{_mandir}/man3/Gnome2::*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
