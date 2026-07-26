%global source0_hash 775eaff53637320ec0d6e273ac3e15dead3922b96406f93913fdd03ce3965b9e

# Run X11 tests
%{bcond_without perl_Prima_enables_x11_test}
# Support bidirectional text with FriBidi library
%{bcond_without perl_Prima_enables_fribidi}
# Support GIF image format
%{bcond_without perl_Prima_enables_gif}
# Use GTK2 file dialogs and fonts. GTK3 takes precedence.
%{bcond_with perl_Prima_enables_gtk2}
# Use GTK3 file dialogs and fonts
%{bcond_without perl_Prima_enables_gtk3}
# Use HarfBuzz library for rendering a text
%{bcond_without perl_Prima_enables_harfbuzz}
# Use libheif for rendering HEIF images
%{bcond_without perl_Prima_enables_heif}
# Use libjxl for rendering JXL images
%{bcond_without perl_Prima_enables_jxl}
# Use LibThai library for wrapping a Thai text
%{bcond_without perl_Prima_enables_libthai}
# Support colorful cursor via Xcursor
%{bcond_without perl_Prima_enables_xcursor}
# Support FreeType fonts via xft
%{bcond_without perl_Prima_enables_xft}
# Support WebP image format
%{bcond_without perl_Prima_enables_wepb}

%define use_gtk2 0
%define use_gtk3 0
%if %{with perl_Prima_enables_gtk3}
%define use_gtk3 1
%else
%if %{with perl_Prima_enables_gtk2}
%define use_gtk2 1
%endif
%endif

Name:           perl-Prima
Version:        1.77
Release:        2%{?dist}
Summary:        Perl graphic toolkit
# Copying:              BSD-2-Clause text
# examples/tiger.eps:   AGPL-3.0-or-later (bundled from GhostScript? CPAN RT#122271)
# img/codec_jpeg.c:     LGPL-2.0-or-later (EXIF parser is based on io-jpeg.c
#                       from gdk-pixbuf)
# img/codec_X11.c:      MIT-open-group
# img/imgscale.c:       ImageMagick (resizing filters are based on magick/resize.c
#                       from ImageMagick)
# img/polyfill.c:       MIT-open-group AND HPND
# include/unix/queue.h: BSD-4-Clause
# LICENSE:              BSD-2-Clause text and (AGPL-3.0-or-later notice for examples/tiger.eps file)
# pod/Prima/Widget/pack.pod:    TCL
# pod/Prima/Widget/place.pod:   TCL
# pod/prima-gencls.pod: "under the BSD License"
# Prima.pm:             "under the BSD License"
# Prima/PS/Unicode.pm:  BSD-3-Clause
# unix/render.c:        HPND-sell-variant
License:        BSD-2-Clause AND BSD-3-Clause AND BSD-4-Clause AND MIT-open-group AND HPND AND HPND-sell-variant AND TCL AND ImageMagick AND LGPL-2.0-or-later AND AGPL-3.0-or-later
URL:            https://metacpan.org/dist/Prima
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KARASIK/Prima-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
%if %{with perl_Prima_enables_gtk3}
BuildRequires:  giflib-devel >= 4
%endif
BuildRequires:  gcc
BuildRequires:  libjpeg-devel
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.12
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# pkgconfig is optional, but it provides better compiler options, so use it
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
%if %{with perl_Prima_enables_fribidi}
BuildRequires:  pkgconfig(fribidi)
%endif
%if %{use_gtk2}
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.7
%endif
%if %{use_gtk3}
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.9
%endif
%if %{with perl_Prima_enables_harfbuzz}
BuildRequires:  pkgconfig(harfbuzz)
%endif
%if %{with perl_Prima_enables_heif}
BuildRequires:  pkgconfig(libheif) >= 1.12.0
%endif
%if %{with perl_Prima_enables_jxl}
BuildRequires:  pkgconfig(libjxl)
%endif
BuildRequires:  pkgconfig(libpng)
%if %{with perl_Prima_enables_libthai}
BuildRequires:  pkgconfig(libthai)
%endif
BuildRequires:  pkgconfig(libtiff-4)
%if %{with perl_Prima_enables_wepb}
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwebpdemux)
BuildRequires:  pkgconfig(libwebpmux)
%endif
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
%if %{with perl_Prima_enables_xcursor}
BuildRequires:  pkgconfig(xcursor)
%endif
BuildRequires:  pkgconfig(xext)
%if %{with perl_Prima_enables_xft}
BuildRequires:  pkgconfig(xft)
%endif
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xrandr) >= 1.5
BuildRequires:  pkgconfig(xrender)
# Run-time:
# AnyEvent not used, t/misc/syntax.t fakes it.
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
# Getopt::Long not used at tests
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::RefHash)
# Optional run-time:
BuildRequires:  perl(Compress::Raw::Zlib)
# gv not used at a tests
# Tests:
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
%if %{with perl_Prima_enables_x11_test}
# X11 tests:
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  font(:lang=en)
# Tests exhibit a proportional font
BuildRequires:  liberation-sans-fonts
%endif
Recommends:     perl(Compress::Raw::Zlib)
Suggests:       gv
# Public modules without a package keyword:
Provides:       perl(Prima::noARGV) = %{version}
Provides:       perl(Prima::PS::Drawable::Path) = %{version}
Provides:       perl(Prima::PS::Drawable::Region) = %{version}
Provides:       perl(Prima::PS::Setup) = %{version}

%{?perl_default_filter}

