%global source0_hash f080ab6cd9d96a5357570cb60a99e09ebe5eef11cf322c35373dbe815378a1f2
Name:           ugrep
Version:        7.8.5
Release:        1%{?dist}
Summary:        A more powerful, ultra fast, user-friendly, compatible grep
License:        BSD-3-Clause
URL:            https://github.com/Genivia/ugrep
Source0:        https://github.com/Genivia/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
Provides:       bundled(libreflex) = 5.5.0
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  brotli-devel
BuildRequires:  bzip2-devel
BuildRequires:  gcc-c++
BuildRequires:  libzstd-devel
BuildRequires:  lz4-devel
BuildRequires:  make
BuildRequires:  pcre2-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Ugrep is an ultra fast, user-friendly, compatible grep.  Ugrep combines the
best features of other grep, adds new features, and searches fast.  Includes a
TUI and adds Google-like search, fuzzy search, hexdumps, searches nested
archives (zip, 7z, tar, pax, cpio), compressed files (gz, Z, bz2, lzma, xz,
lz4, zstd, brotli), pdfs, docs, and more.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
autoreconf -fiv

%build

%ifarch %{arm}
%configure --disable-neon
%else
%configure
%endif
%make_build
%install
%make_install
%oreon_autofiles main

%check

%make_build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
