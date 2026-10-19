%global source2_hash 027f4da27c8fef29e71aa2e6c1bccf038e2382d512c36181049b907c7769f4f1
%global source1_hash 4b892474bfeb975ee6fce1e7e6c7bced6da0555de577ba6a934a8195cfae61c9
%global source0_hash 39c3ec6ef5604bfa206e8aa10fc05d5119040f6de4a554bc0fb98ca1aed838dc
%global source2_key_fpr A441880C3D4C7C36C5DD41E13B7ECB2B30DE0871
%bcond_without check
Name:           munge
Version:        0.5.18
Release:        1%{?dist}
Summary:        Enables uid & gid authentication across a host cluster
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
URL:            https://dun.github.io/munge/
Source0:        https://github.com/dun/munge/releases/download/munge-%{version}/munge-%{version}.tar.xz
Source1:        https://github.com/dun/munge/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz.asc
Source2:        https://github.com/dun.gpg
Source3:        munge.sysusers
Source4:        README.md
Requires:       munge-libs = %{version}-%{release}
Requires:       logrotate
%if %{with check}
%endif
%{?systemd_requires}
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  procps-ng
BuildRequires:  systemd-rpm-macros
BuildRequires:  util-linux
BuildRequires:  zlib-devel
# /oreon:deps
%description
MUNGE (MUNGE Uid 'N' Gid Emporium) is an authentication service for creating
and validating credentials. It is designed to be highly scalable for use
in an HPC cluster environment.
It allows a process to authenticate the UID and GID of another local or
remote process within a group of hosts having common users and groups.
These hosts form a security realm that is defined by a shared cryptographic
key. Clients within this security realm can create and validate credentials
without the use of root privileges, reserved ports, or platform-specific
methods.

%package devel
Summary:        Development files for uid * gid authentication across a host cluster
Requires:       munge-libs%{?_isa} = %{version}-%{release}
%description devel
Header files for developing using MUNGE.

%package libs
Summary:        Runtime libs for uid * gid authentication across a host cluster
%description libs
Runtime libraries for using MUNGE.

%prep

%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -N -S git
cp "%{SOURCE4}"  README-Fedora.md

%autopatch

%build

%configure  --disable-static --with-crypto-lib=openssl --runstatedir="%{_rundir}" --with-systemdunitdir="%{_unitdir}"  --with-sysconfigdir="%{_sysconfdir}/sysconfig/" --with-logrotateddir="%{_sysconfdir}/logrotate.d/"
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/munge.conf
rm %{buildroot}/%{_libdir}/libmunge.la
chmod 700 %{buildroot}%{_var}/lib/munge %{buildroot}%{_var}/log/munge
chmod 700 %{buildroot}%{_sysconfdir}/munge
mkdir -p %{buildroot}%{_rundir}/munge
touch %{buildroot}%{_rundir}/munge/munged.pid
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with check}
%make_build check \
    LD_LIBRARY_PATH=%{buildroot}%{_libdir} \
    root=/tmp/munge-$$ VERBOSE=t verbose=t
%endif
%preun

%systemd_preun munge.service
%post

%systemd_post munge.service
%postun

%systemd_postun_with_restart munge.service
%ldconfig_scriptlets   libs
%files -f %{oreon_filedir}/main.list
%files -n munge-devel -f %{oreon_filedir}/munge-devel.list
%files -n munge-libs -f %{oreon_filedir}/munge-libs.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.5.18-1
- Prepare for Oreon 11 (RP1)
