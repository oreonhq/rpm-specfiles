%global source0_hash 6dd5511b92b64df115b358c064e7701b350b343f30711232a8d74c6274c962a5

Name:		gti		
Version:	1.6.1
Release:	14%{?dist}
Summary:	Just a silly gti launcher
Patch0:		gti-1.2.0-nostrip.patch

License:	MIT
URL:		http://r-wos.org/hacks/%{name}
Source0:	https://github.com/rwos/%{name}/archive/v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires: make
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

%files
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*

%changelog
%autochangelog
