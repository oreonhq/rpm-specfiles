%global source0_hash none
%global with_debug 0
%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif
%global gomodulesmode GO111MODULE=on
%global import_path %{provider}.%{provider_tld}/%{project}/%{repo}
Name: pack
Version: 0.40.9
Release:        1%{?dist}
Summary:        Convert code into runnable images
License: Apache-2.0 and BSD-2-Clause and BSD-3-Clause and ISC and MIT
URL: https://github.com/buildpacks/%{name}
Source0:        v%{version}-vendor.tar.gz
Provides: %{name}cli = %{version}-%{release}
Provides: %{name}-cli = %{version}-%{release}
# oreon:deps
BuildRequires:  git
BuildRequires:  glib2-devel
BuildRequires:  glibc-static
BuildRequires:  go-rpm-macros
BuildRequires:  golang
BuildRequires:  make
# /oreon:deps
%description
%{name} is a CLI implementation of the Platform Interface Specification
for Cloud Native Buildpacks.

%prep
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%set_build_flags
export CGO_CFLAGS=$CFLAGS
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-flto=auto//g')
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-Wp,D_GLIBCXX_ASSERTIONS//g')
CGO_CFLAGS=$(echo $CGO_CFLAGS | sed 's/-specs=\/usr\/lib\/rpm\/redhat\/redhat-annobin-cc1//g')
export LDFLAGS=''
%ifarch x86_64
export CGO_CFLAGS+=" -m64 -mtune=generic -fcf-protection=full"
%endif
%gobuild -o out/%{name} .
%install
export GOPATH=$(pwd)/_build:$(pwd)
make DESTDIR=%{buildroot} PREFIX=%{_prefix} install
%{!?_licensedir:%global license %doc}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
