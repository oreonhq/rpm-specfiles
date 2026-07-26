%global source0_hash cdae785ad8a0c2de20972a8bcfb8b73a2b558e62b06a26b36301c33ee3ae01f8

# Conditional for release vs. snapshot builds. Set to 1 for release build.
%if ! 0%{?rel_build:1}
    %global rel_build 1
%endif

# Settings used for build from snapshots.
%if 0%{?rel_build}
    %global gitref          %{version}
    %global gittar          avocado-%{version}.tar.gz
%else
    %if ! 0%{?commit:1}
        %global commit      e4ede79f097dcc1dbd30e43ffe3b7daf52d2204d
    %endif
    %if ! 0%{?commit_date:1}
        %global commit_date 20251010
    %endif
    %global shortcommit     %(c=%{commit};echo ${c:0:9})
    %global gitrel          .%{commit_date}git%{shortcommit}
    %global gitref          %{commit}
    %global gittar          avocado-%{shortcommit}.tar.gz
%endif

# Selftests are provided but may need to be skipped because many of
# the functional tests are time and resource sensitive and can
# cause race conditions and random build failures. They are
# enabled by default.
# You can disable them with rpmbuild ... --without tests
%bcond_without tests

# Only Fedora 36 and later have a suitable python3-resutlsdb_api
# package
%if 0%{?fedora} >= 36
%global with_resultsdb 1
%else
%global with_resultsdb 0
%endif

Name: python-avocado
Version: 112.0
Release: 1%{?gitrel}%{?dist}
Summary: Framework with tools and libraries for Automated Testing
# Found licenses:
# avocado/core/tapparser.py: MIT
# avocado/utils/external/gdbmi_parser.py: MIT
# avocado/utils/external/spark.py: MIT
# optional_plugins/html/avocado_result_html/templates/bootstrap.min.css: MIT
# optional_plugins/html/avocado_result_html/templates/bootstrap.min.js: MIT
# selftests/.data/jenkins-junit.xsd: MIT
# Other files: GPLv2 and GPLv2+
License: GPLv2+ and GPLv2 and MIT
URL: https://avocado-framework.github.io/
Source0: https://github.com/avocado-framework/avocado/archive/%{gitref}/%{gittar}
BuildArch: noarch

BuildRequires: kmod
BuildRequires: procps-ng
BuildRequires: python3-devel
BuildRequires: python3-docutils
BuildRequires: python3-jinja2
BuildRequires: python3-lxml
BuildRequires: python3-psutil
BuildRequires: python3-setuptools
%if ! 0%{?rhel}
BuildRequires: python-aexpect
%endif
%if %{with_resultsdb}
BuildRequires: python3-resultsdb_api
BuildRequires: python3-pycdlib
%endif

%if %{with tests}
BuildRequires: python3-jsonschema
%if ! 0%{?rhel} >= 9
BuildRequires: genisoimage
%endif
BuildRequires: libcdio
BuildRequires: psmisc
%if ! 0%{?rhel}
BuildRequires: perl-Test-Harness
BuildRequires: python3-xmlschema
BuildRequires: ansible-core
%endif
BuildRequires: glibc-all-langpacks
BuildRequires: python3-netifaces
BuildRequires: python3-yaml
BuildRequires: nmap-ncat
BuildRequires: gcc
BuildRequires: gdb
BuildRequires: gdb-gdbserver
%endif
# with tests

%description
Avocado is a set of tools and libraries (what people call
these days a framework) to perform automated testing.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n avocado-%{gitref}
%if 0%{?rhel}
sed -e 's/"PyYAML>=4.2b2"/"PyYAML>=3.12"/' -i optional_plugins/varianter_yaml_to_mux/setup.py
%endif
%if 0%{?fedora} >= 42
sed -e '/"markupsafe<3.0.0"/d' -i optional_plugins/html/setup.py
sed -e '/"markupsafe<3.0.0"/d' -i optional_plugins/ansible/setup.py
%endif

%build
%py3_build
pushd optional_plugins/html
    %py3_build
popd
%if %{with_resultsdb}
pushd optional_plugins/resultsdb
    %py3_build
popd
%endif
pushd optional_plugins/varianter_yaml_to_mux
    %py3_build
popd
pushd optional_plugins/golang
    %py3_build
