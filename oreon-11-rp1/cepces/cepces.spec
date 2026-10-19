%global source0_hash f0b3d4eccd683c964ea7df2b929a71c991b3f37c18710431b685948aaef9fec2
%bcond_without selinux
%global selinux_variants targeted
%global selinuxtype targeted
%global selinux_package_dir %{_datadir}/selinux/packages
%global logdir %{_localstatedir}/log/%{name}
%global modulename %{name}
Name:           cepces
Version:        0.5.0
Release:        1%{?dist}
Summary:        Certificate Enrollment through CEP/CES
License:        GPL-3.0-or-later
URL:            https://github.com/openSUSE/%{name}
Source0:        https://github.com/openSUSE/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       python%{python3_pkgversion}-%{name} = %{version}-%{release}
%if %{with selinux}
Requires:       (%{name}-selinux if selinux-policy-%{selinuxtype})
%endif
Recommends:     logrotate
Supplements:    %{name}-certmonger = %{version}-%{release}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-cepces = %{version}-%{release}
# /oreon:deps
%package -n       python3-cepces+user-submit
Summary:        Metapackage for python3-cepces user-submit extras
Requires:       python3-cepces = %{version}-%{release}
Provides:       python3dist(cepces[user-submit]) = %{version}-%{release}

%description -n python3-cepces+user-submit
Metapackage for python3-cepces user-submit extras.

%description
cepces is an application for enrolling certificates through CEP and CES.
It requires certmonger to operate.

Only simple deployments using Microsoft Active Directory Certificate Services
have been tested.

%package -n python%{python3_pkgversion}-%{name}
Summary:        Python part of %{name}
Requires:       krb5-libs
Requires(pre):  krb5-libs
Requires(post): krb5-libs
Recommends:     keyutils
Recommends:     pinentry
Recommends:     (pinentry-qt6 if plasma-workspace)
%description -n python%{python3_pkgversion}-%{name}
%{name} is an application for enrolling certificates through CEP and CES.
This package provides the Python part for CEP and CES interaction.

%package certmonger
Summary:        certmonger integration for %{name}
Requires(pre):  %{name} = %{version}-%{release}
Requires:       certmonger
%description certmonger
Installing %{name}-certmonger adds %{name} as a CA configuration.
Uninstall revert the action.

%if %{with selinux}
%package selinux
Summary:        SELinux support for %{name}
BuildRequires:  selinux-policy-devel
Requires:       %{name} = %{version}-%{release}
Requires:       selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-%{selinuxtype}
%description selinux
SELinux support for %{name}
# endif with selinux
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%if %{with selinux}
for SELINUXVARIANT in %{selinux_variants}; do
    make %{?_smp_mflags} -C selinux clean all
    mv -v selinux/%{modulename}.pp selinux/%{modulename}-${SELINUXVARIANT}.pp
done
%endif
%install
%pyproject_install
install -d -m0755 %{buildroot}%{logdir}
%if %{with selinux}
rm -fv selinux-files.txt
for SELINUXVARIANT in %{selinux_variants}; do
    install -d -m 755 %{buildroot}%{selinux_package_dir}/${SELINUXVARIANT}
    bzip2 selinux/%{modulename}-${SELINUXVARIANT}.pp
    MODULE_PATH=%{selinux_package_dir}/${SELINUXVARIANT}/%{modulename}.pp.bz2
    install -p -m 644 selinux/%{name}-${SELINUXVARIANT}.pp.bz2 \
      %{buildroot}${MODULE_PATH}
    echo ${MODULE_PATH} >> selinux-files.txt
done
%endif
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}/
install -m 644  conf/cepces.conf.dist  %{buildroot}%{_sysconfdir}/%{name}/cepces.conf
install -m 644  conf/logging.conf.dist %{buildroot}%{_sysconfdir}/%{name}/logging.conf
install -d -m 0755 %{buildroot}%{_sysconfdir}/logrotate.d
cat <<EOF>%{buildroot}%{_sysconfdir}/logrotate.d/%{name}
/var/log/%{name}/*.log {
    compress
    delaycompress
    missingok
    rotate 4
}
EOF
%oreon_autofiles python3-cepces usr/lib/python3*/site-packages/cepces* usr/lib64/python3*/site-packages/cepces* usr/bin/*
%oreon_autofiles cepces-certmonger usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cepces-selinux usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/lib/python3*/site-packages/cepces* usr/lib64/python3*/site-packages/cepces* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pyproject_check_import
%pytest
%if %{with selinux}
%pre selinux

for SELINUXVARIANT in %{selinux_variants}; do
    %selinux_relabel_pre -s ${SELINUXVARIANT}
done
%post selinux

for SELINUXVARIANT in %{selinux_variants}; do
    MODULE_PATH=%{selinux_package_dir}/${SELINUXVARIANT}/%{modulename}.pp.bz2
    %selinux_modules_install -s ${SELINUXVARIANT} ${MODULE_PATH}
done
%postun selinux

if [ $1 -eq 0 ]; then
    for SELINUXVARIANT in %{selinux_variants}; do
        %selinux_modules_uninstall -s ${SELINUXVARIANT} %{modulename}
    done
fi
%posttrans selinux

for SELINUXVARIANT in %{selinux_variants}; do
    %selinux_relabel_post -s ${SELINUXVARIANT}
done
%endif
%post certmonger

if [[ "$1" == "1" ]]; then
    getcert add-ca -c %{name} \
      -e %{_libexecdir}/certmonger/%{name}-submit --install >/dev/null || :
fi
%preun certmonger

if [[ "$1" == "0" ]]; then
    getcert remove-ca -c %{name} >/dev/null || :
fi
%files
%files -n python3-cepces -f %{oreon_filedir}/python3-cepces.list
%files -n cepces-certmonger -f %{oreon_filedir}/cepces-certmonger.list
%files -n cepces-selinux -f %{oreon_filedir}/cepces-selinux.list

%changelog

%autochangelog
