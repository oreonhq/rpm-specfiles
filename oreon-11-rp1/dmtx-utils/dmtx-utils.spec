%global source0_hash 0d396ec14f32a8cf9e08369a4122a16aa2e5fa1675e02218f16f1ab777ea2a28

Name:           dmtx-utils
Version:        0.7.6
Release:        24%{?dist}
Summary:        Tools for working with Data Matrix 2D bar-codes

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
# http://www.libdmtx.org/ doesn't work any more
# outdated info is still at http://libdmtx.sourceforge.net/
URL:            https://github.com/dmtx
Source0:        https://github.com/dmtx/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/dmtx/dmtx-utils/commit/f7b97efc3bd6fc2e4403803f46514ae28318743b
Patch0:         dmtx-utils-0.7.6-buffer.patch
# https://github.com/dmtx/dmtx-utils/pull/18
Patch1:         dmtx-utils-0.7.6-types.patch

BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libdmtx)
BuildRequires:  pkgconfig(MagickWand)

Provides:       libdmtx-utils = %{version}-%{release}
Obsoletes:      libdmtx-utils < 0.7.4

%description
libdmtx is open source software for reading and writing Data Matrix 2D
bar-codes on Linux, Unix, OS X, Windows, and mobile devices. At its core
libdmtx is a shared library, allowing C/C++ programs to use its capabilities
without restrictions or overhead.

The included utility programs, dmtxread and dmtxwrite, provide the official
interface to libdmtx from the command line, and also serve as a good reference
for programmers who wish to write their own programs that interact with
libdmtx.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

./autogen.sh

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING COPYING.LESSER
%doc AUTHORS ChangeLog KNOWNBUG README README.linux TODO
%{_bindir}/dmtx*
%{_mandir}/man1/dmtx*.1*

%changelog
%autochangelog
