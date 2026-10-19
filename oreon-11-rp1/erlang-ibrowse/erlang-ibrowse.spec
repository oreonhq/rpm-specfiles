%global source0_hash 6d6370b0547f8edef604c37c085584872db8bc7b8e50f5ea570a2138376c4086
%global realname ibrowse
Name:		erlang-%{realname}
Version:	4.5.0
Release:        1%{?dist}
BuildArch:	noarch
Summary:        Erlang HTTP client
License:	BSD-3-Clause OR LGPL-2.1-or-later
URL:		https://github.com/cmullaparthi/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/cmullaparthi/%{realname}/archive/v%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-ibrowse-0001-use-is_ipv6_host-1-function-from-httpc.patch
Patch2:		erlang-ibrowse-0002-use-ssl-handshake-2-function-for-erlang-otp-21.patch
# oreon:deps
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{version}

%build

%{erlang3_compile}
%install
%{erlang3_install}
install -D -p -m 0644 priv/%{realname}.conf %{buildroot}%{erlang_appdir}/priv/%{realname}.conf
%oreon_autofiles main

%check

%{erlang3_test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
