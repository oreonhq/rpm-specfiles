%global source0_hash 577b8788029148f93217d00a1bbdc500db68ee77b2246bbd892269b5bb98c41a
%global realname cl
Name:		erlang-%{realname}
Version:	1.2.4
Release:        1%{?dist}
Summary:        OpenCL binding for Erlang
License:	MIT
URL:		https://github.com/tonyrog/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/tonyrog/%{realname}/archive/%{realname}-%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-cl-0001-Remove-handmade-makefile.patch
# oreon:deps
BuildRequires:  erlang-edown
BuildRequires:  erlang-rebar3
BuildRequires:  gcc
BuildRequires:  ocl-icd-devel
BuildRequires:  opencl-headers
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{realname}-cl-%{version}

%build

%{erlang3_compile}
mkdir -p ./priv
gcc c_src/cl_hash.c $CFLAGS -fPIC -c -I%{_libdir}/erlang/usr/include -o c_src/cl_hash.o
gcc c_src/cl_nif.c  $CFLAGS -fPIC -c -I%{_libdir}/erlang/usr/include -o c_src/cl_nif.o
gcc c_src/cl_hash.o c_src/cl_nif.o $LDFLAGS -shared -L%{_libdir}/erlang/usr/lib -lei -lOpenCL -o priv/cl_nif.so
%install
%{erlang3_install}
%oreon_autofiles main

%check

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
