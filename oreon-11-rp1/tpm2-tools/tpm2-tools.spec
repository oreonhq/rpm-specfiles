%global source0_hash 1cb73185cae814b4e15c7c2d0b22642d640faf48775f4156a1fd92edf84bef73
Name:    tpm2-tools
Version: 5.8
Release:        1%{?dist}
Summary:        A bunch of TPM testing toolS build upon tpm2-tss
License: BSD-3-Clause
URL:     https://github.com/tpm2-software/tpm2-tools
Source0:        https://github.com/tpm2-software/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Requires: tpm2-tss%{?_isa} >= 3.1.0
# oreon:deps
BuildRequires:  autoconf-archive
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(tss2-esys)
BuildRequires:  pkgconfig(tss2-mu)
BuildRequires:  pkgconfig(tss2-sys)
BuildRequires:  pkgconfig(uuid)
# /oreon:deps
%description
tpm2-tools is a batch of tools for tpm2.0. It is based on tpm2-tss.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{version}%{?candidate:-%{candidate}}

%build

%configure --prefix=/usr --disable-static --disable-silent-rules
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.7-5
- Prepare for Oreon 11 (RP1)
