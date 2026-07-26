%global source0_hash 7ef7210effd25ac1f82f190fcfaef53e49d7bc40bb94112c4aa07266c32a851b

%global srcname base64url

Name:      erlang-%{srcname}
Version:   1.0.1
Release:   %autorelease
BuildArch: noarch
License:   MIT
Summary:   Standalone URL safe base64-compatible codec
URL:       https://github.com/dvv/%{srcname}
VCS:       git:%{url}.git
Source0:   %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildRequires: erlang-rebar3

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build
%{erlang3_compile}

%check
%{erlang3_test}

%install
%{erlang3_install}

%files
%license LICENSE.txt
%doc README.md
%{erlang_appdir}

%changelog
%autochangelog
