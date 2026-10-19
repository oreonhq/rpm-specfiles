%global source0_hash 7bb8ea8af519befefff93ec3c9e32108d7f2b83216c9bc7b01aef5098861c82f
Summary:        Compact and feature-rich WordStar-compatible editor
Name:           jupp
Version:        41
Release:        1%{?dist}
License:        GPL-1.0-only AND BSD-3-Clause AND ISC AND MirOS AND Unicode-DFS-2016
URL:            https://www.mirbsd.org/jupp.htm
Source0:        https://www.mirbsd.org/MirOS/dist/%{name}/joe-3.1%{name}%{version}.tgz
Patch0:         jupp-configure-c99.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libselinux-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
%description
Jupp is a compact and feature-rich WordStar-compatible editor and also the
MirOS fork of the JOE 3.x editor which provides easy conversion for former
PC users as well as powerfulness for programmers, while not doing annoying
things like word wrap "automagically". It can double as a hex editor and
comes with a character map plus Unicode support. Additionally it contains
an extension to visibly display tabs and spaces, has a cleaned up, extended
and beautified options menu, more CUA style key-bindings, an improved math
functionality and a bracketed paste mode automatically used with Xterm.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}
%oreon_prep
%build

chmod +x configure
export CFLAGS="$CFLAGS -std=gnu11"  # http://www.mirbsd.org/jupp.htm#build
%configure --disable-termidx --sysconfdir=%{_sysconfdir}/%{name}
%make_build sysconfjoesubdir=
%install
%make_install sysconfjoesubdir=
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/{jmacs,joe,jpico,jstar,rjoe}rc
rm -f $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}/{jmacs,jpico,jstar,jupp,rjoe}*
mv -f $RPM_BUILD_ROOT%{_bindir}/{joe,%{name}}
mv -f $RPM_BUILD_ROOT%{_mandir}/man1/{joe,%{name}}.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
