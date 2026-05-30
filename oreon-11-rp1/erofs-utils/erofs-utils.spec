%global source0_hash a9ef5ab67c4b8d2d3e9ed71f39cd008bda653142a720d8a395a36f1110d0c432

%bcond curl     1
%bcond deflate  %[ 0%{?fedora} >= 34 || 0%{?rhel} >=  8 ]
%bcond fuse     1
%bcond jsonc    1
%bcond libnl3   1
%bcond libxml2  1
%bcond lz4      %[ 0%{?fedora} >= 34 || 0%{?rhel} >=  9 ]
%bcond lzma     %[ 0%{?fedora} >= 36 || 0%{?rhel} >= 10 ]
%bcond oci      %[ %{with curl} && %{with jsonc} ]
%bcond openssl  1
%bcond qpl      %[ 0%{?fedora} >= 41 && "%{_arch}" == "x86_64" ]
%bcond s3       %[ %{with curl} && %{with libxml2} && %{with openssl} ]
%bcond selinux  1
%bcond uuid     1
%bcond xxhash   1
%bcond zlib     1
%bcond zstd     1

Name:           erofs-utils
Version:        1.9.1
Release:        1%{?dist}

Summary:        Utilities for working with EROFS
License:        GPL-2.0-only AND GPL-2.0-or-later AND (GPL-2.0-only OR Apache-2.0) AND (GPL-2.0-or-later OR Apache-2.0) AND (GPL-2.0-only OR BSD-2-Clause) AND (GPL-2.0-or-later OR BSD-2-Clause) AND MIT AND Unlicense
URL:            https://erofs.docs.kernel.org/

Source:        https://git.kernel.org/pub/scm/linux/kernel/git/xiang/erofs-utils.git/snapshot/%{name}-%{version}.tar.gz

BuildRequires:  %[ "%{toolchain}" == "clang" ? "clang compiler-rt" : "gcc" ]
BuildRequires:  libtool
BuildRequires:  make
%{?with_curl:BuildRequires:  pkgconfig(libcurl)}
%{?with_deflate:BuildRequires:  pkgconfig(libdeflate)}
%{?with_fuse:BuildRequires:  pkgconfig(fuse3) >= 3.2}
%{?with_jsonc:BuildRequires:  pkgconfig(json-c)}
%{?with_libnl3:BuildRequires:  pkgconfig(libnl-genl-3.0) >= 3.1}
%{?with_libxml2:BuildRequires:  pkgconfig(libxml-2.0)}
%{?with_lz4:BuildRequires:  pkgconfig(liblz4) >= 1.9.3}
%{?with_lzma:BuildRequires:  pkgconfig(liblzma) >= 5.4}
%{?with_openssl:BuildRequires:  pkgconfig(openssl)}
%{?with_qpl:BuildRequires:  pkgconfig(qpl) >= 1.5.0}
%{?with_selinux:BuildRequires:  pkgconfig(libselinux)}
%{?with_uuid:BuildRequires:  pkgconfig(uuid)}
%{?with_xxhash:BuildRequires:  pkgconfig(libxxhash)}
%{?with_zlib:BuildRequires:  pkgconfig(zlib)}
%{?with_zstd:BuildRequires:  pkgconfig(libzstd) >= 1.4.0}

Recommends:     erofs-fuse%{?_isa} = %{version}-%{release}

%description
EROFS stands for Enhanced Read-Only File System.  It aims to be a general
read-only file system solution for various use cases instead of just focusing
on saving storage space without considering runtime performance.

This package includes tools to create, check, and extract EROFS images.

%if %{with fuse}
%package -n erofs-fuse
Summary:        FUSE support for mounting EROFS images
Requires:       fuse3

%description -n erofs-fuse
EROFS stands for Enhanced Read-Only File System.  It aims to be a general
read-only file system solution for various use cases instead of just focusing
on saving storage space without considering runtime performance.

This package includes erofsfuse to mount EROFS images.
%endif


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%build
autoreconf -fi
%configure \
    --enable-multithreading \
    --%{?with_curl:with}%{!?with_curl:without}-libcurl \
    --%{?with_deflate:with}%{!?with_deflate:without}-libdeflate \
    --%{?with_fuse:enable}%{!?with_fuse:disable}-fuse \
    --%{?with_jsonc:with}%{!?with_jsonc:without}-json-c \
    --%{?with_libnl3:with}%{!?with_libnl3:without}-libnl3 \
    --%{?with_libxml2:with}%{!?with_libxml2:without}-libxml2 \
    --%{?with_lz4:enable}%{!?with_lz4:disable}-lz4 \
    --%{?with_lzma:enable}%{!?with_lzma:disable}-lzma \
    --%{?with_oci:enable}%{!?with_oci:disable}-oci \
    --%{?with_openssl:with}%{!?with_openssl:without}-openssl \
    --%{?with_qpl:with}%{!?with_qpl:without}-qpl \
    --%{?with_s3:enable}%{!?with_s3:disable}-s3 \
    --%{?with_selinux:with}%{!?with_selinux:without}-selinux \
    --%{?with_uuid:with}%{!?with_uuid:without}-uuid \
    --%{?with_xxhash:with}%{!?with_xxhash:without}-xxhash \
    --%{?with_zlib:with}%{!?with_zlib:without}-zlib \
    --%{?with_zstd:with}%{!?with_zstd:without}-libzstd
%make_build

%install
%make_install


%files
%{_bindir}/dump.erofs
%{_bindir}/fsck.erofs
%{_bindir}/mkfs.erofs
%{_sbindir}/mount.erofs
%{_mandir}/man1/dump.erofs.1*
%{_mandir}/man1/fsck.erofs.1*
%{_mandir}/man1/mkfs.erofs.1*
%{_mandir}/man8/mount.erofs.8*
%doc AUTHORS ChangeLog README docs/PERFORMANCE.md docs/compress-hints.example
%license LICENSES/Apache-2.0 LICENSES/GPL-2.0 LICENSES/MIT

%if %{with fuse}
%files -n erofs-fuse
%{_bindir}/erofsfuse
%{_mandir}/man1/erofsfuse.1*
%doc AUTHORS ChangeLog README
%license LICENSES/Apache-2.0 LICENSES/GPL-2.0 LICENSES/MIT
%endif


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.9.1-1
- Prepare for Oreon 11 (RP1)
