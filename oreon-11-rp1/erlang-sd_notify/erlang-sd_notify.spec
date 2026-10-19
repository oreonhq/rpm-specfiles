%global source0_hash 06d37072249faf35c7c9a0651c8131b74cac166242a8b7612e51ae2b9f5761f0
%global realname sd_notify
Name:		erlang-%{realname}
Version:	1.1
Release:        1%{?dist}
BuildArch:	noarch
Summary:        Erlang interface to systemd notify subsystem
License:	MIT
URL:		https://github.com/systemd/erlang-%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/systemd/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
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
