%global source1_hash 009602041c297f222f8eb86f0cde1e089b78acb827122f397cf3ccf11dfaa12c
%global source0_hash 0d4304f6723d076f868feb013e3d7be925dfbb10dcdc23177dbcbf6606b7d5fa
%bcond_without gscan2pdf_enables_test
%global wayland 0
Name:           gscan2pdf
Version:        2.13.5
Release:        1%{?dist}
Summary:        GUI for producing a multipage PDF from a scan
License:        GPL-3.0-only AND GPL-2.0-only AND LGPL-2.0-or-later AND CC0-1.0
URL:            https://gscan2pdf.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Source1:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz.asc
Source2:        gpgkey-463293E4AE33871846F30227B321F203110FCAF3.gpg
Patch0:         gscan2pdf-2.9.0-Do-not-warn-about-missing-pdftk.patch
Patch1:         gscan2pdf-2.12.7-Symlink-gscan2pdf.svg-files.patch
Patch2:         gscan2pdf-2.13.5-Set-locale-to-C-for-tests-that-compare-textual-messa.patch
BuildArch:      noarch
%if %{with gscan2pdf_enables_test}
%endif
Suggests:       cuneiform
Recommends:     gocr
Recommends:     djvulibre
Requires:       libtiff-tools >= 4.7.0
Requires:       perl(if)
Recommends:     perl(Image::Magick)
Requires:       perl(PDF::Builder) >= 3.022
Requires:       ImageMagick
Recommends:     ImageMagick-djvu
Recommends:     poppler-utils
Requires:       sane-backends >= 1.0.17
Requires:       sane-frontends
Suggests:       tesseract
Recommends:     unpaper
Recommends:     xdg-utils
Recommends:     xz
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Glib\\) >= 1\.210$
%global __requires_exclude %{__requires_exclude}|^perl\\(PDF::Builder\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Gtk3::Entry\\)
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  ImageMagick-djvu
BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
BuildRequires:  djvulibre
BuildRequires:  file
BuildRequires:  font(dejavusans)
BuildRequires:  fontconfig
BuildRequires:  gawk
BuildRequires:  gettext
BuildRequires:  ghostscript
BuildRequires:  gnupg2
BuildRequires:  libappstream-glib
BuildRequires:  libtiff-tools
BuildRequires:  make
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Config::General)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::UUID)
BuildRequires:  perl(Date::Calc)
BuildRequires:  perl(Encode)
BuildRequires:  perl(English)
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Filesys::Df)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Glib)
BuildRequires:  perl(Glib::Object::Introspection)
BuildRequires:  perl(Glib::Object::Subclass)
BuildRequires:  perl(GooCanvas2)
BuildRequires:  perl(GooCanvas2::Canvas)
BuildRequires:  perl(Gtk3)
BuildRequires:  perl(Gtk3::ImageView)
BuildRequires:  perl(Gtk3::ImageView::Tool::Dragger)
BuildRequires:  perl(Gtk3::ImageView::Tool::Selector)
BuildRequires:  perl(Gtk3::ImageView::Tool::SelectorDragger)
BuildRequires:  perl(Gtk3::SimpleList)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::TokeParser)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(IPC::System::Simple)
BuildRequires:  perl(Image::Magick)
BuildRequires:  perl(Image::Sane)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Locale::Language)
BuildRequires:  perl(Locale::gettext)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(PDF::Builder)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Proc::Killfam)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Set::IntSpan)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sub::Override)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Thread::Queue)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(base)
BuildRequires:  perl(if)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-Pod-Html
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  poppler-utils
BuildRequires:  sane-backends-drivers-scanners
BuildRequires:  sane-frontends
BuildRequires:  unpaper
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
A GUI to ease the process of producing a multipage PDF from a scan.

%package tests
Summary:        Tests for %{name}
License:        GPL-3.0-only
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       file
Requires:       fontconfig
Requires:       perl-Test-Harness
Requires:       font(dejavusans)
Requires:       ghostscript
Requires:       ImageMagick-djvu
Requires:       perl(PDF::Builder) >= 3.022
Requires:       poppler-utils
Requires:       sane-backends-drivers-scanners
Requires:       xorg-x11-server-Xvfb
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a scanners t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/99_pod.t
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
for TEST in 0601_Dialog_Scan 1601_import_DjVu 1604_import_multipage_DjVu \
    1642_import_png_with_error; do
    rm %{buildroot}%{_libexecdir}/%{name}/t/"$TEST".t
done
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
unset GNOME_DESKTOP_SESSION_ID KDE_FULL_SESSION LOGDIR OCROSCRIPTS \
    SANE_DEFAULT_DEVICE XDG_CONFIG_HOME XDG_CURRENT_DESKTOP
pushd "$DIR"
xvfb-run -d prove -I . -j 1
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with gscan2pdf_enables_test}
unset GNOME_DESKTOP_SESSION_ID KDE_FULL_SESSION LOGDIR OCROSCRIPTS \
    SANE_DEFAULT_DEVICE XDG_CONFIG_HOME XDG_CURRENT_DESKTOP
xvfb-run -d make test
%endif
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/net.sourceforge.gscan2pdf.appdata.xml
%post

touch --no-create %{_datadir}/pixmaps || :
%postun

if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/pixmaps || :
fi
%files -f %{oreon_filedir}/main.list
%files -n gscan2pdf-tests -f %{oreon_filedir}/gscan2pdf-tests.list

%changelog

%autochangelog
