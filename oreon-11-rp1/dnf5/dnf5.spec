# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 242f0e775bc8e1017a5bfec841c776beafa7ea6b5bd2e4d7bc0ff9d7c57998f3

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global project_version_prime 5
%global project_version_major 4
%global project_version_minor 6
%global project_version_micro 0

# ========== build options ==========

# Toolchain
%bcond_with    clang
%bcond_with    sanitizers

# Core features
%bcond dnf5_obsoletes_dnf 1
%bcond_without acl
%bcond_without comps
%bcond_without modulemd
%bcond_without systemd
%bcond_without focus_new

# Main components
%bcond_without dnf5
%bcond_without dnf5daemon_client
%bcond_without dnf5daemon_server
%bcond_without libdnf_cli

# Plugins
%bcond_without dnf5_plugins
%bcond_without plugin_actions
%bcond_without plugin_appstream
%bcond_without plugin_expired_pgp_keys
%bcond_without plugin_local
%bcond_without plugin_manifest
%bcond_without plugin_rhsm
%if %{with systemd}
%bcond_without plugin_systemd_inhibit
%else
%bcond_with    plugin_systemd_inhibit
%endif
%bcond_without python_plugins_loader

# Documentation
%bcond_with    html
%bcond_without man

# Language bindings
# TODO Go bindings fail to build, disable for now
%bcond_with    go
%bcond_without perl5
%bcond_without python3
%bcond_without ruby

# Testing
%bcond_without tests
%bcond_with    performance_tests
%bcond_with    dnf5daemon_tests

%if %{with clang}
%global toolchain clang
%endif

Name:           dnf5
Version:        5.4.6.0
Release:        1%{?dist}
Summary:        Command-line package manager
License:        GPL-2.0-or-later
URL:            https://github.com/rpm-software-management/dnf5
Source0:        https://github.com/rpm-software-management/dnf5/archive/%{version}/dnf5-%{version}.tar.gz

Requires:       libdnf5%{?_isa} = %{version}-%{release}
Requires:       libdnf5-cli%{?_isa} = %{version}-%{release}
%if %{without dnf5_obsoletes_dnf}
Requires:       dnf-data
%endif
Recommends:     (dnf5-plugins if dnf-plugins-core)
Recommends:     bash-completion
Requires:       coreutils
Recommends:     (libdnf5-plugin-expired-pgp-keys if gnupg2)

Provides:       microdnf = %{version}-%{release}
Obsoletes:      microdnf < 4

%if %{with dnf5_obsoletes_dnf}
Provides:       dnf = %{version}-%{release}
Obsoletes:      dnf < 5

Provides:       yum = %{version}-%{release}
Obsoletes:      yum < 5

Conflicts:      python3-dnf-plugins-core < 4.7.0
%endif

Provides:       dnf5-command(advisory) = %{version}-%{release}
Provides:       dnf5-command(autoremove) = %{version}-%{release}
Provides:       dnf5-command(check) = %{version}-%{release}
Provides:       dnf5-command(check-upgrade) = %{version}-%{release}
Provides:       dnf5-command(clean) = %{version}-%{release}
Provides:       dnf5-command(debuginfo-install) = %{version}-%{release}
Provides:       dnf5-command(distro-sync) = %{version}-%{release}
Provides:       dnf5-command(downgrade) = %{version}-%{release}
Provides:       dnf5-command(download) = %{version}-%{release}
Provides:       dnf5-command(environment) = %{version}-%{release}
Provides:       dnf5-command(group) = %{version}-%{release}
Provides:       dnf5-command(history) = %{version}-%{release}
Provides:       dnf5-command(info) = %{version}-%{release}
Provides:       dnf5-command(install) = %{version}-%{release}
Provides:       dnf5-command(leaves) = %{version}-%{release}
Provides:       dnf5-command(list) = %{version}-%{release}
Provides:       dnf5-command(makecache) = %{version}-%{release}
Provides:       dnf5-command(mark) = %{version}-%{release}
%if %{with modulemd}
Provides:       dnf5-command(module) = %{version}-%{release}
%endif
Provides:       dnf5-command(offline) = %{version}-%{release}
Provides:       dnf5-command(provides) = %{version}-%{release}
Provides:       dnf5-command(reinstall) = %{version}-%{release}
Provides:       dnf5-command(replay) = %{version}-%{release}
Provides:       dnf5-command(remove) = %{version}-%{release}
Provides:       dnf5-command(repo) = %{version}-%{release}
Provides:       dnf5-command(repoquery) = %{version}-%{release}
Provides:       dnf5-command(search) = %{version}-%{release}
Provides:       dnf5-command(swap) = %{version}-%{release}
Provides:       dnf5-command(system-upgrade) = %{version}-%{release}
Provides:       dnf5-command(upgrade) = %{version}-%{release}
Provides:       dnf5-command(versionlock) = %{version}-%{release}


# ========== versions of dependencies ==========

%if %{with modulemd}
%global libmodulemd_version 2.5.0
%endif
%global librepo_version 1.20.0
%global libsolv_version 0.7.36
%global sqlite_version 3.35.0
%global swig_version 4.3


# ========== build requires ==========

BuildRequires:  bash-completion-devel
BuildRequires:  cmake >= 3.22
BuildRequires:  doxygen
BuildRequires:  gettext
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(librepo) >= %{librepo_version}
BuildRequires:  pkgconfig(libsolv) >= %{libsolv_version}
BuildRequires:  pkgconfig(libsolvext) >= %{libsolv_version}
BuildRequires:  pkgconfig(rpm) >= 4.19.0
BuildRequires:  pkgconfig(sqlite3) >= %{sqlite_version}
BuildRequires:  toml11-static
BuildRequires:  zlib-devel

%if %{with acl}
BuildRequires:  pkgconfig(libacl)
%endif

%if %{with clang}
BuildRequires:  clang
%else
BuildRequires:  gcc-c++ >= 14.1
%endif

%if %{with tests}
BuildRequires:  createrepo_c
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  rpm-build
%endif

%if %{with modulemd}
BuildRequires:  pkgconfig(modulemd-2.0) >= %{libmodulemd_version}
%endif

%if %{with systemd}
BuildRequires:  pkgconfig(sdbus-c++) >= 0.8.1
BuildRequires:  systemd-devel

 # We need to get the SYSTEMD_SYSTEM_UNIT_DIR from
 # /usr/share/pkgconfig/systemd.pc
