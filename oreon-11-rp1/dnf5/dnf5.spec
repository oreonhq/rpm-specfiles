%global source0_hash 242f0e775bc8e1017a5bfec841c776beafa7ea6b5bd2e4d7bc0ff9d7c57998f3
%global project_version_prime 5
%global project_version_major 4
%global project_version_minor 6
%global project_version_micro 0
%bcond dnf5_obsoletes_dnf %[0%{?fedora} > 40 || 0%{?rhel} > 10]
Name:           dnf5
Version:        %{project_version_prime}.%{project_version_major}.%{project_version_minor}.%{project_version_micro}
Release:        1%{?dist}
Summary:        Command-line package manager
License:        GPL-2.0-or-later
URL:            https://github.com/rpm-software-management/dnf5
Source0:        https://github.com/rpm-software-management/dnf5/archive/refs/tags/5.4.6.0.tar.gz#/dnf5-5.4.6.0.tar.gz
Requires:       libdnf5%{?_isa} = %{version}-%{release}
Requires:       libdnf5-cli%{?_isa} = %{version}-%{release}
%if %{without dnf5_obsoletes_dnf}
Requires:       dnf-data
%endif
Recommends:     (dnf5-plugins if dnf-plugins-core)
Recommends:     bash-completion
Requires:       coreutils
%if %{with dnf5_obsoletes_dnf}
Provides:       dnf = %{version}-%{release}
Obsoletes:      dnf < 5
Provides:       yum = %{version}-%{release}
Obsoletes:      yum < 5
Conflicts:      python3-dnf-plugins-core < 4.7.0
%endif
Provides:       dnf5-command(advisory)
Provides:       dnf5-command(autoremove)
Provides:       dnf5-command(check)
Provides:       dnf5-command(check-upgrade)
Provides:       dnf5-command(clean)
Provides:       dnf5-command(distro-sync)
Provides:       dnf5-command(downgrade)
Provides:       dnf5-command(download)
Provides:       dnf5-command(environment)
Provides:       dnf5-command(group)
Provides:       dnf5-command(history)
Provides:       dnf5-command(info)
Provides:       dnf5-command(install)
Provides:       dnf5-command(leaves)
Provides:       dnf5-command(list)
Provides:       dnf5-command(makecache)
Provides:       dnf5-command(mark)
Provides:       dnf5-command(module)
Provides:       dnf5-command(offline)
Provides:       dnf5-command(provides)
Provides:       dnf5-command(reinstall)
Provides:       dnf5-command(replay)
Provides:       dnf5-command(remove)
Provides:       dnf5-command(repo)
Provides:       dnf5-command(repoquery)
Provides:       dnf5-command(search)
Provides:       dnf5-command(swap)
Provides:       dnf5-command(system-upgrade)
Provides:       dnf5-command(upgrade)
Provides:       dnf5-command(versionlock)
%bcond_without dnf5daemon_client
%bcond_without dnf5daemon_server
%bcond_without libdnf_cli
%bcond_without dnf5
%bcond_without dnf5_plugins
%bcond_without plugin_actions
%bcond_without plugin_appstream
%bcond_without plugin_expired_pgp_keys
%bcond_without plugin_rhsm
%bcond_without plugin_manifest
%bcond_without python_plugins_loader
%bcond_without plugin_local
%bcond_without acl
%bcond_without comps
%bcond_without modulemd
%bcond_without systemd
%bcond_with    html
%bcond_without man
%bcond_with    go
%bcond_without perl5
%bcond_without python3
%bcond_without ruby
%bcond_with    clang
%bcond_with    sanitizers
%bcond_without tests
%bcond_with    performance_tests
%bcond_with    dnf5daemon_tests
%bcond_without focus_new
%if %{with clang}
    %global toolchain clang
