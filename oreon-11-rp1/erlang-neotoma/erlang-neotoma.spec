%global source0_hash 97e01d4577d9882b9cb10e079bd33114f1293abae5180dc272be17e419daa0df
%global realname neotoma
Name:		erlang-%{realname}
Version:	1.7.4
Release:        1%{?dist}
BuildArch:	noarch
Summary:        Erlang library and packrat parser-generator for parsing expression grammars
License:	MIT
URL:		https://github.com/seancribbs/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/seancribbs/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
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
mkdir -p %{buildroot}%{erlang_appdir}/priv
install -p -m 0644 priv/neotoma_parse.peg priv/peg_includes.hrl %{buildroot}%{erlang_appdir}/priv/
%oreon_autofiles main

%check

%{erlang3_test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
