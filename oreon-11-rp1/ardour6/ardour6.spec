%global source0_hash dcb68215822e3f826c9fc0826c7f9f98c9b6d39a4cb9ab67432c85eb5c636732
%bcond_with websockets
%bcond_with tests
%bcond_without verbose_build
%if %{with verbose_build}
%global _verbose -v
%else
%global _verbose %{nil}
%endif
%bcond_without system_libs
%if "%_lib" == "lib64"
%bcond_without apply_64bit_patches
%else
%bcond_with apply_64bit_patches
%endif
%global internal_libs_re (alsa_audiobackend|ardour.*|audiographer|canvas|dummy_audiobackend|evoral|gtkmm2ext|jack_audiobackend|midipp|pan[12]in2out|panbalance|panvbap|pbd|ptformat|pulseaudio_backend.so|qmdsp|temporal|timecode|waveview|widgets)
%global __provides_exclude_from ^%{_libdir}/(%{name}|lv2)/.*$
%global __requires_exclude ^lib%{internal_libs_re}\.so.*$
Name:       ardour6
Version:    6.9.0
Release:        1%{?dist}
Summary:        Digital Audio Workstation
License:    GPL-3.0-only
URL:        https://ardour.org
Source0:        Ardour-%{version}.tar.bz2
Source1:    LICENSING
Source2:    gpl-3.0.txt
Patch0:     0001-wscript-fix-testing-equality-is-none-issue.patch
Patch1:     0002-Update-waf-binary-using-doc-updating_waf.txt.patch
Patch2:     0003-wscript-fix-regexp-escaping-with-the-more-strict-Pyt.patch
Patch3:     0004-wscript-detect-if-qm-dsp-is-self-contained-or-need-l.patch
Patch4:     0005-remove-unused-function-from-autowaf.py-it-no-longer-.patch
Patch5:     0006-upgrade-waf-to-2.0.26-includes-new-autowaf.py-versio.patch
Patch6:     0007-Deal-with-kissfft-130.patch
Patch7:     0001-Fix-failure-to-build-with-libxml2-version-2.12.patch
Patch8:     ardour6-c99.patch
Patch9:     0008-Potential-fix-for-taglib-v2.0-crashes-when-exporting.patch
Patch10:    0009-Add-missing-include-for-iostream-needed-for-taglib-2.patch
Patch100:   %{name}-vst-lib64.patch
Patch1001:   ardour-%{version}-lv2-include-path-meson.patch
%if %{with websockets}
%endif
Requires:       google-droid-sans-mono-fonts
Requires:       google-noto-sans-fonts
Provides:       bundled(gtk-theme-engine-clearlooks) = 2.9.0
Provides:       bundled(libsmf) = 1.2
Provides:       bundled(lua) = 5.3.5
Provides:       bundled(LuaBridge) = 1.0.2
Provides:       bundled(midi++) = 4.1.0
Provides:       bundled(pbd) = 4.1.0
Provides:       ardour6-backend-dummy%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      ardour6-backend-dummy < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       ardour6-backend-alsa%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      ardour6-backend-alsa < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       ardour6-backend-jack%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      ardour6-backend-jack < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       ardour6-backend-pulseaudio%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      ardour6-backend-pulseaudio < %{?epoch:%{epoch}:}%{version}-%{release}
# oreon:deps
BuildRequires:  (qm-dsp-static >= 1.7 with qm-dsp-static < 1.8)
BuildRequires:  boost-devel
BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  fontconfig
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  graphviz
BuildRequires:  itstool
BuildRequires:  kernel-headers
BuildRequires:  kiss-fft-static
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(aubio)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairomm-1.0)
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(giomm-2.4)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glibmm-2.4)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtkmm-2.4)
BuildRequires:  pkgconfig(hidapi-hidraw)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(lilv-0)
BuildRequires:  pkgconfig(lrdf)
BuildRequires:  pkgconfig(ltc)
BuildRequires:  pkgconfig(lv2)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(pangomm-1.4)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(rubberband)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(serd-0)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(sord-0)
BuildRequires:  pkgconfig(soundtouch-1.0)
BuildRequires:  pkgconfig(sratom-0)
BuildRequires:  pkgconfig(suil-0)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(vamp-hostsdk)
BuildRequires:  pkgconfig(vamp-sdk)
BuildRequires:  pkgconfig(x11)
BuildRequires:  python-unversioned-command
BuildRequires:  python3
BuildRequires:  symlinks
# /oreon:deps
%description
Ardour is a multi-channel digital audio workstation, allowing users to record,
edit, mix and master audio and MIDI projects. It is targeted at audio
engineers, musicians, soundtrack editors and composers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S gendiff -N -n Ardour-%{version}
%autopatch -p1 %{!?with_apply_64bit_patches:-M 99}%{?with_apply_64bit_patches:-M 999}