%endif
%global libmodulemd_version 2.5.0
%global librepo_version 1.20.0
%global libsolv_version 0.7.35
%global sqlite_version 3.35.0
%global swig_version 4
%if %{with acl}
%endif
%if %{with clang}
%else
%endif
%if %{with tests}
%endif
%if %{with comps}
%endif
%if %{with modulemd}
%endif
%if %{with systemd}
%endif
%if %{with html} || %{with man}
%endif
%if %{with sanitizers}
%endif
%if %{with libdnf_cli}
%endif
%if %{with dnf5_plugins}
%if %{with plugin_manifest}
%endif
%endif
%if %{with dnf5daemon_server}
%if %{with dnf5daemon_tests}
%endif
%endif
%if %{with plugin_rhsm}
%endif
%if %{with perl5} || %{with ruby} || %{with python3}
%endif
%if %{with perl5}
%if %{with tests}
%endif
%endif
%if %{with ruby}
%if %{with tests}
%endif
%endif
%if %{with python3}
%endif
# oreon:deps
BuildRequires:  bash-completion
BuildRequires:  cmake
BuildRequires:  createrepo_c
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libcurl-devel
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  pkgconfig(appstream)
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(libcomps)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libpkgmanifest)
BuildRequires:  pkgconfig(librepo)
BuildRequires:  pkgconfig(librhsm)
BuildRequires:  pkgconfig(libsolv)
BuildRequires:  pkgconfig(libsolvext)
BuildRequires:  pkgconfig(modulemd-2.0)
BuildRequires:  pkgconfig(rpm)
BuildRequires:  pkgconfig(ruby)
BuildRequires:  pkgconfig(sdbus-c++)
BuildRequires:  pkgconfig(smartcols)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  python3-devel
BuildRequires:  python3dist(breathe)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-autoapi)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  rpm-build
BuildRequires:  rubygem-test-unit
BuildRequires:  swig
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  toml11-static
BuildRequires:  zlib-devel
# /oreon:deps
%description
DNF5 is a command-line package manager that automates the process of installing,
upgrading, configuring, and removing computer programs in a consistent manner.
It supports RPM packages, modulemd modules, and comps groups & environments.

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
%package -n libdnf5
Summary:        Package management library
License:        LGPL-2.1-or-later
Requires:       libsolv%{?_isa} >= %{libsolv_version}
Requires:       librepo%{?_isa} >= %{librepo_version}
Requires:       sqlite-libs%{?_isa} >= %{sqlite_version}
%if %{with dnf5_obsoletes_dnf}
Conflicts:      dnf-data < 4.20.0
%endif
%description -n libdnf5
Package management library.

%package -n libdnf5-cli
Summary:        Library for working with a terminal in a command-line package manager
License:        LGPL-2.1-or-later
Requires:       libdnf5%{?_isa} = %{version}-%{release}
%description -n libdnf5-cli
Library for working with a terminal in a command-line package manager.

%if %{with libdnf_cli}
%package -n dnf5-devel
Summary:        Development files for dnf5
License:        LGPL-2.1-or-later
Requires:       dnf5%{?_isa} = %{version}-%{release}
Requires:       libdnf5-devel%{?_isa} = %{version}-%{release}
Requires:       libdnf5-cli-devel%{?_isa} = %{version}-%{release}
%description -n dnf5-devel
Development files for dnf5.

%if %{with libdnf_cli}
%package -n libdnf5-devel
Summary:        Development files for libdnf
License:        LGPL-2.1-or-later
Requires:       libdnf5%{?_isa} = %{version}-%{release}
Requires:       libsolv-devel%{?_isa} >= %{libsolv_version}
%description -n libdnf5-devel
Development files for libdnf.

%if %{with libdnf_cli}
%package -n libdnf5-cli-devel
Summary:        Development files for libdnf5-cli
License:        LGPL-2.1-or-later
Requires:       libdnf5-cli%{?_isa} = %{version}-%{release}
%description -n libdnf5-cli-devel
Development files for libdnf5-cli.

%if %{with libdnf_cli}
%package -n perl-libdnf5
Summary:        Perl 5 bindings for the libdnf library
License:        LGPL-2.1-or-later
Requires:       libdnf5%{?_isa} = %{version}-%{release}
%description -n perl-libdnf5
Perl 5 bindings for the libdnf library.

%if %{with libdnf_cli}
%package -n perl-libdnf5-cli
Summary:        Perl 5 bindings for the libdnf5-cli library
License:        LGPL-2.1-or-later
Requires:       libdnf5-cli%{?_isa} = %{version}-%{release}
%description -n perl-libdnf5-cli
Perl 5 bindings for the libdnf5-cli library.

%if %{with libdnf_cli}
%package -n python3-libdnf5
Summary:        Python 3 bindings for the libdnf5 library
License:        LGPL-2.1-or-later
Requires:       libdnf5%{?_isa} = %{version}-%{release}
%description -n python3-libdnf5
Python 3 bindings for the libdnf library.

