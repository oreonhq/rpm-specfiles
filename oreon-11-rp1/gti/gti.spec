%global source0_hash f8a3afdd3967fe7d88bd1b0b9f5cb62ae04dc9ba458238da91efc213f61a9cf9
Name:		gti		
Version:	1.9.1
Release:        1%{?dist}
Summary:        Just a silly gti launcher
Patch0:		gti-1.2.0-nostrip.patch
License:	MIT
URL:		http://r-wos.org/hacks/%{name}
Source0:        https://github.com/rwos/%{name}/archive/v%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Just a silly gti launcher, basically Inspired by sl. It displays a ASCII-art 
animation to punish you for your typing error, after that it launches git.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .nostrip

%build

make %{?_smp_mflags}  CFLAGS="%{optflags}" LDFLAGS="%{?__global_ldflags}" 
%install
make install DESTDIR=%{buildroot}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
