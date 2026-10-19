%global source0_hash 32e3252ddc333f273457a90b21eefb8e721c1feb1ab3bafd047b67fc77a31f7b
%global _hardened_build 1
Name:           pwauth
Version:        2.3.10
Release:        35%{?dist}
Summary:        External plugin for mod_authnz_external authenticator
License:        BSD-3-Clause
URL:            https://github.com/phokz/pwauth/
Source0:        https://github.com/phokz/pwauth/archive/%{name}-%{version}.tar.gz
Source1:        pwauth.pam
Patch1:         pwauth-make.patch
Patch2:         pwauth-strchr.patch
Patch3:         pwauth-cleanup.patch
Requires:       httpd
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pam-devel
# /oreon:deps
%description
Pwauth is an authenticator designed to be used with mod_auth_external
or mod_authnz_external and the Apache HTTP daemon to support reasonably
secure web authentication out of the system password database on most
versions of Unix.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P1 -p1 -b .make
%patch -P2 -p1 -b .strchr
%patch -P3 -p1 -b .cleanup

%build

export CFLAGS="${RPM_OPT_FLAGS}"
export LDFLAGS="${RPM_LD_FLAGS}"
%make_build CFLAGS="${CFLAGS} -Wno-comment" LDFLAGS="${LDFLAGS}"
%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_sysconfdir}/pam.d
install -p -m 4750 -t %{buildroot}%{_bindir} pwauth
install -p -m 0750 -t %{buildroot}%{_bindir} unixgroup
install -p -T %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/pwauth
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
