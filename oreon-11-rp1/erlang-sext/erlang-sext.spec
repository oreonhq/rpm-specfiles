%global source0_hash 568c83993184d069e8df5c643e6403243c317cd0a3becd4d684794dc016c3627

%global realname sext

Name:		erlang-%{realname}
Version:	1.8.0
Release:	%autorelease
BuildArch:	noarch
Summary:	Sortable Erlang Term Serialization
License:	Apache-2.0
URL:		https://github.com/uwiger/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch:		erlang-sext-0001-Handle-OTP-26-external-term-format-changes.patch
BuildRequires:	erlang-edown
BuildRequires:	erlang-rebar3

%description
A sortable serialization library This library offers a serialization format (a
la term_to_binary()) that preserves the Erlang term order.

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
%license LICENSE
%doc NOTICE README.md examples/
%{erlang_appdir}/

%changelog
%autochangelog
