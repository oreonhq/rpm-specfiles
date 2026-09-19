%global source0_hash d8fc4d678ec2ae1508bc2a00f631e2ea01028cb5b45e3609a2af87b4b0bfe4cb

%global realname hamcrest
%global git_commit 0766ea004f7dd900c36b06aff14dbbac1d03b425
%global git_date 20181106

Name:		erlang-%{realname}
Version:	0.1.0
Release:	%autorelease -s %{git_date}git%{sub %git_commit 0 7}
BuildArch:	noarch
Summary:	A framework for writing matcher objects using declarative rules
License:	BSD-3-Clause
URL:		https://github.com/hyperthunk/%{realname}-erlang
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{git_commit}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-proper
BuildRequires:	erlang-rebar3

%description
Hamcrest is a framework for writing matcher objects allowing 'match' rules to
be defined declaratively. There are a number of situations where matchers are
invaluable, such as UI validation, or data filtering, but it is in the area of
writing flexible tests that matchers are most commonly used.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-erlang-%{git_commit}

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
# FIXME requires proprietary library - QuickCheck
#%%{erlang3_test}

%files
%license LICENCE
%doc NOTES README.markdown
%{erlang_appdir}/

%changelog
%autochangelog
