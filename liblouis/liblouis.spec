Name:           liblouis
Version:        3.33.0
Release:        7%{?dist}
Summary:        Braille translation and back-translation library

# LGPL-2.1-or-later: the project as a whole
# LGPL-2.0-or-later: parts of gnulib
# - gnulib/_Noreturn.h
# - gnulib/arg-nonnull.h
# - gnulib/c++defs.h
# - gnulib/warn-on-use.h
License:        LGPL-2.1-or-later AND LGPL-2.0-or-later
URL:            https://liblouis.io
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  hardlink
BuildRequires:  help2man
BuildRequires:  libyaml-devel
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
BuildRequires:  texlive-eurosym
BuildRequires:  texlive-xetex
BuildRequires:  python3-devel

Provides:       bundled(gnulib)

Requires:       %{name}-tables = %{version}-%{release}

%description
Liblouis is an open-source braille translator and back-translator named in
honor of Louis Braille. It features support for computer and literary braille,
supports contracted and uncontracted translation for many languages and has
support for hyphenation. New languages can easily be added through tables that
support a rule- or dictionary based approach. Liblouis also supports math
braille (Nemeth and Marburg).

Liblouis has features to support screen-reading programs. This has led to its
use in two open-source screen readers, NVDA and Orca. It is also used in some
commercial assistive technology applications for example by ViewPlus.

Liblouis is based on the translation routines in the BRLTTY screen reader for
Linux. It has, however, gone far beyond these routines.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
License:        LGPL-2.1-or-later

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        tables
Summary:        Data tables
# LGPL-2.1-or-later: most of the tables
# LGPL-3.0-or-later:
# - tables/Es-Es-G0.utb
# - tables/et-g0.utb
# - tables/is-chardefs6.cti
# - tables/is-chardefs8.cti
# - tables/pt-pt-g2.ctb
# - tables/sr-chardefs.cti
# - tables/sr-g1.ctb
License:        LGPL-2.1-or-later AND LGPL-3.0-or-later
BuildArch:      noarch

%description    tables
Data tables for liblouis, containing attributes and dot patterns.


%package        utils
Summary:        Command-line utilities to test %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# GPL-3.0-or-later: the source code in tools
# LGPL-2.0-or-later AND LGPL-2.1-or-later: tools/gnulib
# LGPL-3.0-or-later: tools/gnulib/version-etc.{c,h}
# LGPL-3.0-or-later OR GPL-2.0-or-later:
# - tools/gnulib/unistr/u16-mbtoucr.c
# - tools/gnulib/unistr/u16-to-u8.c
License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-2.0-or-later AND (LGPL-3.0-or-later OR GPL-2.0-or-later)

%description    utils
Six test programs are provided as part of the liblouis package. They
are intended for testing liblouis and for debugging tables. None of
them is suitable for braille transcription.


%package -n python3-louis
Summary:        Python 3 language bindings for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
License:        LGPL-2.1-or-later

%description -n python3-louis
This package provides Python 3 language bindings for %{name}.


%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
# See doc/liblouis.texi
License:        LGPL-3.0-or-later

%description doc
This package provides the documentation for liblouis.


%prep
%autosetup
chmod 664 tables/*


%generate_buildrequires
cd python
%pyproject_buildrequires


%build
%configure --disable-static --enable-ucs4

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

# parallel builds fail
%if 0%{?rhel}
LD_LIBRARY_PATH=$PWD/liblouis/.libs \
%endif
make
cd doc; xetex %{name}.texi
cd ../python
%pyproject_wheel


%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} make check


%install
%make_install
rm -f %{buildroot}/%{_infodir}/dir
rm -f %{buildroot}/%{_libdir}/%{name}.la
rm -rf %{buildroot}/%{_bindir}/lou_maketable*
rm -rf %{buildroot}/%{_defaultdocdir}/%{name}/

# Install internal.h for MuseScore
install -pm 0644 liblouis/internal.h %{buildroot}%{_includedir}/%{name}

# Hardlink table files with identical content
hardlink -t %{buildroot}%{_datadir}/%{name}/tables/

cd python
%pyproject_install
%pyproject_save_files louis
cd -


%files
%doc README AUTHORS NEWS ChangeLog TODO
%license COPYING.LESSER
%{_libdir}/%{name}.so.*
%{_infodir}/%{name}.info*

%files devel
%doc HACKING
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{name}.so

%files tables
%{_datadir}/%{name}/

%files utils
%license COPYING
%{_bindir}/lou_*
%{_mandir}/man1/lou_*.1*

%files -n python3-louis -f %{pyproject_files}

%files doc
%doc doc/%{name}.{html,txt,pdf}


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.33.0-7
- Prepare for Oreon 11 (RP1)
