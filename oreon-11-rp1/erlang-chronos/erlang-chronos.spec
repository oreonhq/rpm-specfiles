%global source0_hash 4b21ecd28129011badccf0347030ab5db7d99dd97bbac44841b2e6ccacde8465

%global realname chronos

Name:		erlang-%{realname}
Version:	0.5.1
Release:	%autorelease
BuildArch:	noarch
Summary:	Timer utility for Erlang tests
License:	MIT
URL:		https://github.com/lehoff/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
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
# Requires a proprietary eqc library
#%%{erlang3_test}

%files
%doc
%{erlang_appdir}/

%changelog
%autochangelog
