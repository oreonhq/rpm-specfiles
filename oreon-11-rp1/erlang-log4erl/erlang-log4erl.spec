%global source0_hash 155128da51bbf1876b1815544ef24265c582d82925dbcf8b8e5abfead2b5d737

%global realname log4erl
%global git_commit 76ef24cb3928fbacd5777eadeedac0df0a0dc822

Name:		erlang-%{realname}
Version:	0.9.0
Release:	%autorelease
BuildArch:	noarch
Summary:	A logger for Erlang in the spirit of Log4J
# src/time_compat.erl is licensed under Apache-2.0 the rest is MPL.
License:	MPL-1.1 AND Apache-2.0
URL:		https://github.com/ahmednawras/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{git_commit}/%{realname}-%{version}.tar.gz
Patch1:		erlang-log4erl-0001-Stop-using-deprecated-function-crypto-hmac-3.patch
Patch2:		erlang-log4erl-0002-Remove-deprecated-function-httpd_util-integer_to_hex.patch
BuildRequires:	erlang-mochiweb
BuildRequires:	erlang-rebar3

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{git_commit}
# in mochiweb
rm -f src/mochinum.erl

%build
%{erlang3_compile}

%install
%{erlang3_install}
install -D -p -m 0644 priv/l4e.conf %{buildroot}%{erlang_appdir}/priv/l4e.conf
install -D -p -m 0644 priv/log4erl.conf %{buildroot}%{erlang_appdir}/priv/log4erl.conf

%check
%{erlang3_test}

%files
%license LICENSE.txt
%doc API.txt Appenders_API.txt CHANGELOG.txt CONFIGURATION.txt README.txt TODO.txt
%{erlang_appdir}/

%changelog
%autochangelog