BuildRequires:  systemd
%endif

%if %{with html} || %{with man}
BuildRequires:  python3dist(breathe)
BuildRequires:  python3dist(sphinx) >= 4.1.2
BuildRequires:  python3dist(sphinx-autoapi)
BuildRequires:  python3dist(sphinx-rtd-theme)
%endif

%if %{with sanitizers}
# compiler-rt is required by sanitizers in clang
BuildRequires:  compiler-rt
BuildRequires:  libasan
BuildRequires:  liblsan
BuildRequires:  libubsan
%endif

%if %{with libdnf_cli}
# required for libdnf5-cli
BuildRequires:  pkgconfig(smartcols)
%endif

%if %{with dnf5_plugins}
BuildRequires:  libcurl-devel >= 7.62.0
%if %{with plugin_manifest}
BuildRequires:  pkgconfig(libpkgmanifest)
%endif
%endif

%if %{with dnf5daemon_server}
# required for dnf5daemon-server
BuildRequires:  pkgconfig(sdbus-c++) >= 0.9.0
BuildRequires:  systemd-rpm-macros
%if %{with dnf5daemon_tests}
BuildRequires:  dbus-daemon
BuildRequires:  polkit
BuildRequires:  python3-devel
BuildRequires:  python3dist(dbus-python)
%endif
%endif

%if %{with plugin_rhsm}
BuildRequires:  pkgconfig(librhsm) >= 0.0.3
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
%endif

# ========== language bindings section ==========

%if %{with perl5} || %{with ruby} || %{with python3}
BuildRequires:  swig >= %{swig_version}
%endif

%if %{with perl5}
# required for perl-libdnf5 and perl-libdnf5-cli
BuildRequires:  perl-devel
BuildRequires:  perl-generators
%if %{with tests}
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(warnings)
BuildRequires:  perl(FindBin)
%endif
%endif

%if %{with ruby}
# required for ruby-libdnf5 and ruby-libdnf5-cli
BuildRequires:  pkgconfig(ruby)
%if %{with tests}
BuildRequires:  rubygem-test-unit
%endif
%endif

%if %{with python3}
# required for python3-libdnf5 and python3-libdnf5-cli
BuildRequires:  python3-devel
%endif

%description
DNF5 is a command-line package manager that automates the process of installing,
upgrading, configuring, and removing computer programs in a consistent manner.
It supports RPM packages%{?with_modulemd:, modulemd modules,} and comps groups & environments.

%post
%if %{with dnf5_obsoletes_dnf}
%systemd_post dnf-makecache.timer
%else
%systemd_post dnf5-makecache.timer
%endif

%preun
%if %{with dnf5_obsoletes_dnf}
%systemd_preun dnf-makecache.timer
%else
%systemd_preun dnf5-makecache.timer
%endif

%postun
%if %{with dnf5_obsoletes_dnf}
%systemd_postun_with_restart dnf-makecache.timer
%else
%systemd_postun_with_restart dnf5-makecache.timer
%endif

%files -f dnf5.lang
%{_bindir}/dnf5
%if %{with dnf5_obsoletes_dnf}
%{_bindir}/dnf
%{_bindir}/yum
%endif
%{_unitdir}/dnf*-makecache.service
%{_unitdir}/dnf*-makecache.timer

%{_bindir}/microdnf

%dir %{_sysconfdir}/dnf/dnf5-aliases.d
%doc %{_sysconfdir}/dnf/dnf5-aliases.d/README
%dir %{_datadir}/dnf5
%dir %{_datadir}/dnf5/aliases.d
%{_datadir}/dnf5/aliases.d/compatibility.conf
%dir %{_libdir}/dnf5
%dir %{_libdir}/dnf5/plugins
%dir %{_datadir}/dnf5/dnf5-plugins
%dir %{_sysconfdir}/dnf/dnf5-plugins
%doc %{_libdir}/dnf5/plugins/README
%dir %{_libdir}/libdnf5/plugins
%{bash_completions_dir}/dnf*
%{zsh_completions_dir}/_dnf5
%license COPYING.md
%license gpl-2.0.txt
%doc AUTHORS.md CHANGELOG.md CONTRIBUTING.md README.md
%if %{with man}
%{_mandir}/man8/dnf5.8.*
%{_mandir}/man8/dnf5-advisory.8.*
%{_mandir}/man8/dnf5-autoremove.8.*
%{_mandir}/man8/dnf5-check.8.*
%{_mandir}/man8/dnf5-check-upgrade.8.*
%{_mandir}/man8/dnf5-clean.8.*
%{_mandir}/man8/dnf5-debuginfo-install.8.*
%{_mandir}/man8/dnf5-distro-sync.8.*
%{_mandir}/man8/dnf5-do.8.*
%{_mandir}/man8/dnf5-downgrade.8.*
%{_mandir}/man8/dnf5-download.8.*
%{_mandir}/man8/dnf5-environment.8.*
%{_mandir}/man8/dnf5-group.8.*
%{_mandir}/man8/dnf5-history.8.*
%{_mandir}/man8/dnf5-info.8.*
%{_mandir}/man8/dnf5-install.8.*
%{_mandir}/man8/dnf5-leaves.8.*
%{_mandir}/man8/dnf5-list.8.*
%{_mandir}/man8/dnf5-makecache.8.*
%{_mandir}/man8/dnf5-mark.8.*
%{_mandir}/man8/microdnf.8.*
%if %{with modulemd}
%{_mandir}/man8/dnf5-module.8.*
%endif
%{_mandir}/man8/dnf5-offline.8.*
%{_mandir}/man8/dnf5-provides.8.*
%{_mandir}/man8/dnf5-reinstall.8.*
%{_mandir}/man8/dnf5-remove.8.*
%{_mandir}/man8/dnf5-replay.8.*
%{_mandir}/man8/dnf5-repo.8.*
%{_mandir}/man8/dnf5-repoquery.8.*
%{_mandir}/man8/dnf5-search.8.*
%{_mandir}/man8/dnf5-status.8.*
%{_mandir}/man8/dnf5-swap.8.*
%{_mandir}/man8/dnf5-system-upgrade.8.*
%{_mandir}/man8/dnf5-upgrade.8.*
%{_mandir}/man8/dnf5-versionlock.8.*
%{_mandir}/man7/dnf5-aliases.7.*
%{_mandir}/man7/dnf5-caching.7.*
%{_mandir}/man7/dnf5-comps.7.*
%{_mandir}/man7/dnf5-filtering.7.*
%{_mandir}/man7/dnf5-forcearch.7.*
%{_mandir}/man7/dnf5-installroot.7.*
%if %{with modulemd}
%{_mandir}/man7/dnf5-modularity.7.*
%endif
%{_mandir}/man7/dnf5-specs.7.*
%{_mandir}/man7/dnf5-system-state.7.*
%{_mandir}/man7/dnf5-changes-from-dnf4.7.*
%{_mandir}/man5/dnf5.conf.5.*
%{_mandir}/man5/dnf5.conf-vendorpolicy*.5.*
%{_mandir}/man5/dnf5.conf-todo.5.*
%{_mandir}/man5/dnf5.conf-deprecated.5.*

