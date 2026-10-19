%global source0_hash 23c425a4b45af243990db983d98717d4d066887df2c8ec2547b163e28a9da17c
%global source1_hash c4d12e0a9cb0c0a443b9c9cff07a1b8581e891d334e37273117334ddf2883a64
%global policy_version 43.1.1
%global with_selinux 1
%global selinuxtype targeted
Name:    keylime
Version: 7.14.3
Release:        1%{?dist}
Summary:        Open source TPM software for Bootstrapping and Maintaining Trust
URL:            https://github.com/keylime/keylime
Source0:        https://github.com/keylime/keylime/archive/refs/tags/v%{version}.tar.gz#/keylime-%{version}.tar.gz
Source1:        https://github.com/RedHat-SP-Security/%{name}-selinux/archive/refs/tags/v%{policy_version}.tar.gz#/keylime-selinux-%{policy_version}.tar.gz
Source2:        %{name}.sysusers
Source3:        %{name}.tmpfiles
Patch: 0002-Fix-efivar-availability-check-in-test_create_mb_poli.patch
License: Apache-2.0 AND MIT
BuildArch: noarch
Requires: python3-%{name} = %{version}-%{release}
Requires: %{name}-base = %{version}-%{release}
Requires: %{name}-verifier = %{version}-%{release}
Requires: %{name}-registrar = %{version}-%{release}
Requires: %{name}-tenant = %{version}-%{release}
Requires: %{name}-tools = %{version}-%{release}
Obsoletes: %{name}-webapp < 6.4.2
Obsoletes: python3-%{name}-agent < 7.0.0
Requires: keylime-agent
Suggests: %{name}-agent-rust
Conflicts: keylime < 6.3.0-3
%{?python_enable_dependency_generator}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 42
Requires:       python3-keylime = %{version}-%{release}
# /oreon:deps
%description
Keylime is a TPM based highly scalable remote boot attestation
and runtime integrity measurement solution.

%package base
Summary: The base package contains the default configuration
License: MIT
Conflicts: keylime < 6.3.0-3
Requires(pre): python3-jinja2
Requires: procps-ng
Requires: tpm2-tss
Requires: openssl
%if 0%{?with_selinux}
Recommends:       (%{name}-selinux = %{version}-%{release} if selinux-policy-%{selinuxtype})
%endif
%{lua:
  for i in string.gmatch(rpm.expand("%efi"):gsub("_","-"), "%S+") do
    print('Requires: (efivar-libs if filesystem('..i..'))\n')
  end
}
%description base
The base package contains the Keylime default configuration

%package -n python3-%{name}
Summary: The Python Keylime module
License: MIT
Conflicts: keylime < 6.3.0-3
Requires: %{name}-base = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}}
Requires: python3-tornado
Requires: python3-sqlalchemy
Requires: python3-alembic
Requires: python3-cryptography
Requires: python3-pyyaml
Requires: python3-packaging
Requires: python3-requests
Requires: python3-gpg
Requires: python3-lark
Requires: python3-pyasn1
Requires: python3-pyasn1-modules
Requires: python3-psutil
Requires: python3-jsonschema
Requires: python3-typing-extensions
Requires: tpm2-tools
%description -n python3-%{name}
The python3-keylime module implements the functionality used
by Keylime components.

%package verifier
Summary: The Python Keylime Verifier component
License: MIT
Conflicts: keylime < 6.3.0-3
Requires: %{name}-base = %{version}-%{release}
Requires: python3-%{name} = %{version}-%{release}
%description verifier
The Keylime Verifier continuously verifies the integrity state
of the machine that the agent is running on.

%package registrar
Summary: The Keylime Registrar component
License: MIT
Conflicts: keylime < 6.3.0-3
Requires: %{name}-base = %{version}-%{release}
Requires: python3-%{name} = %{version}-%{release}
%description registrar
The Keylime Registrar is a database of all agents registered
with Keylime and hosts the public keys of the TPM vendors.

%if 0%{?with_selinux}
# SELinux subpackage
%package selinux
Summary:             keylime SELinux policy
Requires:            selinux-policy-%{selinuxtype}
Requires(post):      selinux-policy-%{selinuxtype}
BuildRequires:       selinux-policy-devel
%{?selinux_requires}
%description selinux
Custom SELinux policy module
%endif

