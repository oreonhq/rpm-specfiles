%global source0_hash 85d99b79c981a404874c02e0342176cf75c7698e2b51fe41031cf6526d974f1a
%bcond_with jar
%bcond_with java
%ifarch i686
%global _lto_cflags %{nil}
%endif
Summary:        GNU tools and libraries for localized translated messages
Name: gettext
Version: 1.0
Release:        1%{?dist}
License: GPL-3.0-or-later and LGPL-2.0-or-later and GFDL-1.2-or-later
URL: https://www.gnu.org/software/gettext/
Source0:        https://mirrors.kernel.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source2: msghack.py
Source3: msghack.1
%if %{with java}
%if %{with jar}
%endif
%endif
Provides: bundled(gnulib)
Requires: %{name}-runtime = %{version}-%{release}
Requires: libtextstyle%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  automake
BuildRequires:  emacs
BuildRequires:  gcc-c++
BuildRequires:  gcc-java
BuildRequires:  glib2-devel
BuildRequires:  glibc-langpack-de
BuildRequires:  glibc-langpack-en
BuildRequires:  glibc-langpack-fa
BuildRequires:  glibc-langpack-fr
BuildRequires:  glibc-langpack-ja
BuildRequires:  glibc-langpack-tr
BuildRequires:  glibc-langpack-zh
BuildRequires:  java-1.6.0-openjdk-devel
BuildRequires:  libacl-devel
BuildRequires:  libgcj
BuildRequires:  libtool
BuildRequires:  libunistring-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  teckit
BuildRequires:  texinfo-tex
BuildRequires:  texlive-dvipdfmx
BuildRequires:  texlive-dvips
BuildRequires:  texlive-xetex
BuildRequires:  xz
# /oreon:deps
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
Requires: %{name}-libs%{_isa} = %{version}-%{release}
Requires: %{name}-envsubst = %{version}-%{release}
Conflicts: %{name} <= 0.21-15%{?dist}.0.20220203
%description runtime
The GNU gettext-runtime package provides an easy to use runtime libraries and
programs for creating, using, and modifying natural language catalogs
and is a powerful and simple method for internationalizing programs.

%package common-devel
Summary: Common development files for %{name}
License: GPL-3.0-or-later
BuildArch: noarch
%description common-devel
This package contains common architecture independent gettext development files.

%package devel
Summary: Development files for %{name}
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
export CFLAGS="$RPM_OPT_FLAGS -D__SUPPORT_SNAN__"
%endif
export CPPFLAGS="-I%{_includedir}/libxml2"
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
chmod 755 ${RPM_BUILD_ROOT}%{_libdir}/preloadable_libintl.so
rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir
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
%if %{with jar}
%else
rm -f ${RPM_BUILD_ROOT}%{_datadir}/%{name}/libintl.jar
%endif
rm -f ${RPM_BUILD_ROOT}%{_datadir}/%{name}/gettext.jar
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/its
rm ${RPM_BUILD_ROOT}%{_libdir}/lib*.la
rm ${RPM_BUILD_ROOT}%{_libdir}/libgettext{src,lib}.so
install -d ${RPM_BUILD_ROOT}%{_emacs_sitestartdir}
mv ${RPM_BUILD_ROOT}%{_emacs_sitelispdir}/%{name}/start-po.el ${RPM_BUILD_ROOT}%{_emacs_sitestartdir}
rm ${RPM_BUILD_ROOT}%{_emacs_sitelispdir}/%{name}/start-po.elc
%find_lang %{name}-runtime
%find_lang %{name}-tools
%oreon_autofiles libtextstyle usr/*/lib*.so.*
%oreon_autofiles libtextstyle-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles msghack usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}:$PWD/gettext-runtime/intl/.libs
make check LIBUNISTRING=-lunistring
%ldconfig_scriptlets libs
%files -f %{oreon_filedir}/main.list
%files -n gettext-runtime -f %{oreon_filedir}/gettext-runtime.list
%files -n gettext-common-devel -f %{oreon_filedir}/gettext-common-devel.list
%files -n gettext-devel -f %{oreon_filedir}/gettext-devel.list
%files -n gettext-libs -f %{oreon_filedir}/gettext-libs.list
%files -n libtextstyle -f %{oreon_filedir}/libtextstyle.list
%files -n libtextstyle-devel -f %{oreon_filedir}/libtextstyle-devel.list
%files -n emacs-gettext -f %{oreon_filedir}/emacs-gettext.list
%files -n msghack -f %{oreon_filedir}/msghack.list
%files -n gettext-envsubst -f %{oreon_filedir}/gettext-envsubst.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0-1
- Prepare for Oreon 11 (RP1)
