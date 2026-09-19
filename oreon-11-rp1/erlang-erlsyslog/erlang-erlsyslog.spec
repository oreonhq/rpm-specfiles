%global source0_hash 9533c9d3d2a29e7fda93ea6ede43ba5d3fb9b09dbf79cdb1fe35a52669779562

%global realname erlsyslog

Name:		erlang-%{realname}
Version:	0.8.0
Release:	%autorelease
Summary:	Syslog facility for Erlang
License:	MIT
URL:		https://github.com/lemenkov/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-rebar3
BuildRequires:	gcc

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{version}

%build
mkdir -p ./ebin
sed -i -e "s,%VSN%,%{version},g" src/erlsyslog.app.src > ebin/erlsyslog.app

%{erlang3_compile}

# FIXME we don't have a port compiler plugin for rebar3 yet
mkdir -p priv/
gcc c_src/erlsyslog_drv.c	$CFLAGS -fPIC -c -I%{_libdir}/erlang/usr/include -o c_src/erlsyslog_drv.o
gcc c_src/erlsyslog_drv.o	$LDFLAGS -shared -L%{_libdir}/erlang/usr/lib -lei -o priv/erlsyslog_drv.so

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%doc example
%{erlang_appdir}/

%changelog
%autochangelog