popd
%if ! 0%{?rhel}
pushd optional_plugins/ansible
    %py3_build
popd
%endif
pushd optional_plugins/varianter_pict
    %py3_build
popd
pushd optional_plugins/varianter_cit
    %py3_build
popd
pushd optional_plugins/result_upload
    %py3_build
popd
pushd optional_plugins/mail
    %py3_build
popd
%if ! 0%{?rhel}
pushd optional_plugins/spawner_remote
    %py3_build
popd
%endif
rst2man man/avocado.rst man/avocado.1

%install
%py3_install
for exe in \
    avocado \
    avocado-runner-noop \
    avocado-runner-dry-run \
    avocado-runner-exec-test \
    avocado-runner-python-unittest \
    avocado-runner-avocado-instrumented \
    avocado-runner-tap \
    avocado-runner-asset \
    avocado-runner-package \
    avocado-runner-pip \
    avocado-runner-podman-image \
    avocado-runner-sysinfo \
    avocado-runner-vmimage \
    avocado-external-runner \
    avocado-software-manager
do
    mv %{buildroot}%{_bindir}/$exe %{buildroot}%{_bindir}/$exe-%{python3_version}
    ln -s $exe-%{python3_version} %{buildroot}%{_bindir}/$exe-3
    ln -s $exe-%{python3_version} %{buildroot}%{_bindir}/$exe
done
# configuration is held at /etc/avocado only and part of the
# python-avocado-common package
rm -rf %{buildroot}%{python3_sitelib}/avocado/etc
# ditto for libexec files
rm -rf %{buildroot}%{python3_sitelib}/avocado/libexec
pushd optional_plugins/html
    %py3_install
popd
%if %{with_resultsdb}
pushd optional_plugins/resultsdb
    %py3_install
popd
%endif
pushd optional_plugins/varianter_yaml_to_mux
    %py3_install
popd
pushd optional_plugins/golang
    %py3_install
popd
%if ! 0%{?rhel}
pushd optional_plugins/ansible
    %py3_install
popd
%endif
pushd optional_plugins/varianter_pict
    %py3_install
popd
pushd optional_plugins/varianter_cit
    %py3_install
popd
pushd optional_plugins/result_upload
    %py3_install
popd
pushd optional_plugins/mail
    %py3_install
popd
%if ! 0%{?rhel}
pushd optional_plugins/spawner_remote
    %py3_install
popd
%endif
# cleanup plugin test cruft
rm -rf %{buildroot}%{python3_sitelib}/tests
mkdir -p %{buildroot}%{_sysconfdir}/avocado
cp -r avocado/etc/avocado/scripts %{buildroot}%{_sysconfdir}/avocado/scripts
cp -r avocado/etc/avocado/sysinfo %{buildroot}%{_sysconfdir}/avocado/sysinfo
mkdir -p %{buildroot}%{_libexecdir}/avocado
cp avocado/libexec/avocado-bash-utils %{buildroot}%{_libexecdir}/avocado/avocado-bash-utils
cp avocado/libexec/avocado_debug %{buildroot}%{_libexecdir}/avocado/avocado_debug
cp avocado/libexec/avocado_error %{buildroot}%{_libexecdir}/avocado/avocado_error
cp avocado/libexec/avocado_info %{buildroot}%{_libexecdir}/avocado/avocado_info
cp avocado/libexec/avocado_warn %{buildroot}%{_libexecdir}/avocado/avocado_warn
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 man/avocado.1 %{buildroot}%{_mandir}/man1/avocado.1
mkdir -p %{buildroot}%{_pkgdocdir}
install -m 0644 README.rst %{buildroot}%{_pkgdocdir}
install -d -m 0755 %{buildroot}%{_sharedstatedir}/avocado/data
# place examples in documentation directory
install -d -m 0755 %{buildroot}%{_docdir}/avocado
cp -r examples/gdb-prerun-scripts %{buildroot}%{_docdir}/avocado/gdb-prerun-scripts
cp -r examples/plugins %{buildroot}%{_docdir}/avocado/plugins
cp -r examples/tests %{buildroot}%{_docdir}/avocado/tests
cp -r examples/varianter_cit %{buildroot}%{_docdir}/avocado/varianter_cit
cp -r examples/varianter_pict %{buildroot}%{_docdir}/avocado/varianter_pict
cp -r examples/yaml_to_mux %{buildroot}%{_docdir}/avocado/yaml_to_mux
mkdir -p %{buildroot}%{_datarootdir}/avocado
mv %{buildroot}%{python3_sitelib}/avocado/schemas %{buildroot}%{_datarootdir}/avocado
find %{buildroot}%{_docdir}/avocado -type f -name '*.py' -exec chmod -c -x {} ';'

