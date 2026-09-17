%global source0_hash d2e3c48cd6202180f88c7d064ba6a6c30b9cdd7860a4ce1ab7c06f50fb684051

%global srcname eimp
%global p1_utils_ver 1.0.26

Name:    erlang-%{srcname}
Version: 1.0.26
Release: %autorelease
License: Apache-2.0
Summary: Erlang Image Manipulation Process
URL:     https://github.com/processone/%{srcname}
VCS:     git:%{url}.git
Source0: %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch:   erlang-eimp-0001-Disable-Rebar3-plugins.patch
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: erlang-p1_utils >= %{p1_utils_ver}
BuildRequires: erlang-rebar3
BuildRequires: erlang-rebar3-pc
BuildRequires: gcc
BuildRequires: gd-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libpng-devel
BuildRequires: libwebp-devel
Requires: erlang-p1_utils >= %{p1_utils_ver}

%description
eimp is an Erlang/Elixir application for manipulating graphic images
using external C libraries. It supports WebP, JPEG, PNG and GIF.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}
rm -f configure

%build
autoreconf -ivf
%configure
%{erlang3_compile}
# FIXME we don't have a port compiler plugin for rebar3 yet
mkdir -p priv/bin
gcc c_src/eimp.c $CFLAGS -DHAVE_WEBP -DHAVE_GD -DHAVE_JPEG -DHAVE_PNG -fPIC -c -I%{_libdir}/erlang/usr/include -o c_src/eimp.o
gcc c_src/eimp.o $LDFLAGS -L%{_libdir}/erlang/usr/lib -lei -L%{_libdir} -lwebp -lpng -ljpeg -lgd  -lpthread -o priv/bin/eimp

%install
%{erlang3_install}
install -p -D -m 755 priv/bin/* --target-directory=%{buildroot}%{erlang_appdir}/priv/bin/

%check
%{erlang3_test}

%files
%license LICENSE.txt
%doc README.md
%{erlang_appdir}/

%changelog
%autochangelog