%if %{with dnf5_obsoletes_dnf}
# dnf compatibility symlinks
%{_mandir}/man8/dnf.8.*
%{_mandir}/man8/dnf-advisory.8.*
%{_mandir}/man8/dnf-autoremove.8.*
%{_mandir}/man8/dnf-check.8.*
%{_mandir}/man8/dnf-check-upgrade.8.*
%{_mandir}/man8/dnf-clean.8.*
%{_mandir}/man8/dnf-debuginfo-install.8.*
%{_mandir}/man8/dnf-distro-sync.8.*
%{_mandir}/man8/dnf-do.8.*
%{_mandir}/man8/dnf-downgrade.8.*
%{_mandir}/man8/dnf-download.8.*
%{_mandir}/man8/dnf-environment.8.*
%{_mandir}/man8/dnf-group.8.*
%{_mandir}/man8/dnf-history.8.*
%{_mandir}/man8/dnf-info.8.*
%{_mandir}/man8/dnf-install.8.*
%{_mandir}/man8/dnf-leaves.8.*
%{_mandir}/man8/dnf-list.8.*
%{_mandir}/man8/dnf-makecache.8.*
%{_mandir}/man8/dnf-mark.8.*
%if %{with modulemd}
%{_mandir}/man8/dnf-module.8.*
%endif
%{_mandir}/man8/dnf-offline.8.*
%{_mandir}/man8/dnf-provides.8.*
%{_mandir}/man8/dnf-reinstall.8.*
%{_mandir}/man8/dnf-remove.8.*
%{_mandir}/man8/dnf-replay.8.*
%{_mandir}/man8/dnf-repo.8.*
%{_mandir}/man8/dnf-repoquery.8.*
%{_mandir}/man8/dnf-search.8.*
%{_mandir}/man8/dnf-status.8.*
%{_mandir}/man8/dnf-swap.8.*
%{_mandir}/man8/dnf-system-upgrade.8.*
%{_mandir}/man8/dnf-upgrade.8.*
%{_mandir}/man8/dnf-versionlock.8.*
%{_mandir}/man8/yum.8.*
%{_mandir}/man7/dnf-aliases.7.*
%{_mandir}/man7/dnf-caching.7.*
%{_mandir}/man7/dnf-comps.7.*
%{_mandir}/man7/dnf-filtering.7.*
%{_mandir}/man7/dnf-forcearch.7.*
%{_mandir}/man7/dnf-installroot.7.*
%if %{with modulemd}
%{_mandir}/man7/dnf-modularity.7.*
%endif
%{_mandir}/man7/dnf-specs.7.*
%{_mandir}/man7/dnf-system-state.7.*
%{_mandir}/man7/dnf-changes-from-dnf4.7.*
%{_mandir}/man5/dnf.conf.5.*
%{_mandir}/man5/dnf.conf-vendorpolicy*.5.*
%{_mandir}/man5/dnf.conf-todo.5.*
%{_mandir}/man5/dnf.conf-deprecated.5.*
%endif
%endif

%if %{with systemd}
%{_unitdir}/dnf5-offline-transaction.service
%{_unitdir}/dnf5-offline-transaction-cleanup.service
%{_unitdir}/system-update.target.wants/dnf5-offline-transaction.service
%endif

%if %{without dnf5_plugins}
%exclude %{_datadir}/dnf5/aliases.d/compatibility-plugins.conf
%exclude %{_datadir}/dnf5/aliases.d/compatibility-reposync.conf
%endif

# ========== libdnf5 ==========
%package -n libdnf5
Summary:        Package management library
License:        LGPL-2.1-or-later
Requires:       libsolv%{?_isa} >= %{libsolv_version}
Requires:       librepo%{?_isa} >= %{librepo_version}
Requires:       rpm-libs%{?_isa} >= 5.99.90
Requires:       sqlite-libs%{?_isa} >= %{sqlite_version}
Recommends:     (libdnf5-plugin-systemd-inhibit if systemd)
%if %{with dnf5_obsoletes_dnf}
Conflicts:      dnf-data < 4.20.0
%endif

%description -n libdnf5
Package management library.

