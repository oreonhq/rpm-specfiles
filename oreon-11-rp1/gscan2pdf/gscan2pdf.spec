%global source0_hash 0d4304f6723d076f868feb013e3d7be925dfbb10dcdc23177dbcbf6606b7d5fa

# Run tests. They are quite fragile (especially regarding to ImageMagick and
# fonts) and take long and need many dependencies.
%bcond_without gscan2pdf_enables_test

# There is no native X11 on RHEL ≥ 10
%if 0%{?rhel} >= 10
%global wayland 1
%else
%global wayland 0
%endif

Name:           gscan2pdf
Version:        2.13.5
Release:        3%{?dist}
Summary:        GUI for producing a multipage PDF from a scan
# icons/180_degree.svg: GPL-3.0-only
# icons/scanner.svg:    GPL-2.0-only
# icons/pdf.svg:        LGPL-2.0-or-later (a copy of
#           Nuvola/icons/scalable/mimetypes/gnome-mime-application-pdf.svg
#           from gnome-themes-extras-0.9.0)
# net.sourceforge.gscan2pdf.appdata.xml:    CC0-1.0
# other files:          GPL-3.0-only
License:        GPL-3.0-only AND GPL-2.0-only AND LGPL-2.0-or-later AND CC0-1.0
URL:            https://gscan2pdf.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Source1:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz.asc
# Key exported from Petr Pisar's keyring
Source2:        gpgkey-463293E4AE33871846F30227B321F203110FCAF3.gpg
# Do not warn about missing pdftk, bug #1708054, not upstreamable
Patch0:         gscan2pdf-2.9.0-Do-not-warn-about-missing-pdftk.patch
# Replace copies of gscan2pdf.svg with links, not upstreamable
Patch1:         gscan2pdf-2.12.7-Symlink-gscan2pdf.svg-files.patch
# Fix locale in tests, proposed upstream,
# <https://sourceforge.net/p/gscan2pdf/patches/26/>
Patch2:         gscan2pdf-2.13.5-Set-locale-to-C-for-tests-that-compare-textual-messa.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
# awk in Makefile.PL
BuildRequires:  gawk
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# pod2html in Makefile.PL
BuildRequires:  perl-Pod-Html
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
%if %{with gscan2pdf_enables_test}
# Run-time:
# ImageMagick for "convert" tool executed from _thread_threshold() and
# _write_image_object()
BuildRequires:  ImageMagick
# libtiff-tools for /usr/bin/tiffcp and
# (/usr/bin/tiff2ps or poppler-utils) for PostScript support
BuildRequires:  libtiff-tools >= 4.7.0
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config::General) >= 2.40
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::UUID)
BuildRequires:  perl(Date::Calc)
BuildRequires:  perl(Encode)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Filesys::Df)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Glib) >= 1.220
BuildRequires:  perl(Glib::Object::Introspection)
BuildRequires:  perl(Glib::Object::Subclass)
BuildRequires:  perl(GooCanvas2)
BuildRequires:  perl(GooCanvas2::Canvas)
BuildRequires:  perl(Gtk3) >= 0.028
# Gtk3::Entry is not provided by perl-Gtk3
BuildRequires:  perl(Gtk3::ImageView)
BuildRequires:  perl(Gtk3::ImageView::Tool::Dragger)
BuildRequires:  perl(Gtk3::ImageView::Tool::Selector)
BuildRequires:  perl(Gtk3::ImageView::Tool::SelectorDragger)
BuildRequires:  perl(Gtk3::SimpleList)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::TokeParser)
BuildRequires:  perl(if)
BuildRequires:  perl(Image::Magick)
BuildRequires:  perl(Image::Sane)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Locale::gettext) >= 1.05
BuildRequires:  perl(Locale::Language)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(PDF::Builder) >= 3.022
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Proc::Killfam)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Set::IntSpan) >= 1.10
BuildRequires:  perl(Socket)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Thread::Queue)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
# Optional run-time:
# djvulibre for djvused program
BuildRequires:  djvulibre
BuildRequires:  poppler-utils
BuildRequires:  unpaper
# xz not used at tests
# Tests:
BuildRequires:  file
# fontconfig for a fc-list tool
BuildRequires:  fontconfig
# We need to pass a specific font name to ImageMagick, bug #1494563
BuildRequires:  font(dejavusans)
# ghostscript for pdf2ps used in t/1163_save_multipage_pdf_as_ps.t
BuildRequires:  ghostscript
BuildRequires:  ImageMagick-djvu
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(IPC::System::Simple)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Override)
BuildRequires:  perl(Test::More)
# poppler-utils for pdffonts and pdfinfo
BuildRequires:  sane-backends-drivers-scanners
%if %{wayland}
BuildRequires:  mutter
BuildRequires:  xwayland-run
%else
BuildRequires:  xorg-x11-server-Xvfb
%endif
# Optional tests:
%if 0%{?fedora} < 43 && 0%{?fedora} >= 41
# Some tests (e.g. t/52_process_chain_udt.t) attempt to load PNM or PBM
# images and Glib::Object::Introspection then warns "Caught error getting
# pixbuf: Couldn’t recognize the image file format...". That's because
# a support for the formats was removed from gdk-pixbuf2-modules.
# PNM and PBM are again supported by glycin >= 2.0.alpha.5 linked from
# gdk-pixbuf2.
BuildRequires:  gdk-pixbuf2-modules-extra
%endif
# pdftk not packaged (bug #1708054)
# poppler-utils for pdfunite, pdftotext
# sane-frontends for scanadf
BuildRequires:  sane-frontends
# Test::Perl::Critic not used
%endif
# libappstream-glib for appstream-util
BuildRequires:  libappstream-glib
Suggests:       cuneiform
# Prefer gocr over cuneiform, or tesseract
Recommends:     gocr
# djvulibre for djvused program
Recommends:     djvulibre
%if 0%{?fedora} < 43 && 0%{?fedora} >= 41
# Some operations like Threshold use PBM as an intermediate format and then
# Glib::Object::Introspection warns "Caught error getting pixbuf:
# Couldn’t recognize the image file format..." and gscan2pdf fails to load it.
# That's because a support for the format was removed from
# gdk-pixbuf2-modules-2.42.11 and later added as a separate package.
# PNM and PBM are again supported by glycin >= 2.0.alpha.5 linked from
# gdk-pixbuf2.
Requires:       gdk-pixbuf2-modules-extra
%endif
# libtiff-tools for /usr/bin/tiffcp and
# (/usr/bin/tiff2ps or poppler-utils) for PostScript support
Requires:       libtiff-tools >= 4.7.0
Requires:       perl(if)
Recommends:     perl(Image::Magick)
Requires:       perl(PDF::Builder) >= 3.022
# convert tool executed from _write_image_object() and _thread_threshold()
Requires:       ImageMagick
Recommends:     ImageMagick-djvu
# poppler-utils for pdfimages, pdfinfo, and pdftotext
Recommends:     poppler-utils
Requires:       sane-backends >= 1.0.17
Requires:       sane-frontends
Suggests:       tesseract
Recommends:     unpaper
# xdg-utils for xdg-email command
Recommends:     xdg-utils
Recommends:     xz

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Glib\\) >= 1\.210$
%global __requires_exclude %{__requires_exclude}|^perl\\(PDF::Builder\\)$

