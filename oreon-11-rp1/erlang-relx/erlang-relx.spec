%global source0_hash 5f6df424568c3df19b5b76f98f4dc2d33068244a29593ebcbe2a3db8224289b4

%global realname relx

Name:		erlang-%{realname}
Version:	4.10.0
Release:	%autorelease
BuildArch:	noarch
Summary:	Release assembler for Erlang/OTP Releases
License:	Apache-2.0
URL:		https://github.com/erlware/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/v%{version}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-bbmustache
BuildRequires:	erlang-rebar3

%description
Relx assembles releases for an Erlang/OTP release. Given a release
specification and a list of directories in which to search for OTP applications
it will generate a release output.

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
%license LICENSE.md
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
