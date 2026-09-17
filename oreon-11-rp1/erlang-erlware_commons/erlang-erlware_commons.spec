%global source0_hash d6cb47d3cd6a37274c997bab0689973b95294b5daebb31e60c43286bd29d6d98

%global realname erlware_commons

Name:     erlang-%{realname}
Version:  1.8.1
Release:  %autorelease
Summary:  Extension to Erlang's standard library
License:  MIT
URL:      https://github.com/erlware/%{realname}
VCS:      git:%{url}.git
Source0:  %{url}/archive/v%{version}/%{realname}-%{version}.tar.gz
# The "color" tests does not play well with Fedora's build system - no tty in
# mock, so we disable it.
Patch:    erlang-erlware_commons-0001-Disable-color-test.patch
Patch:    erlang-erlware_commons-0002-Use-correct-version-instead-of-relying-to-git-one.patch
BuildArch:     noarch
BuildRequires: erlang-cf
BuildRequires: erlang-rebar3
# For tests only
BuildRequires: git-core

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{version}

%build
%{erlang3_compile}

%install
%{erlang3_install}
cp -arv priv/ %{buildroot}%{erlang_appdir}/

%check
%{erlang3_test}

%files
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
