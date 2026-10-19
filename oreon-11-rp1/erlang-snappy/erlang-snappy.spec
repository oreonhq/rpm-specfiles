%global source0_hash e33564d1d4e7709c099b59fcdde78ee47011ea98f3cdd8a86dfeb9390cccdad6
%global realname snappy
Name:		erlang-%{realname}
Version:	1.2.1
Release:        1%{?dist}
Summary:        An Erlang NIF wrapper for Google's snappy library
License:	Apache-2.0
URL:		https://github.com/skunkwerks/%{realname}-erlang-nif
VCS:		git:%{url}.git
Source0:        https://github.com/skunkwerks/%{realname}-erlang-nif/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-snappy-0001-No-bundled-snappy.patch
Patch3:		erlang-snappy-0002-Added-a-check-for-empty-IOLists-during-decompression.patch
# oreon:deps
BuildRequires:  erlang-rebar3
BuildRequires:  gcc-c++
BuildRequires:  snappy-devel
# /oreon:deps
%description
An Erlang NIF wrapper for Google's snappy compressor/decompressor.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-erlang-nif-%{version}
rm -rf c_src/snappy
rm -rf rebar.config rerar.config.script

%build

%{erlang3_compile}
mkdir -p priv/
g++ c_src/snappy_nif.cc	$CFLAGS -fPIC -c -I%{_libdir}/erlang/usr/include -o c_src/snappy_nif.o
g++ c_src/snappy_nif.o	$LDFLAGS -shared -L%{_libdir}/erlang/usr/lib -lei -L%{_libdir} -lsnappy -lm -o priv/snappy_nif.so
%install
%{erlang3_install}
%oreon_autofiles main

%check

%{erlang3_test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
