%global source0_hash fbe8d9392d89bc2dbd57713a98411f165c8b2f76be79abfd6501fd3f0193b545
%global srcname idna
Name:       erlang-%{srcname}
Version:    7.1.0
Release:        1%{?dist}
BuildArch:  noarch
License:    MIT
Summary:        A pure Erlang IDNA implementation that folllows RFC5891
URL:        https://github.com/benoitc/erlang-%{srcname}
VCS:        git:%{url}.git
Source0:        https://github.com/benoitc/%{name}/archive/%{version}/%{srcname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  erlang-rebar3
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%{erlang3_compile}
%install
%{erlang3_install}
%oreon_autofiles main

%check

%{erlang3_test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
