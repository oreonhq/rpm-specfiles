%global source0_hash 0f50797d86f6de214d43b2bf5e1d4cea5665a825eecdc9cdb188a76c80def52e

%global realname cowlib

Name:		erlang-%{realname}
Version:	2.16.0
Release:	%autorelease
BuildArch:	noarch
Summary:	Support library for manipulating Web protocols
License:	Apache-2.0
URL:		https://github.com/ninenines/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildRequires:  erlang-proper
BuildRequires:  erlang-rebar3

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{realname}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
# FIXME QuickCheck tests doesn't work with Proper atm
%{erlang3_test}

%files
%license LICENSE
%doc README.asciidoc
%{erlang_appdir}/

%changelog
%autochangelog