%if %{with system_libs}
# remove bundled library sources
for i in fluidsynth hidapi libltc qm-dsp; do
    find "libs/$i" \( -name \*.\[ch\] -o -name \*.cc -o -name \*.\[ch\]pp \) -delete
done
%endif

# use versionized name for man page
cp -p ardour.1 ardour6.1

cp %{SOURCE1} %{SOURCE2} .

%build

export LC_ALL=C.UTF-8
%set_build_flags
./waf configure \
%if %{with strict}
    --strict \
%endif
%if %{with tests}
    --test \
%endif
    --prefix="%_prefix" \
    --bindir="%_bindir" \
    --configdir="%_sysconfdir" \
    --datadir="%_datadir" \
    --includedir="%_includedir" \
    --libdir="%_libdir" \
    --mandir="%_mandir" \
    --docdir="%_docdir" \
    --docs \
    --lxvst \
    --vst3 \
    --nls \
    --noconfirm \
    --no-phone-home \
    --optimize \
%ifarch %ix86 x86_64
    --arch="%optflags -msse -mfpmath=sse -DUSE_XMMINTRIN" \
%else
    --arch="%optflags" \
%endif
%if %{with system_libs}
    --use-external-libs \
%endif
    --freedesktop \
    --with-backends=dummy,alsa,jack,pulseaudio
./waf build %{_verbose} %{?_smp_mflags}
./waf i18n %{_verbose} %{?_smp_mflags}
%install
./waf --destdir=%{buildroot} install %{_verbose}
ln -snf ../fonts/google-droid/DroidSansMono.ttf %{buildroot}%{_datadir}/%{name}/ArdourMono.ttf
ln -snf ../fonts/google-noto/NotoSans-Regular.ttf %{buildroot}%{_datadir}/%{name}/ArdourSans.ttf
install -d -m755 %{buildroot}%{_mandir}/man1
install -p -m644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
mkdir -p %{buildroot}%{_datadir}/applications/
desktop-file-install --dir %{buildroot}%{_datadir}/applications \
    --set-key=Name --set-value="Ardour %{version}" \
    --set-generic-name="Digital Audio Workstation" \
    --set-key=X-GNOME-FullName \
    --set-value="Ardour v%{version} (Digital Audio Workstation)" \
    --set-comment="Record, mix and master audio" \
    --remove-category=AudioEditing \
    --add-category=X-AudioEditing \
    build/gtk2_ardour/%{name}.desktop
rm %{buildroot}%{_datadir}/%{name}/templates/.stub
%find_lang %{name}
%find_lang gtk2_%{name}
%find_lang gtkmm2ext3
find %{buildroot}%{_datadir}/%{name} | \
    sed 's|^%{buildroot}||g' | \
    while read f; do
        if [ "$f" = "${f/ /}" ]; then
            _f="$f"
        else
            _f="\"${f}\""
        fi
        if [ -d "%{buildroot}${f}" ]; then
            echo "%%dir ${_f}"
        else
            if [ "${f}" = "${f#%{_datadir}/%{name}/locale}" ]; then
                echo "${_f}"
            fi
        fi
    done > %{name}-datafiles.list
find %{buildroot} -type l | while read src; do
    tgt="$(readlink "$src")"
    if [ "${tgt#/}" != "$tgt" -a "${tgt#%{buildroot}/}" = "$tgt" ]; then
        ln -snf "%{buildroot}${tgt}" "$src"
    fi
done
symlinks -r -c %{buildroot}
%oreon_autofiles main

%check

%if %{with tests}
WAFTPATH="$PWD/doc/waft"
pushd libs/ardour
sh "$WAFTPATH" --targets=libardour-tests && LV2_PATH= ./run-tests.sh
popd
%endif
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
rm -f %{buildroot}%{_bindir}/run-tests
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
