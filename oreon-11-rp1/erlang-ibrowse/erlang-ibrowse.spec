%global source0_hash 3f903f8d60e9354a7fff71785820f1f067774422b6503ddbdb47e4fe23919972

%global realname ibrowse

Name:		erlang-%{realname}
Version:	4.4.2
Release:	%autorelease
BuildArch:	noarch
Summary:	Erlang HTTP client
License:	BSD-3-Clause OR LGPL-2.1-or-later
URL:		https://github.com/cmullaparthi/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/v%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-ibrowse-0001-use-is_ipv6_host-1-function-from-httpc.patch
Patch2:		erlang-ibrowse-0002-use-ssl-handshake-2-function-for-erlang-otp-21.patch
BuildRequires:	erlang-rebar3

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

%check
%{erlang3_test}

%files
%license BSD_LICENSE LICENSE
%doc CHANGELOG CONTRIBUTORS README.md doc/
%{erlang_appdir}/

%changelog
%autochangelog
