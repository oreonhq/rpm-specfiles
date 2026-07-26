%global source0_hash d7a5a8e8121e77f36f65b6932f0f3b8d49a924c92559e079e2286a7daaaee792

%global realname bitcask

Name:		erlang-%{realname}
Version:	2.1.0
Release:	%autorelease
Summary:	Eric Brewer-inspired key/value store
License:	Apache-2.0
URL:		https://github.com/basho/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Source1:	bitcask.licensing
Patch:		erlang-bitcask-0001-Don-t-use-deprecated-erlang-now-0.patch
Patch:		erlang-bitcask-0002-Remove-eqc-we-still-don-t-use-them.patch
Patch:		erlang-bitcask-0003-Remove-pc-target.patch
Patch:		erlang-bitcask-0004-Fix-32-bit-portability-issues-in-NIF-code.patch
BuildRequires:	erlang-cuttlefish
BuildRequires:	erlang-meck
BuildRequires:	erlang-rebar3
BuildRequires:	gcc

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-%{version}

%build
%{erlang3_compile}

# FIXME we don't have a port compiler plugin for rebar3 yet
mkdir -p priv
gcc $CFLAGS -fPIC -c -I%{_libdir}/erlang/usr/include c_src/bitcask_nifs.c -o c_src/bitcask_nifs.o
gcc $CFLAGS -fPIC -c -I%{_libdir}/erlang/usr/include c_src/erl_nif_util.c -o c_src/erl_nif_util.o
gcc $CFLAGS -fPIC -c -I%{_libdir}/erlang/usr/include c_src/murmurhash.c -o c_src/murmurhash.o
gcc $LDFLAGS -shared -L%{_libdir}/erlang/usr/lib -lei c_src/bitcask_nifs.o c_src/erl_nif_util.o c_src/murmurhash.o -o priv/bitcask.so

%install
%{erlang3_install}

cp -arv priv/bitcask.schema %{buildroot}%{erlang_appdir}/priv
cp -arv priv/bitcask_multi.schema %{buildroot}%{erlang_appdir}/priv

%check
%{erlang3_test}

%files
%doc README.md THANKS doc/
%{erlang_appdir}/

%changelog
%autochangelog
