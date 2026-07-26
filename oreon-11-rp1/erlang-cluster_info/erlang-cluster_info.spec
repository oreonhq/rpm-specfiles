%global source0_hash 64fd1a833c6ba780e2033238034adc28aee951cddb9888741a3e13363bd5644c

%global realname cluster_info

Name:		erlang-%{realname}
Version:	2.1.0
Release:	%autorelease
BuildArch:	noarch
Summary:	Cluster info/postmortem inspector for Erlang applications
License:	Apache-2.0
URL:		https://github.com/basho/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-cluster_info-0001-OTP-25-update.patch
BuildRequires:	erlang-lager
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
%license LICENSE
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
