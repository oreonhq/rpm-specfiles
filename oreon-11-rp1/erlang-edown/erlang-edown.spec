%global source0_hash 0f70c7397faef6e1919dead80da7aebd2a05c79138770947f83f0c0adaa1563d

%global realname edown

Name:		erlang-%{realname}
Version:	0.9.2
Release:	%autorelease
BuildArch:	noarch
Summary:	EDoc extension for generating GitHub-flavored Markdown
License:	Apache-2.0
URL:		https://github.com/uwiger/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch:		erlang-edown-0001-Remove-pre-18.0-code.patch
Patch:		erlang-edown-0002-Don-t-use-git-command-for-branch-retrieval.patch
BuildRequires:	erlang-edoc
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
%{erlang3_test}

%files
%doc NOTICE README.md doc/
%{erlang_appdir}/

%changelog
%autochangelog
