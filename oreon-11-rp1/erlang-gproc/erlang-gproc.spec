%global source0_hash 7601cc4fcce4e31bf696098c444bb34e8d3b16e7efae6bd0f1cd0e70a78b1874
%global realname gproc
Name:		erlang-%{realname}
Version:	1.3.0
Release:        1%{?dist}
BuildArch:	noarch
Summary:        Extended process registry for Erlang
License:	Apache-2.0
URL:		https://github.com/uwiger/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/uwiger/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  erlang-edown
BuildRequires:  erlang-gen_leader
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
install -D -p -m 0644 priv/sys.config %{buildroot}%{erlang_appdir}/priv/sys.config
rm -f doc/edoc-info
rm -f doc/overview.edoc
rm -f doc/README.md
%oreon_autofiles main

%check

%{erlang3_test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
