%global source0_hash d7bd2d29c1a87b85329547fb29a0eca52d944e60699982152775002e24c09228

%global apiver 2.6
%global so_version 1

%bcond autoreconf 1

# Doxygen HTML help is not suitable for packaging due to a minified JavaScript
# bundle inserted by Doxygen itself. See discussion at
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555.
#
# We can enable the Doxygen PDF documentation as a substitute.
#
# We still generate the HTML documentation, but strip out all the JavaScript
# that causes policy issues. This degrades it in the browser, but is sufficient
# to keep the Devhelp documentation working.
%bcond doc_pdf 1

Name:           gconfmm26
Version:        2.28.3
Release:        %autorelease
Summary:        C++ wrapper for GConf2

License:        LGPL-2.1-or-later
# Source files under other licenses belong to the build system or to unpackaged
# tools, and do not contribute to the license of the binary RPMs.
#
# FSFAP:
#   - INSTALL
#
# FSFAP AND GPL-2.0-or-later WITH Autoconf-exception-generic AND LGPL-2.1-or-later
#   - configure (LGPL-2.1-or-later is since it is based on configure.ac)
#
# FSFULLR AND LGPL-2.1-or-later:
#   (LGPL-2.1-or-later comes from the corresponding Makefile.am)
#   - Makefile.in
#   - docs/Makefile.in
#   - tools/Makefile.in
#   - gconf/gconfmm/Makefile.in
#   - gconf/src/Makefile.in
#
# FSFULLR AND GPL-2.0-or-later WITH Autoconf-exception-generic:
#   - aclocal.m4
#   - build/ltoptions.m4
#   - build/ltsugar.m4
#   - build/ltversion.m4
#   - build/lt~obsolete.m4
#
# FSFUL AND FSFULLR AND GPL-2.0-or-later WITH Libtool-exception:
#   - build/libtool.m4
#
# GPL-2.0-or-later:
#   - build/compile-binding.am
#   - build/doc-reference.am
#   - docs/doc-install.pl
#   - docs/doc-postprocess.pl
#   - docs/tagfile-to-devhelp2.xsl
#   - tools/extra_defs_gen/generate_defs_gconf.cc
#   - tools/m4/, possibly
#
# GPL-2.0-or-later WITH Autoconf-exception-generic:
#   - build/config.guess
#   - build/config.sub
#   - build/depcomp
#   - build/missing
#
# GPL-2.0-or-later WITH Libtool-exception:
#   - build/ltmain.sh
#
# X11:
#   - build/install-sh
#
# The autotools build system is complicated and pulls bits of scripts from many
# places, so don’t be surprised if some small detail is missing from this
# license analysis.
SourceLicense:  %{shrink:
                %{license} AND
                FSFAP AND
                FSFULLR AND
                GPL-2.0-or-later AND
                GPL-2.0-or-later WITH Autoconf-exception-generic AND
                GPL-2.0-or-later WITH Libtool-exception AND
                X11
                }
URL:            https://gtkmm.org/
%global majmin %(echo %{version} | cut -d . -f -2)
Source:         https://download.gnome.org/sources/gconfmm/%{majmin}/gconfmm-%{version}.tar.xz

# Do not wrap “#include <gconf/gconf-schema.h>” in “extern "C" {  }” to prevent
# “error: template with C linkage”
#
# See:
#   https://lists.fedoraproject.org/archives/list/
#     devel@lists.fedoraproject.org/thread/
#     J3P4TRHLWNDIKXF76OLYZNAPTABCZ3U5/#6QDPOFWECGRT42AQFD2IO6U33PN3K4GF
# as well as the discussion at:
#   https://gitlab.gnome.org/GNOME/glib/-/merge_requests/1935
#
# Note that gconfmm was archived in the migration to Gnome GitLab, and has been
# considered deprecated by upstream for ten years or so as of 2021, so there is
# no longer an upstream to receive such patches.
Patch:          gconfmm26-2.28.3-no-extern-c-glib-includes.patch

BuildRequires:  gcc-c++
BuildRequires:  make

%if %{with autoreconf}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  mm-common
%endif

BuildRequires:  pkgconfig(glibmm-2.4)
BuildRequires:  pkgconfig(gconf-2.0)

# For the documentation:
BuildRequires:  doxygen
BuildRequires:  perl-interpreter
BuildRequires:  perl(Getopt::Long)
# dot
BuildRequires:  graphviz
# xsltproc
BuildRequires:  libxslt
BuildRequires:  pkgconfig(mm-common-libstdc++)
BuildRequires:  pkgconfig(sigc++-2.0)
# Already a BR above:
#BuildRequires:  pkgconfig(glibmm-2.4)
BuildRequires:  pkgconfig(cairomm-1.0)
# Font specified for use in dot diagrams
BuildRequires:  font(freesans)
%if %{with doc_pdf}
BuildRequires:  doxygen-latex
BuildRequires:  make
%endif

