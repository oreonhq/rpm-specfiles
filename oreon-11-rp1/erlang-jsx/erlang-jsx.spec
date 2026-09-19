%global source0_hash dbcd1a117e4e297fbbd9e7441d300185e7192a9ed881082f949d132c798acf78

%global realname jsx

Name:		erlang-%{realname}
Version:	3.1.0
Release:	%autorelease
BuildArch:	noarch
Summary:	A streaming, evented json parsing toolkit
License:	MIT
URL:		https://github.com/talentdeficit/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/v%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-jsx-0001-Adapt-to-OTP-24.patch
BuildRequires:	erlang-rebar3

%description
An Erlang application for consuming, producing and manipulating json. inspired
by yajl.

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
%doc CHANGES.md README.md
%{erlang_appdir}/

%changelog
%autochangelog
