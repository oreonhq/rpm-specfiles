%global source0_hash 544b73e2204fa71caeb5a8aeb0b0d1d7f3ec6726c06c172bc723470610c2bda1

%define _legacy_common_support 1

%global forgeurl https://github.com/mricon/pam_url
%global commit 58e33bfaed3064ddc93f352b8272d42c17a20313
%forgemeta

Summary:        PAM module to authenticate with HTTP servers
Name:           pam_url
Version:        0.3.3
Release:        28%{?dist}
Epoch:          1
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            %{forgeurl}
Source:         %{forgesource}

Patch0:         pam_url-0.3.3-curl-timeout.patch
Patch1:         pam_url-0.3.3-nolibcheck.patch

Requires:       pam

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(libconfig)
BuildRequires:  pkgconfig(libcurl)

%description
The pam_url module enables you to authenticate users against a Web application,
such as totpcgi.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup
%patch -P 0 -p 1
%patch -P 1 -p 1

%build
CFLAGS="%{optflags} -std=c99" make %{?_smp_mflags} pamlib=%{_lib}/security all

%install
make DESTDIR=%{buildroot} pamlib=%{_lib}/security install

%files
%doc AUTHOR COPYING INSTALL README examples
%config(noreplace) %{_sysconfdir}/pam_url.conf
/%{_lib}/security/pam_url.so

%changelog
%autochangelog
