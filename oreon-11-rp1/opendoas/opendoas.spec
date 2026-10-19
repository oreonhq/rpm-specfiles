%global source2_hash 5afb979ea20496060d8c66ef8dadb6aa53b91e7ee43099caf8317967596d1dcd
%global source0_hash 28dca29adec5f4336465812d9e2243f599e62a78903de71c24f0cd6fe667edac
Name:           opendoas
Version:        6.8.2
Release:        1%{?dist}
Summary:        Portable fork of the OpenBSDs doas command
License:        ISC AND BSD-3-Clause
URL:            https://github.com/Duncaen/OpenDoas
Source0:        https://github.com/Duncaen/OpenDoas/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %url/releases/download/v%{version}/%{name}-%{version}.tar.gz.sig
Source2:        https://xn--1xa.duncano.de/duncan.asc
Patch0:         01-patch-makefile-to-remove-chown.patch
Provides:       doas = %{version}-%{release}
Provides:       bundled(libopenbsd)
# oreon:deps
BuildRequires:  byacc
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  pam-devel
# /oreon:deps
%description
doas is a minimal replacement for the venerable sudo. It was initially written
by Ted Unangst of the OpenBSD project to provide 95% of the features of sudo
with a fraction of the codebase.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

%set_build_flags
./configure --prefix=%{_prefix} --with-timestamp --with-pam
%make_build
%install
%make_install
mkdir -p  %{_sysconfdir}
cat > %{buildroot}%{_sysconfdir}/doas.conf << EOF
permit :wheel
EOF
mkdir -p  %{buildroot}%{_sysconfdir}/pam.d
cat > %{buildroot}%{_sysconfdir}/pam.d/doas << EOF
auth       include      system-auth
account    include      system-auth
password   include      system-auth
session    optional     pam_keyinit.so revoke
session    required     pam_limits.so
session    include      system-auth
EOF
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
