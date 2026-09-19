%global source0_hash 7bb8ea8af519befefff93ec3c9e32108d7f2b83216c9bc7b01aef5098861c82f

Summary:        Compact and feature-rich WordStar-compatible editor
Name:           jupp
Version:        41
Release:        10%{?dist}
# jupp itself is GPL-1.0-only but uses other source codes, breakdown:
# BSD-3-Clause: popen.inc
# ISC: strlfun.inc
# MirOS: {compat,win32}.c and jupprc and strlfun.inc and types.h
# Unicode-DFS-2016: i18n.c
License:        GPL-1.0-only AND BSD-3-Clause AND ISC AND MirOS AND Unicode-DFS-2016
URL:            https://www.mirbsd.org/jupp.htm
Source0:        https://www.mirbsd.org/MirOS/dist/%{name}/joe-3.1%{name}%{version}.tgz
Patch0:         jupp-configure-c99.patch
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  libselinux-devel

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

%autosetup -p1 -n %{name}

%build
chmod +x configure
export CFLAGS="$CFLAGS -std=gnu11"  # http://www.mirbsd.org/jupp.htm#build
%configure --disable-termidx --sysconfdir=%{_sysconfdir}/%{name}
%make_build sysconfjoesubdir=

%install
%make_install sysconfjoesubdir=

# Some cleanups to be done by upstream for future releases
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/{jmacs,joe,jpico,jstar,rjoe}rc
rm -f $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}/{jmacs,jpico,jstar,jupp,rjoe}*
mv -f $RPM_BUILD_ROOT%{_bindir}/{joe,%{name}}
mv -f $RPM_BUILD_ROOT%{_mandir}/man1/{joe,%{name}}.1

%files
%license COPYING
%doc HINTS INFO LIST NEWS README
%dir %{_sysconfdir}/%{name}/
%config(noreplace) %{_sysconfdir}/%{name}/%{name}rc
%dir %{_sysconfdir}/%{name}/charmaps/
%config(noreplace) %{_sysconfdir}/%{name}/charmaps/*
%dir %{_sysconfdir}/%{name}/syntax/
%config(noreplace) %{_sysconfdir}/%{name}/syntax/*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
