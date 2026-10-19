%global source0_hash e5a4ec9c6312ec5a850dea13ffa2cd50850e694fd79597cf76acb548287134d9
%global realname getopt
Name:		erlang-%{realname}
Version:	1.0.3
Release:        1%{?dist}
BuildArch:	noarch
Summary:        Erlang module to parse command line arguments using the GNU getopt syntax
License:	BSD-3-Clause
URL:		https://github.com/jcomellas/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/jcomellas/%{realname}/archive/v%{version}/%{realname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
Command-line parsing module that uses a syntax similar to that of GNU getopt.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n %{realname}-%{version}
chmod 0644 examples/*.escript

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