%files -n libdnf5 -f libdnf5.lang
%if %{with dnf5_obsoletes_dnf}
%config(noreplace) %{_sysconfdir}/dnf/dnf.conf
%dir %{_sysconfdir}/dnf/vars
%dir %{_sysconfdir}/dnf/protected.d
%dir %{_sysconfdir}/dnf/usr-drift-protected-paths.d
%else
%exclude %{_sysconfdir}/dnf/dnf.conf
%endif
%ghost %attr(0644, root, root) %{_sysconfdir}/dnf/versionlock.toml
%dir %{_datadir}/dnf5/libdnf.conf.d
%dir %{_sysconfdir}/dnf/libdnf5.conf.d
%dir %{_datadir}/dnf5/repos.override.d
%dir %{_sysconfdir}/dnf/repos.override.d
%dir %{_sysconfdir}/dnf/libdnf5-plugins
%dir %{_datadir}/dnf5/repos.d
%dir %{_datadir}/dnf5/vars.d
%dir %{_datadir}/dnf5/vendors.d
%dir %{_datadir}/dnf5/libdnf.plugins.conf.d
%dir %{_sysconfdir}/dnf/vendors.d
%dir %{_sysconfdir}/dnf/suggest-reboot.d
%dir %{_datadir}/dnf5/suggest-reboot.d
%dir %{_libdir}/libdnf5
%{_libdir}/libdnf5.so.2*
%dir %{_prefix}/lib/sysimage/libdnf5
%attr(0755, root, root) %ghost %dir %{_prefix}/lib/sysimage/libdnf5/comps_groups
%attr(0755, root, root) %ghost %dir %{_prefix}/lib/sysimage/libdnf5/comps_groups/environments
%attr(0755, root, root) %ghost %dir %{_prefix}/lib/sysimage/libdnf5/comps_groups/groups
%verify(not md5 size mtime) %attr(0644, root, root) %ghost %{_prefix}/lib/sysimage/libdnf5/environments.toml
%verify(not md5 size mtime) %attr(0644, root, root) %ghost %{_prefix}/lib/sysimage/libdnf5/groups.toml
%if %{with modulemd}
%verify(not md5 size mtime) %attr(0644, root, root) %ghost %{_prefix}/lib/sysimage/libdnf5/modules.toml
%endif
%verify(not md5 size mtime) %attr(0644, root, root) %ghost %{_prefix}/lib/sysimage/libdnf5/nevras.toml
%attr(0755, root, root) %ghost %dir %{_prefix}/lib/sysimage/libdnf5/offline
%verify(not md5 size mtime) %attr(0644, root, root) %ghost %{_prefix}/lib/sysimage/libdnf5/offline/offline-transaction-state.toml
%attr(0755, root, root) %ghost %dir %{_prefix}/lib/sysimage/libdnf5/offline/packages
%verify(not md5 size mtime) %attr(0644, root, root) %ghost %{_prefix}/lib/sysimage/libdnf5/offline/transaction.json
%verify(not md5 size mtime) %attr(0644, root, root) %ghost %{_prefix}/lib/sysimage/libdnf5/packages.toml
%verify(not md5 size mtime) %attr(0644, root, root) %ghost %{_prefix}/lib/sysimage/libdnf5/system.toml
%verify(not md5 size mtime) %attr(0644, root, root) %ghost %{_prefix}/lib/sysimage/libdnf5/transaction_history.sqlite{,-shm,-wal}
%license lgpl-2.1.txt
%ghost %attr(0755, root, root) %dir %{_var}/cache/libdnf5
%{_tmpfilesdir}/libdnf5.conf
%attr(0755, root, root) %dir %{_sharedstatedir}/dnf
%verify(not md5 size mtime) %attr(0644, root, root) %{_sharedstatedir}/dnf/system-repo.lock

# ========== libdnf5-cli ==========

%if %{with libdnf_cli}
%package -n libdnf5-cli
Summary:        Library for working with a terminal in a command-line package manager
License:        LGPL-2.1-or-later
Requires:       libdnf5%{?_isa} = %{version}-%{release}

%description -n libdnf5-cli
Library for working with a terminal in a command-line package manager.

%files -n libdnf5-cli -f libdnf5-cli.lang
%{_libdir}/libdnf5-cli.so.3*
%license COPYING.md
%license lgpl-2.1.txt
%endif

# ========== dnf5-devel ==========

%package -n dnf5-devel
Summary:        Development files for dnf5
License:        LGPL-2.1-or-later
Requires:       dnf5%{?_isa} = %{version}-%{release}
Requires:       libdnf5-devel%{?_isa} = %{version}-%{release}
Requires:       libdnf5-cli-devel%{?_isa} = %{version}-%{release}

%description -n dnf5-devel
Development files for dnf5.

%files -n dnf5-devel
%{_includedir}/dnf5/
%license COPYING.md
%license lgpl-2.1.txt


# ========== libdnf5-devel ==========

%package -n libdnf5-devel
Summary:        Development files for libdnf
License:        LGPL-2.1-or-later
Requires:       libdnf5%{?_isa} = %{version}-%{release}
Requires:       libsolv-devel%{?_isa} >= %{libsolv_version}

%description -n libdnf5-devel
Development files for libdnf.

%files -n libdnf5-devel
%{_includedir}/libdnf5/
%dir %{_libdir}/libdnf5
%{_libdir}/libdnf5.so
%{_libdir}/pkgconfig/libdnf5.pc
%license COPYING.md
%license lgpl-2.1.txt


# ========== libdnf5-cli-devel ==========

%package -n libdnf5-cli-devel
Summary:        Development files for libdnf5-cli
License:        LGPL-2.1-or-later
Requires:       libdnf5-cli%{?_isa} = %{version}-%{release}

%description -n libdnf5-cli-devel
Development files for libdnf5-cli.

%files -n libdnf5-cli-devel
%{_includedir}/libdnf5-cli/
%{_libdir}/libdnf5-cli.so
%{_libdir}/pkgconfig/libdnf5-cli.pc
%license COPYING.md
%license lgpl-2.1.txt


# ========== perl-libdnf5 ==========

%if %{with perl5}
%package -n perl-libdnf5
Summary:        Perl 5 bindings for the libdnf library
License:        LGPL-2.1-or-later
Requires:       libdnf5%{?_isa} = %{version}-%{release}


%description -n perl-libdnf5
Perl 5 bindings for the libdnf library.

%files -n perl-libdnf5
%{perl_vendorarch}/libdnf5
%{perl_vendorarch}/auto/libdnf5
%license COPYING.md
%license lgpl-2.1.txt
%endif


# ========== perl-libdnf5-cli ==========

%if %{with perl5} && %{with libdnf_cli}
%package -n perl-libdnf5-cli
Summary:        Perl 5 bindings for the libdnf5-cli library
License:        LGPL-2.1-or-later
Requires:       libdnf5-cli%{?_isa} = %{version}-%{release}


%description -n perl-libdnf5-cli
Perl 5 bindings for the libdnf5-cli library.

%files -n perl-libdnf5-cli
%{perl_vendorarch}/libdnf5_cli
%{perl_vendorarch}/auto/libdnf5_cli
%license COPYING.md
%license lgpl-2.1.txt
%endif


# ========== python3-libdnf5 ==========

%if %{with python3}
%package -n python3-libdnf5
Summary:        Python 3 bindings for the libdnf5 library
License:        LGPL-2.1-or-later
Requires:       libdnf5%{?_isa} = %{version}-%{release}

%description -n python3-libdnf5
Python 3 bindings for the libdnf library.

%files -n python3-libdnf5
%{python3_sitearch}/libdnf5
%{python3_sitearch}/libdnf5-*.dist-info
%license COPYING.md
%license lgpl-2.1.txt
%endif


# ========== python3-libdnf5-cli ==========

