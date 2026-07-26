%global source0_hash 3c9ae7c41ba86a857dd2ed81927fedd7afb078fd2fdb3c079dd998a27381f15b

%global realname snappy

Name:		erlang-%{realname}
Version:	1.1.2
Release:	%autorelease
Summary:	An Erlang NIF wrapper for Google's snappy library
License:	Apache-2.0
URL:		https://github.com/skunkwerks/%{realname}-erlang-nif
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-snappy-0001-No-bundled-snappy.patch
Patch3:		erlang-snappy-0002-Added-a-check-for-empty-IOLists-during-decompression.patch
BuildRequires:	erlang-rebar3
BuildRequires:	gcc-c++
BuildRequires:	snappy-devel

%description
An Erlang NIF wrapper for Google's snappy compressor/decompressor.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-erlang-nif-%{version}
rm -rf c_src/snappy
rm -rf rebar.config rerar.config.script

%build
%{erlang3_compile}

# FIXME we don't have a port compiler plugin for rebar3 yet
mkdir -p priv/
g++ c_src/snappy_nif.cc	$CFLAGS -fPIC -c -I%{_libdir}/erlang/usr/include -o c_src/snappy_nif.o
g++ c_src/snappy_nif.o	$LDFLAGS -shared -L%{_libdir}/erlang/usr/lib -lei -L%{_libdir} -lsnappy -lm -o priv/snappy_nif.so

%install
%{erlang3_install}

%check
%{erlang3_test}

%files
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
