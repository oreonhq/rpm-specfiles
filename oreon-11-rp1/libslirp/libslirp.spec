%global source0_hash bc37833d51ea2418ba32d4c8c019a7bf009c8cbcbe1007571d69936bdcde232c
Name:           libslirp
Version:        4.9.5
Release:        1%{?dist}
Summary:        A general purpose TCP-IP emulator
License:        BSD-3-Clause AND MIT
URL:            https://gitlab.freedesktop.org/slirp/%{name}
Source0:        https://src.fedoraproject.org/repo/pkgs/libslirp/%{name}-%{version}.tar.xz/sha512/daede9dfe0c5f4e14258f66e46eef3475a79da61e88e5e19bf1a283002dfbc6a0ea72961e6aee1b6fa1ab39ea435a48d6c371f195138573e40854415b45941c9/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  glib2-devel
BuildRequires:  meson
# /oreon:deps
%description
A general purpose TCP-IP emulator used by virtual machine hypervisors
to provide virtual networking services.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libslirp-devel -f %{oreon_filedir}/libslirp-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.9.1-3
- Import
