%global source0_hash d1fb86e260cfe7da6031f94d2e44c0da55903dbae0a2fa0fae78c91ae1b56f00

%ifarch aarch64
%global mingw_build_win32 0
%endif

%{?mingw_package_header}

Name:      mingw-gettext
Version:   0.26
Release:   15%{?dist}
Summary:   GNU libraries and utilities for producing multi-lingual messages

License:   GPL-2.0-or-later AND LGPL-2.0-or-later
URL:       http://www.gnu.org/software/gettext/
Source0:        https://mirrors.kernel.org/gnu/gettext/gettext-%{version}.tar.xz

BuildArch: noarch

BuildRequires: make
%if 0%{?mingw_build_win32} == 1
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-binutils
BuildRequires: mingw32-win-iconv
BuildRequires: mingw32-termcap
%endif

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-binutils
BuildRequires: mingw64-win-iconv
BuildRequires: mingw64-termcap


%description
MinGW Windows Gettext library


%if 0%{?mingw_build_win32} == 1
# Win32
%package -n mingw32-gettext
Summary:         GNU libraries and utilities for producing multi-lingual messages

%description -n mingw32-gettext
MinGW Windows Gettext library

%package -n mingw32-gettext-static
Summary:        Static version of the MinGW Windows Gettext library
Requires:       mingw32-gettext = %{version}-%{release}

%description -n mingw32-gettext-static
Static version of the MinGW Windows Gettext library.
%endif

# Win64
%package -n mingw64-gettext
Summary:         GNU libraries and utilities for producing multi-lingual messages

%description -n mingw64-gettext
MinGW Windows Gettext library

%package -n mingw64-gettext-static
Summary:        Static version of the MinGW Windows Gettext library
Requires:       mingw64-gettext = %{version}-%{release}

%description -n mingw64-gettext-static
Static version of the MinGW Windows Gettext library.


%{?mingw_debug_package}


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n gettext-%{version}
python3 - <<'PY'
import pathlib, re
root = pathlib.Path(".")
pat_ns = re.compile(
    r"\} > config\.h && \\\n"
    r"\tif test -n \".*HAVE_GLOBAL_SYMBOL_PIPE.*\"; then \\\n"
    r"(?:.*\n)*?\tfi\n",
    re.M,
)
for rel in (
    "libtextstyle/lib/Makefile.in",
    "gettext-tools/libgettextpo/Makefile.in",
):
    p = root / rel
    t = p.read_text()
    n, c = pat_ns.subn("} > config.h\n", t, count=1)
    if c != 1:
        raise SystemExit(f"namespacing strip failed: {rel}")
    p.write_text(n)

nren = 0
for p in root.rglob("*"):
    if not p.is_file():
        continue
    if p.name != "error.c" and not p.name.endswith("-error.c"):
        continue
    p.rename(p.with_name(p.name[: -len("error.c")] + "errfn.c"))
    nren += 1
if nren < 7:
    raise SystemExit(f"error.c rename count low: {nren}")

pat_err = re.compile(r"(^|[^A-Za-z0-9])error\.(c|lo|o|obj|Tpo|Plo)\b", re.M)
nsub = 0
for p in root.rglob("Makefile.in"):
    t = p.read_text()
    nt, c = pat_err.subn(lambda m: m.group(1) + "errfn." + m.group(2), t)
    if c:
        p.write_text(nt)
        nsub += c
if nsub < 50:
    raise SystemExit(f"Makefile.in error rename subs low: {nsub}")