%if %{with tests}
%check
    # LANG: to make the results predictable, we pin the language
    # that is used during test execution.
    # AVOCADO_CHECK_LEVEL: package build environments have the least
    # amount of resources we have observed so far. Let's avoid tests that
    # require too much resources or are time sensitive
    PATH=%{buildroot}%{_bindir}:%{buildroot}%{_libexecdir}/avocado:$PATH \
        PYTHONPATH=%{buildroot}%{python3_sitelib}:. \
        LANG=en_US.UTF-8 \
        AVOCADO_CHECK_LEVEL=0 \
        %{python3} selftests/check.py --skip static-checks --disable-plugin-checks robot
%endif

%package -n python3-avocado
Summary: %{summary}
Requires: python-avocado-common == %{version}-%{release}
Requires: gdb
Requires: gdb-gdbserver
Requires: procps-ng
%if ! 0%{?rhel}
Requires: python3-pycdlib
%endif

%description -n python3-avocado
Avocado is a set of tools and libraries (what people call
these days a framework) to perform automated testing.

%files -n python3-avocado
%license LICENSE
%{_pkgdocdir}/README.rst
%{python3_sitelib}/avocado/
%{python3_sitelib}/avocado_framework-%{version}-py%{python3_version}.egg-info
%{_bindir}/avocado-%{python3_version}
%{_bindir}/avocado-3
%{_bindir}/avocado
%{_bindir}/avocado-runner-noop-%{python3_version}
%{_bindir}/avocado-runner-noop-3
%{_bindir}/avocado-runner-noop
%{_bindir}/avocado-runner-dry-run-%{python3_version}
%{_bindir}/avocado-runner-dry-run-3
%{_bindir}/avocado-runner-dry-run
%{_bindir}/avocado-runner-exec-test-%{python3_version}
%{_bindir}/avocado-runner-exec-test-3
%{_bindir}/avocado-runner-exec-test
%{_bindir}/avocado-runner-python-unittest-%{python3_version}
%{_bindir}/avocado-runner-python-unittest-3
%{_bindir}/avocado-runner-python-unittest
%{_bindir}/avocado-runner-avocado-instrumented-%{python3_version}
%{_bindir}/avocado-runner-avocado-instrumented-3
%{_bindir}/avocado-runner-avocado-instrumented
%{_bindir}/avocado-runner-tap-%{python3_version}
%{_bindir}/avocado-runner-tap-3
%{_bindir}/avocado-runner-tap
%{_bindir}/avocado-runner-asset-%{python3_version}
%{_bindir}/avocado-runner-asset-3
%{_bindir}/avocado-runner-asset
%{_bindir}/avocado-runner-package-%{python3_version}
%{_bindir}/avocado-runner-package-3
%{_bindir}/avocado-runner-package
%{_bindir}/avocado-runner-pip-%{python3_version}
%{_bindir}/avocado-runner-pip-3
%{_bindir}/avocado-runner-pip
%{_bindir}/avocado-runner-podman-image-%{python3_version}
%{_bindir}/avocado-runner-podman-image-3
%{_bindir}/avocado-runner-podman-image
%{_bindir}/avocado-runner-sysinfo-%{python3_version}
%{_bindir}/avocado-runner-sysinfo-3
%{_bindir}/avocado-runner-sysinfo
%{_bindir}/avocado-runner-vmimage-%{python3_version}
%{_bindir}/avocado-runner-vmimage-3
%{_bindir}/avocado-runner-vmimage
%{_bindir}/avocado-software-manager-%{python3_version}
%{_bindir}/avocado-software-manager-3
%{_bindir}/avocado-software-manager
%{_bindir}/avocado-external-runner-%{python3_version}
%{_bindir}/avocado-external-runner-3
%{_bindir}/avocado-external-runner

