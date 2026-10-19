%global source0_hash 728c9715493141ab6920411e6d319310d4ce205559c16a5aa8f4fa72e6def559
Name: anyterm
Version: 1.2.3
Release:        1%{?dist}
Summary:        A web-based terminal emulator
License: GPL-2.0-or-later
URL: https://anyterm.org
Source0:        anyterm-1.2.3.tar.xz
Source1: anyterm-cmd
Source4: anyterm.conf
Source5: anyterm.service
Source6: anyterm.sysusers.conf
Source7: anyterm.tmpfiles.conf
Patch0: anyterm-change-url-prefix.patch
Patch1: anyterm-upstream-fixes-r18810.patch
Patch2: anyterm-char8_t.patch
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
%{?sysusers_requires_compat}
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
# /oreon:deps
%package httpd
Summary: Httpd proxy configuration for anyterm
License: GPL-2.0-or-later
Requires: %{name} = %{version}-%{release}
Requires: httpd
%description
The Anyterm web-based terminal emulator, permits terminal and/or arbitrary
command access via http. The anyterm daemon can be configured to run any
arbitrary command, redirecting all standard input / output / error to
and from any javascript-enabled web browser in real time.

%description httpd
The httpd configuration necessary to proxy anyterm.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p0
%patch -P1 -p3
%patch -P2 -p1

%build

export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
make %{?_smp_mflags} CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" OPTIMISE_FLAGS="$CXXFLAGS"
gzip anytermd.1
%install
install -Dp -m0755 anytermd %{buildroot}%{_sbindir}/anytermd
install -Dp -m0644 anytermd.1.gz %{buildroot}%{_mandir}/man1/anytermd.1.gz
install -Dp -m0755 %{SOURCE1} %{buildroot}%{_libexecdir}/%{name}/anyterm-cmd
install -Dp -m0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/httpd/conf.d/anyterm.conf
install -Dp -m0644 %{SOURCE5} %{buildroot}%{_unitdir}/%{name}.service
install -Dp -m0644 %{SOURCE6} %{buildroot}%{_sysusersdir}/%{name}.conf
install -Dp -m0644 %{SOURCE7} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -Dp -m0644 browser/anyterm.css %{buildroot}%{_datadir}/%{name}/anyterm.css
install -Dp -m0644 browser/anyterm.html %{buildroot}%{_datadir}/%{name}/anyterm.html
install -Dp -m0644 browser/anyterm.js %{buildroot}%{_datadir}/%{name}/anyterm.js
install -Dp -m0644 browser/copy.gif %{buildroot}%{_datadir}/%{name}/copy.gif
install -Dp -m0644 browser/copy.png %{buildroot}%{_datadir}/%{name}/copy.png
install -Dp -m0644 browser/paste.gif %{buildroot}%{_datadir}/%{name}/paste.gif
install -Dp -m0644 browser/paste.png %{buildroot}%{_datadir}/%{name}/paste.png
install -Dp -m0644 browser/resizer.png %{buildroot}%{_datadir}/%{name}/resizer.png
%oreon_autofiles anyterm-httpd usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%pre

%sysusers_create_compat %{SOURCE6}
%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list
%files -n anyterm-httpd -f %{oreon_filedir}/anyterm-httpd.list

%changelog

%autochangelog