# Gtk3::Entry is not provided by perl-Gtk3
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Gtk3::Entry\\)

%description
A GUI to ease the process of producing a multipage PDF from a scan.

%package tests
Summary:        Tests for %{name}
License:        GPL-3.0-only
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       file
# fontconfig for a fc-list tool
Requires:       fontconfig
%if 0%{?fedora} < 43 && 0%{?fedora} >= 41
# Some tests (e.g. t/52_process_chain_udt.t) attempt to load PNM or PBM
# images and Glib::Object::Introspection then warns "Caught error getting
# pixbuf: Couldn’t recognize the image file format...". That's because
# a support for the formats was removed from gdk-pixbuf2-modules.
# PNM and PBM are again supported by glycin >= 2.0.alpha.5 linked from
# gdk-pixbuf2.
Requires:       gdk-pixbuf2-modules-extra
%endif
Requires:       perl-Test-Harness
# We need to pass a specific font name to ImageMagick, bug #1494563
Requires:       font(dejavusans)
# ghostscript for pdf2ps used in t/1163_save_multipage_pdf_as_ps.t
Requires:       ghostscript
Requires:       ImageMagick-djvu
Requires:       perl(PDF::Builder) >= 3.022
# poppler-utils for pdffonts and pdfinfo
Requires:       poppler-utils
Requires:       sane-backends-drivers-scanners
%if %{wayland}
Requires:       mutter
Requires:       xwayland-run
%else
Requires:       xorg-x11-server-Xvfb
%endif
# Optional tests:
# pdftk not packaged (bug #1708054)
# poppler-utils for pdfunite, pdftotext
# sane-frontends for scanadf
Requires:       sane-frontends

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
# Symlink identical files
rm scanners/FujitsuS510.Lineart
ln -s FujitsuS510 scanners/FujitsuS510.Lineart
rm scanners/snapscanS510.Color
ln -s snapscanS510 scanners/snapscanS510.Color
# Remove unused tests
rm t/91_critic.t
# Disable currently failing tests
# TODO: Fix them with upstream
# glib randomly fails with "GLib-GObject-WARNING **:
# ../gobject/gsignal.c:2647: instance '0x559dcdc1e290' has no handler with id
# '7415' at t/0602_Dialog_Scan.t line 313.".
rm t/0603_Dialog_Scan.t
# ImageMagick reports 255x30 image size
rm t/113_save_pdf_with_downsample.t
# ???
rm t/1111_save_pdf.t
# Fails with got: '179', expected '296' if not run separately. New test in 2.11.0.
rm t/169_import_scan.t
# gocr does not recognize a text
rm t/431_gocr.t t/432_gocr.t
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 SHAREDIR=%{_datadir}
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}

