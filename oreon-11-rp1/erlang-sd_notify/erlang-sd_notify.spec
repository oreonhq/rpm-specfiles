%global source0_hash 06d37072249faf35c7c9a0651c8131b74cac166242a8b7612e51ae2b9f5761f0

%global realname sd_notify

Name:		erlang-%{realname}
Version:	1.1
Release:	%autorelease
BuildArch:	noarch
Summary:	Erlang interface to systemd notify subsystem
License:	MIT
URL:		https://github.com/systemd/erlang-%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/v%{version}/erlang-%{realname}-%{version}.tar.gz
BuildRequires:	erlang-rebar3

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%license LICENSE
%{erlang_appdir}/

%changelog
%autochangelog
