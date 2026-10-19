%global source0_hash 136c629ea8af2419925ac92ed55783a5d81f7b89562686d48256f79db6a75b05
%global commit	39b7ceece0e3daf675444ec711efd9fc534c100a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:		mpssh
Version:	1.3.3
Release:        26%{?dist}
Summary:        Parallel ssh tool
License:	LicenseRef-Callaway-BSD
URL:		https://github.com/ndenev/%{name}
Source0:        https://github.com/ndenev/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch0:		mpssh-1.3.3.dont_override_cflags.patch
Requires:	openssh-clients
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssh-clients
# /oreon:deps
%description
mpssh is a parallel ssh tool. What it does is connecting to a number of hosts
specified in the hosts file and execute the same command on all of them

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{commit}
%patch -P0

%build

CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ;
LDFLAGS="${LDFLAGS:-%?__global_ldflags}"; export LDFLAGS
make %{?_smp_mflags}
sed -i "s,/usr/local,%{_prefix},g" %{name}.1
cp debian/copyright .
gzip %{name}.1
%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}
install -p -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -p -D -m 0644 %{name}.1.gz %{buildroot}%{_mandir}/man1/%{name}.1.gz
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
