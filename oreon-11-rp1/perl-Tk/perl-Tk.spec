%global source0_hash 32aa7271a6bdfedc3330119b3825daddd0aa4b5c936f84ad74eabb932a200a5e
%global use_x11_tests 1
%bcond perl_Tk_enables_optional_test %{undefined rhel}
Name:           perl-Tk
Version:        804.036
Release:        1%{?dist}
Summary:        Perl Graphical User Interface ToolKit
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND SWL
URL:            https://metacpan.org/release/Tk
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SREZIC/Tk-%{version}.tar.gz
Patch0:         perl-Tk-widget.patch
Patch1:         perl-Tk-debian.patch.gz
Patch2:         perl-Tk-seg.patch
Patch3:         perl-Tk-c99.patch
Patch4:         perl-Tk-Fix-STRLEN-vs-int-pointer-confusion-in-Tcl_GetByteAr.patch
Patch5:         perl-Tk-Fix-build-with-clang-16.patch
Patch6:         perl-Tk-pregcomp2.c-Avoid-using-incompatible-pointer-type.patch
Patch7:         perl-Tk-Avoid-using-incompatible-pointer-type-for-old_warn.patch
Patch8:         perl-Tk-Fix-incompatible-pointer-type-in-function-GetTextIndex.patch
%if 0%{?use_xwayland_run}
%else
%endif
%if %{with perl_Tk_enables_optional_test}
%endif
Requires:       perl(locale)
Provides:       perl(Tk::LabRadio) = 4.004
Provides:       perl(Tk) = %{version}
%{?perl_default_filter}
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(Tk\\)
%global __provides_exclude %__provides_exclude|perl\\(Tk::Clipboard\\)$
%global __provides_exclude %__provides_exclude|perl\\(Tk::Frame\\)$
%global __provides_exclude %__provides_exclude|perl\\(Tk::Listbox\\)$
%global __provides_exclude %__provides_exclude|perl\\(Tk::Scale\\)$
%global __provides_exclude %__provides_exclude|perl\\(Tk::Scrollbar\\)$
%global __provides_exclude %__provides_exclude|perl\\(Tk::Table\\)$
%global __provides_exclude %__provides_exclude|perl\\(Tk::Toplevel\\)$
%global __provides_exclude %__provides_exclude|perl\\(Tk::Widget\\)$
%global __provides_exclude %__provides_exclude|perl\\(Tk::Wm\\)$
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(TkTest\\)
Provides:       perl(Tk::BrowseEntry)
Provides:       perl(Tk::Canvas)
Provides:       perl(Tk::Derived)
Provides:       perl(Tk::DialogBox)
Provides:       perl(Tk::ROText)
Provides:       perl(Tk::FileSelect)
Provides:       perl(Tk::Frame)
Provides:       perl(Tk::ItemStyle)
Provides:       perl(Tk::LabEntry)
Provides:       perl(Tk::Toplevel)
Provides:       perl(Tk::Widget)
Provides:       perl(Tk::FileSelect)
Provides:       perl(Tk::Frame)
Provides:       perl(Tk::ItemStyle)
Provides:       perl(Tk::LabEntry)
Provides:       perl(Tk::Toplevel)
Provides:       perl(Tk::Tree)
Provides:       perl(Tk::Widget)
Provides:       perl(Tk::Tree)
# oreon:deps
BuildRequires:  font(:lang=en)
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  google-noto-sans-fonts
BuildRequires:  libX11-devel
BuildRequires:  libXft-devel
BuildRequires:  liberation-sans-fonts
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Leak)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(DirHandle)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Command::MM)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Text::Tabs)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(locale)
BuildRequires:  perl(open)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(subs)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
This a re-port of a perl interface to Tk8.4.
C code is derived from Tcl/Tk8.4.5.
It also includes all the C code parts of Tix8.1.4 from SourceForge.
The perl code corresponding to Tix's Tcl code is not fully implemented.

Perl API is essentially the same as Tk800 series Tk800.025 but has not
been verified as compliant. There ARE differences see pod/804delta.pod.

%package devel
Summary: perl-Tk ExtUtils::MakeMaker support module
Requires: perl-Tk = %{version}-%{release}
%description devel
%{summary}

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if 0%{?use_xwayland_run}
Requires:       xwayland-run
Requires:       mutter
Requires:       mesa-dri-drivers
%else
Requires:       xorg-x11-server-Xvfb
%endif
Requires:       google-noto-sans-fonts
Requires:       font(:lang=en)
Requires:       liberation-sans-fonts
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Tk-%{version}
find . -type f -exec perl -MConfig -pi -e \
's,^(#!)(/usr/local)?/bin/perl\b,$Config{startperl}, if ($. == 1)' {} \;
chmod -x pod/Popup.pod Tixish/lib/Tk/balArrow.xbm
# fix for widget as docs
%patch -P 0
perl -pi -e \
's,\@demopath\@,%{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}/demos,g' demos/widget
# debian patch
#%%patch -P 1 -p1
# patch to fix #235666 ... seems like caching code is broken
%patch -P 2 -p1 -b .seg
%patch -P 3 -p1 -b .c99
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1
%patch -P 7 -p1
%patch -P 8 -p1

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor X11LIB=%{_libdir} XFT=1 NO_PACKLIST=1 NO_PERLLOCAL=1
find . -name Makefile | xargs perl -pi -e 's/$/ -std=gnu99/ if /^CCFLAGS/;s/^\tLD_RUN_PATH=[^\s]+\s*/\t/'
%{make_build}
%check

    export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
    %if 0%{?use_xwayland_run}
        xwfb-run -c mutter -- make test
    %else
        xvfb-run -d make test
    %endif
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
chmod -R u+rwX,go+rX,go-w %{buildroot}/*
mkdir __demos
cp -pR %{buildroot}%{perl_vendorarch}/Tk/demos __demos
find __demos/ -type f -exec chmod -x {} \;
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/pod.t
mkdir -p %{buildroot}%{_libexecdir}/%{name}/demos/demos/images
cp demos/demos/images/cursor* %{buildroot}%{_libexecdir}/%{name}/demos/demos/images
perl -i -pe 's{-Mblib", "blib/script}{%{_bindir}}' %{buildroot}%{_libexecdir}/%{name}/t/exefiles.t
perl -i -ne 'print $_ unless m{gedi}' %{buildroot}%{_libexecdir}/%{name}/t/exefiles.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
%if 0%{?use_xwayland_run}
    xwfb-run -c mutter -- prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
%else
    xvfb-run -d prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
%endif
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n perl-Tk-devel -f %{oreon_filedir}/perl-Tk-devel.list
%files -n perl-Tk-tests -f %{oreon_filedir}/perl-Tk-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 804.036-24
- Prepare for Oreon 11 (RP1)
