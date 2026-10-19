%global source0_hash f3ff48dd240317a74ee45855f4265e8565d344217ecf85efe778b477f7a3288d
%global date 20241112
%global commit ca81c1dbed5c7e30fe79d44953ccfeaab98d2b4f
%global shortcommit %global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           mce-inject
Version:        0^%{date}git%{shortcommit}
Release:        1%{?dist}
Summary:        Linux machine check injector tool
License:        GPL-2.0-only
URL:            https://git.kernel.org/pub/scm/utils/cpu/mce/mce-inject.git
Source0:        https://git.kernel.org/pub/scm/utils/cpu/mce/%{name}.git/snapshot/%{name}-%{commit}.tar.gz
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed
# /oreon:deps
%description
mce-inject allows to inject machine check errors on the software level into a
running Linux kernel. This is intended for validation of the kernel machine
check handler.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit} -p1

# Preseve timestamps on install
sed -i 's/install -m/install -pm/g' Makefile

# https://fedoraproject.org/wiki/Changes/Unify_bin_and_sbin
sed -i 's:$(prefix)/sbin:%{_bindir}:g' Makefile

%build

%make_build CFLAGS="%{build_cflags}"
%install
%make_install destdir="%{buildroot}"
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
