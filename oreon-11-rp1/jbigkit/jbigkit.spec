# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 de7106b6bfaf495d6865c7dd7ac6ca1381bd12e0d81405ea81e7f2167263d932
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           jbigkit
Version:        2.1
Release:        33%{?dist}
Summary:        JBIG1 lossless image compression tools

License:        GPL-2.0-or-later
URL:            http://www.cl.cam.ac.uk/~mgk25/jbigkit/
Source0:        http://www.cl.cam.ac.uk/~mgk25/download/jbigkit-%{version}.tar.gz
Patch0:         jbigkit-2.1-shlib.patch
Patch1:         jbigkit-2.0-warnings.patch
# jbigkit: Partial Fedora build flags injection (bug #1548546)
Patch2:         jbigkit-ldflags.patch
# patch for coverity issues - backported from upstream
Patch3:         jbigkit-covscan.patch

# gcc is no longer in buildroot by default
# gcc needed for libjbig library and several filters - jbigtopbm, pbmtojbig e.g.
BuildRequires: gcc
# uses make
BuildRequires: make
# uses autosetup
BuildRequires: git-core

Requires:       jbigkit-libs%{?_isa} = %{version}-%{release}

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
%oreon_verify_sources
%autosetup -n jbigkit-2.1 -S git


%build
# get the correct redhat build flags
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

%check
make test

%ldconfig_scriptlets libs

%files
%{_bindir}/jbgtopbm
%{_bindir}/jbgtopbm85
%{_bindir}/pbmtojbg
%{_bindir}/pbmtojbg85
%{_mandir}/man1/jbgtopbm.1.gz
%{_mandir}/man1/pbmtojbg.1.gz
%license COPYING

%files libs
%{_libdir}/libjbig.so.2.1
%{_libdir}/libjbig85.so.2.1
%doc ANNOUNCE TODO CHANGES
%license COPYING

%files devel
%{_libdir}/libjbig.so
%{_libdir}/libjbig85.so
%{_includedir}/jbig*.h

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1-33
- Prepare for Oreon 11 (RP1)
