%global source0_hash 59f4c4b53c12b79b61a0eb303264e6cafeb36386ca3bcd3a41d2ada2d3333841

%global realname ct_helper
%global git_commit f5b31c3ab5516be169b1873441a12ce7dbc93186
%global git_date 20250208

Name:		erlang-%{realname}
Version:	0
Release:	%autorelease -p -s %{git_date}git%{sub %git_commit 0 7}
BuildArch:	noarch
Summary:	Helper modules for common_test suites
License:	ISC
URL:		https://github.com/ninenines/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{git_commit}/%{realname}-%{git_commit}.tar.gz
BuildRequires:  erlang-rebar3

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{git_commit}

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%license LICENSE
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
