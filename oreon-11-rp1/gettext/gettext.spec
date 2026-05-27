%global source0_hash none

%bcond_with jar
%bcond_with java
# Disabled lto flags on i686 to avoid lto memory allocation error
%ifarch i686
%global _lto_cflags %{nil}
%endif

Summary: GNU tools and libraries for localized translated messages
Name: gettext
Version: 1.0
Release: 1%{?dist}

# The following are licensed under LGPLv2+:
# - libintl and its headers
# - libasprintf and its headers
# - libintl.jar
# - GNU.Gettext.dll
# - gettext.sh
# The following are licensed under GFDL:
# - gettext-tools/doc/FAQ.html
# - gettext-tools/doc/tutorial.html
# - gettext info files
# - libasprintf info files
# - libtextstyle info files
# Everything else is GPLv3+
License: GPL-3.0-or-later and LGPL-2.0-or-later and GFDL-1.2-or-later
URL: https://www.gnu.org/software/gettext/
Source: https://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.gz
Source2: msghack.py
Source3: msghack.1

# for bootstrapping
# BuildRequires: autoconf >= 2.62
BuildRequires: automake
BuildRequires: libtool
# BuildRequires: bison

BuildRequires: gcc-c++
%if %{with java}
# libintl.jar requires gcj >= 4.3 to build
BuildRequires: gcc-java, libgcj
# For javadoc
BuildRequires: java-1.6.0-openjdk-devel
%if %{with jar}
BuildRequires: %{_bindir}/fastjar
# require zip and unzip for brp-java-repack-jars
BuildRequires: zip, unzip
%endif
%endif
# for po-mode.el
BuildRequires: emacs
# ensure 'ARCHIVE_FORMAT=dirxz'
BuildRequires: xz
# for documentation
BuildRequires: teckit
BuildRequires: texlive-dvips
BuildRequires: texlive-dvipdfmx
BuildRequires: texinfo-tex
BuildRequires: texlive-xetex
# following suggested by DEPENDENCIES:
BuildRequires: ncurses-devel
BuildRequires: libxml2-devel
BuildRequires: glib2-devel
BuildRequires: libacl-devel
BuildRequires: libunistring-devel
# for the tests
BuildRequires: glibc-langpack-de
BuildRequires: glibc-langpack-en
BuildRequires: glibc-langpack-fa
BuildRequires: glibc-langpack-fr
BuildRequires: glibc-langpack-ja
BuildRequires: glibc-langpack-tr
BuildRequires: glibc-langpack-zh
BuildRequires: make
Provides: bundled(gnulib)
Requires: %{name}-runtime = %{version}-%{release}
Requires: libtextstyle%{?_isa} = %{version}-%{release}

%description
The GNU gettext package provides a set of tools and documentation for
producing multi-lingual messages in programs. Tools include a set of
conventions about how programs should be written to support message
catalogs, a directory and file naming organization for the message
catalogs, a runtime library which supports the retrieval of translated
messages, and stand-alone programs for handling the translatable and
the already translated strings. Gettext provides an easy to use
library and tools for creating, using, and modifying natural language
catalogs and is a powerful and simple method for internationalizing
programs.


%package runtime
Summary: GNU runtime libraries and programs for producing multi-lingual messages
License: GPL-3.0-or-later and LGPL-2.0-or-later
# Depend on the exact version of the library sub package
Requires: %{name}-libs%{_isa} = %{version}-%{release}
Requires: %{name}-envsubst = %{version}-%{release}
Conflicts: %{name} <= 0.21-15%{?dist}.0.20220203


%description runtime
The GNU gettext-runtime package provides an easy to use runtime libraries and
programs for creating, using, and modifying natural language catalogs
and is a powerful and simple method for internationalizing programs.


%package common-devel
Summary: Common development files for %{name}
# autopoint archive
License: GPL-3.0-or-later
BuildArch: noarch

%description common-devel
This package contains common architecture independent gettext development files.


