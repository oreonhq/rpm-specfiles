%global source0_hash 8866a6be438902027d670c15e90df2c18b837784241b3d3a46f28104c3ffee1b

Name:           sasl-xoauth2
Version:        0.27
Release:        2%{?dist}
Summary:        The xoauth2 plugin for cyrus-sasl

License:        Apache-2.0
URL:            https://github.com/tarickb/%{name}
Source0:        https://github.com/tarickb/%{name}/archive/refs/tags/release-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
%if 0%{?rhel} < 8
BuildRequires:  cmake3
%else
BuildRequires:  cmake
%endif
BuildRequires:  cyrus-sasl-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  sqlite-devel
BuildRequires:  pandoc
BuildRequires:  argparse-manpage
BuildRequires:  python3-msal
# dependency on cyrus-sasl is not enforced by the resolver
# The package is a plugin for cyrus-sasl so it does not make any sense without
Requires:       cyrus-sasl-lib
Requires:       python3-msal

%description
sasl-xoauth2 is a SASL plugin that enables client-side use of OAuth 2.0.

Among other things it enables the use of Gmail or Outlook/Office 365 SMTP
relays from Postfix.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-release-%{version}

%build
%if 0%{?rhel} && 0%{?rhel} < 8
%cmake3 -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir}
%cmake3_build
%else
%cmake \
  -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} \
  -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build
%endif

%install
%if 0%{?rhel} && 0%{?rhel} < 8
%cmake3_install
%else
%cmake_install
%endif

%check
%ctest

%files
%doc README.md
%license COPYING
%dir %{_libdir}/sasl-xoauth2
%{_libdir}/sasl-xoauth2/test-config
%dir %{_libdir}/sasl2
%{_libdir}/sasl2/libsasl-xoauth2.so
%{_bindir}/sasl-xoauth2-tool
%config(noreplace) %{_sysconfdir}/sasl-xoauth2.conf
%{_mandir}/man5/%{name}.conf.5.gz
%{_mandir}/man1/%{name}-tool.1.gz

%changelog
%autochangelog
