%global source0_hash 0de478fcf326f25d931938c3744e61c5cd67596b46e5b1e3bb2abf99d5445632

# tests currently fail in a way that stalls Koji
#
# test_unpredictable_token_factory (mailman.utilities.tests.test_uid.TestUID.test_unpredictable_token_factory) ... ok
# /builddir/build/BUILD/mailman3-3.3.10-build/mailman-3.3.10/venv/bin/python: can't open file '/builddir/build/BUILD/mailman3-3.3.10-build/mailman-3.3.10/venv/bin/runner': [Errno 2] No such file or directory
# /builddir/build/BUILD/mailman3-3.3.10-build/mailman-3.3.10/venv/bin/python: can't open file '/builddir/build/BUILD/mailman3-3.3.10-build/mailman-3.3.10/venv/bin/runner': [Errno 2] No such file or directory
# Exception in thread Thread-7 (loop):
# Traceback (most recent call last):
#   File "/usr/lib64/python3.14/threading.py", line 1081, in _bootstrap_inner
#     self._context.run(self.run)
#     ~~~~~~~~~~~~~~~~~^^^^^^^^^^
#   File "/usr/lib64/python3.14/threading.py", line 1023, in run
#     self._target(*self._args, **self._kwargs)
#     ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/builddir/build/BUILD/mailman3-3.3.10-build/mailman-3.3.10/src/mailman/testing/helpers.py", line 203, in loop
#     self.start_check()
#     ~~~~~~~~~~~~~~~~^^
#   File "/builddir/build/BUILD/mailman3-3.3.10-build/mailman-3.3.10/src/mailman/rest/tests/test_membership.py", line 675, in _wait_for_both
#     cls.client = get_lmtp_client(quiet=True)
#                  ~~~~~~~~~~~~~~~^^^^^^^^^^^^
#   File "/builddir/build/BUILD/mailman3-3.3.10-build/mailman-3.3.10/src/mailman/testing/helpers.py", line 241, in get_lmtp_client
#     raise RuntimeError('Connection refused')
# RuntimeError: Connection refused
%bcond tests 0

%if %{defined rhel} && 0%{?rhel} <= 9
%bcond downgrade_deps 1
%else
%bcond downgrade_deps 0
%endif

%global pypi_name mailman

%global baseversion 3.3.10
#global prerelease rc2

Name:           mailman3
Version:        %{baseversion}%{?prerelease:~%{prerelease}}
Release:        3%{?dist}
Summary:        The GNU mailing list manager

License:        GPL-3.0-or-later
URL:            http://www.list.org
Source0:        https://pypi.python.org/packages/source/m/%{pypi_name}/%{pypi_name}-%{baseversion}%{?prerelease}.tar.gz
Source1:        mailman3.cfg
Source2:        mailman3-tmpfiles.conf
Source3:        mailman3.service
Source4:        mailman3.logrotate
Source5:        mailman3-digests.service
Source6:        mailman3-digests.timer
Source7:        mailman3-sysusers.conf
# Fix the package name for the Python >= 3.13 nntplib requirement
Patch:          mailman3-fix-pyproject-escaping.diff
# rebased from https://gitlab.com/mailman/mailman/-/commit/3a22537382d41ab3e46b859054547755963b069d.patch
Patch:          mailman3-py313-nntplib.diff
# Fix for removal of contextmanager support in pathlib
Patch:          https://gitlab.com/mailman/mailman/-/merge_requests/1309.patch#/mailman3-py313-pathlib.diff

BuildArch:      noarch

# Ensure that tests will work...
BuildRequires:  glibc-langpack-en

BuildRequires:  python3-devel >= 3.5
BuildRequires:  python3-setuptools
BuildRequires:  pyproject-rpm-macros

# SELinux https://fedoraproject.org/wiki/SELinux/IndependentPolicy#Creating_the_Spec_File
Provides:  %{name}-selinux == %{version}-%{release}
%global selinux_variants mls targeted
Requires: selinux-policy %{?_selinux_policy_version: >= %{_selinux_policy_version}}
BuildRequires: git-core
BuildRequires: pkgconfig(systemd)
BuildRequires: selinux-policy
BuildRequires: selinux-policy-devel
Requires(post): selinux-policy-base %{?_selinux_policy_version: >= %{_selinux_policy_version}}
Requires(post): libselinux-utils
Requires(post): policycoreutils
Requires(post): policycoreutils-python-utils
# SELinux https://fedoraproject.org/wiki/SELinux_Policy_Modules_Packaging_Draft
BuildRequires:  checkpolicy, selinux-policy-devel
BuildRequires:  hardlink

# Scriptlets
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}

%if %{with downgrade_deps}
BuildRequires:  sed
%endif