# Do not export private modules (not starting with "Prima")
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\((am|apc|bi|bs|bt|ci|cl|cm|CodeEditor|cr|cs|CustomPodView|Divider|dmfp|dt|Editor|fdo|fds|fe|fp|fr|fra|frr|fs|fw|gm|gr|grow|gsci|gt|gui|ict|im|is|ItemsOutline|kb|km|le|lj|lp|mb|mbi|MenuOutline|MPropListViewer|mt|MyOutline|nt|PackPropListViewer|PropListViewer|rop|Round3D|sbmp|ss|sv|ta|tb|tka|tm|tno|tns|tw|wc|ws)\\)

# Filter under-specified provides
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Prima\\)$

%description
Prima is a general purpose extensible graphical user interface toolkit with
a rich set of standard widgets and an emphasis on 2D image processing tasks.
A Perl program using PRIMA looks and behaves identically on X, Win32.

%package AnyEvent
Summary:        AnyEvent bridge for Prima Perl graphic toolkit
License:        BSD-2-Clause
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description AnyEvent
This is an experiment to bring in AnyEvent::Impl::Prima into the
Prima toolkit's core.

%package Test
Summary:        Test tools for Prima Perl graphic toolkit
License:        BSD-2-Clause
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Test
This Perl module contains a small set or tool used for testing of
Prima-related code together with standard Perl Test:: suite.

%package tests
Summary:        Tests for %{name}
License:        BSD-2-Clause
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-Test = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
%if %{with perl_Prima_enables_x11_test}
Requires:       xorg-x11-server-Xvfb
Requires:       font(:lang=en)
# Tests exhibit a proportional font
Requires:       liberation-sans-fonts
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Prima-%{version}
# Normalize end-of-lines
find -type f \( -name '*.pm' -o -name '*.pl' -o -name '*.PL' -o -name '*.t' \
     -o -name Changes -o -name README.md \) -exec perl -i -pe 's/\r\n/\n/' {} +
# Help generators to recognize Perl scripts
for F in $(find t -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
unset AUTOMATED_TESTING NONINTERACTIVE_TESTING PERL_BATCH
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 \
    OPTIMIZE="$RPM_OPT_FLAGS" \
    DEBUG=0 \
    VERBOSE=1 \
    WITH_COCOA=0 \
    WITH_FONTCONFIG=1 \
    WITH_FREETYPE=1 \
    WITH_FRIBIDI=%{with perl_Prima_enables_fribidi} \
    WITH_GTK2=%{use_gtk2} \
    WITH_GTK3=%{use_gtk3} \
    WITH_HARFBUZZ=%{with perl_Prima_enables_harfbuzz} \
    WITH_HOMEBREW=0 \
    WITH_ICONV=1 \
    WITH_LIBTHAI=%{with perl_Prima_enables_libthai} \
    WITH_OPENMP=1 \
    WITH_XFT=%{with perl_Prima_enables_xft}
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
find %{buildroot} -type f -name '*.a' -size 0 -delete
find %{buildroot}/%{_mandir} -type f -size 0 -delete
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/misc/syntax.t
find %{buildroot}%{_libexecdir}/%{name}/t -name '*.xt' -delete
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# t/misc/fs.t writes into CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/t "$DIR"
pushd "$DIR"
unset DISPLAY XDG_SESSION_TYPE
%if %{with perl_Prima_enables_x11_test}
    xvfb-run -d prove -I . -r -j 1 t
%else
    prove -I . -r -j 1 t
%endif
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset DISPLAY XDG_SESSION_TYPE
# Not parallel-safe
%if %{with perl_Prima_enables_x11_test}
    xvfb-run -d make test
%else
    make test
%endif

%files
%license Copying LICENSE AGPLv3
# "examples" directory is installed into perl_vendorarch
%doc Changes README.md
%{_bindir}/podview
%{_bindir}/prima-*
%{_bindir}/VB
%{perl_vendorarch}/auto/Prima
%{perl_vendorarch}/prima-gencls.pod
%{perl_vendorarch}/Prima.pm
%{perl_vendorarch}/Prima
%exclude %{perl_vendorarch}/Prima/examples/socket_anyevent1.pl
%exclude %{perl_vendorarch}/Prima/examples/socket_anyevent2.pl
%exclude %{perl_vendorarch}/Prima/Stress.*
%exclude %{perl_vendorarch}/Prima/sys/AnyEvent.pm
%exclude %{perl_vendorarch}/Prima/sys/Test.*
%{perl_vendorarch}/vb-large.png
%{_mandir}/man1/podview.*
%{_mandir}/man1/prima-*.*
%{_mandir}/man1/VB.*
%{_mandir}/man3/pod::Prima::*
%{_mandir}/man3/pod::prima-gencls.*
%{_mandir}/man3/Prima.*
%{_mandir}/man3/Prima::*
%exclude %{_mandir}/man3/Prima::Stress.*
%exclude %{_mandir}/man3/Prima::sys::AnyEvent.*
%exclude %{_mandir}/man3/Prima::sys::Test.*

%files AnyEvent
%{perl_vendorarch}/Prima/examples/socket_anyevent1.pl
%{perl_vendorarch}/Prima/examples/socket_anyevent2.pl
%{perl_vendorarch}/Prima/sys/AnyEvent.pm
%{_mandir}/man3/Prima::sys::AnyEvent.*

%files Test
%{perl_vendorarch}/Prima/Stress.*
%{perl_vendorarch}/Prima/sys/Test.*
%{_mandir}/man3/Prima::Stress.*
%{_mandir}/man3/Prima::sys::Test.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
