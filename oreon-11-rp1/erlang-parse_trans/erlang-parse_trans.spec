%global source0_hash b0708c261ed8e24f35f43a04842649fe6768f796d425aac45f408200f9db6f71

%global realname parse_trans

Name:		erlang-%{realname}
Version:	3.4.1
Release:	%autorelease
BuildArch:	noarch
Summary:	Parse transform utilities for Erlang
License:	Apache-2.0
URL:		https://github.com/uwiger/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-edown
BuildRequires:	erlang-rebar3

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n %{realname}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%license LICENSE
%doc doc/ examples/ README.md
%{erlang_appdir}/

%changelog
%autochangelog
