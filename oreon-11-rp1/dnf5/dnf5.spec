%global source0_hash 242f0e775bc8e1017a5bfec841c776beafa7ea6b5bd2e4d7bc0ff9d7c57998f3
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}
%global py3_sitearch %(python3 -c 'import sysconfig; print(sysconfig.get_path("platlib", "posix_prefix", {"base": "/usr", "platbase": "/usr"}))')

Name: dnf5
Version: 5.4.6.0
Release: 4%{?dist}
Summary: Command-line package manager
License: GPL-2.0-or-later AND LGPL-2.1-or-later
URL: https://github.com/rpm-software-management/dnf5
Source0: https://github.com/rpm-software-management/dnf5/archive/%{version}/dnf5-%{version}.tar.gz
Requires: libdnf5%{?_isa} = %{version}-%{release}
Requires: libdnf5-cli%{?_isa} = %{version}-%{release}
Requires: rpm

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: patchelf
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: pkgconf
BuildRequires: gettext
BuildRequires: fmt-devel
BuildRequires: toml11-devel
BuildRequires: json-c-devel
BuildRequires: libsolv-devel
BuildRequires: librepo-devel
BuildRequires: libmodulemd-devel
BuildRequires: libcomps-devel
BuildRequires: rpm-devel
BuildRequires: sqlite-devel
BuildRequires: libxml2-devel
BuildRequires: glib2-devel
BuildRequires: libacl-devel
BuildRequires: libsmartcols-devel
BuildRequires: zchunk-devel
BuildRequires: systemd-devel
BuildRequires: sdbus-cpp-devel
BuildRequires: libcurl-devel
BuildRequires: openssl-devel
BuildRequires: pkgconfig(bash-completion)
BuildRequires: python3-devel
BuildRequires: swig

%description
DNF5 is the C++ rewrite of the DNF package manager, with libdnf5 and the
dnf5daemon D-Bus service.

%package -n libdnf5
Summary: Package management library
License: LGPL-2.1-or-later
Requires: rpm-libs%{?_isa}

%description -n libdnf5
Package management library.

%package -n libdnf5-cli
Summary: Library for terminal output in a command-line package manager
License: LGPL-2.1-or-later
Requires: libdnf5%{?_isa} = %{version}-%{release}

%description -n libdnf5-cli
Library for working with a terminal in a command-line package manager.

%package devel
Summary: Development files for dnf5
License: LGPL-2.1-or-later
Requires: dnf5%{?_isa} = %{version}-%{release}
Requires: libdnf5-devel%{?_isa} = %{version}-%{release}
Requires: libdnf5-cli-devel%{?_isa} = %{version}-%{release}

%description devel
Headers for dnf5 command plugins.

%package -n libdnf5-devel
Summary: Development files for libdnf5
License: LGPL-2.1-or-later
Requires: libdnf5%{?_isa} = %{version}-%{release}
Requires: libsolv-devel%{?_isa}

%description -n libdnf5-devel
Headers and libraries for developing against libdnf5.

%package -n libdnf5-cli-devel
Summary: Development files for libdnf5-cli
License: LGPL-2.1-or-later
Requires: libdnf5-cli%{?_isa} = %{version}-%{release}
Requires: libdnf5-devel%{?_isa} = %{version}-%{release}

%description -n libdnf5-cli-devel
Headers and libraries for developing against libdnf5-cli.

%package -n python3-libdnf5
Summary: Python 3 bindings for libdnf5
License: LGPL-2.1-or-later
Requires: libdnf5%{?_isa} = %{version}-%{release}

%description -n python3-libdnf5
Python 3 bindings for the libdnf5 library.

%package -n python3-libdnf5-cli
Summary: Python 3 bindings for libdnf5-cli
License: LGPL-2.1-or-later
Requires: libdnf5-cli%{?_isa} = %{version}-%{release}
Requires: python3-libdnf5%{?_isa} = %{version}-%{release}

%description -n python3-libdnf5-cli
Python 3 bindings for the libdnf5-cli library.

%package -n libdnf5-plugin-actions
Summary: libdnf5 plugin that runs actions on hooks
License: LGPL-2.1-or-later
Requires: libdnf5%{?_isa} = %{version}-%{release}

