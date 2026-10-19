%global source0_hash fac65d7f39ae73c1c9221a97075eebeb27696299b02ad1e01ec039ab0eca9fca
%bcond_without gnulib
%bcond_without most
Name:           bzip3
Version:        1.5.4
Release:        1%{?dist}
Summary:        Tools for compressing and decompressing bzip3 files
License:        LGPL-3.0-or-later AND BSD-2-Clause
SourceLicense:  GPL-3.0-or-later AND GPL-3.0-or-later WITH Autoconf-exception-macro AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND GPL-2.0-or-later WITH Autoconf-exception-generic AND GPL-2.0-or-later WITH Libtool-exception AND (GPL-2.0-or-later OR MIT) AND LGPL-3.0-or-later AND BSD-2-Clause AND Apache-2.0 AND X11 AND FSFULLR AND FSFUL AND FSFAP
URL:            https://github.com/iczelia/%{name}
Source0:        https://github.com/iczelia/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Patch0:         bzip3-1.5.0-Do-not-use-usr-bin-env-in-shell-bangs.patch
Patch1:         bzip3-1.5.3-autoconf-Define-extra_cflags-variable.patch
%if %{with gnulib}
%endif
Requires:       %{name}-grep = %{version}-%{release}
Requires:       %{name}-less = %{version}-%{release}
Requires:       %{name}-more = %{version}-%{release}
%if %{with most}
Requires:       %{name}-most = %{version}-%{release}
%endif
Requires:       %{name}-tools%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  bash
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  gnulib-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconf-pkg-config
BuildRequires:  sed
# /oreon:deps
%description
These are tools for compressing, decompressing, printing, and searching bzip3
files. bzip3 features higher compression ratios and better performance than
bzip2 thanks to an order-0 context mixing entropy coder, a fast
Burrows-Wheeler transform code making use of suffix arrays and a run-length
encoding with Lempel-Ziv prediction pass based on LZ77-style string matching
and PPM-style context modeling.

If you only need bzip3 tool, consider installing %{name}-tools package
instead.

%package libs
Summary:        Shared libraries for bzip3 compression and decompression
License:        LGPL-3.0-or-later AND Apache-2.0 
Provides:       bundled(libsais) = 2.7.0
%description libs
This is a library for compressing and decompressing bzip3 compression format.
bzip3 features higher compression ratios and better performance than bzip2
thanks to an order-0 context mixing entropy coder, a fast Burrows-Wheeler
transform code making use of suffix arrays and a run-length encoding with
Lempel-Ziv prediction pass based on LZ77-style string matching and PPM-style
context modeling.

%package devel
Summary:        Files for developing with bzip3 library
License:        LGPL-3.0-or-later
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
Header files, a pkg-config module and link objects for building applications
which use a bzip3 library.

%package grep
Summary:        Print lines matching a pattern in bzip3-compressed files
License:        LGPL-3.0-or-later
BuildArch:      noarch
Requires:       %{name}-tools = %{version}-%{release}
Requires:       grep
%description grep
This package contains a bz3most tool. It displays bzip3-compressed files with
the "most" pager.

%package less
Summary:        View bzip3-compressed files with less pager
License:        LGPL-3.0-or-later
BuildArch:      noarch
Requires:       %{name}-tools = %{version}-%{release}
Requires:       less
%description less
This package contains a bz3less tool. It displays bzip3-compressed files with
the "less" pager.

%package more
Summary:        View bzip3-compressed files with more pager
License:        LGPL-3.0-or-later
BuildArch:      noarch
Requires:       %{name}-tools = %{version}-%{release}
Requires:       util-linux-core
%description more
This package contains a bz3more tool. It displays bzip3-compressed files with
the "more" pager.

%if %{with most}
%package most
Summary:        View bzip3-compressed files with most pager
License:        LGPL-3.0-or-later
BuildArch:      noarch
Requires:       %{name}-tools = %{version}-%{release}
Requires:       most
%description most
This package contains a bz3most tool. It displays bzip3-compressed files with
the "most" pager.
%endif

%package tools
Summary:        Tools for compressing and decompressing bzip3 archives
License:        LGPL-3.0-or-later
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Recommends:     (%{name}-grep if grep)
Recommends:     (%{name}-less if less)
Recommends:     (%{name}-more if util-linux-core)
%if %{with most}
Recommends:     (%{name}-most if most)
%endif
%description tools
This package contains bunzip3, bz3cat, and bzip3 tools.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Remove generated autoconf files
rm aclocal.m4 configure Makefile.in
# Remove generated manual pages
for F in *.1.in; do
    rm "${F%%.in}"
done
# Unbundle autoconf macros and scripts, except those not yet packaged in
# autoconf-archive
find build-aux -type f \! \( \
%if %{without gnulib}
    -name git-version-gen -o \
%endif
    -name ax_progvar.m4 -o \
    -name ax_subst_man_date.m4 -o \
    -name ax_subst_transformed_package_name.m4 \
    \) -delete
%if %{with gnulib}
# Execute git-version-gen from a system location
ln -s %{_datadir}/gnulib/build-aux/git-version-gen build-aux/git-version-gen
%endif

%build

autoreconf -vfi
%configure \
    --disable-arch-native \
    --with-pic \
    --with-pthread \
    --enable-shared \
    --disable-static \
    --disable-static-exe
%{make_build}
%check

make check roundtrip %{?_smp_mflags}
%install
%{make_install}
find %{buildroot} -name '*.la' -delete
if cmp %{buildroot}%{_mandir}/man1/{bz3cat,bunzip3}.1; then
    rm %{buildroot}%{_mandir}/man1/bunzip3.1
    ln -s bz3cat.1 %{buildroot}%{_mandir}/man1/bunzip3.1
fi
%oreon_autofiles bzip3-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bzip3-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles bzip3-grep usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bzip3-less usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bzip3-more usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bzip3-most usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bzip3-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n bzip3-libs -f %{oreon_filedir}/bzip3-libs.list
%files -n bzip3-devel -f %{oreon_filedir}/bzip3-devel.list
%files -n bzip3-grep -f %{oreon_filedir}/bzip3-grep.list
%files -n bzip3-less -f %{oreon_filedir}/bzip3-less.list
%files -n bzip3-more -f %{oreon_filedir}/bzip3-more.list
%files -n bzip3-most -f %{oreon_filedir}/bzip3-most.list
%files -n bzip3-tools -f %{oreon_filedir}/bzip3-tools.list

%changelog

%autochangelog
