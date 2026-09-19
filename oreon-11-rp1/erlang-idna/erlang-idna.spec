%global source0_hash fbe8d9392d89bc2dbd57713a98411f165c8b2f76be79abfd6501fd3f0193b545

%global srcname idna

Name:       erlang-%{srcname}
Version:    7.1.0
Release:    %autorelease
BuildArch:  noarch
License:    MIT
Summary:    A pure Erlang IDNA implementation that folllows RFC5891
URL:        https://github.com/benoitc/erlang-%{srcname}
VCS:        git:%{url}.git
Source0:    %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildRequires: erlang-rebar3

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%license LICENSE
%doc CHANGELOG
%doc README.md
%{erlang_appdir}

%changelog
%autochangelog