%if %{with python3} && %{with libdnf_cli}
%package -n python3-libdnf5-cli
Summary:        Python 3 bindings for the libdnf5-cli library
License:        LGPL-2.1-or-later
Requires:       libdnf5-cli%{?_isa} = %{version}-%{release}

%description -n python3-libdnf5-cli
Python 3 bindings for the libdnf5-cli library.

%files -n python3-libdnf5-cli
%{python3_sitearch}/libdnf5_cli
%{python3_sitearch}/libdnf5_cli-*.dist-info
%license COPYING.md
%license lgpl-2.1.txt
%endif


# ========== ruby-libdnf5 ==========

%if %{with ruby}
%package -n ruby-libdnf5
Summary:        Ruby bindings for the libdnf library
License:        LGPL-2.1-or-later
Provides:       ruby(libdnf) = %{version}-%{release}
Requires:       libdnf5%{?_isa} = %{version}-%{release}
Requires:       ruby(release)

%description -n ruby-libdnf5
Ruby bindings for the libdnf library.

%files -n ruby-libdnf5
%{ruby_vendorarchdir}/libdnf5
%license COPYING.md
%license lgpl-2.1.txt
%endif


# ========== ruby-libdnf5-cli ==========

%if %{with ruby} && %{with libdnf_cli}
%package -n ruby-libdnf5-cli
Summary:        Ruby bindings for the libdnf5-cli library
License:        LGPL-2.1-or-later
Provides:       ruby(libdnf_cli) = %{version}-%{release}
Requires:       libdnf5-cli%{?_isa} = %{version}-%{release}
Requires:       ruby(release)

%description -n ruby-libdnf5-cli
Ruby bindings for the libdnf5-cli library.

%files -n ruby-libdnf5-cli
%{ruby_vendorarchdir}/libdnf5_cli
%license COPYING.md
%license lgpl-2.1.txt
%endif


# ========== libdnf5-plugin-actions ==========

%if %{with plugin_actions}
%package -n libdnf5-plugin-actions
Summary:        Libdnf5 plugin that allows to run actions (external executables) on hooks
License:        LGPL-2.1-or-later
Requires:       libdnf5%{?_isa} = %{version}-%{release}

%description -n libdnf5-plugin-actions
Libdnf5 plugin that allows to run actions (external executables) on hooks.

%files -n libdnf5-plugin-actions -f libdnf5-plugin-actions.lang
%{_libdir}/libdnf5/plugins/actions.*
%config(noreplace) %{_sysconfdir}/dnf/libdnf5-plugins/actions.conf
%dir %{_sysconfdir}/dnf/libdnf5-plugins/actions.d
%if %{with man}
%{_mandir}/man8/libdnf5-actions.8.*
%endif
%endif

# ========== libdnf5-plugin-appstream ==========

%if %{with plugin_appstream}

%package -n libdnf5-plugin-appstream
Summary:        Libdnf5 plugin to install repository AppStream data
License:        LGPL-2.1-or-later
Requires:       libdnf5%{?_isa} = %{version}-%{release}
BuildRequires:  pkgconfig(appstream) >= 0.16

%description -n libdnf5-plugin-appstream
Libdnf5 plugin that installs repository's AppStream data, for repositories
which provide them.

%files -n libdnf5-plugin-appstream
%{_libdir}/libdnf5/plugins/appstream.so
%config(noreplace) %{_sysconfdir}/dnf/libdnf5-plugins/appstream.conf

%endif

# ========== libdnf5-plugin-expired-pgp-keys ==========

%if %{with plugin_expired_pgp_keys}
%package -n libdnf5-plugin-expired-pgp-keys
Summary:        Libdnf5 plugin for detecting and removing expired PGP keys
License:        LGPL-2.1-or-later
Requires:       libdnf5%{?_isa} = %{version}-%{release}
Requires:       gnupg2
Requires:       rpm-libs%{?_isa} >= 5.99.90

%description -n libdnf5-plugin-expired-pgp-keys
Libdnf5 plugin for detecting and removing expired PGP keys.

%files -n libdnf5-plugin-expired-pgp-keys -f libdnf5-plugin-expired-pgp-keys.lang
%{_libdir}/libdnf5/plugins/expired-pgp-keys.*
%config(noreplace) %{_sysconfdir}/dnf/libdnf5-plugins/expired-pgp-keys.conf
%if %{with man}
%{_mandir}/man8/libdnf5-expired-pgp-keys.8.*
%endif
%endif

# ========== libdnf5-plugin-plugin_rhsm ==========

%if %{with plugin_rhsm}
%package -n libdnf5-plugin-rhsm
Summary:        Libdnf5 rhsm (Oreon Subscription Manager) plugin
License:        LGPL-2.1-or-later
Requires:       libdnf5%{?_isa} = %{version}-%{release}

%description -n libdnf5-plugin-rhsm
Libdnf5 plugin with basic support for Oreon subscriptions.
Synchronizes the the enrollment with the vendor system. This can change
the contents of the repositories configuration files according
to the subscription levels.

%files -n libdnf5-plugin-rhsm -f libdnf5-plugin-rhsm.lang
%{_libdir}/libdnf5/plugins/rhsm.*
%config(noreplace) %{_sysconfdir}/dnf/libdnf5-plugins/rhsm.conf
%endif


# ========== python3-libdnf5-plugins-loader ==========

%if %{with python_plugins_loader}
%package -n python3-libdnf5-python-plugins-loader
Summary:        Libdnf5 plugin that allows loading Python plugins
License:        LGPL-2.1-or-later
Requires:       libdnf5%{?_isa} = %{version}-%{release}
Requires:       python3-libdnf5%{?_isa} = %{version}-%{release}

%description -n python3-libdnf5-python-plugins-loader
Libdnf5 plugin that allows loading Python plugins.

%files -n python3-libdnf5-python-plugins-loader
%{_libdir}/libdnf5/plugins/python_plugins_loader.*
%config(noreplace) %{_sysconfdir}/dnf/libdnf5-plugins/python_plugins_loader.conf
%dir %{_sysconfdir}/dnf/libdnf5-plugins/python_plugins_loader.d
%dir %{python3_sitelib}/libdnf_plugins/
%doc %{python3_sitelib}/libdnf_plugins/README
%endif

# ========== libdnf5-plugin-local ==========

