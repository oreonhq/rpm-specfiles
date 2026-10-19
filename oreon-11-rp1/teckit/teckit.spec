%global source1_hash e4a5f9b2a6ac72f0e695801fddff1c30a1b8b2a57cf72d8b661805ee2b5cd8f2
%global source0_hash 3f55cd3670f1ff1a439d5a40071870b9e4ca2be8877a0eb80e24783cb532b380
%global source2_key_fpr 15D41BC02EB807D405EFFAF6C9183BEA0288CDEE
Name:           teckit
Version:        2.5.13
Release:        2%{?dist}
Summary:        Encoding conversion library and mapping compiler
License:        (LGPL-2.1-or-later OR CPL-1.0) AND (LGPL-2.1-or-later OR GPL-2.0-or-later OR MPL-2.0)
SourceLicense:  %{license} AND LGPL-2.0-or-later AND GPL-2.0-or-later AND GPL-2.0-or-later WITH Autoconf-exception-generic AND Unicode-3.0 AND (MPL-1.1 OR GPL-1.0-or-later) AND NPL-1.1 AND GPL-2.0-or-later WITH GNAT-exception AND Zlib AND BSL-1.0
URL:            https://software.sil.org/teckit/
Source0:        https://github.com/silnrsi/teckit/releases/download/v%{version}/teckit-%{version}.tar.xz
Source1:        https://github.com/silnrsi/teckit/releases/download/v%{version}/teckit-%{version}.tar.xz.asc
Source2:        gpgkey-15D41BC02EB807D405EFFAF6C9183BEA0288CDEE.gpg
Source3:        repackage.sh
Provides:       bundels(graphite2)
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  expat-devel
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  gpgverify
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-interpreter
BuildRequires:  zlib-devel
# /oreon:deps
%description
TECkit is a low-level toolkit intended to be used by other applications that
need to perform encoding conversions (e.g., when importing legacy data into
a Unicode-based application). The primary component of the TECkit package is
therefore a library that performs conversions; this is the "TECkit engine".
The engine relies on mapping tables in a specific binary format (for which
documentation is available); there is a compiler that creates such tables from
a human-readable mapping description (a simple text file).

%package devel
Summary:        Developmental files for TECkit library
License:        LGPL-2.1-or-later OR CPL-1.0
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Header files, pkg-config module, and documentation for developing application
that use TECkit, a character encoding and mapping, library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" 2>/dev/null | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; }
%gpgverify -k2 -s1 -d0
_repack=%{_builddir}/teckit-%{version}_repackaged.tar.xz
cp -p %{SOURCE0} teckit-%{version}.tar.xz
cp %{SOURCE3} .
bash repackage.sh %{version}
test -f "$_repack" || { echo "teckit repackage failed: $_repack missing" >&2; exit 1; }
%setup -q -c -T -D -n teckit-%{version}_repackaged
tar xJf "$_repack" --strip-components=1
# Remove bundled libraries
rm -r zlib-*/*.{c,h} SFconv/expat
# Remove pre-build executables
rm -r perl_binaries

%build

autoreconf -fi
%configure \
    --disable-debug \
    --disable-final \
    --without-old-lib-names \
    --disable-profile \
    --disable-profilefn \
    --enable-shared \
    --disable-static \
    --with-system-zlib \
    --disable-tetex-build
%{make_build}
%install
%{make_install}
rm -f %{buildroot}%{_libdir}/*.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%{make_build} check
%files -f %{oreon_filedir}/main.list
%files -n teckit-devel -f %{oreon_filedir}/teckit-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.5.13-2
- Import
