%global source0_hash b7b3016383f4373e26dc566fecb94e7b8b97eb7d9b54647dcca372790018c03e
%global selinuxtype targeted
%global moduletype contrib
%global modulename authlogin_duo
%bcond_with tests
Name:           duo_unix
Version:        2.2.3
Release:        1%{?dist}
Summary:        Duo two-factor authentication for UNIX systems
License:        GPL-2.0-with-classpath-exception AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND BSD-4-Clause AND FSFAP AND FSFULLR AND GPL-1.0-only AND LicenseRef-URLEnc-MIT AND MIT AND SSH-short
URL:            https://duo.com/
Source0:        https://dl.duosecurity.com/%{name}-%{version}.tar.gz
Suggests:       %{name}-doc = %{version}-%{release}
%if %{with tests}
%endif
Recommends:     pam_duo = %{version}-%{release}
# oreon:deps
BuildRequires:  bzip2
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(systemd)
BuildRequires:  python3
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Duo provides simple two-factor authentication as a service via:

    1.  Phone callback
    2.  SMS-delivered one-time passcode
    3.  Duo mobile app to generate one-time passcode
    4.  Duo mobile app for smartphone push authentication
    5.  Duo hardware token to generate one-time passcode

This package allows an admin (or ordinary user) to quickly add Duo
authentication to any UNIX login without setting up secondary user
accounts, directory synchronization, servers, or hardware.

%package        doc
Summary:        Documentation and license files for %{name}
BuildArch:      noarch
%description    doc
Documentation and license files for %{name}

%package -n     pam_duo
Summary:        A PAM module for duo authentication
Suggests:       %{name}-doc = %{version}-%{release}
Requires:       pam
Requires:       (%{name}-selinux if selinux-policy-%{selinuxtype})
%description -n pam_duo
A PAM module for duo authentication

%package        devel
Summary:        Development files and documentation for duo_unix
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pam_duo%{?_isa} = %{version}-%{release}
%description    devel
Development files and documentation for duo_unix

%package        selinux
Summary:        SELinux rules for %{name}
Requires:       selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-%{selinuxtype}
Requires:       pam_duo%{?_isa} = %{version}-%{release}
%{?selinux_requires}
%description    selinux
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure \
  --with-pam=%{_libdir}/security \
  --sysconfdir=%{_sysconfdir}/duo \
  --includedir=%{_includedir}/duo \
  --with-debug=yes \
  %{nil}
%make_build
%make_build -C pam_duo semodule
%install
%make_install
%make_install -C pam_duo semodule-install
rm -r %{buildroot}%{_datadir}/LICENSES/
rm %{buildroot}%{_libdir}/security/pam_duo.la
%oreon_autofiles pam_duo usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with tests}
%check

make check
%endif
%pre selinux

%selinux_relabel_pre -s %{selinuxtype}
%post selinux

%selinux_modules_install %{_datadir}/selinux/packages/%{modulename}.pp.bz2
%postun selinux

if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall %{_datadir}/selinux/packages/%{modulename}.pp.bz2
fi
%posttrans selinux

%selinux_relabel_post -s %{selinuxtype}
%files -f %{oreon_filedir}/main.list
%files -n duo_unix-doc -f %{oreon_filedir}/duo_unix-doc.list
%files -n pam_duo -f %{oreon_filedir}/pam_duo.list
%files -n duo_unix-devel -f %{oreon_filedir}/duo_unix-devel.list
%files -n duo_unix-selinux -f %{oreon_filedir}/duo_unix-selinux.list

%changelog

%autochangelog
