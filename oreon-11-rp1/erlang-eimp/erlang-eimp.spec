%global source0_hash 841c0d34f97e28f259d71773ea0a6b25c9cbc6cc6711ef4a38c67959ae5b93a7
%global srcname eimp
%global p1_utils_ver 1.0.27
Name:    erlang-%{srcname}
Version: 1.0.27
Release:        1%{?dist}
License: Apache-2.0
Summary:        Erlang Image Manipulation Process
URL:     https://github.com/processone/%{srcname}
VCS:     git:%{url}.git
Source0:        https://github.com/processone/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch:   erlang-eimp-0001-Disable-Rebar3-plugins.patch
Requires: erlang-p1_utils >= %{p1_utils_ver}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  erlang-p1_utils
BuildRequires:  erlang-rebar3
BuildRequires:  erlang-rebar3-pc
BuildRequires:  gcc
BuildRequires:  gd-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  libwebp-devel
# /oreon:deps
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
mkdir -p priv/bin
gcc c_src/eimp.c $CFLAGS -DHAVE_WEBP -DHAVE_GD -DHAVE_JPEG -DHAVE_PNG -fPIC -c -I%{_libdir}/erlang/usr/include -o c_src/eimp.o
gcc c_src/eimp.o $LDFLAGS -L%{_libdir}/erlang/usr/lib -lei -L%{_libdir} -lwebp -lpng -ljpeg -lgd  -lpthread -o priv/bin/eimp
%install
%{erlang3_install}
install -p -D -m 755 priv/bin/* --target-directory=%{buildroot}%{erlang_appdir}/priv/bin/
%oreon_autofiles main

%check

%{erlang3_test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
