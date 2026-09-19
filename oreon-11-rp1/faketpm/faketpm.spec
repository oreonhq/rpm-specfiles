%global source0_hash 53e0fc3602ccf03e9eecb8650c5091be65499151169bfb0ab17228af296948c4

Name:           faketpm
Version:        0.0.1
Release:        %autorelease
Summary:        Fake TPM for systems that lack a real one

License:        BSD-3-Clause
URL:            https://github.com/davide125/faketpm
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  bzip2
BuildRequires:  make
BuildRequires:  selinux-policy-devel
BuildRequires:  systemd-rpm-macros

Requires:       kmod
Requires:       swtpm
Requires:       (%{name}-selinux = %{version}-%{release} if selinux-policy)

BuildArch:      noarch

%description
This project provides a fake Trusted Platform Module (TPM) for systems that
lack a real one. To do so it leverages SWTPM, a software TPM emulator.

%package        selinux
Summary:        SELinux module for %{name}

Requires(pre):  libselinux-utils
Requires(post): libselinux-utils
Requires(post): policycoreutils
Requires(post): selinux-policy-base
Requires(post): swtpm-selinux

%description    selinux
This package provides the SELinux policy module to ensure %{name}
runs properly under an environment with SELinux enabled.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%make_build

%install
%make_install DATADIR="%{_datadir}" UNITDIR="%{_unitdir}"

mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%pre selinux
%selinux_relabel_pre

%post selinux
%selinux_modules_install %{_datadir}/selinux/packages/%{name}.pp.bz2
%selinux_relabel_post

%posttrans selinux
%selinux_relabel_post

%postun selinux
%selinux_modules_uninstall %{name}
if [ $1 -eq 0 ]; then
    %selinux_relabel_post
fi

%files
%license LICENSE
%doc README.md
%attr(0750, tss,root) %dir %{_localstatedir}/lib/%{name}/
%{_unitdir}/%{name}.service

%files selinux
%license LICENSE
%{_datadir}/selinux/devel/include/contrib/%{name}.if
%{_datadir}/selinux/packages/%{name}.pp.bz2

%changelog
%autochangelog
