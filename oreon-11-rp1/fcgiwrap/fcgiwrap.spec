%global source0_hash c72f2933669ebd21605975c5a11f26b9739e32e4f9d324fb9e1a1925e9c2ae88
%global commit 99c942c90063c73734e56bacaa65f947772d9186
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20181108
Name:           fcgiwrap
Version:        1.1.0
Release:        1%{?dist}
Summary:        Simple FastCGI wrapper for CGI scripts
License:        MIT
URL:            https://github.com/gnosek/fcgiwrap
Source0:        https://github.com/gnosek/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
Source1:        %{name}@.service
Source2:        %{name}@.socket
Source3:        %{name}
Source4:        SETUP
Source5:        README.SELinux
Patch0:         %{name}-1.1.0-use_pkg-config_libsystemd.patch
Patch1:         %{name}-1.1.0-declare_cgi_error_noreturn.patch
Patch2:         %{name}-1.1.0-fix_kill_param_sequence.patch
ExcludeArch: %{ix86}
%{?systemd_requires}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  fcgi-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd-devel
# /oreon:deps
%description
This package provides a simple FastCGI wrapper for CGI scripts with/
following features:
 - very lightweight (84KB of private memory per instance)
 - fixes broken CR/LF in headers
 - handles environment in a sane way (CGI scripts get HTTP-related environment
   vars from FastCGI parameters and inherit all the others from
   environment of fcgiwrap )
 - no configuration, so you can run several sites off the same
   fcgiwrap pool
 - passes CGI std error output to std error stream of cgiwrap or FastCGI
 - support systemd socket activation, launcher program like spawn-fcgi
   is no longer required on systemd-enabled distributions

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}
install -pm 0644 %{SOURCE4} .
install -pm 0644 %{SOURCE5} .

%build

autoreconf -i
%configure --prefix="" --with-systemd
%make_build
%install
%make_install
rm -f %{buildroot}%{_unitdir}/fcgiwrap.service
rm -f %{buildroot}%{_unitdir}/fcgiwrap.socket
install -Dm 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}@.service
install -Dm 644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}@.socket
install -Dm 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
%oreon_autofiles main

%post

%systemd_post %{name}@.service %{name}@.socket
%preun

%systemd_preun %{name}@.service %{name}@.socket
%postun

%systemd_postun_with_restart %{name}@.service %{name}@.socket
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
