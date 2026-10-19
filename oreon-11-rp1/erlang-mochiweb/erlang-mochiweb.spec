%global source0_hash c7c64b38841e15f29b21320ff43d7809b531fb08cd126b30e5bd7752c2cd2990
%global realname mochiweb
Name:		erlang-%{realname}
Version:	3.5.0
Release:        1%{?dist}
BuildArch:	noarch
Summary:        An Erlang library for building lightweight HTTP servers
License:	MIT
URL:		https://github.com/mochi/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/mochi/%{realname}/archive/v%{version}/%{realname}-%{version}.tar.gz
Provides:	%{realname} = %{version}-%{release}
# oreon:deps
BuildRequires:  erlang-rebar3
BuildRequires:  erlang-xmerl
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{version}
rm -f .gitignore ./examples/example_project/.gitignore

%build

%{erlang3_compile}
%install
%{erlang3_install}
cp -arv scripts %{buildroot}%{_erllibdir}/%{realname}-%{version}
cp -arv support %{buildroot}%{_erllibdir}/%{realname}-%{version}
%oreon_autofiles main

%check

%{erlang3_test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
