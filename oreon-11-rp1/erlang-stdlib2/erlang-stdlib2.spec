%global source0_hash be52d339f8f353cd2f5d294ed0e75a2d38abbf2e81dbf49850cd4b6b7311a0a2

%global realname stdlib2

Name:		erlang-%{realname}
Version:	1.4.6
Release:	%autorelease
BuildArch:	noarch
Summary:	Erlang stdlib extensions
# Original sources seems to be licensed under BSD-2-Clause, the files added by
# Kivra are licensed under Apache-2.0
License:	BSD-2-Clause AND Apache-2.0
URL:		https://github.com/kivra/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/v%{version}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-folsom
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

%check
%{erlang3_test}

%files
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