repls = [
    (
        "#define GLWTHREAD_ONCE_INIT { -1, 0, -1 }",
        "#define GLWTHREAD_ONCE_INIT { -1, 0, -1, {0} }",
    ),
    (
        "#define GLWTHREAD_MUTEX_INIT { GLWTHREAD_INITGUARD_INIT }",
        "#define GLWTHREAD_MUTEX_INIT { GLWTHREAD_INITGUARD_INIT, 0, {0} }",
    ),
    (
        "#define GLWTHREAD_RECMUTEX_INIT { GLWTHREAD_INITGUARD_INIT, 0, 0 }",
        "#define GLWTHREAD_RECMUTEX_INIT { GLWTHREAD_INITGUARD_INIT, 0, 0, {0} }",
    ),
    (
        "#define GLWTHREAD_RWLOCK_INIT { GLWTHREAD_INITGUARD_INIT }",
        "#define GLWTHREAD_RWLOCK_INIT { GLWTHREAD_INITGUARD_INIT, {0}, {0}, {0}, 0 }",
    ),
]
nh = 0
for name in (
    "windows-once.h",
    "windows-mutex.h",
    "windows-recmutex.h",
    "windows-rwlock.h",
):
    for p in root.rglob(name):
        t = p.read_text()
        nt = t
        for a, b in repls:
            if a in nt:
                nt = nt.replace(a, b)
        if nt != t:
            p.write_text(nt)
            nh += 1
if nh < 4:
    raise SystemExit(f"windows INIT header patch count low: {nh}")
PY

%build
%mingw_configure            \
    --disable-java          \
    --disable-native-java   \
    --disable-csharp        \
    --enable-static         \
    --enable-threads=win32  \
    --without-emacs         \
    --disable-openmp        \
    --disable-dependency-tracking \
    --disable-namespacing   \
    lt_cv_to_host_file_cmd=func_convert_file_noop \
    lt_cv_to_tool_file_cmd=func_convert_file_noop \
    gl_cv_warn_c__fanalyzer=no \
    gl_cv_warn_cxx__fanalyzer=no
find build_win* -name Makefile -print0 2>/dev/null | xargs -0 -r sed -i \
    -e 's/ -fanalyzer//g' \
    -e 's/ -Wno-error/ -Wno-missing-field-initializers -Wno-error/g'
%mingw_make_build


%install
%mingw_make_install

%if 0%{?mingw_build_win32} == 1
rm -f %{buildroot}%{mingw32_datadir}/locale/locale.alias
rm -f %{buildroot}%{mingw32_libdir}/charset.alias

rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw32_docdir}
rm -rf %{buildroot}%{mingw32_infodir}

rm -rf %{buildroot}%{mingw32_libdir}/gettext

rm -f %{buildroot}%{mingw32_libdir}/libgettextlib.a
rm -f %{buildroot}%{mingw32_libdir}/libgettextsrc.a

rm -f %{buildroot}%{mingw32_datadir}/gettext/javaversion.class
%endif

rm -f %{buildroot}%{mingw64_datadir}/locale/locale.alias
rm -f %{buildroot}%{mingw64_libdir}/charset.alias

rm -rf %{buildroot}%{mingw64_mandir}
rm -rf %{buildroot}%{mingw64_docdir}
rm -rf %{buildroot}%{mingw64_infodir}

rm -rf %{buildroot}%{mingw64_libdir}/gettext

find %{buildroot} -name "*.la" -delete
rm -f %{buildroot}%{mingw64_libdir}/libgettextlib.a
rm -f %{buildroot}%{mingw64_libdir}/libgettextsrc.a

rm -f %{buildroot}%{mingw64_datadir}/gettext/javaversion.class

%mingw_find_lang %{name} --all-name


