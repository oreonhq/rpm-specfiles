%global source0_hash 775eaff53637320ec0d6e273ac3e15dead3922b96406f93913fdd03ce3965b9e
%{bcond_without perl_Prima_enables_x11_test}
%{bcond_without perl_Prima_enables_fribidi}
%{bcond_without perl_Prima_enables_gif}
%{bcond_with perl_Prima_enables_gtk2}
%{bcond_without perl_Prima_enables_gtk3}
%{bcond_without perl_Prima_enables_harfbuzz}
%{bcond_without perl_Prima_enables_heif}
%{bcond_without perl_Prima_enables_jxl}
%{bcond_without perl_Prima_enables_libthai}
%{bcond_without perl_Prima_enables_xcursor}
%{bcond_without perl_Prima_enables_xft}
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
Release:        1%{?dist}
Summary:        Perl graphic toolkit
License:        BSD-2-Clause AND BSD-3-Clause AND BSD-4-Clause AND MIT-open-group AND HPND AND HPND-sell-variant AND TCL AND ImageMagick AND LGPL-2.0-or-later AND AGPL-3.0-or-later
URL:            https://metacpan.org/dist/Prima
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KARASIK/Prima-%{version}.tar.gz
%if %{with perl_Prima_enables_gtk3}
%endif
%if %{with perl_Prima_enables_fribidi}
%endif
%if %{use_gtk2}
%endif
%if %{use_gtk3}
%endif
%if %{with perl_Prima_enables_harfbuzz}
%endif
%if %{with perl_Prima_enables_heif}
%endif
%if %{with perl_Prima_enables_jxl}
%endif
%if %{with perl_Prima_enables_libthai}
%endif
%if %{with perl_Prima_enables_wepb}
%endif
%if %{with perl_Prima_enables_xcursor}
%endif
%if %{with perl_Prima_enables_xft}
%endif
%if %{with perl_Prima_enables_x11_test}
%endif
Recommends:     perl(Compress::Raw::Zlib)
Suggests:       gv
Provides:       perl(Prima::noARGV) = %{version}
Provides:       perl(Prima::PS::Drawable::Path) = %{version}
Provides:       perl(Prima::PS::Drawable::Region) = %{version}
Provides:       perl(Prima::PS::Setup) = %{version}
%{?perl_default_filter}
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\((am|apc|bi|bs|bt|ci|cl|cm|CodeEditor|cr|cs|CustomPodView|Divider|dmfp|dt|Editor|fdo|fds|fe|fp|fr|fra|frr|fs|fw|gm|gr|grow|gsci|gt|gui|ict|im|is|ItemsOutline|kb|km|le|lj|lp|mb|mbi|MenuOutline|MPropListViewer|mt|MyOutline|nt|PackPropListViewer|PropListViewer|rop|Round3D|sbmp|ss|sv|ta|tb|tka|tm|tno|tns|tw|wc|ws)\\)
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Prima\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  font(:lang=en)
BuildRequires:  gcc
BuildRequires:  giflib-devel
BuildRequires:  liberation-sans-fonts
BuildRequires:  libjpeg-devel
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Raw::Zlib)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::RefHash)
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libthai)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwebpdemux)
BuildRequires:  pkgconfig(libwebpmux)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/misc/syntax.t
find %{buildroot}%{_libexecdir}/%{name}/t -name '*.xt' -delete
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset DISPLAY XDG_SESSION_TYPE
%if %{with perl_Prima_enables_x11_test}
    xvfb-run -d make test
%else
    make test
%endif
%files -f %{oreon_filedir}/main.list
%files -n perl-Prima-AnyEvent -f %{oreon_filedir}/perl-Prima-AnyEvent.list
%files -n perl-Prima-Test -f %{oreon_filedir}/perl-Prima-Test.list
%files -n perl-Prima-tests -f %{oreon_filedir}/perl-Prima-tests.list

%changelog

%autochangelog
