%global source0_hash none
%bcond version_overlay 0
%bcond tests 1
%bcond verbose_build 1
%if %{with verbose_build}
%global _verbose -v
%else
%global _verbose %{nil}
%endif
%bcond system_libs 1
%if "%_lib" == "lib64"
%bcond apply_64bit_patches 1
%else
%bcond apply_64bit_patches 0
%endif
%global internal_libs_re (aaf|alsa_audiobackend|ardour.*|audiographer|canvas|dummy_audiobackend|evoral|gtkmm2ext|jack_audiobackend|midipp|pan[12]in2out|panbalance|panvbap|pbd|ptformat|pulseaudio_backend.so|qmdsp|suil|temporal|timecode|waveview|widgets|ydk|ydk-pixbuf|ydkmm|ytk|ytkmm|ztk|ztkmm)
%global __provides_exclude_from ^%{_libdir}/(%{name}|lv2)/.*$
%global __requires_exclude ^lib%{internal_libs_re}\.so.*$
%global broken_tests temporal ardour/test_fpu
Name:       ardour9
Version:    9.2.0
%global plain_version %{lua:
    local plain_version = (string.gsub(macros.version, '^([^%^~]+)[%^~]+.*$', '%1'))
    if plain_version ~= macros.version then
        macros.prepostver = (string.gsub(macros.version, '^[^%^~]+[%^~]+([^%^~]+).*$', '%1'))
        macros.snapshot = (string.gsub(macros.version, '^[^%^~]+[%^~]+[^%^~]+[%^~]+([^%^~]+).*$', '%1'))
    end
    print(plain_version)
}
%global archive_version %{plain_version}%{?prepostver:.%{prepostver}}%{?snapshot:.%{snapshot}}
%global major %{lua:
    print((string.gsub(macros.plain_version, '^(%d+)%..*$', '%1')))
}
Release:        1%{?dist}
Summary:        Digital Audio Workstation
License:    GPL-3.0-only
URL:        https://ardour.org
Source0:        Ardour-%{version}.tar.bz2
Source1:    LICENSING
Source2:    gpl-3.0.txt
Patch100:   %{name}-vst-lib64.patch
Patch101:    ardour9-mark-versionized.patch
%if %{with version_overlay}
%endif
Requires:       google-droid-sans-mono-fonts
Requires:       google-noto-sans-fonts
Provides:       bundled(gtk-theme-engine-clearlooks) = 2.9.0
Provides:       bundled(libsmf) = 1.2
Provides:       bundled(lua) = 5.3.5
Provides:       bundled(LuaBridge) = 1.0.2
Provides:       bundled(midi++) = 4.1.0
Provides:       bundled(pbd) = 4.1.0
Provides:       bundled(ytk) = 2.24.23
Provides:       bundled(ydk) = 2.24.23
Provides:       bundled(ytkmm) = 2.24.5
Provides:       bundled(ydkmm) = 2.24.5
Provides:       bundled(ydk-pixbuf) = 2.31.1
Provides:       bundled(suil) = 0.10.8
Provides:       bundled(ztk) = 2.14.0
Provides:       bundled(ztkmm) = 2.22.7
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
BuildRequires:  pkgconfig(hidapi-hidraw)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libwebsockets)
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
BuildRequires:  pkgconfig(sratom-0)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(vamp-hostsdk)
BuildRequires:  pkgconfig(vamp-sdk)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  python-unversioned-command
BuildRequires:  python3
BuildRequires:  symlinks
# /oreon:deps
%description
Ardour is a multi-channel digital audio workstation, allowing users to record,
edit, mix and master audio and MIDI projects. It is targeted at audio
engineers, musicians, soundtrack editors and composers.

%prep

%autosetup -S gendiff -N -n Ardour-%{archive_version}
%if 0%{?PATCH0:1}
%autopatch -p1 -M99
%endif
%autopatch -p1 %{?with_apply_64bit_patches:100} %{?with_version_overlay:101}

%if %{with system_libs}
# remove bundled library sources
for i in fluidsynth hidapi libltc qm-dsp; do
    find "libs/$i" \( -name \*.\[ch\] -o -name \*.cc -o -name \*.\[ch\]pp \) -delete
done
%endif

# use versionized name for man page
cp -p ardour.1 %{name}.1

cp %{SOURCE1} %{SOURCE2} .

%build

export LC_ALL=C.UTF-8
%set_build_flags
./waf configure \
%if %{with tests}
    --test \
    --single-tests \
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
    --cxx17 \
    --no-execstack \
    --freedesktop \
    --with-backends=dummy,alsa,jack,pulseaudio
./waf build %{_verbose} %{?_smp_mflags}
./waf i18n %{_verbose} %{?_smp_mflags}
%install
./waf --destdir=%{buildroot} install %{_verbose}
%if %{with version_overlay}
version="9"
pushd gtk2_ardour/resources
for srcfile in Ardour-icon_*px.png; do
    size="${srcfile#Ardour-icon_}"; size="${size%px.png}"
    pointsize="$(($size * 9 / 25 + 5))"
    offset="$(($size / 10))"
    magick convert \
        "$srcfile" \
        -gravity NorthEast \
        -stroke black \
        -fill white \
        -pointsize "$pointsize" \
        -annotate "+${offset}+0" "$version" \
        "%{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/%{name}.png"
done
popd
%endif
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
%find_lang libytk%{major}
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
rm -rf xdg-config-home
mkdir xdg-config-home
export XDG_CONFIG_HOME="${PWD}/xdg-config-home"
WAFTPATH="$PWD/doc/waft"
pushd libs/ardour
sh "$WAFTPATH" --targets=libardour-tests
popd
for exe in build/libs/*/run-tests; do
    dir="${exe%/run-tests}"
    component="${dir#build/libs/}"
    mode=run-all
    skip_some=","
    for broken_test in %broken_tests; do
        if [ "$broken_test" = "$component" ]; then
            mode=skip-all
            break
        fi
        bt_component="${broken_test%/*}"
        bt_test="${broken_test#*/}"
        if [ "$bt_component" = "$component" ]; then
            mode=skip-some
            skip_some="${skip_some}${bt_test},"
        fi
    done
    case "$mode" in
        skip-all)
            ;;
        skip-some)
            for path in "${dir}"/test_*; do
                unit_test="${path##*/}"
                if [ "$skip_some" = "${skip_some/,${unit_test},/}" ]; then
                    LV2_PATH= ./gtk2_ardour/artest "$component" "$unit_test"
                fi
            done
            ;;
        run-all)
            LV2_PATH= ./gtk2_ardour/artest "$component"
            ;;
    esac
done
%endif
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