%if %{with plugin_local}
%package -n libdnf5-plugin-local
Summary:        Libdnf5 plugin that copies all downloaded packages to a local repository
License:        LGPL-2.1-or-later
Requires:       libdnf5%{?_isa} = %{version}-%{release}
Requires:       createrepo_c

%description -n libdnf5-plugin-local
Libdnf5 plugin that automatically copies all downloaded packages to
a repository on the local filesystem and generates repo metadata.

%files -n libdnf5-plugin-local
%{_libdir}/libdnf5/plugins/local.*
%config(noreplace) %{_sysconfdir}/dnf/libdnf5-plugins/local.conf
%if %{with man}
%{_mandir}/man8/libdnf5-local.8.*
%endif
%endif

# ========== libdnf5-plugin-systemd-inhibit ==========

%if %{with plugin_systemd_inhibit}
%package -n libdnf5-plugin-systemd-inhibit
Summary:        Libdnf5 plugin that prevents system shutdown during a package transaction
License:        LGPL-2.1-or-later
Requires:       libdnf5%{?_isa} = %{version}-%{release}
BuildRequires:  pkgconfig(sdbus-c++) >= 0.8.1
BuildRequires:  oreon-rpm-macros

%description -n libdnf5-plugin-systemd-inhibit
Libdnf5 plugin that acquires a systemd inhibitor lock during a package
transaction to prevent system shutdown or reboot while packages are being
installed, removed, or updated.

%files -n libdnf5-plugin-systemd-inhibit
%{_libdir}/libdnf5/plugins/systemd-inhibit.*
%config(noreplace) %{_sysconfdir}/dnf/libdnf5-plugins/00-systemd-inhibit.conf
%endif


# ========== dnf5daemon-client ==========

%if %{with dnf5daemon_client}
%package -n dnf5daemon-client
Summary:        Command-line interface for dnf5daemon-server
License:        GPL-2.0-or-later
Requires:       libdnf5%{?_isa} = %{version}-%{release}
Requires:       libdnf5-cli%{?_isa} = %{version}-%{release}
Requires:       dnf5daemon-server

%description -n dnf5daemon-client
Command-line interface for dnf5daemon-server.

%files -n dnf5daemon-client -f dnf5daemon-client.lang
%{_bindir}/dnf5daemon-client
%license COPYING.md
%license gpl-2.0.txt
%if %{with man}
%{_mandir}/man8/dnf5daemon-client.8.*
%endif
%endif


# ========== dnf5daemon-server ==========

%if %{with dnf5daemon_server}
%package -n dnf5daemon-server
Summary:        Package management service with a DBus interface
License:        GPL-2.0-or-later
Requires:       libdnf5%{?_isa} = %{version}-%{release}
Requires:       libdnf5-cli%{?_isa} = %{version}-%{release}
Requires:       dbus
Requires:       polkit
%if %{without dnf5_obsoletes_dnf}
Requires:       dnf-data
%endif

%description -n dnf5daemon-server
Package management service with a DBus interface.

%post -n dnf5daemon-server
%systemd_post dnf5daemon-server.service

%preun -n dnf5daemon-server
%systemd_preun dnf5daemon-server.service

%postun -n dnf5daemon-server
%systemd_postun_with_restart dnf5daemon-server.service

%files -n dnf5daemon-server -f dnf5daemon-server.lang
%config(noreplace) %{_sysconfdir}/dnf/dnf5daemon-server.conf
%{_sbindir}/dnf5daemon-server
%{_unitdir}/dnf5daemon-server.service
%{_datadir}/dbus-1/system.d/org.rpm.dnf.v0.conf
%{_datadir}/dbus-1/system-services/org.rpm.dnf.v0.service
%{_datadir}/dbus-1/interfaces/org.rpm.dnf.v0.*.xml
%{_datadir}/polkit-1/actions/org.rpm.dnf.v0.policy
%license COPYING.md
%license gpl-2.0.txt
%if %{with man}
%{_mandir}/man8/dnf5daemon-server.8.*
%{_mandir}/man8/dnf5daemon-dbus-api.8.*
%endif


# ========== dnf5daemon-server-polkit ==========

%package -n dnf5daemon-server-polkit
Summary:        Polkit rule to allow wheel group members install trusted packages
License:        GPL-2.0-or-later
Requires:       polkit
Requires:       dnf5daemon-server = %{version}-%{release}
BuildArch:      noarch

%description -n dnf5daemon-server-polkit
Polkit rule to allow active local wheel group members install packages from
trusted repositories using dnf5daemon-server.

%files -n dnf5daemon-server-polkit
%{_datadir}/polkit-1/rules.d/org.rpm.dnf.v0.rules
%endif


# ========== dnf5-plugins ==========
%if %{with dnf5_plugins}

%package -n dnf5-plugins
Summary:        Plugins for dnf5
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
Requires:       dnf5%{?_isa} = %{version}-%{release}
Requires:       libcurl%{?_isa} >= 7.62.0
Requires:       libdnf5%{?_isa} = %{version}-%{release}
Requires:       libdnf5-cli%{?_isa} = %{version}-%{release}
Provides:       dnf5-command(builddep) = %{version}-%{release}
Provides:       dnf5-command(changelog) = %{version}-%{release}
Provides:       dnf5-command(config-manager) = %{version}-%{release}
Provides:       dnf5-command(copr) = %{version}-%{release}
Provides:       dnf5-command(needs-restarting) = %{version}-%{release}
Provides:       dnf5-command(repoclosure) = %{version}-%{release}
Provides:       dnf5-command(reposync) = %{version}-%{release}
Provides:       dnf5-command(repomanage) = %{version}-%{release}

%description -n dnf5-plugins
Core DNF5 plugins that enhance dnf5 with builddep, changelog, config-manager,
copr, needs-restarting, repoclosure, repomanage, and reposync commands.

