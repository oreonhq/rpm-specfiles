%global source0_hash e5a4ec9c6312ec5a850dea13ffa2cd50850e694fd79597cf76acb548287134d9

%global realname getopt

Name:		erlang-%{realname}
Version:	1.0.3
Release:	%autorelease
BuildArch:	noarch
Summary:	Erlang module to parse command line arguments using the GNU getopt syntax
License:	BSD-3-Clause
URL:		https://github.com/jcomellas/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/v%{version}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-rebar3

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

%check
%{erlang3_test}

%files
%license LICENSE.txt
%doc README.md examples/
%{erlang_appdir}/

%changelog
%autochangelog