%if %{with libdnf_cli}
%package -n python3-libdnf5-cli
Summary:        Python 3 bindings for the libdnf5-cli library
License:        LGPL-2.1-or-later
Requires:       libdnf5-cli%{?_isa} = %{version}-%{release}
%description -n python3-libdnf5-cli
Python 3 bindings for the libdnf5-cli library.

%if %{with libdnf_cli}
%package -n ruby-libdnf5
Summary:        Ruby bindings for the libdnf library
License:        LGPL-2.1-or-later
Provides:       ruby(libdnf) = %{version}-%{release}
Requires:       libdnf5%{?_isa} = %{version}-%{release}
Requires:       ruby(release)
%description -n ruby-libdnf5
Ruby bindings for the libdnf library.

%if %{with libdnf_cli}
%package -n ruby-libdnf5-cli
Summary:        Ruby bindings for the libdnf5-cli library
License:        LGPL-2.1-or-later
Provides:       ruby(libdnf_cli) = %{version}-%{release}
Requires:       libdnf5-cli%{?_isa} = %{version}-%{release}
Requires:       ruby(release)
%description -n ruby-libdnf5-cli
Ruby bindings for the libdnf5-cli library.

%if %{with libdnf_cli}
%package -n libdnf5-plugin-actions
Summary:        Libdnf5 plugin that allows to run actions (external executables) on hooks
License:        LGPL-2.1-or-later
Requires:       libdnf5%{?_isa} = %{version}-%{release}
%description -n libdnf5-plugin-actions
Libdnf5 plugin that allows to run actions (external executables) on hooks.

%if %{with libdnf_cli}
%package -n libdnf5-plugin-appstream
Summary:        Libdnf5 plugin to install repository AppStream data
License:        LGPL-2.1-or-later
Requires:       libdnf5%{?_isa} = %{version}-%{release}
BuildRequires:  pkgconfig(appstream) >= 0.16
%description -n libdnf5-plugin-appstream
Libdnf5 plugin that installs repository's AppStream data, for repositories which provide them.

%if %{with libdnf_cli}
%package -n libdnf5-plugin-expired-pgp-keys
Summary:        Libdnf5 plugin for detecting and removing expired PGP keys
License:        LGPL-2.1-or-later
Requires:       libdnf5%{?_isa} = %{version}-%{release}
Requires:       gnupg2
%if 0%{?fedora} >= 43 || 0%{?rhel} >= 11 || 0%{?oreon} >= 11
Requires:       rpm-libs%{?_isa} >= 5.99.90
%endif
%description -n libdnf5-plugin-expired-pgp-keys
Libdnf5 plugin for detecting and removing expired PGP keys.

%if %{with libdnf_cli}
%package -n libdnf5-plugin-rhsm
Summary:        Libdnf5 rhsm (Red Hat Subscription Manager) plugin
License:        LGPL-2.1-or-later
Requires:       libdnf5%{?_isa} = %{version}-%{release}
%description -n libdnf5-plugin-rhsm
Libdnf5 plugin with basic support for Red Hat subscriptions.
Synchronizes the the enrollment with the vendor system. This can change
the contents of the repositories configuration files according
to the subscription levels.

%if %{with libdnf_cli}
%package -n python3-libdnf5-python-plugins-loader
Summary:        Libdnf5 plugin that allows loading Python plugins
License:        LGPL-2.1-or-later
Requires:       libdnf5%{?_isa} = %{version}-%{release}
Requires:       python3-libdnf5%{?_isa} = %{version}-%{release}
%description -n python3-libdnf5-python-plugins-loader
Libdnf5 plugin that allows loading Python plugins.

%if %{with libdnf_cli}
%package -n libdnf5-plugin-local
Summary:        Libdnf5 plugin that automatically copies all downloaded packages to a local repository
License:        LGPL-2.1-or-later
Requires:       libdnf5%{?_isa} = %{version}-%{release}
Requires:       createrepo_c
%description -n libdnf5-plugin-local
Libdnf5 plugin that automatically copies all downloaded packages to a repository on the local filesystem and generates repo metadata.

%if %{with libdnf_cli}
%package -n dnf5daemon-client
Summary:        Command-line interface for dnf5daemon-server
License:        GPL-2.0-or-later
Requires:       libdnf5%{?_isa} = %{version}-%{release}
Requires:       libdnf5-cli%{?_isa} = %{version}-%{release}
Requires:       dnf5daemon-server
%description -n dnf5daemon-client
Command-line interface for dnf5daemon-server.

