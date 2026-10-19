%global source0_hash ca3be808e3d0c785955f1613e6e860fc51b5db086b821b48707466da1a06392c
%define _legacy_common_support 1
Name:		bspwm
Version:	0.9.12
Release:        1%{?dist}
Summary:        A tiling window manager based on binary space partitioning
License:	LicenseRef-Callaway-BSD
URL:		https://github.com/baskerville/bspwm
Source0:        https://github.com/baskerville/%{name}/archive/%{version}.tar.gz
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  xcb-util-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  xcb-util-wm-devel
# /oreon:deps
%description
bspwm is a tiling window manager that represents windows as the leaves of a
full binary tree.

It only responds to X events, and the messages it receives on a dedicated
socket.

bspc is a program that writes messages on bspwm's socket.

bspwm doesn't handle any keyboard or pointer inputs: a third party program
(e.g. sxhkd) is needed in order to translate keyboard and pointer events to
bspc invocations.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

make VERBOSE=1 %{?_smp_mflags} CFLAGS="%{optflags}" \
	LDFLAGS="%{?__global_ldflags}"
%install
%make_install PREFIX="%{_prefix}"
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}/%{_datadir}/xsessions/%{name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
