%global source0_hash 7d7fa6a9f5f53d607ab851d739ae3d3b99ca86e2cb1425a6cab9299f673aee16
%global owner neurobin
Name: shc
Summary:        Shell script compiler
URL: https://neurobin.org/projects/softwares/unix/shc/
Version: 4.0.3
Release:        1%{?dist}
Source0:        https://github.com/%{owner}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
License: GPL-3.0-only
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
SHC is a generic shell script compiler. It takes
a script, which is specified on the command line
and produces C source code. The generated source
code is then compiled and linked to produce a s-
tripped binary. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
