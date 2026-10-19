%global source0_hash 629fa8cb0dfd9ad457c5bf47a42f0953b673e62c8ad6b1d03ddc4e2bd20008f1
Name:           liblouis
Version:        3.39.0
Release:        1%{?dist}
Summary:        Braille translation and back-translation library
License:        LGPL-2.1-or-later AND LGPL-2.0-or-later
URL:            https://liblouis.io
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Provides:       bundled(gnulib)
Requires:       %{name}-tables = %{version}-%{release}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-liblouis = %{version}-%{release}
# /oreon:deps
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
License:        LGPL-2.1-or-later AND LGPL-3.0-or-later
BuildArch:      noarch
%description    tables
Data tables for liblouis, containing attributes and dot patterns.

%package        utils
Summary:        Command-line utilities to test %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
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
License:        LGPL-3.0-or-later
%description doc
This package provides the documentation for liblouis.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup
chmod 664 tables/*

%build

%configure --disable-static --enable-ucs4
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool
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
install -pm 0644 liblouis/internal.h %{buildroot}%{_includedir}/%{name}
hardlink -t %{buildroot}%{_datadir}/%{name}/tables/
cd python
%pyproject_install
cd -
%oreon_autofiles python3-louis usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/*/lib*.so.*

%files
%files -n liblouis-devel -f %{oreon_filedir}/liblouis-devel.list
%files -n liblouis-tables -f %{oreon_filedir}/liblouis-tables.list
%files -n liblouis-utils -f %{oreon_filedir}/liblouis-utils.list
%files -n python3-louis -f %{oreon_filedir}/python3-louis.list
%files -n liblouis-doc -f %{oreon_filedir}/liblouis-doc.list

%changelog

%autochangelog
