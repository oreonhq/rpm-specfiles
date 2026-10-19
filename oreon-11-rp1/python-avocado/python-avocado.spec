%global source0_hash a916c90b43e67d4593feef121f820d3fd8c93c2aca2dbd2d8865f83a622d3487
%if ! 0%{?rel_build:1}
    %global rel_build 1
%endif
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
%bcond_without tests
%global with_resultsdb 0
Name: python-avocado
Version: 113.0
Release:        1%{?dist}
Summary:        Framework with tools and libraries for Automated Testing
License: GPLv2+ and GPLv2 and MIT
URL: https://avocado-framework.github.io/
Source0:        https://github.com/avocado-framework/avocado/archive/%{version}/avocado-%{version}.tar.gz
BuildArch: noarch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gdb
BuildRequires:  gdb-gdbserver
BuildRequires:  glibc-all-langpacks
BuildRequires:  kmod
BuildRequires:  libcdio
BuildRequires:  nmap-ncat
BuildRequires:  procps-ng
BuildRequires:  psmisc
BuildRequires:  python3-devel
BuildRequires:  python3-docutils
BuildRequires:  python3-jinja2
BuildRequires:  python3-jsonschema
BuildRequires:  python3-lxml
BuildRequires:  python3-netifaces
BuildRequires:  python3-psutil
BuildRequires:  python3-setuptools
BuildRequires:  python3-yaml
# /oreon:deps
%description
Avocado is a set of tools and libraries (what people call
these days a framework) to perform automated testing.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n avocado-%{gitref}

%build

%py3_build
pushd optional_plugins/html
    %py3_build
popd
pushd optional_plugins/varianter_yaml_to_mux
    %py3_build
popd
pushd optional_plugins/golang
    %py3_build
popd
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
rm -rf %{buildroot}%{python3_sitelib}/avocado/etc
rm -rf %{buildroot}%{python3_sitelib}/avocado/libexec
pushd optional_plugins/html
    %py3_install
popd
pushd optional_plugins/varianter_yaml_to_mux
    %py3_install
popd
pushd optional_plugins/golang
    %py3_install
popd
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with tests}
%check

    PATH=%{buildroot}%{_bindir}:%{buildroot}%{_libexecdir}/avocado:$PATH \
        PYTHONPATH=%{buildroot}%{python3_sitelib}:. \
        LANG=en_US.UTF-8 \
        AVOCADO_CHECK_LEVEL=0 \
        %{python3} selftests/check.py --skip static-checks --disable-plugin-checks robot
%endif
%package -n python3-avocado
Summary:        Framework with tools and libraries for Automated Testing
Requires: python-avocado-common == %{version}-%{release}
Requires: gdb
Requires: gdb-gdbserver
Requires: procps-ng
%description -n python3-avocado
Avocado is a set of tools and libraries (what people call
these days a framework) to perform automated testing.

%package -n python-avocado-common
Summary: Avocado common files
License: GPLv2+
%description -n python-avocado-common
Common files (such as configuration) for the Avocado Testing Framework.

%package -n python3-avocado-plugins-output-html
Summary: Avocado HTML report plugin
License: GPLv2+ and MIT
Requires: python3-avocado == %{version}-%{release}
%description -n python3-avocado-plugins-output-html
Adds to avocado the ability to generate an HTML report at every job results
directory. It also gives the user the ability to write a report on an
arbitrary filesystem location.

%package -n python3-avocado-plugins-varianter-yaml-to-mux
Summary: Avocado plugin to generate variants out of yaml files
License: GPLv2+
Requires: python3-avocado == %{version}-%{release}
%description -n python3-avocado-plugins-varianter-yaml-to-mux
Can be used to produce multiple test variants with test parameters
defined in a yaml file(s).

%package -n python3-avocado-plugins-golang
Summary: Avocado plugin for execution of golang tests
License: GPLv2+
Requires: python3-avocado == %{version}-%{release}
Requires: golang
%description -n python3-avocado-plugins-golang
Allows Avocado to list golang tests, and if golang is installed,
also run them.

%package -n python3-avocado-plugins-varianter-pict
Summary: Varianter with combinatorial capabilities by PICT
License: GPLv2+
Requires: python3-avocado == %{version}-%{release}
%description -n python3-avocado-plugins-varianter-pict
This plugin uses a third-party tool to provide variants created by
Pair-Wise algorithms, also known as Combinatorial Independent Testing.

%package -n python3-avocado-plugins-varianter-cit
Summary: Varianter with Combinatorial Independent Testing capabilities
License: GPLv2+
Requires: python3-avocado == %{version}-%{release}
%description -n python3-avocado-plugins-varianter-cit
A varianter plugin that generates variants using Combinatorial
Independent Testing (AKA Pair-Wise) algorithm developed in
collaboration with CVUT Prague.

%package -n python3-avocado-plugins-result-upload
Summary: Avocado plugin propagate job results to a remote host
License: GPLv2+
Requires: python3-avocado == %{version}-%{release}
%description -n python3-avocado-plugins-result-upload
This optional plugin is intended to upload the Avocado Job results to
a dedicated sever.

%package -n python3-avocado-plugins-result-mail
Summary: Avocado Mail Notification for Jobs
License: GPLv2+
Requires: python3-avocado == %{version}-%{release}
%description -n python3-avocado-plugins-result-mail
The Mail result plugin enables you to receive email notifications
for job start and completion events within the Avocado testing framework.

%package -n python-avocado-examples
Summary: Avocado Test Framework Example Tests
License: GPLv2+
Conflicts: python3-avocado < %{version}-%{release}, python3-avocado > %{version}-%{release}
%description -n python-avocado-examples
The set of example tests present in the upstream tree of the Avocado framework.
Some of them are used as functional tests of the framework, others serve as
examples of how to write tests on your own.

%package -n python-avocado-bash
Summary: Avocado Test Framework Bash Utilities
License: GPLv2+ and GPLv2
Requires: python-avocado-common == %{version}-%{release}
%description -n python-avocado-bash
A small set of utilities to interact with Avocado from the Bourne
Again Shell code (and possibly other similar shells).

%files -f %{oreon_filedir}/main.list
%files -n python3-avocado -f %{oreon_filedir}/python3-avocado.list
%files -n python-avocado-common -f %{oreon_filedir}/python-avocado-common.list
%files -n python3-avocado-plugins-output-html -f %{oreon_filedir}/python3-avocado-plugins-output-html.list
%files -n python3-avocado-plugins-varianter-yaml-to-mux -f %{oreon_filedir}/python3-avocado-plugins-varianter-yaml-to-mux.list
%files -n python3-avocado-plugins-golang -f %{oreon_filedir}/python3-avocado-plugins-golang.list
%files -n python3-avocado-plugins-varianter-pict -f %{oreon_filedir}/python3-avocado-plugins-varianter-pict.list
%files -n python3-avocado-plugins-varianter-cit -f %{oreon_filedir}/python3-avocado-plugins-varianter-cit.list
%files -n python3-avocado-plugins-result-upload -f %{oreon_filedir}/python3-avocado-plugins-result-upload.list
%files -n python3-avocado-plugins-result-mail -f %{oreon_filedir}/python3-avocado-plugins-result-mail.list
%files -n python-avocado-examples -f %{oreon_filedir}/python-avocado-examples.list
%files -n python-avocado-bash -f %{oreon_filedir}/python-avocado-bash.list

%changelog

%autochangelog
