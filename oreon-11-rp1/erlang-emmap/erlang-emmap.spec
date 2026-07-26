%global source0_hash fa83828e39d18988c17ef17619830919e79e9084190012304df0a1bcb17ef8ac

%global realname emmap
%global git_commit f4a6f82d20a4ea08f723a033988b9a83bbcaf850
%global git_date 20230313

Name:		erlang-%{realname}
Version:	2.0.11
Release:	%autorelease -s %{git_date}git%{sub %git_commit 0 7}
Summary:	Erlang mmap interface
License:	Apache-2.0
URL:		https://github.com/saleyn/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{git_commit}/%{realname}-%{version}.tar.gz
Patch1:		erlang-emmap-0001-Fix-for-i686.patch
Patch2:		erlang-emmap-0002-Enough-space-for-i686.patch
BuildRequires:	erlang-edown
BuildRequires:	erlang-rebar3
BuildRequires:	gcc
BuildRequires:	gcc-c++

%description
This Erlang library provides a wrapper that allows you to memory map files into
the Erlang memory space.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%ifarch %{ix86}
%autosetup -p1 -n %{realname}-%{git_commit}
%else
%autosetup -N -n %{realname}-%{git_commit}
%endif

%build
%{erlang3_compile}

# FIXME we don't have a port compiler plugin for rebar3 yet
g++ c_src/emmap.cpp $CFLAGS -fPIC -c -I%{_libdir}/erlang/usr/include -o c_src/emmap.o
g++ c_src/emmap.o $LDFLAGS -shared -L%{_libdir}/erlang/usr/lib -lei -ldl -o priv/emmap.so

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
