%global source0_hash a93fc671e85edb94d6daba3c60114f056a65c1ec4616af6b471440f228c58662

%global realname gproc

Name:		erlang-%{realname}
Version:	1.1.0
Release:	%autorelease
BuildArch:	noarch
Summary:	Extended process registry for Erlang
License:	Apache-2.0
URL:		https://github.com/uwiger/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-edown
BuildRequires:	erlang-gen_leader
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
install -D -p -m 0644 priv/sys.config %{buildroot}%{erlang_appdir}/priv/sys.config
# Remove edoc config files (not needed for end-users)
rm -f doc/edoc-info
rm -f doc/overview.edoc
rm -f doc/README.md

%check
%{erlang3_test}

%files
%license LICENSE
%doc doc/* README.md
%{erlang_appdir}/

%changelog
%autochangelog