%files -n dnf5-plugins -f dnf5-plugin-builddep.lang -f dnf5-plugin-changelog.lang -f dnf5-plugin-config-manager.lang -f dnf5-plugin-copr.lang -f dnf5-plugin-needs-restarting.lang -f dnf5-plugin-repoclosure.lang -f dnf5-plugin-reposync.lang
%{_libdir}/dnf5/plugins/builddep_cmd_plugin.so
%{_libdir}/dnf5/plugins/changelog_cmd_plugin.so
%{_libdir}/dnf5/plugins/config-manager_cmd_plugin.so
%{_libdir}/dnf5/plugins/copr_cmd_plugin.so
%{_libdir}/dnf5/plugins/needs_restarting_cmd_plugin.so
%{_libdir}/dnf5/plugins/repoclosure_cmd_plugin.so
%{_libdir}/dnf5/plugins/reposync_cmd_plugin.so
%{_libdir}/dnf5/plugins/repomanage_cmd_plugin.so
%if %{with man}
%{_mandir}/man8/dnf*-builddep.8.*
%{_mandir}/man8/dnf*-changelog.8.*
%{_mandir}/man8/dnf*-config-manager.8.*
%{_mandir}/man8/dnf*-copr.8.*
%{_mandir}/man8/dnf*-needs-restarting.8.*
%{_mandir}/man8/dnf*-repoclosure.8.*
%{_mandir}/man8/dnf*-reposync.8.*
%{_mandir}/man8/dnf*-repomanage.8.*
%endif
%{_datadir}/dnf5/aliases.d/compatibility-plugins.conf
%{_datadir}/dnf5/aliases.d/compatibility-reposync.conf


# ========== dnf5-automatic plugin ==========

%package plugin-automatic
Summary:        Package manager - automated upgrades
License:        LGPL-2.1-or-later
Requires:       dnf5%{?_isa} = %{version}-%{release}
Requires:       libdnf5%{?_isa} = %{version}-%{release}
Requires:       libdnf5-cli%{?_isa} = %{version}-%{release}
Recommends:     libcurl-full%{?_isa}
Provides:       dnf5-command(automatic) = %{version}-%{release}
%if %{with dnf5_obsoletes_dnf}
Provides:       dnf-automatic = %{version}-%{release}
Obsoletes:      dnf-automatic < 5
%else
Conflicts:      dnf-automatic < 5
%endif

%description plugin-automatic
Alternative command-line interface "dnf upgrade" suitable to be executed
automatically and regularly from systemd timers, cron jobs or similar.

%files plugin-automatic -f dnf5-plugin-automatic.lang
%ghost %attr(0644, root, root) %{_sysconfdir}/motd.d/dnf5-automatic
%{_libdir}/dnf5/plugins/automatic_cmd_plugin.so
%{_datadir}/dnf5/dnf5-plugins/automatic.conf
%{_datadir}/dbus-1/system.d/org.rpm.dnf.v0.Automatic.conf
%ghost %attr(0644, root, root) %config(noreplace) %{_sysconfdir}/dnf/automatic.conf
%ghost %attr(0644, root, root) %config(noreplace) %{_sysconfdir}/dnf/dnf5-plugins/automatic.conf
%if %{with man}
%{_mandir}/man8/dnf*-automatic.8.*
%endif
%{_unitdir}/dnf5-automatic.service
%{_unitdir}/dnf5-automatic.timer
%{_unitdir}/dnf-automatic.service
%{_unitdir}/dnf-automatic.timer
%if %{with dnf5_obsoletes_dnf}
%{_bindir}/dnf-automatic
%else
%exclude %{_bindir}/dnf-automatic
%endif

# ========== dnf5-manifest plugin ==========

%if %{with plugin_manifest}
%package plugin-manifest
Summary:        DNF5 plugin for working with RPM package manifest files
License:        LGPL-2.1-or-later
Requires:       dnf5%{?_isa} = %{version}-%{release}
Requires:       libdnf5%{?_isa} = %{version}-%{release}
Requires:       libdnf5-cli%{?_isa} = %{version}-%{release}
Provides:       dnf5-command(manifest) = %{version}-%{release}

%description plugin-manifest
DNF5 plugin for working with RPM package manifest files.

%files plugin-manifest
%{_libdir}/dnf5/plugins/manifest_cmd_plugin.so
%if %{with man}
%{_mandir}/man8/dnf*-manifest.8.*
%endif
%endif

%endif


# ========== unpack, build, check & install ==========

%prep
%oreon_sha256

%autosetup -p1 -n dnf5-%{version}


%build
%cmake \
    -DPERL_INSTALLDIRS=vendor \
    \
    -DENABLE_SOLV_FOCUSNEW=%{?with_focus_new:ON}%{!?with_focus_new:OFF} \
    \
    -DWITH_DNF5DAEMON_CLIENT=%{?with_dnf5daemon_client:ON}%{!?with_dnf5daemon_client:OFF} \
    -DWITH_DNF5DAEMON_SERVER=%{?with_dnf5daemon_server:ON}%{!?with_dnf5daemon_server:OFF} \
    -DWITH_LIBDNF5_CLI=%{?with_libdnf_cli:ON}%{!?with_libdnf_cli:OFF} \
    -DWITH_DNF5=%{?with_dnf5:ON}%{!?with_dnf5:OFF} \
    -DWITH_DNF5_OBSOLETES_DNF=%{?with_dnf5_obsoletes_dnf:ON}%{!?with_dnf5_obsoletes_dnf:OFF} \
    -DWITH_DNF5_PLUGINS=%{?with_dnf5_plugins:ON}%{!?with_dnf5_plugins:OFF} \
    -DWITH_PLUGIN_ACTIONS=%{?with_plugin_actions:ON}%{!?with_plugin_actions:OFF} \
    -DWITH_PLUGIN_APPSTREAM=%{?with_plugin_appstream:ON}%{!?with_plugin_appstream:OFF} \
    -DWITH_PLUGIN_EXPIRED_PGP_KEYS=%{?with_plugin_expired_pgp_keys:ON}%{!?with_plugin_expired_pgp_keys:OFF} \
    -DWITH_PLUGIN_LOCAL=%{?with_plugin_local:ON}%{!?with_plugin_local:OFF} \
    -DWITH_PLUGIN_RHSM=%{?with_plugin_rhsm:ON}%{!?with_plugin_rhsm:OFF} \
    -DWITH_PLUGIN_MANIFEST=%{?with_plugin_manifest:ON}%{!?with_plugin_manifest:OFF} \
    -DWITH_PLUGIN_SYSTEMD_INHIBIT=%{?with_plugin_systemd_inhibit:ON}%{!?with_plugin_systemd_inhibit:OFF} \
    -DWITH_PYTHON_PLUGINS_LOADER=%{?with_python_plugins_loader:ON}%{!?with_python_plugins_loader:OFF} \
    \
    -DWITH_ACL=%{?with_acl:ON}%{!?with_acl:OFF} \
    -DWITH_COMPS=%{?with_comps:ON}%{!?with_comps:OFF} \
    -DWITH_MODULEMD=%{?with_modulemd:ON}%{!?with_modulemd:OFF} \
    -DWITH_SYSTEMD=%{?with_systemd:ON}%{!?with_systemd:OFF} \
    -DSYSTEMD_DIR=%{_unitdir} \
    -DTMPFILES_DIR=%{_tmpfilesdir} \
    \
    -DWITH_HTML=%{?with_html:ON}%{!?with_html:OFF} \
    -DWITH_MAN=%{?with_man:ON}%{!?with_man:OFF} \
    \
    -DWITH_GO=%{?with_go:ON}%{!?with_go:OFF} \
    -DWITH_PERL5=%{?with_perl5:ON}%{!?with_perl5:OFF} \
    -DWITH_PYTHON3=%{?with_python3:ON}%{!?with_python3:OFF} \
    -DWITH_RUBY=%{?with_ruby:ON}%{!?with_ruby:OFF} \
    \
    -DWITH_SANITIZERS=%{?with_sanitizers:ON}%{!?with_sanitizers:OFF} \
    -DWITH_TESTS=%{?with_tests:ON}%{!?with_tests:OFF} \
    -DWITH_PERFORMANCE_TESTS=%{?with_performance_tests:ON}%{!?with_performance_tests:OFF} \
    -DWITH_DNF5DAEMON_TESTS=%{?with_dnf5daemon_tests:ON}%{!?with_dnf5daemon_tests:OFF} \
    \
    -DVERSION_PRIME=%{project_version_prime} \
    -DVERSION_MAJOR=%{project_version_major} \
    -DVERSION_MINOR=%{project_version_minor} \
    -DVERSION_MICRO=%{project_version_micro}
