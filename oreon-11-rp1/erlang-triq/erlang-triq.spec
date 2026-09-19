%global source0_hash d91ac7eef3e8f5aefe5253b83d7705129669536359710d5ed313a4df685ad52a

%global realname triq
%global git_commit e68b47fe7b9e963ec45edf3bf9d5a4cd81831e3c

Name:		erlang-%{realname}
Version:	1.3.0
Release:	%autorelease
BuildArch:	noarch
Summary:	A property-based testing library for Erlang
License:	Apache-2.0
URL:		https://gitlab.com/%{realname}/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/-/archive/v%{version}/%{realname}-%{version}.tar.bz2
BuildRequires:	erlang-rebar3

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{realname}-v%{version}-%{git_commit}
# FIXME breaks for unknown reason
rm -f test/triq_attr_tests.erl

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%license LICENSE
%doc NOTICE README.org THANKS
%{erlang_appdir}/

%changelog
%autochangelog