%description
This is GNU Mailman, a mailing list management system distributed under the
terms of the GNU General Public License (GPL) version 3 or later.  The name of
this software is spelled 'Mailman' with a leading capital 'M' but with a lower
case second `m'.  Any other spelling is incorrect.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{baseversion}%{?prerelease}

%if %{with downgrade_deps}
# Downgrade a few dependencies to satisfiable compatible versions
sed -e "s/flufl.i18n>=3.2/flufl.i18n>=2.0/" \
    -i pyproject.toml
%endif

# SELinux
mkdir SELinux
echo '%{_localstatedir}/lib/%{name}/data(/.*)? gen_context(system_u:object_r:etc_mail_t,s0)' \
    > SELinux/%{name}.fc
# remember to bump the following version if the policy is updated
cat > SELinux/%{name}.te << EOF
policy_module(%{name}, 1.4)
EOF

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

cd SELinux
for selinuxvariant in %{selinux_variants}; do
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile
  mv %{name}.pp %{name}.pp.${selinuxvariant}
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile clean
done
cd -

%install
%pyproject_install
# license file is actually copied in but not tagged as license
# make build fails when this changes so we know to change it
# to -l
%pyproject_save_files -L %{pypi_name}

# move scripts away from _bindir to avoid conflicts and create a wrapper script
mkdir -p %{buildroot}%{_libexecdir}/%{name}
mv %{buildroot}%{_bindir}/* %{buildroot}%{_libexecdir}/%{name}/
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
if [ "\$(whoami)" != "mailman" ]; then
    echo "This command must be run under the mailman user."
    exit 1
fi
%{_libexecdir}/%{name}/mailman \$@
EOF
chmod +x %{buildroot}%{_bindir}/%{name}
echo "%{_bindir}/%{name}" >> %{pyproject_files}
echo "%%dir %{_libexecdir}/%{name}" >> %{pyproject_files}
echo "%{_libexecdir}/%{name}/mailman" >> %{pyproject_files}
echo "%{_libexecdir}/%{name}/master" >> %{pyproject_files}
echo "%{_libexecdir}/%{name}/runner" >> %{pyproject_files}

# service files
install -D -m 0640 %{SOURCE1} %{buildroot}%{_sysconfdir}/mailman.cfg
install -D -m 0644 %{SOURCE2} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -D -m 0644 %{SOURCE7} %{buildroot}%{_sysusersdir}/%{name}.conf
install -D -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}.service
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d/
sed -e 's,@LOGDIR@,%{_localstatedir}/log/%{name},g;s,@BINDIR@,%{_bindir},g' \
    %{SOURCE4} > %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
# periodic task
install -D -m 0644 %{SOURCE5} %{buildroot}%{_unitdir}/%{name}-digests.service
install -D -m 0644 %{SOURCE6} %{buildroot}%{_unitdir}/%{name}-digests.timer

mkdir -p %{buildroot}%{_localstatedir}/{lib,spool,log}/%{name}
mkdir -p %{buildroot}/run/%{name} %{buildroot}/run/lock/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}.d
# Mailman will auto-create the following dir, but not with the correct group
# owner (MTAs such as Postfix must read and write to it). Set it here in RPM's
# file listing.
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}/data

# SELinux
for selinuxvariant in %{selinux_variants}; do
  install -d %{buildroot}%{_datadir}/selinux/${selinuxvariant}
  install -p -m 644 SELinux/%{name}.pp.${selinuxvariant} \
    %{buildroot}%{_datadir}/selinux/${selinuxvariant}/%{name}.pp
done
hardlink -cv %{buildroot}%{_datadir}/selinux

%check
# alembic's is_offline_mode does not work without proper
# initialization; _proxy not defined
# the mailman.rest.* modules transitively imports mailman.rest.users which does not work
# for a similar but different reason
#   File "/builddir/build/BUILD/mailman3-3.3.10-build/BUILDROOT/usr/lib/python3.13/site-packages/mailman/rest/users.py", line 61, in __init__
#     super().__init__(config.password_context.encrypt)
#                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# AttributeError: 'NoneType' object has no attribute 'encrypt'
%pyproject_check_import -e mailman.database.alembic.env -e mailman.rest.domains -e mailman.rest.gunicorn -e mailman.rest.root -e mailman.rest.users -e mailman.rest.wsgiapp -e mailman.runners.rest

%if %{with tests}
# tests need a proper locale
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
# Mailman3 can only be tested when its installed (it starts runners and won't
# find the buildroot), so we use a venv
%python3 -m venv --system-site-packages --without-pip --clear venv
# Tests fail with nspawn mock due to lack of access to /dev/stdout
# TODO: Figure out a fix for this
venv/bin/python -m nose2 -v || :
%endif

%pre
# SELinux
for selinuxvariant in %{selinux_variants}; do
    %selinux_relabel_pre -s ${selinuxvariant}
done

%post
# Service
%systemd_post %{name}.service %{name}-digests.timer
# SELinux
for selinuxvariant in %{selinux_variants}; do
    %selinux_modules_install -s ${selinuxvariant} %{_datadir}/selinux/${selinuxvariant}/%{name}.pp || :
done

%preun
# Service
%systemd_preun %{name}.service %{name}-digests.timer

%postun
# Service
%systemd_postun_with_restart %{name}.service %{name}-digests.timer
# SELinux
if [ $1 -eq 0 ] ; then
  for selinuxvariant in %{selinux_variants}; do
    %selinux_modules_uninstall -s ${selinuxvariant} %{_datadir}/selinux/${selinuxvariant}/%{name}.pp || :
  done
fi

%posttrans
# SELinux
for selinuxvariant in %{selinux_variants}; do
    %selinux_relabel_post -s ${selinuxvariant}
done

%files -f %{pyproject_files}
%doc README.md
%license %{python3_sitelib}/mailman-%{version}.dist-info/licenses/COPYING
%{_unitdir}/*.service
%{_unitdir}/*.timer
%{_tmpfilesdir}/%{name}.conf
%{_sysusersdir}/%{name}.conf
%config(noreplace) %attr(640,mailman,mailman) %{_sysconfdir}/mailman.cfg
%dir %{_sysconfdir}/%{name}.d
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %attr(755,mailman,mailman) %{_localstatedir}/lib/%{name}
%dir %attr(2775,mailman,mail)   %{_localstatedir}/lib/%{name}/data
%dir %attr(755,mailman,mailman) %{_localstatedir}/spool/%{name}
%dir %attr(755,mailman,mailman) %{_localstatedir}/log/%{name}
%dir %attr(755,mailman,mailman) /run/%{name}
%dir %attr(755,mailman,mailman) /run/lock/%{name}
# SELinux
%doc SELinux/*
%{_datadir}/selinux/*/%{name}.pp

%changelog
%autochangelog
