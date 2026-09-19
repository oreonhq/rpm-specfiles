%global source0_hash 2c027503b4a673d5ac7a09065c9eb479228e5997eaf4f217bec235bffcbbc56b

%global realname eradius

Name:		erlang-%{realname}
Version:	2.3.1
Release:	%autorelease
BuildArch:	noarch
Summary:	Erlang RADIUS server framework
License:	MIT
URL:		https://github.com/travelping/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-eradius-0001-Ignore-plugins.patch
Patch2:		erlang-eradius-0002-Disable-prometheus-support.patch
BuildRequires:	erlang-meck
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
%doc METRICS.md README.md sample/
%{erlang_appdir}/

%changelog
%autochangelog
