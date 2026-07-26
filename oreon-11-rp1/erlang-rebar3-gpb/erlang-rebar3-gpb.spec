%global source0_hash 01ddf0681dc8aca4375cd7279130acf59e53033a76a32698b449d28c1d899488

%global realname rebar3_gpb_plugin

Name:		erlang-rebar3-gpb
Version:	2.23.8
Release:	%autorelease
Summary:	A protobuf compiler for Rebar3
License:	MIT
URL:		https://github.com/lrascao/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	erlang-gpb
BuildRequires:	erlang-rebar3

%description
A Rebar3 plugin for automatically compiling .proto files using the gpb protobuf
compiler.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{version}

%build
%{erlang3_compile}

%check
%{erlang3_test}

%install
%{erlang3_install}

%files
%license LICENSE
%doc README.md
%{erlang_appdir}

%changelog
%autochangelog