%description -n libdnf5-plugin-actions
libdnf5 plugin that runs external executables on transaction hooks.

%package -n libdnf5-plugin-expired-pgp-keys
Summary: libdnf5 plugin that removes expired PGP keys
License: LGPL-2.1-or-later
Requires: libdnf5%{?_isa} = %{version}-%{release}
Requires: gnupg2

%description -n libdnf5-plugin-expired-pgp-keys
libdnf5 plugin for detecting and removing expired PGP keys.

%package -n libdnf5-plugin-systemd-inhibit
Summary: libdnf5 plugin that blocks shutdown during transactions
License: LGPL-2.1-or-later
Requires: libdnf5%{?_isa} = %{version}-%{release}

%description -n libdnf5-plugin-systemd-inhibit
libdnf5 plugin that holds a systemd inhibitor lock during a package transaction.

%package -n dnf5daemon-client
Summary: Command-line interface for dnf5daemon-server
Requires: libdnf5%{?_isa} = %{version}-%{release}
Requires: libdnf5-cli%{?_isa} = %{version}-%{release}
Requires: dnf5daemon-server = %{version}-%{release}

%description -n dnf5daemon-client
Command-line interface for dnf5daemon-server.

%package -n dnf5daemon-server
Summary: Package management service with a D-Bus interface
Requires: libdnf5%{?_isa} = %{version}-%{release}
Requires: libdnf5-cli%{?_isa} = %{version}-%{release}
Requires: dbus

%description -n dnf5daemon-server
Package management service with a D-Bus interface.

%package plugins
Summary: Plugins for dnf5
License: LGPL-2.1-or-later AND GPL-2.0-or-later
Requires: dnf5%{?_isa} = %{version}-%{release}
Requires: libdnf5%{?_isa} = %{version}-%{release}
Requires: libdnf5-cli%{?_isa} = %{version}-%{release}
Provides: dnf5-command(builddep) = %{version}-%{release}
Provides: dnf5-command(changelog) = %{version}-%{release}
Provides: dnf5-command(config-manager) = %{version}-%{release}
Provides: dnf5-command(copr) = %{version}-%{release}
Provides: dnf5-command(needs-restarting) = %{version}-%{release}
Provides: dnf5-command(repoclosure) = %{version}-%{release}
Provides: dnf5-command(repomanage) = %{version}-%{release}
Provides: dnf5-command(reposync) = %{version}-%{release}

%description plugins
dnf5 builddep, changelog, config-manager, copr, needs-restarting, repoclosure,
repomanage and reposync commands.

%package plugin-automatic
Summary: dnf5 plugin for automatic upgrades
License: LGPL-2.1-or-later
Requires: dnf5%{?_isa} = %{version}-%{release}
Requires: libdnf5%{?_isa} = %{version}-%{release}
Requires: libdnf5-cli%{?_isa} = %{version}-%{release}
Provides: dnf5-command(automatic) = %{version}-%{release}

%description plugin-automatic
dnf5 automatic command for running upgrades from systemd timers.

%prep
%oreon_sha256
%autosetup -n dnf5-%{version} -p1

%build
%oreon_cmake \
  -DWITH_HTML=OFF -DWITH_MAN=OFF -DWITH_TESTS=OFF -DWITH_PERFORMANCE_TESTS=OFF \
  -DWITH_PERL5=OFF -DWITH_PYTHON3=ON -DWITH_RUBY=OFF -DWITH_GO=OFF -DWITH_PYTHON_PLUGINS_LOADER=OFF \
  -DWITH_PLUGIN_APPSTREAM=OFF -DWITH_PLUGIN_MANIFEST=OFF -DWITH_PLUGIN_RHSM=OFF -DWITH_PLUGIN_LOCAL=OFF \
  -DWITH_DNF5_OBSOLETES_DNF=OFF -DWITH_SANITIZERS=OFF
%oreon_cmake_build

