%global source0_hash c732ed02fcc395c0fb3867589d8253bddd98b69dd77e262465bb795686239540
%global _hardened_build 1
%global upstream_version 2.2.1
Name: libcupsfilters
Epoch: 1
Version: 2.2.1
Release:        1%{?dist}
Summary:        Library for developing printing filters
License: Apache-2.0 WITH LLVM-exception
URL: https://github.com/OpenPrinting/libcupsfilters
Source0:        https://github.com/OpenPrinting/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Obsoletes: cups-filters-libs < 2.0
Recommends: liberation-mono-fonts
Requires: colord
Requires: cups-filesystem
Requires: ghostscript >= 10.0.0
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dejavu-sans-fonts
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  ghostscript
BuildRequires:  git-core
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(cups)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libqpdf)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(poppler-cpp)
# /oreon:deps
%description
Libcupsfilters provides a library, which implements common functions used
in cups-browsed daemon and printing filters, and additional files
as banner templates and character sets. The filters are used in CUPS daemon
and in printer applications.

%package devel
Summary: Development files for libcupsfilters
Conflicts: cups-filters-devel{?_isa} < 2.0
Obsoletes: cups-filters-devel < 2.0
Provides: cups-filters-devel = %{epoch}:%{version}-%{release}
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%description devel
Development files for OpenPrinting cupsfilters library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git -n %{name}-%{upstream_version}

%build

./autogen.sh
%configure --disable-mutool\
 --disable-rpath\
 --disable-silent-rules\
 --disable-static\
 --enable-dbus\
 --with-cjk-fonts=droidsansfallback
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build
%check

make check
%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
mkdir -p %{buildroot}%{_pkgdocdir}/fontembed/
install -p -m 0644 cupsfilters/fontembed/README %{buildroot}%{_pkgdocdir}/fontembed/README
rm -f %{buildroot}%{_datadir}/cups/data/*.odt
rm -f %{buildroot}%{_pkgdocdir}/{INSTALL.md,ABOUT-NLS}
rm -f %{buildroot}%{_pkgdocdir}/{LICENSE,COPYING,NOTICE}
%{?ldconfig_scriptlets}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libcupsfilters-devel -f %{oreon_filedir}/libcupsfilters-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.1-7
- Prepare for Oreon 11 (RP1)