%if %{with libdnf_cli}
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
%if %{with libdnf_cli}
%package -n dnf5daemon-server-polkit
Summary:        Polkit rule to allow wheel group members install trusted packages
License:        GPL-2.0-or-later
Requires:       polkit
Requires:       dnf5daemon-server = %{version}-%{release}
BuildArch:      noarch
%description -n dnf5daemon-server-polkit
Polkit rule to allow active local wheel group members install packages from
trusted repositories using dnf5daemon-server.

%if %{with libdnf_cli}
%package -n dnf5-plugins
Summary:        Plugins for dnf5
License:        LGPL-2.1-or-later
Requires:       dnf5%{?_isa} = %{version}-%{release}
Requires:       libcurl%{?_isa} >= 7.62.0
Requires:       libdnf5%{?_isa} = %{version}-%{release}
Requires:       libdnf5-cli%{?_isa} = %{version}-%{release}
Provides:       dnf5-command(builddep)
Provides:       dnf5-command(changelog)
Provides:       dnf5-command(config-manager)
Provides:       dnf5-command(copr)
Provides:       dnf5-command(needs-restarting)
Provides:       dnf5-command(repoclosure)
Provides:       dnf5-command(reposync)
Provides:       dnf5-command(repomanage)
%description -n dnf5-plugins
Core DNF5 plugins that enhance dnf5 with builddep, changelog, config-manager,
copr, needs-restarting, repoclosure, repomanage, and reposync commands.

%if %{with libdnf_cli}
%package plugin-automatic
Summary:        Package manager - automated upgrades
License:        LGPL-2.1-or-later
Requires:       dnf5%{?_isa} = %{version}-%{release}
Requires:       libcurl-full%{?_isa}
Requires:       libdnf5%{?_isa} = %{version}-%{release}
Requires:       libdnf5-cli%{?_isa} = %{version}-%{release}
Provides:       dnf5-command(automatic)
%if %{with dnf5_obsoletes_dnf}
Provides:       dnf-automatic = %{version}-%{release}
Obsoletes:      dnf-automatic < 5
%else
Conflicts:      dnf-automatic < 5
%endif
%description plugin-automatic
Alternative command-line interface "dnf upgrade" suitable to be executed
automatically and regularly from systemd timers, cron jobs or similar.

%package plugin-manifest
Summary:        DNF5 plugin for working with RPM package manifest files
License:        LGPL-2.1-or-later
Requires:       dnf5%{?_isa} = %{version}-%{release}
Requires:       libdnf5%{?_isa} = %{version}-%{release}
Requires:       libdnf5-cli%{?_isa} = %{version}-%{release}
Provides:       dnf5-command(manifest)
%description plugin-manifest
DNF5 plugin for working with RPM package manifest files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir dnf5-%{version}
%oreon_prep
%build

%cmake \
    -DPACKAGE_VERSION=%{version} \
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
    -DWITH_PYTHON_PLUGINS_LOADER=%{?with_python_plugins_loader:ON}%{!?with_python_plugins_loader:OFF} \
    \
    -DWITH_ACL=%{?with_acl:ON}%{!?with_acl:OFF} \
    -DWITH_COMPS=%{?with_comps:ON}%{!?with_comps:OFF} \
    -DWITH_MODULEMD=%{?with_modulemd:ON}%{!?with_modulemd:OFF} \
    -DWITH_SYSTEMD=%{?with_systemd:ON}%{!?with_systemd:OFF} \
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
ln -sr %{buildroot}%{_datadir}/bash-completion/completions/dnf5 %{buildroot}%{_datadir}/bash-completion/completions/dnf
%if %{with man}
    for file in %{buildroot}%{_mandir}/man[578]/dnf5[-.]*; do
        dir=$(dirname $file)
        filename=$(basename $file)
        ln -sr $file $dir/${filename/dnf5/dnf}
    done
%endif
mv %{buildroot}%{_unitdir}/dnf5-makecache.service %{buildroot}%{_unitdir}/dnf-makecache.service
mv %{buildroot}%{_unitdir}/dnf5-makecache.timer %{buildroot}%{_unitdir}/dnf-makecache.timer
ln -s dnf-makecache.service %{buildroot}%{_unitdir}/dnf5-makecache.service
ln -s dnf-makecache.timer %{buildroot}%{_unitdir}/dnf5-makecache.timer
%endif
mkdir -p %{buildroot}%{_prefix}/lib/sysimage/libdnf5
for file in \
    environments.toml groups.toml modules.toml nevras.toml packages.toml \
    system.toml \
    transaction_history.sqlite transaction_history.sqlite-shm \
    transaction_history.sqlite-wal \
    system-repo.lock