%package tenant
Summary: The Python Keylime Tenant
License: MIT
Conflicts: keylime < 6.3.0-3
Requires: %{name}-base = %{version}-%{release}
Requires: python3-%{name} = %{version}-%{release}
%description tenant
The Keylime Tenant can be used to provision a Keylime Agent.

%package tools
Summary: Keylime tools
License: MIT
Conflicts: keylime < 6.3.0-3
Requires: %{name}-base = %{version}-%{release}
Requires: python3-%{name} = %{version}-%{release}
%description tools
The keylime tools package includes miscelaneous tools.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%if 0%{?with_selinux}
make -f %{_datadir}/selinux/devel/Makefile %{name}.pp
bzip2 -9 %{name}.pp
%endif
%pyproject_wheel
mkdir -p manpages
rst2man --syntax-highlight=none docs/man/keylime_tenant.1.rst manpages/keylime_tenant.1
rst2man --syntax-highlight=none docs/man/keylime-policy.1.rst manpages/keylime-policy.1
rst2man --syntax-highlight=none docs/man/keylime_registrar.8.rst manpages/keylime_registrar.8
rst2man --syntax-highlight=none docs/man/keylime_verifier.8.rst manpages/keylime_verifier.8
%install
%pyproject_install
mkdir -p %{buildroot}/%{_sharedstatedir}/%{name}
mkdir -p --mode=0700 %{buildroot}/%{_rundir}/%{name}
mkdir -p --mode=0700 %{buildroot}/%{_sysconfdir}/%{name}/
for comp in "verifier" "tenant" "registrar" "ca" "logging"; do
    mkdir -p --mode=0700  %{buildroot}/%{_sysconfdir}/%{name}/${comp}.conf.d
    install -Dpm 400 config/${comp}.conf %{buildroot}/%{_sysconfdir}/%{name}
done
mkdir -p %{buildroot}/%{_datadir}/%{name}/scripts
for s in create_runtime_policy.sh \
         create_mb_refstate \
         ek-openssl-verify \
         keylime_oneshot_attestation; do
    install -Dpm 755 scripts/${s} \
        %{buildroot}/%{_datadir}/%{name}/scripts/${s}
done
cp -r ./templates %{buildroot}%{_datadir}/%{name}/templates/
mkdir -p --mode=0755 %{buildroot}/%{_bindir}
install -Dpm 755 ./keylime/cmd/convert_config.py %{buildroot}/%{_bindir}/keylime_upgrade_config
%if 0%{?with_selinux}
install -D -m 0644 %{name}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
install -D -p -m 0644 keylime-selinux-%{policy_version}/%{name}.if %{buildroot}%{_datadir}/selinux/devel/include/distributed/%{name}.if
%endif
install -Dpm 644 ./services/%{name}_verifier.service \
    %{buildroot}%{_unitdir}/%{name}_verifier.service
install -Dpm 644 ./services/%{name}_registrar.service \
    %{buildroot}%{_unitdir}/%{name}_registrar.service
for cert_store_dir in %{_datadir} %{_sharedstatedir}; do
    mkdir -p %{buildroot}/"${cert_store_dir}"/%{name}
    cp -r ./tpm_cert_store %{buildroot}/"${cert_store_dir}"/%{name}/
done
install -p -D -m 0644 %{SOURCE2} %{buildroot}/%{_sysusersdir}/%{name}.conf
install -p -D -m 0644 %{SOURCE3} %{buildroot}/%{_tmpfilesdir}/%{name}.conf
install -d %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_mandir}/man8
install -m 644 manpages/keylime_tenant.1 %{buildroot}%{_mandir}/man1/
install -m 644 manpages/keylime-policy.1 %{buildroot}%{_mandir}/man1/
install -m 644 manpages/keylime_registrar.8 %{buildroot}%{_mandir}/man8/
install -m 644 manpages/keylime_verifier.8 %{buildroot}%{_mandir}/man8/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/lib/python3*/site-packages/keylime* usr/lib64/python3*/site-packages/keylime* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