%package -n python-avocado-common
Summary: Avocado common files
License: GPLv2+

%description -n python-avocado-common
Common files (such as configuration) for the Avocado Testing Framework.

%files -n python-avocado-common
%license LICENSE
%{_mandir}/man1/avocado.1.gz
%dir %{_docdir}/avocado
%dir %{_sharedstatedir}/avocado
%dir %{_sysconfdir}/avocado
%dir %{_sysconfdir}/avocado/sysinfo
%dir %{_sysconfdir}/avocado/scripts
%dir %{_sysconfdir}/avocado/scripts/job
%dir %{_sysconfdir}/avocado/scripts/job/pre.d
%dir %{_sysconfdir}/avocado/scripts/job/post.d
%dir %{_sharedstatedir}/avocado/data
%dir %{_datarootdir}/avocado
%dir %{_datarootdir}/avocado/schemas
%{_datarootdir}/avocado/schemas/*
%config(noreplace) %{_sysconfdir}/avocado/sysinfo/commands
%config(noreplace) %{_sysconfdir}/avocado/sysinfo/files
%config(noreplace) %{_sysconfdir}/avocado/sysinfo/profilers
%{_sysconfdir}/avocado/scripts/job/pre.d/README
%{_sysconfdir}/avocado/scripts/job/post.d/README

%package -n python3-avocado-plugins-output-html
Summary: Avocado HTML report plugin
License: GPLv2+ and MIT
Requires: python3-avocado == %{version}-%{release}

%description -n python3-avocado-plugins-output-html
Adds to avocado the ability to generate an HTML report at every job results
directory. It also gives the user the ability to write a report on an
arbitrary filesystem location.

%files -n python3-avocado-plugins-output-html
%{python3_sitelib}/avocado_result_html/
%{python3_sitelib}/avocado_framework_plugin_result_html-%{version}-py%{python3_version}.egg-info

%if %{with_resultsdb}
%package -n python3-avocado-plugins-resultsdb
Summary: Avocado plugin to propagate job results to ResultsDB
License: GPLv2+
Requires: python3-avocado == %{version}-%{release}

%description -n python3-avocado-plugins-resultsdb
Allows Avocado to send job results directly to a ResultsDB
server.

%files -n python3-avocado-plugins-resultsdb
%{python3_sitelib}/avocado_resultsdb/
%{python3_sitelib}/avocado_framework_plugin_resultsdb-%{version}-py%{python3_version}.egg-info
%endif
# with_resultsdb

%package -n python3-avocado-plugins-varianter-yaml-to-mux
Summary: Avocado plugin to generate variants out of yaml files
License: GPLv2+
Requires: python3-avocado == %{version}-%{release}

%description -n python3-avocado-plugins-varianter-yaml-to-mux
Can be used to produce multiple test variants with test parameters
defined in a yaml file(s).

%files -n python3-avocado-plugins-varianter-yaml-to-mux
%{python3_sitelib}/avocado_varianter_yaml_to_mux/
%{python3_sitelib}/avocado_framework_plugin_varianter_yaml_to_mux-%{version}-py%{python3_version}.egg-info

%package -n python3-avocado-plugins-golang
Summary: Avocado plugin for execution of golang tests
License: GPLv2+
Requires: python3-avocado == %{version}-%{release}
Requires: golang

%description -n python3-avocado-plugins-golang
Allows Avocado to list golang tests, and if golang is installed,
also run them.

%files -n python3-avocado-plugins-golang
%{python3_sitelib}/avocado_golang/
%{python3_sitelib}/avocado_framework_plugin_golang-%{version}-py%{python3_version}.egg-info
%{_bindir}/avocado-runner-golang

%if ! 0%{?rhel}
%package -n python3-avocado-plugins-ansible
Summary: Avocado Ansible Dependency plugin
License: GPLv2+
Requires: python3-avocado == %{version}-%{release}
Requires: ansible-core

%description -n python3-avocado-plugins-ansible
Adds to Avocado the ability to use ansible modules as dependecies for
tests.

%files -n python3-avocado-plugins-ansible
%{python3_sitelib}/avocado_ansible*
%{python3_sitelib}/avocado_framework_plugin_ansible*
%{_bindir}/avocado-runner-ansible-module
%endif

%package -n python3-avocado-plugins-varianter-pict
Summary: Varianter with combinatorial capabilities by PICT
License: GPLv2+
Requires: python3-avocado == %{version}-%{release}

%description -n python3-avocado-plugins-varianter-pict
This plugin uses a third-party tool to provide variants created by
Pair-Wise algorithms, also known as Combinatorial Independent Testing.

%files -n python3-avocado-plugins-varianter-pict
%{python3_sitelib}/avocado_varianter_pict/
%{python3_sitelib}/avocado_framework_plugin_varianter_pict-%{version}-py%{python3_version}.egg-info

%package -n python3-avocado-plugins-varianter-cit
Summary: Varianter with Combinatorial Independent Testing capabilities
License: GPLv2+
Requires: python3-avocado == %{version}-%{release}

%description -n python3-avocado-plugins-varianter-cit
A varianter plugin that generates variants using Combinatorial
Independent Testing (AKA Pair-Wise) algorithm developed in
collaboration with CVUT Prague.

%files -n python3-avocado-plugins-varianter-cit
%{python3_sitelib}/avocado_varianter_cit/
%{python3_sitelib}/avocado_framework_plugin_varianter_cit-%{version}-py%{python3_version}.egg-info

%package -n python3-avocado-plugins-result-upload
Summary: Avocado plugin propagate job results to a remote host
License: GPLv2+
Requires: python3-avocado == %{version}-%{release}

%description -n python3-avocado-plugins-result-upload
This optional plugin is intended to upload the Avocado Job results to
a dedicated sever.

%files -n python3-avocado-plugins-result-upload
%{python3_sitelib}/avocado_result_upload/
%{python3_sitelib}/avocado_framework_plugin_result_upload-%{version}-py%{python3_version}.egg-info

%package -n python3-avocado-plugins-result-mail
Summary: Avocado Mail Notification for Jobs
License: GPLv2+
Requires: python3-avocado == %{version}-%{release}

%description -n python3-avocado-plugins-result-mail
The Mail result plugin enables you to receive email notifications
for job start and completion events within the Avocado testing framework.

%files -n python3-avocado-plugins-result-mail
%{python3_sitelib}/avocado_result_mail*
%{python3_sitelib}/avocado_framework_plugin_result_mail*

%if ! 0%{?rhel}
%package -n python3-avocado-plugins-spawner-remote
Summary: Avocado Plugin to spawn tests on a remote host
License: GPLv2+
Requires: python3-avocado == %{version}-%{release}

%description -n python3-avocado-plugins-spawner-remote
This optional plugin is intended to spawn tests on a remote host.

%files -n python3-avocado-plugins-spawner-remote
%{python3_sitelib}/avocado_spawner_remote*
%{python3_sitelib}/avocado_framework_plugin_spawner_remote*
%endif

%package -n python-avocado-examples
Summary: Avocado Test Framework Example Tests
License: GPLv2+
# documentation does not require main package, but needs to be in lock-step if present
Conflicts: python3-avocado < %{version}-%{release}, python3-avocado > %{version}-%{release}

%description -n python-avocado-examples
The set of example tests present in the upstream tree of the Avocado framework.
Some of them are used as functional tests of the framework, others serve as
examples of how to write tests on your own.

%files -n python-avocado-examples
%license LICENSE
%dir %{_docdir}/avocado
%{_docdir}/avocado/gdb-prerun-scripts
%{_docdir}/avocado/plugins
%{_docdir}/avocado/tests
%{_docdir}/avocado/varianter_cit
%{_docdir}/avocado/varianter_pict
%{_docdir}/avocado/yaml_to_mux

%package -n python-avocado-bash
Summary: Avocado Test Framework Bash Utilities
License: GPLv2+ and GPLv2
Requires: python-avocado-common == %{version}-%{release}

%description -n python-avocado-bash
A small set of utilities to interact with Avocado from the Bourne
Again Shell code (and possibly other similar shells).

%files -n python-avocado-bash
%license LICENSE
%dir %{_libexecdir}/avocado
%{_libexecdir}/avocado/avocado-bash-utils
%{_libexecdir}/avocado/avocado_debug
%{_libexecdir}/avocado/avocado_error
%{_libexecdir}/avocado/avocado_info
%{_libexecdir}/avocado/avocado_warn

%changelog
%autochangelog
