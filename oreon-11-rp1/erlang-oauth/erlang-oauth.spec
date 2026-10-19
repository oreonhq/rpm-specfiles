%global source0_hash ecc1da62dcb1cc107c2c896d15c3beed65c9be8dfc743e64335341c0ffe87145
%global realname oauth
Name:		erlang-%{realname}
Version:	2.1.0
Release:        1%{?dist}
BuildArch:	noarch
Summary:        An Erlang OAuth 1.0 implementation
License:	MIT
URL:		http://github.com/erlangpack/%{name}
VCS:		git:%{url}.git
Source0:        http://github.com/erlangpack/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
An Erlang OAuth 1.0 implementation. Includes functions for generating
signatures (client side), verifying signatures (server side), and some
convenience functions for making OAuth HTTP requests (client side).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%{erlang3_compile}
%install
%{erlang3_install}
%oreon_autofiles main

%check

%{erlang3_test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
