%global source0_hash 0e375557cf7ba670b626d0b1691b0257c2e68a4509bb72bf14ae8f8b7a30b3c3

%global srcname epam

Name:       erlang-%{srcname}
Version:    1.0.14
Release:    %autorelease
Summary:    Library for ejabberd for PAM authentication support
License:    Apache-2.0
URL:        https://github.com/processone/%{srcname}
VCS:        git:%{url}.git
Source0:    %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch1:     erlang-epam-0001-Disable-Rebar3-plugins.patch
BuildRequires: gcc
BuildRequires: erlang-rebar3
BuildRequires: pam-devel
Provides: erlang-p1_pam = %{version}-%{release}
Obsoletes: erlang-p1_pam < 1.0.3-4%{?dist}

%description
An Erlang library for ejabberd that helps with PAM authentication.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build
%{erlang3_compile}

# FIXME we don't have a port compiler plugin for rebar3 yet
mkdir -p priv/bin
gcc c_src/epam.c $CFLAGS -fPIC -c -I%{_libdir}/erlang/usr/include -o c_src/epam.o
gcc c_src/epam.o $LDFLAGS -L%{_libdir}/erlang/usr/lib -lei -L%{_libdir} -lpam -o priv/bin/epam

%install
%{erlang3_install}

install -d $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/bin
install -pm755 priv/bin/%{srcname} $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/bin/

%check
%{erlang3_test}

%files
%license LICENSE.txt
%doc CHANGELOG.md
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