find %{__cmake_builddir} -type f -name '*.ninja' -exec sed -i \
  -e 's| -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1||g' \
  -e 's| -specs=/usr/lib/rpm/redhat/redhat-hardened-ld||g' \
  -e 's| -specs=/usr/lib/rpm/redhat/redhat-hardened-ld-errors||g' \
  -e 's| -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1||g' \
  {} +
%cmake_build
%if %{with man}
    %cmake_build --target doc-man
%endif


%check
%if %{with tests}
    %ctest
%endif


%install
%cmake_install

%if %{with dnf5_obsoletes_dnf}
ln -sr %{buildroot}%{_bindir}/dnf5 %{buildroot}%{_bindir}/dnf
ln -sr %{buildroot}%{_bindir}/dnf5 %{buildroot}%{_bindir}/yum
ln -sr %{buildroot}%{bash_completions_dir}/dnf5 %{buildroot}%{bash_completions_dir}/dnf
%if %{with man}
    for file in %{buildroot}%{_mandir}/man[578]/dnf5[-.]*; do
        dir=$(dirname $file)
        filename=$(basename $file)
        ln -sr $file $dir/${filename/dnf5/dnf}
    done
    ln -sr %{buildroot}%{_mandir}/man8/dnf5.8 %{buildroot}%{_mandir}/man8/yum.8
%endif
# Make "dnf-makecache" the "real" unit name, but keep compatibility for playbooks that refer to dnf5-makecache
mv %{buildroot}%{_unitdir}/dnf5-makecache.service %{buildroot}%{_unitdir}/dnf-makecache.service
mv %{buildroot}%{_unitdir}/dnf5-makecache.timer %{buildroot}%{_unitdir}/dnf-makecache.timer
ln -s dnf-makecache.service %{buildroot}%{_unitdir}/dnf5-makecache.service
ln -s dnf-makecache.timer %{buildroot}%{_unitdir}/dnf5-makecache.timer
%endif

# own dirs and files that dnf5 creates on runtime
mkdir -p %{buildroot}%{_prefix}/lib/sysimage/libdnf5
for file in \
    environments.toml groups.toml \
%if %{with modulemd}
    modules.toml \
%endif
    nevras.toml packages.toml \
    system.toml \
    transaction_history.sqlite transaction_history.sqlite-shm \
    transaction_history.sqlite-wal
do
    touch %{buildroot}%{_prefix}/lib/sysimage/libdnf5/$file
done
mkdir -p %{buildroot}%{_prefix}/lib/sysimage/libdnf5/comps_groups
mkdir -p %{buildroot}%{_prefix}/lib/sysimage/libdnf5/offline
touch %{buildroot}%{_sysconfdir}/dnf/versionlock.toml
mkdir -p %{buildroot}%{_sharedstatedir}/dnf
touch %{buildroot}%{_sharedstatedir}/dnf/system-repo.lock

ln -sr %{buildroot}%{_bindir}/dnf5 %{buildroot}%{_bindir}/microdnf
%if %{with man}
ln -sr %{buildroot}%{_mandir}/man8/dnf5.8 %{buildroot}%{_mandir}/man8/microdnf.8
%endif

%if %{with systemd}
mkdir -p %{buildroot}%{_unitdir}/system-update.target.wants/
pushd %{buildroot}%{_unitdir}/system-update.target.wants/
  ln -sr ../dnf5-offline-transaction.service
popd
%endif

mkdir -p %{buildroot}%{_libdir}/libdnf5/plugins

%find_lang dnf5
%if %{with dnf5_plugins}
%find_lang dnf5-plugin-automatic
%find_lang dnf5-plugin-builddep
%find_lang dnf5-plugin-changelog
%find_lang dnf5-plugin-config-manager
%find_lang dnf5-plugin-copr
%find_lang dnf5-plugin-needs-restarting
%find_lang dnf5-plugin-repoclosure
%find_lang dnf5-plugin-reposync
%endif
%if %{with dnf5daemon_client}
%find_lang dnf5daemon-client
%endif
%if %{with dnf5daemon_server}
%find_lang dnf5daemon-server
%endif
%find_lang libdnf5
%if %{with libdnf_cli}
%find_lang libdnf5-cli
%endif
%if %{with plugin_actions}
%find_lang libdnf5-plugin-actions
%endif
%if %{with plugin_expired_pgp_keys}
%find_lang libdnf5-plugin-expired-pgp-keys
%endif
%if %{with plugin_rhsm}
%find_lang libdnf5-plugin-rhsm
%endif

%ldconfig_scriptlets -n libdnf5
%ldconfig_scriptlets -n libdnf5-cli

