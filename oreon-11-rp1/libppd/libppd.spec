%global source0_hash b356aeed1335ef0ca7f799741782a2544e7acee63fb4b047b94e4e0395a9cb62
%global _hardened_build 1
%global upstream_version 2.1.1
%bcond_with tools
Name:           libppd
Epoch:          1
Version:        2.1.1
Release:        1%{?dist}
Summary:        Library for retro-fitting legacy printer drivers
License:        Apache-2.0 WITH LLVM-exception
URL:            https://github.com/OpenPrinting/libppd
Source0:        https://github.com/OpenPrinting/libppd/releases/download/2.1.1/libppd-2.1.1.tar.gz
%if %{without tools}
Requires: cups
%else
Requires: %{name}-tools%{?_isa} = %{epoch}:%{version}-%{release}
%endif
Requires: ghostscript >= 10.0.0
Requires: poppler-utils
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  ghostscript
BuildRequires:  git-core
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(cups)
BuildRequires:  pkgconfig(libcupsfilters)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  poppler-utils
# /oreon:deps
%description
Libppd provides all PPD related function/API which is going
to be removed from CUPS 3.X, but are still required for retro-fitting
support of legacy printers. The library is meant only for retro-fitting
printer applications, any new printer drivers have to be written as
native printer application without libppd.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       cups-devel
Requires:       libcupsfilters-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing retro-fitting printer applications.

%if %{with tools}
%package tools
Summary: PPD compiler tools and definition files
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%description tools
The package contains PPD compiler and definition files needed for generating
PPD files from *.drv files.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git -n %{name}-%{upstream_version}

%build

./autogen.sh
%configure\
  --disable-acroread\
  --disable-mutool\
  --disable-rpath\
  --disable-silent-rules\
  --disable-static\
%if %{with tools}
  --enable-ppdc-utils\
  --enable-testppdfile\
%else
  --disable-ppdc-utils\
  --disable-testppdfile\
%endif
  --with-pdftops=hybrid
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build
%check

make check
%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -f %{buildroot}%{_pkgdocdir}/{LICENSE,NOTICE,COPYING}
rm -f %{buildroot}%{_pkgdocdir}/INSTALL.md
rm -f %{buildroot}%{_pkgdocdir}/CHANGES-1.x.md
%if %{without tools}
rm -rf %{buildroot}%{_datadir}/ppdc
%endif
%{?ldconfig_scriptlets}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libppd-devel -f %{oreon_filedir}/libppd-devel.list
%files -n libppd-tools -f %{oreon_filedir}/libppd-tools.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.1-3
- Prepare for Oreon 11 (RP1)
