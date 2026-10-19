%global source2_hash 8a04221acae72861c2e8a69ab0a0361352f3a7ac1ab7c313cdd1b718f8310ccb
%global source1_hash a057763ad1c8d8433c605b8e63a1f91e8f43aed99ad5696fb790276e451735e2
%global source0_hash be8248a17dedd6ccbaab2fcc45835bb0502d062e40fbded3bc56028ce5eb7acc
%define _lto_cflags %{nil}
Name:		potrace
Version:	1.16
Release:        1%{?dist}
Summary:        Transform bitmaps into vector graphics
License:	GPL-2.0-or-later AND LGPL-2.0-or-later
URL:		http://potrace.sourceforge.net
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:	https://potrace.sourceforge.net/potrace.pdf
Source2:	https://potrace.sourceforge.net/potracelib.pdf
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
%description
Potrace is a utility for tracing a bitmap, which means, transforming a bitmap 
into a smooth, scalable image. The input is a bitmap (PBM, PGM, PPM, or BMP
format), and the default output is an encapsulated PostScript file (EPS).
A typical use is to create EPS files from scanned data, such as company or
university logos, handwritten notes, etc. The resulting image is not "jaggy"
like a bitmap, but smooth. It can then be rendered at any resolution.

Potrace can currently produce the following output formats: EPS, PostScript,
PDF, SVG (scalable vector graphics), Xfig, Gimppath, and PGM (for easy
antialiasing). Additional backends might be added in the future.

Mkbitmap is a program distributed with Potrace which can be used to pre-process
the input for better tracing behavior on greyscale and color images.

%package devel
Summary:	Potrace development library and headers
Requires:	%{name} = %{version}-%{release}
%description devel
This package contains the potrace development library and headers.

%package doc
Summary:	Documentation on how to use the potrace library
%description doc
This package contains documentation for the potrace algorithm and the potrace
library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
cp -a %{SOURCE1} .
cp -a %{SOURCE2} .

%build

%set_build_flags
./configure --build=%{_build} --host=%{_host} --prefix=%{_prefix} --exec-prefix=%{_exec_prefix} --bindir=%{_bindir} --sbindir=%{_sbindir} --sysconfdir=%{_sysconfdir} --datadir=%{_datadir} --includedir=%{_includedir} --libdir=%{_libdir} --libexecdir=%{_libexecdir} --localstatedir=%{_localstatedir} --runstatedir=%{_runstatedir} --sharedstatedir=%{_sharedstatedir} --mandir=%{_mandir} --infodir=%{_infodir} --disable-dependency-tracking --enable-shared --disable-static --enable-metric --with-libpotrace=yes --with-pic
%{__make} %{?_smp_mflags} -j${RPM_BUILD_NCPUS} %{?_make_verbose}
%install
rm -rf %{buildroot}
%make_install
find %{buildroot} -name *.la -exec rm -rf {} \;
rm -rf %{buildroot}%{_docdir}/%{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n potrace-devel -f %{oreon_filedir}/potrace-devel.list
%files -n potrace-doc -f %{oreon_filedir}/potrace-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.16-16
- Prepare for Oreon 11 (RP1)
