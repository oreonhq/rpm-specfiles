%global source0_hash e5abd9666ca423bf36b38740ac6a2ffd6fb80403565a590fddba649114295656

%global owner projectatomic
%global project atomic-reactor

%global dock_obsolete_vr 1.3.7-2

Name:           %{project}
Version:        4.21.0
Release:        8%{?dist}

Summary:        Improved builder for Docker images
# Automatically converted from old format: BSD - review is highly recommended.
License:        BSD-2-Clause
URL:            https://github.com/%{owner}/%{project}
Source0:        https://github.com/containerbuildsystem/atomic-reactor/archive/refs/tags/%{version}.tar.gz

# https://pagure.io/releng/issue/11092
# https://github.com/containerbuildsystem/atomic-reactor/issues/2027
# https://fedoraproject.org/wiki/Changes/RelocateRPMToUsr
Patch0:         atomic-reactor-rpmqa-dbpath.patch

BuildArch:      noarch
Requires:       python3-atomic-reactor = %{version}-%{release}
Requires:       git >= 1.7.10

BuildRequires:  python3-devel
%if 0%{?with_check}
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-capturelog
BuildRequires:  python3-dockerfile-parse >= 0.0.5
BuildRequires:  python3-docker
BuildRequires:  python3-flexmock >= 0.10.2
BuildRequires:  python3-six
BuildRequires:  python3-osbs-client >= 0.45
BuildRequires:  python3-reflink
BuildRequires:  python3-responses
BuildRequires:  python3-jsonschema
BuildRequires:  python3-PyYAML
BuildRequires:  python3-mock
BuildRequires:  python3-docker-squash >= 1.0.0-0.3
%endif
# with_check

Provides:       dock = %{version}-%{release}
Obsoletes:      dock < %{dock_obsolete_vr}

%description
Simple Python tool with command line interface for building Docker
images. It contains a lot of helpful functions which you would
probably implement if you started hooking Docker into your
infrastructure.

%package -n python3-atomic-reactor
Summary:        Python 3 Atomic Reactor library
Requires:       python3-docker
Requires:       python3-requests
Requires:       python3-reflink
Requires:       python3-setuptools
Requires:       python3-dockerfile-parse >= 0.0.5
Requires:       python3-docker-squash >= 1.0.0-0.3
Requires:       python3-jsonschema
Requires:       python3-PyYAML
Provides:       python3-dock = %{version}-%{release}
Obsoletes:      python3-dock < %{dock_obsolete_vr}
%{?python_provide:%python_provide python3-atomic-reactor}

%description -n python3-atomic-reactor
Simple Python 3 library for building Docker images. It contains
a lot of helpful functions which you would probably implement if
you started hooking Docker into your infrastructure.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

#%%autosetup -p1 -n %{name}-%{version}
%setup -q
%patch -P0 -p1
%if 0%{fedora} >= 36
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

mkdir -p %{buildroot}%{_mandir}/man1
cp -a docs/manpage/atomic-reactor.1 %{buildroot}%{_mandir}/man1/

%if 0%{?with_check}
%check
%{__python3} -m pytest -vv tests
%endif
# with_check

%files
%doc README.md
%license LICENSE
%{_bindir}/atomic-reactor
%{_mandir}/man1/atomic-reactor.1*

%files -n python3-atomic-reactor
%doc README.md
%doc docs/*.md
%license LICENSE
%dir %{python3_sitelib}/atomic_reactor
%dir %{python3_sitelib}/atomic_reactor/__pycache__
%{python3_sitelib}/atomic_reactor-%{version}.dist-info/INSTALLER
%{python3_sitelib}/atomic_reactor-%{version}.dist-info/METADATA
%{python3_sitelib}/atomic_reactor-%{version}.dist-info/WHEEL
%{python3_sitelib}/atomic_reactor-%{version}.dist-info/entry_points.txt
%{python3_sitelib}/atomic_reactor-%{version}.dist-info/licenses/LICENSE
%{python3_sitelib}/atomic_reactor-%{version}.dist-info/top_level.txt
%{python3_sitelib}/atomic_reactor/*.*
%{python3_sitelib}/atomic_reactor/__pycache__/*.py*
%{python3_sitelib}/atomic_reactor/cli
%{python3_sitelib}/atomic_reactor/plugins
%{python3_sitelib}/atomic_reactor/schemas
%{python3_sitelib}/atomic_reactor/tasks
%{python3_sitelib}/atomic_reactor/utils

%changelog
%autochangelog