%install
%oreon_cmake_install
mkdir -p %{buildroot}%{_sysconfdir}/dnf/repos.d %{buildroot}%{_localstatedir}/cache/libdnf5
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f" 2>/dev/null || true)
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
rm -f %{buildroot}%{_bindir}/dnf-automatic
rm -f %{buildroot}%{_unitdir}/dnf-automatic.service %{buildroot}%{_unitdir}/dnf-automatic.timer
rm -f %{buildroot}%{_datadir}/polkit-1/rules.d/org.rpm.dnf.v0.rules
mkdir -p %{buildroot}%{_prefix}/lib/sysimage/libdnf5 %{buildroot}%{_sharedstatedir}/dnf %{buildroot}%{_libdir}/libdnf5/plugins
touch %{buildroot}%{_sysconfdir}/dnf/versionlock.toml
mkdir -p %{buildroot}%{_unitdir}/system-update.target.wants
ln -sr %{buildroot}%{_unitdir}/dnf5-offline-transaction.service %{buildroot}%{_unitdir}/system-update.target.wants/dnf5-offline-transaction.service
%find_lang dnf5
%find_lang libdnf5
%find_lang libdnf5-cli
%find_lang dnf5daemon-client
%find_lang dnf5daemon-server
%find_lang libdnf5-plugin-actions
%find_lang libdnf5-plugin-expired-pgp-keys
%find_lang dnf5-plugin-automatic
for d in builddep changelog config-manager copr needs-restarting repoclosure reposync; do
  %find_lang dnf5-plugin-$d
  cat dnf5-plugin-$d.lang >> dnf5-plugins.lang
done

%ldconfig_scriptlets -n libdnf5
%ldconfig_scriptlets -n libdnf5-cli

%files -f dnf5.lang
%license COPYING.md gpl-2.0.txt
%{_bindir}/dnf5
%{_unitdir}/dnf5-makecache.service
%{_unitdir}/dnf5-makecache.timer
%{_unitdir}/dnf5-offline-transaction.service
%{_unitdir}/dnf5-offline-transaction-cleanup.service
%{_unitdir}/system-update.target.wants/dnf5-offline-transaction.service
%dir %{_sysconfdir}/dnf/dnf5-aliases.d
%doc %{_sysconfdir}/dnf/dnf5-aliases.d/README
%dir %{_datadir}/dnf5
%dir %{_datadir}/dnf5/aliases.d
%{_datadir}/dnf5/aliases.d/compatibility.conf
%dir %{_datadir}/dnf5/dnf5-plugins
%dir %{_sysconfdir}/dnf/dnf5-plugins
%dir %{_libdir}/dnf5
%dir %{_libdir}/dnf5/plugins
%doc %{_libdir}/dnf5/plugins/README
%{bash_completions_dir}/dnf5
%{zsh_completions_dir}/_dnf5

%files -n libdnf5 -f libdnf5.lang
%license COPYING.md lgpl-2.1.txt
%dir %{_sysconfdir}/dnf
%config(noreplace) %{_sysconfdir}/dnf/dnf.conf
%dir %{_sysconfdir}/dnf/repos.d
%dir %{_sysconfdir}/dnf/vars
%dir %{_sysconfdir}/dnf/protected.d
%dir %{_sysconfdir}/dnf/usr-drift-protected-paths.d
%dir %{_sysconfdir}/dnf/libdnf5.conf.d
%dir %{_sysconfdir}/dnf/repos.override.d
%dir %{_sysconfdir}/dnf/libdnf5-plugins
%dir %{_sysconfdir}/dnf/vendors.d
%dir %{_sysconfdir}/dnf/suggest-reboot.d
%ghost %attr(0644,root,root) %{_sysconfdir}/dnf/versionlock.toml
%dir %{_datadir}/dnf5/libdnf.conf.d
%dir %{_datadir}/dnf5/repos.override.d
%dir %{_datadir}/dnf5/repos.d
%dir %{_datadir}/dnf5/vars.d
%dir %{_datadir}/dnf5/vendors.d
%dir %{_datadir}/dnf5/libdnf.plugins.conf.d
%dir %{_datadir}/dnf5/suggest-reboot.d
%{_libdir}/libdnf5.so.2*
%dir %{_libdir}/libdnf5
%dir %{_libdir}/libdnf5/plugins
%dir %{_prefix}/lib/sysimage/libdnf5
%dir %{_sharedstatedir}/dnf
%dir %{_localstatedir}/cache/libdnf5
%{_tmpfilesdir}/libdnf5.conf

