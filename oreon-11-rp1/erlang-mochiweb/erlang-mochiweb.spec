%global source0_hash 87fc5335c49c3eea7b7cf32c12e8d8e060d20f90eee6396150b42437e9057161

%global realname mochiweb

Name:		erlang-%{realname}
Version:	3.3.0
Release:	%autorelease
BuildArch:	noarch
Summary:	An Erlang library for building lightweight HTTP servers
License:	MIT
URL:		https://github.com/mochi/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/v%{version}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-rebar3
BuildRequires:	erlang-xmerl
Provides:	%{realname} = %{version}-%{release}

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

# Additional skeleton files
cp -arv scripts %{buildroot}%{_erllibdir}/%{realname}-%{version}
cp -arv support %{buildroot}%{_erllibdir}/%{realname}-%{version}

%check
%{erlang3_test}

%files
%license LICENSE
%doc CHANGES.md README.md examples/
%{erlang_appdir}/

%changelog
%autochangelog
