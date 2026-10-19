%global source0_hash ce1ec81069a3b99d8e62ad54782a76b05403b2d15314af480074ac9e00899bee
%global srcname compute-image-packages
%global commit 3178e68b004eea38dada580de4193994f45dfc50
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           google-compute-engine-oslogin
Version:        1.4.3
Release:        1%{?dist}
Summary:        OS Login Functionality for Google Compute Engine
License:        Apache-2.0
URL:            https://github.com/GoogleCloudPlatform/%{srcname}
Source0:        https://github.com/GoogleCloudPlatform/%{srcname}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz
Requires(post): selinux-policy-base >= %{_selinux_policy_version}
Requires(post): policycoreutils
Requires(post): policycoreutils-python-utils
Requires(pre):  libselinux-utils
Requires(post): libselinux-utils
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
# /oreon:deps
%description
This package contains several libraries and changes to enable OS Login
functionality for Google Compute Engine.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{commit}

# Delete pregenerated SELinux policy module file
rm google_compute_engine_oslogin/policy/oslogin.pp

%build

pushd google_compute_engine_oslogin
export CC="gcc %{optflags}"
export CXX="g++ %{optflags}"
%make_build LIBS="-lcurl -ljson-c"
make -C policy
popd
%install
pushd google_compute_engine_oslogin
%make_install NSS_INSTALL_PATH=%{_libdir} PAM_INSTALL_PATH=%{_libdir}/security INSTALL_SELINUX=true
popd
bzip2 -9 %{buildroot}%{_datadir}/selinux/packages/oslogin.pp
chmod +x %{buildroot}%{_libdir}/*.so*
chmod +x %{buildroot}%{_libdir}/security/*.so*
mkdir -p %{buildroot}%{_localstatedir}/google-sudoers.d
%oreon_autofiles main

%post

%selinux_modules_install %{_datadir}/selinux/packages/oslogin.pp.bz2
%postun

%selinux_modules_uninstall oslogin
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
