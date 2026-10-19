%global source0_hash 8866a6be438902027d670c15e90df2c18b837784241b3d3a46f28104c3ffee1b
Name:           sasl-xoauth2
Version:        0.27
Release:        1%{?dist}
Summary:        The xoauth2 plugin for cyrus-sasl
License:        Apache-2.0
URL:            https://github.com/tarickb/%{name}
Source0:        https://github.com/tarickb/%{name}/archive/refs/tags/release-%{version}.tar.gz
Requires:       cyrus-sasl-lib
Requires:       python3-msal
# oreon:deps
BuildRequires:  argparse-manpage
BuildRequires:  cmake
BuildRequires:  cyrus-sasl-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  jsoncpp-devel
BuildRequires:  libcurl-devel
BuildRequires:  pandoc
BuildRequires:  python3-msal
BuildRequires:  sqlite-devel
# /oreon:deps
%description
sasl-xoauth2 is a SASL plugin that enables client-side use of OAuth 2.0.

Among other things it enables the use of Gmail or Outlook/Office 365 SMTP
relays from Postfix.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-release-%{version}

%build

%cmake \
  -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} \
  -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

%ctest
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