%if 0%{?mingw_build_win32} == 1
# Win32
%files -n mingw32-gettext -f mingw32-%{name}.lang
%license COPYING
%{mingw32_bindir}/autopoint
%{mingw32_bindir}/envsubst.exe
%{mingw32_bindir}/gettext.exe
%{mingw32_bindir}/gettext.sh
%{mingw32_bindir}/gettextize
%{mingw32_bindir}/libasprintf-0.dll
%{mingw32_bindir}/libgettextlib-0-26.dll
%{mingw32_bindir}/libgettextpo-0.dll
%{mingw32_bindir}/libgettextsrc-0-26.dll
%{mingw32_bindir}/libintl-8.dll
%{mingw32_bindir}/libtextstyle-0.dll
%{mingw32_bindir}/msg*.exe
%{mingw32_bindir}/ngettext.exe
%{mingw32_bindir}/printf_gettext.exe
%{mingw32_bindir}/printf_ngettext.exe
%{mingw32_bindir}/recode-sr-latin.exe
%{mingw32_bindir}/xgettext.exe
%{mingw32_includedir}/autosprintf.h
%{mingw32_includedir}/gettext-po.h
%{mingw32_includedir}/libintl.h
%{mingw32_includedir}/textstyle.h
%{mingw32_includedir}/textstyle/stdbool.h
%{mingw32_includedir}/textstyle/version.h
%{mingw32_includedir}/textstyle/woe32dll.h
%{mingw32_libdir}/libasprintf.dll.a
%{mingw32_libdir}/libgettextlib.dll.a
%{mingw32_libdir}/libgettextpo.dll.a
%{mingw32_libdir}/libgettextsrc.dll.a
%{mingw32_libdir}/libintl.dll.a
%{mingw32_libdir}/libtextstyle.dll.a
%dir %{mingw32_libexecdir}/gettext/
%{mingw32_libexecdir}/gettext/cldr-plurals.exe
%{mingw32_libexecdir}/gettext/hostname.exe
%{mingw32_libexecdir}/gettext/project-id
%{mingw32_libexecdir}/gettext/urlget.exe
%{mingw32_libexecdir}/gettext/user-email
%{mingw32_datadir}/gettext/
%{mingw32_datadir}/gettext-%{version}/
%{mingw32_datadir}/aclocal/nls.m4

%files -n mingw32-gettext-static
%{mingw32_libdir}/libasprintf.a
%{mingw32_libdir}/libgettextpo.a
%{mingw32_libdir}/libintl.a
%{mingw32_libdir}/libtextstyle.a

%endif

# Win64
%files -n mingw64-gettext -f mingw64-%{name}.lang
%license COPYING
%{mingw64_bindir}/autopoint
%{mingw64_bindir}/envsubst.exe
%{mingw64_bindir}/gettext.exe
%{mingw64_bindir}/gettext.sh
%{mingw64_bindir}/gettextize
%{mingw64_bindir}/libasprintf-0.dll
%{mingw64_bindir}/libgettextlib-0-26.dll
%{mingw64_bindir}/libgettextpo-0.dll
%{mingw64_bindir}/libgettextsrc-0-26.dll
%{mingw64_bindir}/libintl-8.dll
%{mingw64_bindir}/libtextstyle-0.dll
%{mingw64_bindir}/msg*.exe
%{mingw64_bindir}/ngettext.exe
%{mingw64_bindir}/printf_gettext.exe
%{mingw64_bindir}/printf_ngettext.exe
%{mingw64_bindir}/recode-sr-latin.exe
%{mingw64_bindir}/xgettext.exe
%{mingw64_includedir}/autosprintf.h
%{mingw64_includedir}/gettext-po.h
%{mingw64_includedir}/libintl.h
%{mingw64_includedir}/textstyle.h
%{mingw64_includedir}/textstyle/stdbool.h
%{mingw64_includedir}/textstyle/version.h
%{mingw64_includedir}/textstyle/woe32dll.h
%{mingw64_libdir}/libasprintf.dll.a
%{mingw64_libdir}/libgettextlib.dll.a
%{mingw64_libdir}/libgettextpo.dll.a
%{mingw64_libdir}/libgettextsrc.dll.a
%{mingw64_libdir}/libintl.dll.a
%{mingw64_libdir}/libtextstyle.dll.a
%dir %{mingw64_libexecdir}/gettext/
%{mingw64_libexecdir}/gettext/cldr-plurals.exe
%{mingw64_libexecdir}/gettext/hostname.exe
%{mingw64_libexecdir}/gettext/project-id
%{mingw64_libexecdir}/gettext/urlget.exe
%{mingw64_libexecdir}/gettext/user-email
%{mingw64_datadir}/gettext/
%{mingw64_datadir}/gettext-%{version}/
%{mingw64_datadir}/aclocal/nls.m4

%files -n mingw64-gettext-static
%{mingw64_libdir}/libasprintf.a
%{mingw64_libdir}/libgettextpo.a
%{mingw64_libdir}/libintl.a
%{mingw64_libdir}/libtextstyle.a


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.26-2
- Import
