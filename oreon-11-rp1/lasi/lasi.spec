%global source0_hash 5e5d2306f7d5a275949fb8f15e6d79087371e2a1caa0d8f00585029d1b47ba3b

%undefine __cmake_in_source_build

Name:           lasi
Version:        1.1.3
Release:        18%{?dist}
Summary:        C++ library for creating Postscript documents

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.unifont.org/lasi/
Source0:        http://downloads.sourceforge.net/lasi/libLASi-%{version}.tar.gz
Patch0:         lasi-multilib.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.13.2
BuildRequires:  pango-devel
BuildRequires:  doxygen
# Build fails with this
#BuildRequires:  inkscape
# For testing
BuildRequires:  dejavu-sans-mono-fonts

%description
LASi is a library written by Larry Siden  that provides a C++ stream output
interface ( with operator << ) for creating Postscript documents that can
contain characters from any of the scripts and symbol blocks supported in
Unicode  and by Owen Taylor's Pango layout engine. The library accommodates
right-to-left scripts such as Arabic and Hebrew as easily as left-to-right
scripts. Indic and Indic-derived Complex Text Layout (CTL) scripts, such as
Devanagari, Thai, Lao, and Tibetan are supported to the extent provided by
Pango and by the OpenType fonts installed on your system. All of this is
provided without need for any special configuration or layout calculation on
the programmer's part.

Although the capability to produce Unicode-based multilingual Postscript
documents exists in large Open Source application framework libraries such as
GTK+, QT, and KDE, LASi was designed for projects which require the ability
to produce Postscript independent of any one application framework.

%package        devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pango-devel

%description    devel
%{summary}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n libLASi-%{version}
%patch -P0 -p1 -b .multilib
# Change docdir
sed -i -e '/set(docdir/s| .*| %{_pkgdocdir}|' cmake/modules/instdirs.cmake

%build
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS -std=c++14"
export FFLAGS="$RPM_OPT_FLAGS"
%cmake -DUSE_RPATH=OFF -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%cmake_build

%install
%cmake_install

%check
%ctest --verbose

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog.release COPYING README
%{_libdir}/libLASi.so.2*

%files devel
%{_includedir}/LASi.h
%{_libdir}/libLASi.so
%{_libdir}/pkgconfig/lasi.pc
%doc %{_datadir}/lasi%{version}/

%files doc
%{_pkgdocdir}/html/

%changelog
%autochangelog
