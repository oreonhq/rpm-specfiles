%global source0_hash 8e01b4a50c8876cdd98d8e245c0687c4dc4d883aed161ad9c5ace1fb1fdaae99
ExcludeArch: %{ix86}
%global giturl  https://github.com/aantron/luv
Name:           ocaml-luv
Version:        0.5.14
Release:        1%{?dist}
Summary:        OCaml binding to libuv for cross-platform asynchronous I/O
License:        MIT
URL:            https://aantron.github.io/luv/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/%{version}/luv-%{version}.tar.gz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-ctypes-devel
BuildRequires:  ocaml-dune
BuildRequires:  pkgconfig(libuv)
# /oreon:deps
%description
Luv is a binding to libuv, the cross-platform C library that does
asynchronous I/O in Node.js and runs its main loop.

Besides asynchronous I/O, libuv also supports multiprocessing and
multithreading.  Multiple event loops can be run in different threads.
Libuv also exposes a lot of other functionality, amounting to a full OS
API, and an alternative to the standard module Unix.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-ctypes-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n luv-%{version}

# Remove spurious executable bits
find . -type f -exec chmod 0644 {} +

%build

export LUV_USE_SYSTEM_LIBUV=yes
%dune_build
%install
export LUV_USE_SYSTEM_LIBUV=yes
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export LUV_USE_SYSTEM_LIBUV=yes
%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-luv-devel -f %{oreon_filedir}/ocaml-luv-devel.list

%changelog

%autochangelog