desktop-file-install --delete-original \
  --dir=%{buildroot}/%{_datadir}/applications         \
  %{buildroot}/%{_datadir}/applications/net.sourceforge.gscan2pdf.desktop

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a scanners t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/99_pod.t
# Hang in CI and local mock because finished_callback is called instead of
# queued_callback
for TEST in 1113_save_pdf_with_error 126_save_djvu_with_error \
    133_save_tiff_with_error 1602_import_DjVu_with_error \
    1612_import_TIFF_with_error 1626_import_PDF_with_error \
    1632_import_ppm_with_error \
    213_rotate_with_error 243_threshold_with_error 253_negate_with_error \
    263_unsharp_mask_with_error 273_crop_with_error 283_to_png_with_error \
    354_unpaper_with_error 377_user_defined_with_error \
    434_gocr_with_error; do
    rm %{buildroot}%{_libexecdir}/%{name}/t/"$TEST".t
done
# Regular fail for an unknown reason
for TEST in 0601_Dialog_Scan 1601_import_DjVu 1604_import_multipage_DjVu \
    1642_import_png_with_error; do
    rm %{buildroot}%{_libexecdir}/%{name}/t/"$TEST".t
done
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Many tests write into CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
unset GNOME_DESKTOP_SESSION_ID KDE_FULL_SESSION LOGDIR OCROSCRIPTS \
    SANE_DEFAULT_DEVICE XDG_CONFIG_HOME XDG_CURRENT_DESKTOP
pushd "$DIR"
# Tests overwrite same-named files
%if %{wayland}
xwfb-run -c mutter -- prove -I . -j 1
%else
xvfb-run -d prove -I . -j 1
%endif
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%find_lang %{name}

%check
%if %{with gscan2pdf_enables_test}
unset GNOME_DESKTOP_SESSION_ID KDE_FULL_SESSION LOGDIR OCROSCRIPTS \
    SANE_DEFAULT_DEVICE XDG_CONFIG_HOME XDG_CURRENT_DESKTOP
%if %{wayland}
xwfb-run -c mutter -- make test
%else
xvfb-run -d make test
%endif
%endif
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/net.sourceforge.gscan2pdf.appdata.xml

# Do not call gtk-update-icon-cache because it's needed only for updating icon
# themata in %%{_datadir}/icon/*. This package installs icon into
# %%{_datadir}/pixmaps/gscan2pdf.svg. Pixmaps seems not to be subject of icon
# themata.
%post
touch --no-create %{_datadir}/pixmaps || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/pixmaps || :
fi

%files -f %{name}.lang
%license LICENCE
%doc COPYING History
%{_bindir}/%{name}
%{perl_vendorlib}/Gscan2pdf
%{_datadir}/%{name}
%{_datadir}/applications/net.sourceforge.gscan2pdf.desktop
%dir %{_datadir}/help/*
%{_datadir}/help/*/%{name}
%{_datadir}/metainfo/net.sourceforge.gscan2pdf.appdata.xml
%{_datadir}/pixmaps/%{name}.svg
%{_mandir}/man1/%{name}.1*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
