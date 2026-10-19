%global source0_hash d7bd2d29c1a87b85329547fb29a0eca52d944e60699982152775002e24c09228
%global apiver 2.6
%global so_version 1
%bcond autoreconf 1
%bcond doc_pdf 1
Name:           gconfmm26
Version:        2.28.3
Release:        1%{?dist}
Summary:        C++ wrapper for GConf2
License:        LGPL-2.1-or-later
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
Source0:        https://download.gnome.org/sources/gconfmm/%{majmin}/gconfmm-%{version}.tar.xz
Patch:          gconfmm26-2.28.3-no-extern-c-glib-includes.patch
%if %{with autoreconf}
%endif
%if %{with doc_pdf}
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  doxygen-latex
BuildRequires:  font(freesans)
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  mm-common
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(cairomm-1.0)
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(glibmm-2.4)
BuildRequires:  pkgconfig(mm-common-libstdc++)
BuildRequires:  pkgconfig(sigc++-2.0)
# /oreon:deps
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
find '%{buildroot}%{_docdir}/gconfmm-%{apiver}/reference/html' \
    -type f \( -name '*.js' -o -name '*.js.*' \) -print -delete
%if %{with doc_pdf}
install 'docs/reference/latex/refman.pdf' -p -m 0644 \
    '%{buildroot}%{_docdir}/gconfmm-%{apiver}/reference/gconfmm-%{apiver}.pdf'
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n gconfmm26-devel -f %{oreon_filedir}/gconfmm26-devel.list
%files -n gconfmm26-doc -f %{oreon_filedir}/gconfmm26-doc.list

%changelog

%autochangelog