%description
This package provides a C++ interface for GConf2. It is a sub-package of the
GTKmm project. The interface provides a convenient interface for C++
programmers to create Gnome GUIs with GTK+'s flexible object-oriented
framework.

%package devel
Summary:        Headers for developing programs that will use gconfmm

Requires:       gconfmm26%{?_isa} = %{version}-%{release}

Requires:       glibmm24-devel%{?_isa}
Requires:       GConf2-devel%{?_isa}

%description devel
This package contains the headers that programmers will need to develop
applications which will use gconfmm, part of GTKmm, the C++ interface to the
GTK+.

%package        doc
Summary:        Documentation for gconfmm26
BuildArch:      noarch

%description    doc
Documentation for gconfmm26 can be viewed through the devhelp documentation
browser.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n gconfmm-%{version} -p1

# We want to rebuild the documentation, so we remove the pre-built
# XML too. Note that we will still install the HTML documentation, since the
# devhelp XML requires it, but we will strip out the JavaScript, which will
# degrade the documentation in a web browser.
rm docs/reference/gconfmm-%{apiver}.devhelp2
rm docs/reference/gconfmm-%{apiver}.tag
rm -rf docs/reference/html
%if %{with doc_pdf}
# We enable the Doxygen PDF documentation as a substitute. We must
# enable GENERATE_LATEX and LATEX_BATCHMODE; the rest are precautionary and
# should already be set as we like them.
sed -r -i \
    -e "s/^([[:blank:]]*(GENERATE_LATEX|LATEX_BATCHMODE|USE_PDFLATEX|\
PDF_HYPERLINKS)[[:blank:]]*=[[:blank:]]*)NO[[:blank:]]*/\1YES/" \
    -e "s/^([[:blank:]]*(LATEX_TIMESTAMP)\
[[:blank:]]*=[[:blank:]]*)YES[[:blank:]]*/\1NO/" \
    docs/reference/Doxyfile.in
%endif

for fn in AUTHORS README
do
  iconv --from=ISO-8859-1 --to=UTF-8 "${fn}" > "${fn}.iconv"
  touch -r "${fn}" "${fn}.iconv"
  chmod -v --reference="${fn}" "${fn}.iconv"
  mv -f "${fn}.iconv" "${fn}"
done

%if %{with autoreconf}
# AC_PROG_LIBTOOL is obsolete
sed -r -i 's/AC_PROG_LIBTOOL/LT_INIT/' configure.ac
%endif

if [ "$(sha256sum -b < COPYING)" = "$(sha256sum -b < COPYING.LIB)" ]
then
  # The license files are identical; replace one with a symbolic link.
  ln -svf COPYING COPYING.LIB
fi

%conf
%if %{with autoreconf}
NOCONFIGURE=1 ./autogen.sh
%endif
%configure --enable-warnings=max

%build
%make_build

%if %{with doc_pdf}
%make_build -C 'docs/reference/latex'
%endif

%install
%make_install
find %{buildroot} -type f -name '*.la' -print -delete

install -t %{buildroot}%{_datadir}/doc/gconfmm-%{apiver} -m 0644 -p \
    AUTHORS ChangeLog NEWS README

# Strip out bundled and/or pre-minified JavaScript; this degrades the browser
# experience, but the HTML is still usable for devhelp.
find '%{buildroot}%{_docdir}/gconfmm-%{apiver}/reference/html' \
    -type f \( -name '*.js' -o -name '*.js.*' \) -print -delete
%if %{with doc_pdf}
install 'docs/reference/latex/refman.pdf' -p -m 0644 \
    '%{buildroot}%{_docdir}/gconfmm-%{apiver}/reference/gconfmm-%{apiver}.pdf'
%endif

%files
%license COPYING COPYING.LIB
%{_libdir}/libgconfmm-%{apiver}.so.%{so_version}{,.*}

%files devel
%{_includedir}/gconfmm-%{apiver}/
%{_libdir}/gconfmm-%{apiver}/
%{_libdir}/libgconfmm-%{apiver}.so
%{_libdir}/pkgconfig/gconfmm-%{apiver}.pc

%files doc
%license COPYING COPYING.LIB
# Note: JavaScript has been removed from HTML reference manual, degrading the
# browser experience. It is still needed for Devhelp support.
%doc %{_datadir}/doc/gconfmm-%{apiver}/
%doc %{_datadir}/devhelp/

%changelog
%autochangelog