%files -n libdnf5-cli -f libdnf5-cli.lang
%license COPYING.md lgpl-2.1.txt
%{_libdir}/libdnf5-cli.so.3*

%files devel
%{_includedir}/dnf5/

%files -n libdnf5-devel
%{_includedir}/libdnf5/
%{_libdir}/libdnf5.so
%{_libdir}/pkgconfig/libdnf5.pc

%files -n libdnf5-cli-devel
%{_includedir}/libdnf5-cli/
%{_libdir}/libdnf5-cli.so
%{_libdir}/pkgconfig/libdnf5-cli.pc

%files -n python3-libdnf5
%{py3_sitearch}/libdnf5/
%{py3_sitearch}/libdnf5-*.dist-info/

%files -n python3-libdnf5-cli
%{py3_sitearch}/libdnf5_cli/
%{py3_sitearch}/libdnf5_cli-*.dist-info/

%files -n libdnf5-plugin-actions -f libdnf5-plugin-actions.lang
%{_libdir}/libdnf5/plugins/actions.so
%config(noreplace) %{_sysconfdir}/dnf/libdnf5-plugins/actions.conf
%dir %{_sysconfdir}/dnf/libdnf5-plugins/actions.d

%files -n libdnf5-plugin-expired-pgp-keys -f libdnf5-plugin-expired-pgp-keys.lang
%{_libdir}/libdnf5/plugins/expired-pgp-keys.so
%config(noreplace) %{_sysconfdir}/dnf/libdnf5-plugins/expired-pgp-keys.conf

%files -n libdnf5-plugin-systemd-inhibit
%{_libdir}/libdnf5/plugins/systemd-inhibit.so
%config(noreplace) %{_sysconfdir}/dnf/libdnf5-plugins/00-systemd-inhibit.conf

%files -n dnf5daemon-client -f dnf5daemon-client.lang
%license COPYING.md gpl-2.0.txt
%{_bindir}/dnf5daemon-client

%files -n dnf5daemon-server -f dnf5daemon-server.lang
%license COPYING.md gpl-2.0.txt
%config(noreplace) %{_sysconfdir}/dnf/dnf5daemon-server.conf
%{_sbindir}/dnf5daemon-server
%{_unitdir}/dnf5daemon-server.service
%{_datadir}/dbus-1/system.d/org.rpm.dnf.v0.conf
%{_datadir}/dbus-1/system-services/org.rpm.dnf.v0.service
%{_datadir}/dbus-1/interfaces/org.rpm.dnf.v0.*.xml
%{_datadir}/polkit-1/actions/org.rpm.dnf.v0.policy

%files plugins -f dnf5-plugins.lang
%{_libdir}/dnf5/plugins/builddep_cmd_plugin.so
%{_libdir}/dnf5/plugins/changelog_cmd_plugin.so
%{_libdir}/dnf5/plugins/config-manager_cmd_plugin.so
%{_libdir}/dnf5/plugins/copr_cmd_plugin.so
%{_libdir}/dnf5/plugins/needs_restarting_cmd_plugin.so
%{_libdir}/dnf5/plugins/repoclosure_cmd_plugin.so
%{_libdir}/dnf5/plugins/repomanage_cmd_plugin.so
%{_libdir}/dnf5/plugins/reposync_cmd_plugin.so
%{_datadir}/dnf5/aliases.d/compatibility-plugins.conf
%{_datadir}/dnf5/aliases.d/compatibility-reposync.conf

%files plugin-automatic -f dnf5-plugin-automatic.lang
%{_libdir}/dnf5/plugins/automatic_cmd_plugin.so
%{_datadir}/dnf5/dnf5-plugins/automatic.conf
%{_datadir}/dbus-1/system.d/org.rpm.dnf.v0.Automatic.conf
%{_unitdir}/dnf5-automatic.service
%{_unitdir}/dnf5-automatic.timer
