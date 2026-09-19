%global source0_hash fecad13ac815e80c9556347c0133af1cfd0d9cd1a9e47c069b57f970ef6e549c

%global realname basho_metrics

Name:		erlang-%{realname}
Version:	1.0.0
Release:	%autorelease
Summary:	Fast performance metrics for Erlang
License:	Apache-2.0
URL:		https://github.com/basho/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-basho_metrics-0001-Use-C-11.patch
BuildRequires:	boost-devel
BuildRequires:	erlang-rebar3
BuildRequires:	gcc-c++

%description
An open source Erlang library for efficient calculation of service performance
metrics.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{version}
rm -rf c_src/boost

%build
%{erlang3_compile}

# FIXME we don't have a port compiler plugin for rebar3 yet
mkdir -p ./priv
g++ c_src/basho_metrics_nifs.cpp $CXXFLAGS -fPIC -std=c++11 -c -I%{_libdir}/erlang/usr/include -o c_src/basho_metrics_nifs.o
g++ c_src/basho_metrics_nifs.o $LDFLAGS -shared -L%{_libdir}/erlang/usr/lib -lei -lstdc++ -o priv/basho_metrics_nifs.so

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%license LICENSE
%doc README.org
%{erlang_appdir}/

%changelog
%autochangelog