do
    touch %{buildroot}%{_prefix}/lib/sysimage/libdnf5/$file
done
mkdir -p %{buildroot}%{_prefix}/lib/sysimage/libdnf5/comps_groups
mkdir -p %{buildroot}%{_prefix}/lib/sysimage/libdnf5/offline
touch %{buildroot}%{_sysconfdir}/dnf/versionlock.toml
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
%ldconfig_scriptlets
%oreon_autofiles libdnf5 usr/*/lib*.so.*
%oreon_autofiles libdnf5-cli usr/*/lib*.so.*
%oreon_autofiles dnf5-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libdnf5-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libdnf5-cli-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles perl-libdnf5 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles perl-libdnf5-cli usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-libdnf5 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-libdnf5-cli usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ruby-libdnf5 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ruby-libdnf5-cli usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles libdnf5-plugin-actions usr/*/lib*.so.*
%oreon_autofiles libdnf5-plugin-appstream usr/*/lib*.so.*
%oreon_autofiles libdnf5-plugin-expired-pgp-keys usr/*/lib*.so.*
%oreon_autofiles libdnf5-plugin-rhsm usr/*/lib*.so.*
%oreon_autofiles python3-libdnf5-python-plugins-loader usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles libdnf5-plugin-local usr/*/lib*.so.*
%oreon_autofiles dnf5daemon-client usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles dnf5daemon-server usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles dnf5daemon-server-polkit usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles dnf5-plugins usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/*/lib*.so.* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/*/lib*.so.* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n libdnf5 -f %{oreon_filedir}/libdnf5.list
%files -n libdnf5-cli -f %{oreon_filedir}/libdnf5-cli.list
%files -n dnf5-devel -f %{oreon_filedir}/dnf5-devel.list
%files -n libdnf5-devel -f %{oreon_filedir}/libdnf5-devel.list
%files -n libdnf5-cli-devel -f %{oreon_filedir}/libdnf5-cli-devel.list
%files -n perl-libdnf5 -f %{oreon_filedir}/perl-libdnf5.list
%files -n perl-libdnf5-cli -f %{oreon_filedir}/perl-libdnf5-cli.list
%files -n python3-libdnf5 -f %{oreon_filedir}/python3-libdnf5.list
%files -n python3-libdnf5-cli -f %{oreon_filedir}/python3-libdnf5-cli.list
%files -n ruby-libdnf5 -f %{oreon_filedir}/ruby-libdnf5.list
%files -n ruby-libdnf5-cli -f %{oreon_filedir}/ruby-libdnf5-cli.list
%files -n libdnf5-plugin-actions -f %{oreon_filedir}/libdnf5-plugin-actions.list
%files -n libdnf5-plugin-appstream -f %{oreon_filedir}/libdnf5-plugin-appstream.list
%files -n libdnf5-plugin-expired-pgp-keys -f %{oreon_filedir}/libdnf5-plugin-expired-pgp-keys.list
%files -n libdnf5-plugin-rhsm -f %{oreon_filedir}/libdnf5-plugin-rhsm.list
%files -n python3-libdnf5-python-plugins-loader -f %{oreon_filedir}/python3-libdnf5-python-plugins-loader.list
%files -n libdnf5-plugin-local -f %{oreon_filedir}/libdnf5-plugin-local.list
%files -n dnf5daemon-client -f %{oreon_filedir}/dnf5daemon-client.list
%files -n dnf5daemon-server -f %{oreon_filedir}/dnf5daemon-server.list
%files -n dnf5daemon-server-polkit -f %{oreon_filedir}/dnf5daemon-server-polkit.list
%files -n dnf5-plugins -f %{oreon_filedir}/dnf5-plugins.list
%files -n dnf5-plugin-automatic -f %{oreon_filedir}/dnf5-plugin-automatic.list
%files -n dnf5-plugin-manifest -f %{oreon_filedir}/dnf5-plugin-manifest.list

%changelog

%autochangelog
%endif
%endif
%endif
%endif
%endif
%endif
%endif
%endif
%endif
%endif
%endif
%endif
%endif
%endif
%endif
%endif
%endif
%endif
%endif
%endif
