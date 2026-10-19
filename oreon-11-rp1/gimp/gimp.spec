%global source0_hash 40b15e90ad0c0c631b76da3c467ea9847fa5c24f37413ac5b492804860a28cd8
%bcond is_default_version 0
%bcond label_overlay 1
%global unwind_arches %{arm} aarch64 hppa ia64 mips ppc %{power64} %{ix86} x86_64
%ifarch %unwind_arches
%bcond libunwind 1
%else
%bcond libunwind 0
%endif
%bcond tests 1
%bcond skip_networking_tests 1
%bcond skip_problematic_tests 1
%bcond skip_user_tests 0
%global skip_tests_networking desktop - gimp:appdata_file
%global skip_tests_problematic app - gimp:save-and-export\
app - gimp:single-window-mode\
app - gimp:ui
%global skip_tests_user app - gimp:core\
app - gimp:save-and-export\
app - gimp:xcf\
app - gimp:single-window-mode\
app - gimp:ui
%global plain_lua_arches riscv64 ppc64le s390x
%global prerelease 1
Summary:        GNU Image Manipulation Program
Name:           gimp
Epoch:          2
Version:        3.2.6
Release:        1%{?dist}
ExcludeArch:    s390x
%global plain_version %{lua:
    local non_snapshot_version = (string.gsub(macros.version, '^(.*)%^.*$', '%1'))
    if non_snapshot_version ~= macros.version then
        macros.snapshot = (string.gsub(macros.version, '^.*%^(.*)$', '%1'))
        macros.git_rev = (string.gsub(macros.snapshot, '^.*git(.*)$', '%1'))
    end
    local plain_version = (string.gsub(non_snapshot_version, "~", "-"))
    print(plain_version)
}
%global major %{lua:
    print((string.gsub(macros.plain_version, '^(%d+)%..*$', '%1')))
}
%global minor %{lua:
    print((string.gsub(macros.plain_version, '^%d+%.(%d+)%..*$', '%1')))
}
%global micro %{lua:
    print((string.gsub(macros.plain_version, '^%d+%.%d+%.(%d+).*$', '%1')))
}
%global bin_version %{major}.%{minor}
%if %prerelease
%global gettext_version 30
%global api_version 3.0
%global lib_api_version 3.0
%else
%global gettext_version %{major}0
%global api_version %{major}.0
%global lib_api_version %{major}.0
%endif
%global interface_age 0
%global binary_age %{lua: print(100 * tonumber(macros.minor) + tonumber(macros.micro))}
%global lt_current %{lua: print(100 * tonumber(macros.minor) + tonumber(macros.micro) - tonumber(macros.interface_age))}
%global lt_revision %interface_age
%global lt_age %{lua: print(tonumber(macros.binary_age) - tonumber(macros.interface_age))}
%global so_version_major %{lua: print(tonumber(macros.lt_current) - tonumber(macros.lt_age))}
%global so_version %{so_version_major}.%{lt_age}.%{lt_revision}
License:        LGPL-3.0-or-later AND GPL-2.0-or-later AND GPL-3.0-or-later AND BSD-3-Clause AND CC-BY-SA-3.0 AND CC-BY-SA-4.0 AND CC0-1.0
URL:            https://www.gimp.org
%global alsa_minver 1.0.0
%global appstream_minver 0.16.1
%global atk_minver 2.4.0
%global bash_completion_minver 2.0
%global babl_minver 0.1.118
%global cairo_minver 1.14.0
%global cairopdf_minver 1.12.2
%global fontconfig_minver 2.12.4
%global freetype2_minver 2.1.7
%global gdk_pixbuf_minver 2.30.8
%global gegl_minver 0.4.64
%global exiv2_minver 0.27.4
%global gettext_minver 0.19.8
%global gexiv2_minver 0.14.0
%global glib_minver 2.70.0
%global gtk3_minver 3.24.0
%global gudev_minver 167
%global harfbuzz_minver 2.8.2
%global jpegxl_minver 0.7.0
%global json_glib_minver 1.2.6
%global lcms_minver 2.8
%global libheif_minver 1.15.1
%global liblzma_minver 5.0.0
%global libpng_minver 1.6.25
%global libmypaint_minver 1.5.0
%global libtiff_minver 4.0.0
%global libunwind_minver 1.1.0
%global lua_minver 5.4
%global openexr_minver 1.6.1
%global openjpeg_minver 2.1.0
%global pango_minver 1.50.0
%global perl_minver 5.10.0
%global poppler_minver 0.69.0
%global poppler_data_minver 0.4.9
%global python3_minver 3.6
%global pygobject_minver 3.0
%global rsvg_minver 2.40.6
%global webkit_minver 2.20.3
%global webp_minver 0.6.0
%global wmf_minver 0.2.8
%if %{with label_overlay}
%endif
%ifnarch %plain_lua_arches
%else
%endif
%if %{with libunwind}
%endif
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       babl%{?_isa} >= %babl_minver
Requires:       fontconfig%{?_isa} >= %fontconfig_minver
Requires:       freetype%{?_isa} >= %freetype2_minver
Requires:       gdk-pixbuf2%{?_isa} >= %gdk_pixbuf_minver
Requires:       gegl04%{?_isa} >= %gegl_minver
Requires:       gjs
Requires:       glib2%{?_isa} >= %glib_minver
Requires:       hicolor-icon-theme
Requires:       lcms2%{?_isa} >= %lcms_minver
%ifnarch %plain_lua_arches
Requires:       lua-lgi-compat
Requires:       luajit
%else
Requires:       lua >= %lua_minver
Requires:       lua-lgi
%endif
Requires:       pango%{?_isa} >= %pango_minver
Requires:       python3dist(pygobject) >= %pygobject_minver
Requires:       xdg-utils
Recommends:     mypaint2-brushes
Obsoletes:      gimp3 < %{version}-%{release}
Provides:       gimp3 = %{version}-%{release}
%if ! %defined snapshot
Source0:        https://download.%{name}.org/pub/%{name}/v3.2/%{name}-%{version}.tar.xz
%else
%endif
Patch1:         gimp-2.99.19-cm-system-monitor-profile-by-default.patch
Patch2:         gimp-2.99.19-no-phone-home-default.patch
Patch3:         gimp-2.99.19-external-help-browser.patch
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  aalib-devel
BuildRequires:  appdata-tools
BuildRequires:  appstream
BuildRequires:  cmake
BuildRequires:  coreutils
BuildRequires:  dbus-daemon
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gegl04-tools
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  gjs
BuildRequires:  glib-networking
BuildRequires:  glibc-langpack-en
BuildRequires:  libgs-devel
BuildRequires:  libxml2
BuildRequires:  libxslt
BuildRequires:  lua-lgi-compat
BuildRequires:  luajit
BuildRequires:  meson
BuildRequires:  perl
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(appstream)
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(babl-0.1)
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-pdf)
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gegl-0.4)
BuildRequires:  pkgconfig(gexiv2)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-no-export-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libjxl_threads)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libmng)
BuildRequires:  pkgconfig(libmypaint)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwebpdemux)
BuildRequires:  pkgconfig(libwebpmux)
BuildRequires:  pkgconfig(libwmf)
BuildRequires:  pkgconfig(mypaint-brushes-2.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(poppler-data)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3dist(pygobject)
BuildRequires:  vala
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  yelp-tools
# /oreon:deps
%description
GIMP (GNU Image Manipulation Program) is a powerful image composition and
editing program, which can be extremely useful for creating logos and other
graphics for web pages. GIMP has many of the tools and filters you would expect
to find in similar commercial offerings, and some interesting extras as well.
GIMP provides a large image manipulation toolbox, including channel operations
and layers, effects, sub-pixel imaging and anti-aliasing, and conversions, all
with multi-level undo.

%package libs
Summary:        GIMP libraries
License:        LGPL-3.0-or-later
Obsoletes:      gimp3-libs < %{version}-%{release}
Provides:       gimp3-libs = %{version}-%{release}
Requires:       babl%{?_isa} >= %babl_minver
Requires:       cairo%{?_isa} >= %cairo_minver
Requires:       fontconfig%{?_isa} >= %fontconfig_minver
Requires:       gdk-pixbuf2%{?_isa} >= %gdk_pixbuf_minver
Requires:       gegl04%{?_isa} >= %gegl_minver
Requires:       glib2%{?_isa} >= %glib_minver
Requires:       lcms2%{?_isa} >= %lcms_minver
Requires:       pango%{?_isa} >= %pango_minver
%description libs
The %{name}-libs package contains shared libraries needed for the GNU Image
Manipulation Program (GIMP).

%package devel
Summary:        GIMP plugin and extension development kit
License:        LGPL-3.0-or-later
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-devel-tools = %{epoch}:%{version}-%{release}
Obsoletes:      gimp3-devel < %{version}-%{release}
Provides:       gimp3-devel = %{version}-%{release}
%description devel
The %{name}-devel package contains the files needed for writing GNU Image
Manipulation Program (GIMP) plug-ins and extensions.

%package devel-tools
Summary:        GIMP plugin and extension development tools
License:        LGPL-3.0-or-later
Requires:       %{name}-devel = %{epoch}:%{version}-%{release}
Obsoletes:      gimp3-devel-tools < %{version}-%{release}
Provides:       gimp3-devel-tools = %{version}-%{release}
%description devel-tools
The %{name}-devel-tools package contains gimptool, a helper program to
build GNU Image Manipulation Program (GIMP) plug-ins and extensions.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
cat << EOF
--- 8< --- Build options ---------------------------------------------------
is default version: %{with is_default_version}
label overlay:      %{with label_overlay}
tests:              %{with tests}
%if %defined snapshot
snapshot:           %{snapshot}
plain_version:      %{plain_version}
git_rev:            %{git_rev}
%endif
--- >8 ---------------------------------------------------------------------
EOF

%setup -q -n gimp-%{plain_version}

%patch 1 -p1 -b .cm-system-monitor-profile-by-default
%patch 2 -p1 -b .no-phone-home-default
%patch 3 -p1 -b .external-help-browser

%build

%global _hardened_build 1
%meson \
%if %{with is_default_version}
    -Denable-default-bin=enabled \
%else
    -Denable-default-bin=disabled \
%endif
    -Dilbm=disabled \
    -Dbug-report-url="https://bugzilla.redhat.com/"
%meson_build
%install
%meson_install
gimp_pc_extract_normalize() {
    PKG_CONFIG_PATH="%{buildroot}%{_libdir}/pkgconfig" \
        pkg-config --variable="$1" gimp-%{lib_api_version} | \
    sed \
        -e 's|^%_mandir|%%{_mandir}|' \
        -e 's|^%_infodir|%%{_infodir}|' \
        -e 's|^%_includedir|%%{_includedir}|' \
        -e 's|^%_libdir|%%{_libdir}|' \
        -e 's|^%_localstatedir|%%{_localstatedir}|' \
        -e 's|^%_sharedstatedir|%%{_sharedstatedir}|' \
        -e 's|^%_sysconfdir|%%{_sysconfdir}|' \
        -e 's|^%_datadir|%%{_datadir}|' \
        -e 's|^%_libexecdir|%%{_libexecdir}|' \
        -e 's|^%_sbindir|%%{_sbindir}|' \
        -e 's|^%_bindir|%%{_bindir}|' \
        -e 's|^%_exec_prefix|%%{_exec_prefix}|' \
        -e 's|^%_prefix|%%{_prefix}|'
}
_gimp_datadir="$(gimp_pc_extract_normalize gimpdatadir)"
_gimp_libdir="$(gimp_pc_extract_normalize gimplibdir)"
_gimp_sysconfdir="$(gimp_pc_extract_normalize gimpsysconfdir)"
_gimp_localedir="$(gimp_pc_extract_normalize gimplocaledir)"
_gimp_scriptdir="${_gimp_datadir}/scripts"
_gimp_plugindir="${_gimp_libdir}/plug-ins"
cat << EOF > macros.gimp
%%_gimp_datadir ${_gimp_datadir}
%%_gimp_libdir ${_gimp_libdir}
%%_gimp_sysconfdir ${_gimp_sysconfdir}
%%_gimp_localedir ${_gimp_localedir}
%%_gimp_scriptdir ${_gimp_scriptdir}
%%_gimp_plugindir ${_gimp_plugindir}
EOF
install -D -m0644 macros.gimp %{buildroot}%{_rpmconfigdir}/macros.d/macros.gimp
echo "%{__python3}=%{__python3}" >> %{buildroot}%{_libdir}/gimp/%{api_version}/interpreters/pygimp.interp
echo "%{_bindir}/gimp-script-fu-interpreter-%{api_version}=%{_bindir}/gimp-script-fu-interpreter-%{api_version}" >> %{buildroot}%{_libdir}/gimp/%{api_version}/interpreters/gimp-script-fu-interpreter.interp
find %{buildroot}%{_libdir}/gimp/%{api_version} -type f | sed "s@^%{buildroot}@@g" | grep -v '\.a$' > gimp-plugin-files
find %{buildroot}%{_libdir}/gimp/%{api_version}/* -type d | sed "s@^%{buildroot}@%%dir @g" >> gimp-plugin-files
grep '\.py$' gimp-plugin-files | \
    sed 's+/[^/]*\.py$+/__pycache__+g' | \
    sort -u > gimp-plugin-files-pycache
cat gimp-plugin-files-pycache >> gimp-plugin-files
%py_byte_compile %{__python3} %{buildroot}%{_libdir}/gimp/%{api_version}
%find_lang gimp%{gettext_version}
%find_lang gimp%{gettext_version}-std-plug-ins
%find_lang gimp%{gettext_version}-script-fu
%find_lang gimp%{gettext_version}-libgimp
%find_lang gimp%{gettext_version}-python
cat gimp%{gettext_version}.lang gimp%{gettext_version}-std-plug-ins.lang gimp%{gettext_version}-script-fu.lang gimp%{gettext_version}-libgimp.lang gimp%{gettext_version}-python.lang > gimp-all.lang
cat gimp-plugin-files gimp-all.lang > gimp.files
%if %{with is_default_version}
ln -snf gimp-%{bin_version} %{buildroot}%{_bindir}/gimp
ln -snf gimp-%{bin_version}.1 %{buildroot}%{_mandir}/man1/gimp.1
ln -snf gimp-console-%{bin_version} %{buildroot}/%{_bindir}/gimp-console
ln -snf gimp-console-%{bin_version}.1 %{buildroot}/%{_mandir}/man1/gimp-console.1
ln -snf gimptool-%{bin_version} %{buildroot}%{_bindir}/gimptool
ln -snf gimptool-%{bin_version}.1 %{buildroot}%{_mandir}/man1/gimptool.1
ln -snf gimprc-%{bin_version}.5 %{buildroot}/%{_mandir}/man5/gimprc.5
%endif
grep -E -rl '^#!\s*/usr/bin/env\s+python' --include=\*.py "%{buildroot}" |
    while read file; do
        sed -r '1s,^#!\s*/usr/bin/env\s+python$,#!%{__python3},' -i "$file"
        sed -r '1s,^#!\s*/usr/bin/env\s+python3$,#!%{__python3},' -i "$file"
    done
grep -E -rl '^#!\s*/usr/bin/env\s+gimp-script-fu' --include=\*.scm "%{buildroot}" |
    while read file; do
        sed -r '1s,^#!\s*/usr/bin/env\s+(gimp-script-fu-interpreter.*)$,#!%{_bindir}/\1,' -i "$file"
    done
rm -rf devel-docs/gimp-%{api_version}
mv %{buildroot}%{_docdir}/gimp-%{api_version} devel-docs
rm -rf %{buildroot}%{_datadir}/gimp/%{api_version}/tests
%if %{without is_default_version}
rm -rf %{buildroot}%{_datadir}/metainfo
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%if %{with tests}
%check

skip_tests=""
%if %{with skip_networking_tests}
skip_tests="$skip_tests
%skip_tests_networking"
%endif
%if %{with skip_problematic_tests}
skip_tests="$skip_tests
%skip_tests_problematic"
%endif
%if %{with skip_user_tests}
skip_tests="$skip_tests
%skip_tests_user"
%endif
all_tests="$(%meson_test --list 2>/dev/null)"
suites="$(echo "$all_tests" | while read suite ignore; do echo "${suite%%+*}"; done | sort -u)"
for suite in $suites; do
    old_suite1="${suite%%:*}"
    old_suite2="${suite#*:}"
    suite_tests="$(
        echo "$all_tests" | grep "^$suite\(+\S\+\)\?" | while read ignore ignore test; do
            if [ "$suite" = "${suite/:/}" ]; then
                if ! echo "$skip_tests" | grep -qFx "$suite - $test"; then
                    echo "$test"
                fi
            else
                if ! echo "$skip_tests" | grep -qFx "$old_suite2 - $old_suite1:$test"; then
                    echo "$test"
                fi
            fi
        done | sort -u
    )"
    if [ -n "$suite_tests" ]; then
        %meson_test --suite "$suite" $suite_tests
    fi
done
%endif
%ldconfig_scriptlets libs
%files -f %{oreon_filedir}/main.list
%files -n gimp-libs -f %{oreon_filedir}/gimp-libs.list
%files -n gimp-devel -f %{oreon_filedir}/gimp-devel.list
%files -n gimp-devel-tools -f %{oreon_filedir}/gimp-devel-tools.list

%changelog

%autochangelog
