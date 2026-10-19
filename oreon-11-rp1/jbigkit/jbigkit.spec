%global source0_hash de7106b6bfaf495d6865c7dd7ac6ca1381bd12e0d81405ea81e7f2167263d932
Name:           jbigkit
Version:        2.1
Release:        1%{?dist}
Summary:        JBIG1 lossless image compression tools
License:        GPL-2.0-or-later
URL:            http://www.cl.cam.ac.uk/~mgk25/jbigkit/
Source0:        http://www.cl.cam.ac.uk/~mgk25/download/jbigkit-%{version}.tar.gz
Patch0:         jbigkit-2.1-shlib.patch
Patch1:         jbigkit-2.0-warnings.patch
Patch2:         jbigkit-ldflags.patch
Patch3:         jbigkit-covscan.patch
Requires:       jbigkit-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  make
# /oreon:deps
%package libs
Summary:        JBIG1 lossless image compression library
%package devel
Summary:        JBIG1 lossless image compression library -- development files
Requires:       jbigkit-libs%{?_isa} = %{version}-%{release}
%description libs
JBIG-KIT provides a portable library of compression and decompression
functions with a documented interface that you can include very easily
into your image or document processing software. In addition, JBIG-KIT
provides ready-to-use compression and decompression programs with a
simple command line interface (similar to the converters found in netpbm).

JBIG-KIT implements the specification:
    ISO/IEC 11544:1993 and ITU-T Recommendation T.82(1993):
     Information technology — Coded representation of picture and audio
     information — Progressive bi-level image compression 

which is commonly referred to as the “JBIG1 standard”

%description devel
The jbigkit-devel package contains files needed for development using 
the JBIG-KIT image compression library.

%description
The jbigkit package contains tools for converting between PBM and JBIG1
formats.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir jbigkit-2.1
%oreon_prep
%build

%set_build_flags
%make_build
%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m0755 libjbig/libjbig.so.%{version} $RPM_BUILD_ROOT/%{_libdir}
install -p -m0755 libjbig/libjbig85.so.%{version} $RPM_BUILD_ROOT/%{_libdir}
ln -sf libjbig.so.%{version} $RPM_BUILD_ROOT/%{_libdir}/libjbig.so
ln -sf libjbig85.so.%{version} $RPM_BUILD_ROOT/%{_libdir}/libjbig85.so
install -p -m0644 libjbig/jbig.h $RPM_BUILD_ROOT%{_includedir}
install -p -m0644 libjbig/jbig85.h $RPM_BUILD_ROOT%{_includedir}
install -p -m0644 libjbig/jbig_ar.h $RPM_BUILD_ROOT%{_includedir}
install -p -m0755 pbmtools/???to??? $RPM_BUILD_ROOT%{_bindir}
install -p -m0755 pbmtools/???to???85 $RPM_BUILD_ROOT%{_bindir}
install -p -m0644 pbmtools/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make test
%ldconfig_scriptlets libs
%files -f %{oreon_filedir}/main.list
%files -n jbigkit-libs -f %{oreon_filedir}/jbigkit-libs.list
%files -n jbigkit-devel -f %{oreon_filedir}/jbigkit-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1-33
- Prepare for Oreon 11 (RP1)
