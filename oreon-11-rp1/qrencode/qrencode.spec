%global source0_hash 5385bc1b8c2f20f3b91d258bf8ccc8cf62023935df2d2676b5b67049f31a049c
%global source1_hash 5385bc1b8c2f20f3b91d258bf8ccc8cf62023935df2d2676b5b67049f31a049c
%global so_ver      4
%global bootstrap   0
%if 0%{?bootstrap}
%global version_old 4.1.1
%global so_ver_old  4
%endif
Name:           qrencode
Version:        4.1.1
Release:        12%{?dist}
Summary:        Generate QR 2D barcodes
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/fukuchi/libqrencode
Source0:        https://github.com/fukuchi/libqrencode/archive/v%{version}/libqrencode-%{version}.tar.gz
%if 0%{?bootstrap}
Source1:        https://github.com/fukuchi/libqrencode/archive/v%{version_old}/libqrencode-%{version_old}.tar.gz
%endif
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  chrpath
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
Qrencode is a utility software using libqrencode to encode string data in
a QR Code and save as a PNG image.

%package        devel
Summary:        QR Code encoding library - Development files
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    devel
The qrencode-devel package contains libraries and header files for developing
applications that use qrencode.

%package        libs
Summary:        QR Code encoding library - Shared libraries
%description    libs
The qrencode-libs package contains the shared libraries and header files for
applications that use qrencode.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{ print $1 }'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{ print $1 }'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%autosetup -n libqrencode-%{version} -p1

%if 0%{?bootstrap}
mkdir -p bootstrap_ver
pushd bootstrap_ver
tar --strip-components=1 -xf %{SOURCE1}
popd
%endif

%build

autoreconf -fi
%configure --with-tests
%make_build
%if 0%{?bootstrap}
pushd bootstrap_ver
autoreconf -fi
%configure --with-tests
%make_build
popd
%endif
%install
%if 0%{?bootstrap}
%make_install -C bootstrap_ver
%{_bindir}/find %{buildroot} -xtype f -not            \
  -name 'lib%{name}.so.%{so_ver_old}*' -delete -print
%{_bindir}/find %{buildroot} -type l -not             \
  -name 'lib%{name}.so.%{so_ver_old}*' -delete -print
%endif
%make_install
rm -f %{buildroot}%{_libdir}/libqrencode.la
chrpath --delete %{buildroot}%{_bindir}/qrencode
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd ./tests
sh test_all.sh
popd
%files -f %{oreon_filedir}/main.list
%files -n qrencode-devel -f %{oreon_filedir}/qrencode-devel.list
%files -n qrencode-libs -f %{oreon_filedir}/qrencode-libs.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.1.1-12
- Prepare for Oreon 11 (RP1)
