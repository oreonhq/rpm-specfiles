%global use_x11_tests 1
%if 0%{?fedora} || 0%{?rhel} > 9
%global use_xwayland_run 1
%endif
%bcond perl_Tk_enables_optional_test %{undefined rhel}

Name:           perl-Tk
Version:        804.036
Release:        24%{?dist}
Summary:        Perl Graphical User Interface ToolKit

License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND SWL
URL:            https://metacpan.org/release/Tk
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SREZIC/Tk-%{version}.tar.gz
Patch0:         perl-Tk-widget.patch
# modified version of http://ftp.de.debian.org/debian/pool/main/p/perl-tk/perl-tk_804.027-8.diff.gz
Patch1:         perl-Tk-debian.patch.gz
# fix segfaults as in #235666 because of broken cashing code
Patch2:         perl-Tk-seg.patch
Patch3:         perl-Tk-c99.patch
# Fix STRLEN vs int pointer confusion in Tcl_GetByteArrayFromObj()
# It breaks tests with Perl 5.38 on s390* (BZ#2222638)
Patch4:         perl-Tk-Fix-STRLEN-vs-int-pointer-confusion-in-Tcl_GetByteAr.patch

# Fix build with clang 16
# https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=271521
Patch5:         perl-Tk-Fix-build-with-clang-16.patch
# Avoid using incompatible pointer type in pregcomp2.c
Patch6:         perl-Tk-pregcomp2.c-Avoid-using-incompatible-pointer-type.patch
# Avoid using incompatible pointer type for `old_warn`
# https://github.com/eserte/perl-tk/issues/98
Patch7:         perl-Tk-Avoid-using-incompatible-pointer-type-for-old_warn.patch
# Avoid using incompatible pointer type in function 'GetTextIndex'
# https://github.com/eserte/perl-tk/issues/103
Patch8:         perl-Tk-Fix-incompatible-pointer-type-in-function-GetTextIndex.patch

# Versions before this have Unicode issues
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  perl-devel >= 3:5.8.3
BuildRequires:  perl-generators
BuildRequires:  freetype-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libX11-devel
BuildRequires:  libXft-devel
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(lib)
BuildRequires:  perl(open)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)

%if %{use_x11_tests}
# Run-time:
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DirHandle)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(if)
BuildRequires:  perl(locale)
# Image::Info is optional
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(overload)
BuildRequires:  perl(subs)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Text::Tabs)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)

# Tests:
# X11 tests:
%if 0%{?use_xwayland_run}
BuildRequires:  xwayland-run
BuildRequires:  mutter
BuildRequires:  mesa-dri-drivers
%else
BuildRequires:  xorg-x11-server-Xvfb
%endif
BuildRequires:  google-noto-sans-fonts
BuildRequires:  font(:lang=en)
# Specific font is needed for tests, bug #1141117, CPAN RT#98831
BuildRequires:  liberation-sans-fonts
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(ExtUtils::Command::MM)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
# Optional tests:
%if %{with perl_Tk_enables_optional_test}
BuildRequires:  perl(Devel::Leak)
%endif
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Test::Pod)
%endif

Requires:       perl(locale)
Provides:       perl(Tk::LabRadio) = 4.004
Provides:       perl(Tk) = %{version}

%{?perl_default_filter}
# Explicity filter "useless" unversioned provides. For some reason, rpm is
# detecting these both with and without version.
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

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(TkTest\\)

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
# X11 tests:
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
%if %{use_x11_tests}
    export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
    %if 0%{?use_xwayland_run}
        xwfb-run -c mutter -- make test
    %else
        xvfb-run -d make test
    %endif
%endif

%install
%{make_install}

find %{buildroot} -type f -name '*.bs' -size 0 -delete

chmod -R u+rwX,go+rX,go-w %{buildroot}/*
mkdir __demos
cp -pR %{buildroot}%{perl_vendorarch}/Tk/demos __demos
find __demos/ -type f -exec chmod -x {} \;

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/pod.t
mkdir -p %{buildroot}%{_libexecdir}/%{name}/demos/demos/images
cp demos/demos/images/cursor* %{buildroot}%{_libexecdir}/%{name}/demos/demos/images
perl -i -pe 's{-Mblib", "blib/script}{%{_bindir}}' %{buildroot}%{_libexecdir}/%{name}/t/exefiles.t
perl -i -ne 'print $_ unless m{gedi}' %{buildroot}%{_libexecdir}/%{name}/t/exefiles.t

cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into temporary files/directories
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

%files
%doc Changes README README.linux ToDo pTk/*license* __demos/demos demos/widget COPYING
%doc blib/man1/widget.1
%{_bindir}/p*
%{_bindir}/tkjpeg
%{perl_vendorarch}/auto/Tk
%{perl_vendorarch}/Tie*
%{perl_vendorarch}/Tk*
%exclude %{perl_vendorarch}/Tk/MMutil.pm
%exclude %{perl_vendorarch}/Tk/install.pm
%exclude %{perl_vendorarch}/Tk/MakeDepend.pm
%{_mandir}/man1/ptked*
%{_mandir}/man1/ptksh*
%{_mandir}/man1/tkjpeg*
%{_mandir}/man3/Tie*
%{_mandir}/man3/Tk*
%exclude %{_mandir}/man1/widget.1*
%exclude %{_bindir}/gedi
%exclude %{_bindir}/widget
%exclude %{perl_vendorarch}/Tk/demos

%files devel
%dir %{perl_vendorarch}/Tk
%{perl_vendorarch}/Tk/MMutil.pm
%{perl_vendorarch}/Tk/install.pm
%{perl_vendorarch}/Tk/MakeDepend.pm

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 804.036-24
- Prepare for Oreon 11 (RP1)
