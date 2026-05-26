# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 5385bc1b8c2f20f3b91d258bf8ccc8cf62023935df2d2676b5b67049f31a049c
%global source1_sha256 5385bc1b8c2f20f3b91d258bf8ccc8cf62023935df2d2676b5b67049f31a049c
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })} \
%{?source1_sha256:%(test -z "%{source1_sha256}" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_sha256}" || { echo "oreon: Source1 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

# Recent so-version, so we do not bump accidentally.
%global so_ver      4

# Set to 1 when building a bootstrap for a bumped so-name.
%global bootstrap   0

%if 0%{?bootstrap}
%global version_old 4.1.1
%global so_ver_old  4
%endif


Name:           qrencode
Version:        4.1.1
Release:        12%{?dist}
Summary:        Generate QR 2D barcodes

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/fukuchi/libqrencode
# fukuchi.org upstream tarball is gone; GitHub tag archive unpacks as libqrencode-<version>/.
Source0:        https://github.com/fukuchi/libqrencode/archive/refs/tags/v%{version}/libqrencode-%{version}.tar.gz
%if 0%{?bootstrap}
Source1:        https://github.com/fukuchi/libqrencode/archive/refs/tags/v%{version_old}/libqrencode-%{version_old}.tar.gz
%endif

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  chrpath
BuildRequires:  libpng-devel
BuildRequires:  SDL-devel
## For ARM 64 support (RHBZ 926414)
BuildRequires:  autoconf >= 2.69
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gettext-devel

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
%oreon_verify_sources
%autosetup -n libqrencode-%{version} -p1

%if 0%{?bootstrap}
mkdir -p bootstrap_ver
pushd bootstrap_ver
tar --strip-components=1 -xf %{SOURCE1}
popd
%endif


%build
## GitHub tag archives ship autotools inputs only; regenerate full build system.
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


%check
pushd ./tests
sh test_all.sh
popd


%files
%{_bindir}/qrencode
%{_mandir}/man1/qrencode.1*


%files libs
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc ChangeLog NEWS README TODO
%{_libdir}/libqrencode.so.%{so_ver}*
%if 0%{?bootstrap}
%{_libdir}/libqrencode.so.%{so_ver_old}*
%endif


%files devel
%{_includedir}/qrencode.h
%{_libdir}/libqrencode.so
%{_libdir}/pkgconfig/libqrencode.pc


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.1.1-12
- Prepare for Oreon 11 (RP1)