CONF_TEMP_DIR="$(mktemp -d)"
%{python3} -m keylime.cmd.convert_config --out "${CONF_TEMP_DIR}" --templates templates/
export KEYLIME_VERIFIER_CONFIG="${CONF_TEMP_DIR}/verifier.conf"
export KEYLIME_TENANT_CONFIG="${CONF_TEMP_DIR}/tenant.conf"
export KEYLIME_REGISTRAR_CONFIG="${CONF_TEMP_DIR}/registrar.conf"
export KEYLIME_CA_CONFIG="${CONF_TEMP_DIR}/ca.conf"
export KEYLIME_LOGGING_CONFIG="${CONF_TEMP_DIR}/logging.conf"
PYTHONPATH="%{buildroot}%{python3_sitelib}:$(pwd)" %{python3} -m unittest
[ "${CONF_TEMP_DIR}" ] && rm -rf "${CONF_TEMP_DIR}"
for e in KEYLIME_VERIFIER_CONFIG \
         KEYLIME_TENANT_CONFIG \
         KEYLIME_REGISTRAR_CONFIG \
         KEYLIME_CA_CONFIG \
         KEYLIME_LOGGING_CONFIG; do
    unset "${e}"
done
%pre base

%sysusers_create_compat %{SOURCE2}
exit 0
%post base

for c in ca logging; do
    [ -e /etc/keylime/"${c}.conf" ] || continue
    /usr/bin/keylime_upgrade_config --component "${c}" \
                                    --input /etc/keylime/"${c}.conf" \
                                    >/dev/null
done
exit 0
%posttrans base

if [ -d %{_sysconfdir}/%{name} ]; then
    chmod 500 %{_sysconfdir}/%{name}
    chown -R %{name}:%{name} %{_sysconfdir}/%{name}
    for comp in "verifier" "tenant" "registrar" "ca" "logging"; do
        [ -d %{_sysconfdir}/%{name}/${comp}.conf.d ] && \
            chmod 500 %{_sysconfdir}/%{name}/${comp}.conf.d
    done
fi
[ -d %{_sharedstatedir}/%{name} ] && \
    chown -R %{name} %{_sharedstatedir}/%{name}/
[ -d %{_sharedstatedir}/%{name}/tpm_cert_store ] && \
    chmod 400 %{_sharedstatedir}/%{name}/tpm_cert_store/*.pem && \
    chmod 500 %{_sharedstatedir}/%{name}/tpm_cert_store/
[ -d %{_localstatedir}/log/%{name} ] && \
    chown -R %{name} %{_localstatedir}/log/%{name}/
exit 0
%post verifier

[ -e /etc/keylime/verifier.conf ] && \
    /usr/bin/keylime_upgrade_config --component verifier \
                                    --input /etc/keylime/verifier.conf \
                                    >/dev/null
%systemd_post %{name}_verifier.service
exit 0
%post registrar

[ -e /etc/keylime/registrar.conf ] && \
    /usr/bin/keylime_upgrade_config --component registrar \
                                    --input /etc/keylime/registrar.conf /
                                    >/dev/null
%systemd_post %{name}_registrar.service
exit 0
%post tenant

[ -e /etc/keylime/tenant.conf ] && \
    /usr/bin/keylime_upgrade_config --component tenant \
                                    --input /etc/keylime/tenant.conf \
                                    >/dev/null
exit 0
%preun verifier

%systemd_preun %{name}_verifier.service
%preun registrar

%systemd_preun %{name}_registrar.service
%postun verifier

%systemd_postun_with_restart %{name}_verifier.service
%postun registrar

%systemd_postun_with_restart %{name}_registrar.service
%if 0%{?with_selinux}
%pre selinux

%selinux_relabel_pre -s %{selinuxtype}
%post selinux

%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
%selinux_relabel_post -s %{selinuxtype}
if [ "$1" -le "1" ]; then # First install
    for svc in registrar verifier; do
        [ -f "%{_unitdir}/%{name}_${svc}".service ] && \
            %systemd_postun_with_restart "%{name}_${svc}".service
    done
fi
exit 0
%postun selinux

if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{name}
    %selinux_relabel_post -s %{selinuxtype}
fi
%endif
%files
%files -n keylime-base -f %{oreon_filedir}/keylime-base.list
%files -n python3-keylime -f %{oreon_filedir}/python3-keylime.list
%files -n keylime-verifier -f %{oreon_filedir}/keylime-verifier.list
%files -n keylime-registrar -f %{oreon_filedir}/keylime-registrar.list
%files -n keylime-selinux -f %{oreon_filedir}/keylime-selinux.list
%files -n keylime-tenant -f %{oreon_filedir}/keylime-tenant.list
%files -n keylime-tools -f %{oreon_filedir}/keylime-tools.list

%changelog

%autochangelog