%package devel
Summary: Development files for %{name}
# autopoint is GPLv3+
# libasprintf is LGPLv2+
# libgettextpo is GPLv3+
License: LGPL-2.0-or-later and GPL-3.0-or-later and GFDL-1.2-or-later
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libs = %{version}-%{release}
Requires: %{name}-common-devel = %{version}-%{release}
Requires: xz
Requires: diffutils
Obsoletes: gettext-autopoint < 0.18.1.1-3
Provides: gettext-autopoint = %{version}-%{release}

%description devel
This package contains all development related files necessary for
developing or compiling applications/libraries that needs
internationalization capability. You also need this package if you
want to add gettext support for your project.


%package libs
Summary: Libraries for %{name}
# libasprintf is LGPLv2+
# libgettextpo is GPLv3+
License: LGPL-2.0-or-later and GPL-3.0-or-later
Requires: libtextstyle%{?_isa} = %{version}-%{release}

%description libs
This package contains libraries used internationalization support.

%package -n libtextstyle
Summary: Text styling library
License: GPL-3.0-or-later

%description -n libtextstyle
Library for producing styled text to be displayed in a terminal
emulator.

%package -n libtextstyle-devel
Summary: Development files for libtextstyle
License: GPL-3.0-or-later and GFDL-1.2-or-later
Requires: libtextstyle%{?_isa} = %{version}-%{release}

%description -n libtextstyle-devel
This package contains all development related files necessary for
developing or compiling applications/libraries that needs text
styling.

%package -n emacs-%{name}
Summary: Support for editing po files within GNU Emacs
BuildArch: noarch
# help users find po-mode.el
Provides: emacs-po-mode
Requires: emacs(bin) >= %{?_emacs_version}%{!?_emacs_version:0}
Provides: emacs-%{name}-el = %{version}-%{release}
Obsoletes: emacs-%{name}-el < %{version}-%{release}

%description -n emacs-%{name}
This package provides a major mode for editing po files within GNU Emacs.

%package -n msghack
Summary: Alter PO files in ways
BuildArch: noarch

%description -n msghack
This program can be used to alter .po files in ways no sane mind would
think about.


%package envsubst
Summary: Substitutes the values of environment variables
Conflicts: %{name} <= 0.21-15%{?dist}.0.20220203

%description envsubst
Substitutes the values of environment variables.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q
autoreconf

# Defeat libtextstyle attempt to bundle libxml2.  The comments
# indicate this is done because the libtextstyle authors do not want
# applications using their code to suffer startup delays due to the
# relocations.  This is not a sufficient reason for Fedora.
sed -e 's/\(gl_cv_libxml_force_included=\)yes/\1no/' \
    -i libtextstyle/configure


%build
%if %{with java}
export JAVAC=gcj
%if %{with jar}
export JAR=fastjar
%endif
%endif
%ifarch ppc ppc64 ppc64le
# prevent test-isinf from failing with gcc-5.3.1 on ppc64le (#1294016)
export CFLAGS="$RPM_OPT_FLAGS -D__SUPPORT_SNAN__"
%endif
# Fedora's libxml2-devel package has an extra "libxml2" path component.
export CPPFLAGS="-I%{_includedir}/libxml2"
# Side effect of unbundling libxml2 from libtextstyle.
export LIBS="-lxml2"
export CFLAGS="$CFLAGS -Wformat"
%configure --enable-nls --disable-static \
    --enable-shared --disable-csharp --disable-rpath \
%if %{with java}
    --enable-java \
%else
    --disable-java --disable-native-java \
%endif
    --with-xz

# Eliminate hardcoded rpaths; workaround libtool reordering -Wl,--as-needed
# after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC=.g..|& -Wl,--as-needed|' \
    -i $(find . -name libtool)

%make_build %{?with_java:GCJFLAGS="-findirect-dispatch"}


%install
%make_install \
    lispdir=%{_datadir}/emacs/site-lisp/gettext \
    aclocaldir=%{_datadir}/aclocal EXAMPLESFILES=""


install -pm 755 %SOURCE2 ${RPM_BUILD_ROOT}%{_bindir}/msghack
install -pm 644 %SOURCE3 ${RPM_BUILD_ROOT}%{_mandir}/man1/msghack.1

# make preloadable_libintl.so executable
chmod 755 ${RPM_BUILD_ROOT}%{_libdir}/preloadable_libintl.so

rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir

# doc relocations
for i in gettext-runtime/man/*.html; do
  rm ${RPM_BUILD_ROOT}%{_datadir}/doc/gettext/`basename $i`
done
rm -r ${RPM_BUILD_ROOT}%{_datadir}/doc/gettext/javadoc*

rm -rf ${RPM_BUILD_ROOT}%{_datadir}/doc/gettext/examples

rm -rf htmldoc
mkdir htmldoc
mv ${RPM_BUILD_ROOT}%{_datadir}/doc/gettext/* ${RPM_BUILD_ROOT}%{_datadir}/doc/libasprintf/* htmldoc
rm -r ${RPM_BUILD_ROOT}%{_datadir}/doc/libasprintf
rm -r ${RPM_BUILD_ROOT}%{_datadir}/doc/gettext

## note libintl.jar does not build with gcj < 4.3
## since it would not be fully portable
%if %{with jar}
### this is no longer needed since examples not packaged
## set timestamp of examples ChangeLog timestamp for brp-java-repack-jars
#for i in `find ${RPM_BUILD_ROOT} examples -newer ChangeLog -type f -name ChangeLog`; do
#  touch -r ChangeLog  $i
#done
%else
# in case another java compiler is installed
rm -f ${RPM_BUILD_ROOT}%{_datadir}/%{name}/libintl.jar
%endif

rm -f ${RPM_BUILD_ROOT}%{_datadir}/%{name}/gettext.jar

# own this directory for third-party *.its files
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/its

# remove .la files
rm ${RPM_BUILD_ROOT}%{_libdir}/lib*.la

# remove internal .so lib files
rm ${RPM_BUILD_ROOT}%{_libdir}/libgettext{src,lib}.so

# move po-mode initialization elisp file to the right place, and remove byte
# compiled file
install -d ${RPM_BUILD_ROOT}%{_emacs_sitestartdir}
mv ${RPM_BUILD_ROOT}%{_emacs_sitelispdir}/%{name}/start-po.el ${RPM_BUILD_ROOT}%{_emacs_sitestartdir}
rm ${RPM_BUILD_ROOT}%{_emacs_sitelispdir}/%{name}/start-po.elc

%find_lang %{name}-runtime
%find_lang %{name}-tools


%check
# this takes quite a lot of time to run

# adapt to rpath removal
export LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}:$PWD/gettext-runtime/intl/.libs

# override LIBUNISTRING to prevent reordering of lib objects
make check LIBUNISTRING=-lunistring

%ldconfig_scriptlets libs

%files -f %{name}-tools.lang
%doc AUTHORS NEWS README THANKS
%doc gettext-tools/misc/disclaim-translations.txt
%doc gettext-tools/man/msg*.1.html
%doc gettext-tools/man/recode*.1.html
%doc gettext-tools/man/xgettext.1.html
%doc gettext-tools/man/po-fetch.1.html
%doc gettext-tools/man/spit.1.html
%doc gettext-tools/doc/FAQ.html
%doc gettext-tools/doc/tutorial.html
%{_bindir}/msgattrib
%{_bindir}/msgcat
%{_bindir}/msgcmp
%{_bindir}/msgcomm
%{_bindir}/msgconv
%{_bindir}/msgen
%{_bindir}/msgexec
%{_bindir}/msgfilter
%{_bindir}/msgfmt
%{_bindir}/msggrep
%{_bindir}/msginit
%{_bindir}/msgmerge
%{_bindir}/msgunfmt
%{_bindir}/msguniq
%{_bindir}/msgpre
%{_bindir}/po-fetch
%{_bindir}/spit
%{_bindir}/recode-sr-latin
%{_bindir}/xgettext
%{_infodir}/gettext*
%exclude %{_mandir}/man1/autopoint.1*
%exclude %{_mandir}/man1/envsubst.1*
%exclude %{_mandir}/man1/gettextize.1*
%exclude %{_mandir}/man1/msghack.1*
%{_mandir}/man1/msg*
%{_mandir}/man1/recode*.1*
%{_mandir}/man1/xgettext.1*
%{_mandir}/man1/po-fetch.1*
%{_mandir}/man1/spit.1*
%{_libdir}/%{name}
%if %{with java}
%exclude %{_libdir}/%{name}/gnu.gettext.*
%endif
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/its
%{_datadir}/%{name}/ABOUT-NLS
%{_datadir}/%{name}/po
%{_datadir}/%{name}/styles
%{_datadir}/%{name}/disclaim-translations.txt
%dir %{_datadir}/%{name}-%{version}
%{_datadir}/%{name}-%{version}/its
%dir %{_datadir}/%{name}/schema
%{_datadir}/%{name}/schema/its*.xsd*
%{_datadir}/%{name}/schema/locating-rules.xsd*
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/cldr-plurals
%{_libexecdir}/%{name}/hostname
%{_libexecdir}/%{name}/project-id
%{_libexecdir}/%{name}/urlget
%{_libexecdir}/%{name}/user-email

%files runtime -f %{name}-runtime.lang
%license COPYING
%doc gettext-runtime/BUGS
%doc gettext-runtime/man/gettext.1.html
%doc gettext-runtime/man/ngettext.1.html
%doc gettext-runtime/intl/COPYING*
%{_bindir}/gettext
%{_bindir}/gettext.sh
%{_bindir}/ngettext
%{_bindir}/printf_gettext
%{_bindir}/printf_ngettext
%exclude %{_mandir}/man1/autopoint.1*
%exclude %{_mandir}/man1/envsubst.1*
%exclude %{_mandir}/man1/gettextize.1*
%exclude %{_mandir}/man1/msg*
%exclude %{_mandir}/man1/recode-sr-latin.1*
%exclude %{_mandir}/man1/xgettext.1*
%{_mandir}/man1/*

%files envsubst
%license COPYING
%doc gettext-runtime/man/envsubst.1.html
%{_bindir}/envsubst
%{_mandir}/man1/envsubst.1*

%files common-devel
%{_datadir}/%{name}/archive.*.tar.xz

%files devel
%doc gettext-runtime/man/*.3.html ChangeLog
%doc gettext-tools/man/autopoint.1.html
%doc gettext-tools/man/gettextize.1.html
%{_bindir}/autopoint
%{_bindir}/gettextize
%{_datadir}/%{name}/projects/
%{_datadir}/%{name}/config.rpath
%{_datadir}/%{name}/*.h
%{_datadir}/%{name}/msgunfmt.tcl
%{_datadir}/%{name}/m4/*
%{_datadir}/aclocal/nls.m4
%{_includedir}/autosprintf.h
%{_includedir}/gettext-po.h
%{_infodir}/autosprintf*
%{_libdir}/libasprintf.so
%{_libdir}/libgettextpo.so
%{_libdir}/preloadable_libintl.so
%{_mandir}/man1/autopoint.1*
%{_mandir}/man1/gettextize.1*
%{_mandir}/man3/*
%{_datadir}/%{name}/javaversion.class
%doc gettext-runtime/intl-java/javadoc*
%if %{with java}
%{_libdir}/%{name}/gnu.gettext.*
%endif

%files libs
%{_libdir}/libasprintf.so.0*
%{_libdir}/libgettextpo.so.0*
%{_libdir}/libgettextlib-1.*.so
%{_libdir}/libgettextsrc-1.*.so
%if %{with jar}
%{_datadir}/%{name}/libintl.jar
%endif

%files -n libtextstyle
%{_libdir}/libtextstyle.so.0*

%files -n libtextstyle-devel
%{_docdir}/libtextstyle/
%{_includedir}/textstyle/
%{_includedir}/textstyle.h
%{_infodir}/libtextstyle*
%{_libdir}/libtextstyle.so

%files -n emacs-%{name}
%dir %{_emacs_sitelispdir}/%{name}
%{_emacs_sitelispdir}/%{name}/*.elc
%{_emacs_sitelispdir}/%{name}/*.el
%{_emacs_sitestartdir}/*.el

%files -n msghack
%license COPYING
%{_bindir}/msghack
%{_mandir}/man1/msghack.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0-1
- Prepare for Oreon 11 (RP1)
