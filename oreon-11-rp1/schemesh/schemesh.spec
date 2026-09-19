%global source0_hash a71ec0e75cc9dbbb919659ec23b6d24780b19de88b5e4a873144af816bd94c25

%global chez_version %(%{_bindir}/scheme --version 2>/dev/null || echo unknown)
%global forgeurl https://github.com/cosmos72/schemesh

Name:    schemesh
Version: 0.9.1
Release: 6%{?dist}
Summary: Fusion between a Unix shell and a Lisp REPL

%forgemeta
License: GPL-2.0-or-later
URL:     %{forgeurl}
Source0: %{forgesource}

BuildRequires: gcc
BuildRequires: make
# chez-scheme < 10.2 outputs --version to stderr
BuildRequires: chez-scheme-devel >= 10.2
BuildRequires: lz4-devel
BuildRequires: ncurses-devel
BuildRequires: libuuid-devel
BuildRequires: zlib-devel

Requires: chez-scheme%{?_isa} = %{chez_version}

%description
Schemesh is an interactive shell scriptable in Lisp.

It is primarily intended as a user-friendly Unix login shell,
replacing bash, zsh, pdksh etc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build
%ifarch ppc64le s390x
EXTRA_LDFLAGS="-lffi"
%endif
%make_build \
    prefix=%{_prefix} \
    libdir=%{_libdir} \
    bindir=%{_bindir} \
    CFLAGS="$CFLAGS" \
    LDFLAGS="$LDFLAGS $EXTRA_LDFLAGS"

%install
%make_install prefix=%{_prefix} libdir=%{_libdir} bindir=%{_bindir}

%check
time ./schemesh_test

%files
%license COPYING
%doc README.md
%doc doc/*
%{_bindir}/schemesh
%{_bindir}/countdown
%{_libdir}/schemesh/

%changelog
%autochangelog
