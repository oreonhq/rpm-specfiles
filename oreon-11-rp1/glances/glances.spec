%global source0_hash 3d344cd3b4ac14b08116aeb691d32c30366b4e555d87d45b693030f41404d26e
%global desc %{expand: \
Glances is a cross-platform monitoring tool which aims to present a large
amount of monitoring information through a curses or Web based interface.
The information dynamically adapts depending on the size of the user interface
It can also work in client/server mode. Remote monitoring could be done via
terminal, Web interface or API (XML-RPC and RESTful). Stats can also be
exported to files or external time/value databases.
Glances is written in Python and uses libraries to grab information from your
system. It is based on an open architecture where developers can add new 
plugins or exports modules.}
Name:		glances	
Version:	4.5.7
Release:        1%{?dist}
Summary:        A cross-platform system monitoring tool
License:	LGPL-3.0-only AND MIT
URL:		https://nicolargo.github.io/glances/
Source0:        https://github.com/nicolargo/glances/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.service
Patch0:		disable-update-check.patch
BuildArch:	noarch
Requires:	python3-fastapi
Requires:	python3-orjson
Requires:	python3-uvicorn
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 68
Requires:       python3-glances = %{version}-%{release}
# /oreon:deps
%package -n       python3-glances+action
Summary:        Metapackage for python3-glances action extras
Requires:       python3-glances = %{version}-%{release}
Provides:       python3dist(glances[action]) = %{version}-%{release}

%description -n python3-glances+action
Metapackage for python3-glances action extras.

%package -n       python3-glances+all
Summary:        Metapackage for python3-glances all extras
Requires:       python3-glances = %{version}-%{release}
Provides:       python3dist(glances[all]) = %{version}-%{release}

%description -n python3-glances+all
Metapackage for python3-glances all extras.

%package -n       python3-glances+browser
Summary:        Metapackage for python3-glances browser extras
Requires:       python3-glances = %{version}-%{release}
Provides:       python3dist(glances[browser]) = %{version}-%{release}

%description -n python3-glances+browser
Metapackage for python3-glances browser extras.

%package -n       python3-glances+cloud
Summary:        Metapackage for python3-glances cloud extras
Requires:       python3-glances = %{version}-%{release}
Provides:       python3dist(glances[cloud]) = %{version}-%{release}

%description -n python3-glances+cloud
Metapackage for python3-glances cloud extras.

%package -n       python3-glances+containers
Summary:        Metapackage for python3-glances containers extras
Requires:       python3-glances = %{version}-%{release}
Requires:       python3dist(docker) >= 6.1.1
Requires:       python3dist(pylxd) >= 2.3.1
Provides:       python3dist(glances[containers]) = %{version}-%{release}

%description -n python3-glances+containers
Metapackage for python3-glances containers extras.

%package -n       python3-glances+export
Summary:        Metapackage for python3-glances export extras
Requires:       python3-glances = %{version}-%{release}
Requires:       python3dist(influxdb) >= 1.0.0
Provides:       python3dist(glances[export]) = %{version}-%{release}

%description -n python3-glances+export
Metapackage for python3-glances export extras.

%package -n       python3-glances+gpu
Summary:        Metapackage for python3-glances gpu extras
Requires:       python3-glances = %{version}-%{release}
Provides:       python3dist(glances[gpu]) = %{version}-%{release}

%description -n python3-glances+gpu
Metapackage for python3-glances gpu extras.

%package -n       python3-glances+graph
Summary:        Metapackage for python3-glances graph extras
Requires:       python3-glances = %{version}-%{release}
Provides:       python3dist(glances[graph]) = %{version}-%{release}

%description -n python3-glances+graph
Metapackage for python3-glances graph extras.

%package -n       python3-glances+mcp
Summary:        Metapackage for python3-glances mcp extras
Requires:       python3-glances = %{version}-%{release}
Requires:       python3dist(mcp) >= 1.0.0
Requires:       python3dist(mcp) < 3
Provides:       python3dist(glances[mcp]) = %{version}-%{release}

%description -n python3-glances+mcp
Metapackage for python3-glances mcp extras.

%package -n       python3-glances+raid
Summary:        Metapackage for python3-glances raid extras
Requires:       python3-glances = %{version}-%{release}
Provides:       python3dist(glances[raid]) = %{version}-%{release}

%description -n python3-glances+raid
Metapackage for python3-glances raid extras.

%package -n       python3-glances+sensors
Summary:        Metapackage for python3-glances sensors extras
Requires:       python3-glances = %{version}-%{release}
Provides:       python3dist(glances[sensors]) = %{version}-%{release}

%description -n python3-glances+sensors
Metapackage for python3-glances sensors extras.

%package -n       python3-glances+smart
Summary:        Metapackage for python3-glances smart extras
Requires:       python3-glances = %{version}-%{release}
Provides:       python3dist(glances[smart]) = %{version}-%{release}

%description -n python3-glances+smart
Metapackage for python3-glances smart extras.

%package -n       python3-glances+snmp
Summary:        Metapackage for python3-glances snmp extras
Requires:       python3-glances = %{version}-%{release}
Requires:       python3dist(pysnmp-lextudio) < 6.2.0
Provides:       python3dist(glances[snmp]) = %{version}-%{release}

%description -n python3-glances+snmp
Metapackage for python3-glances snmp extras.

%package -n       python3-glances+sparklines
Summary:        Metapackage for python3-glances sparklines extras
Requires:       python3-glances = %{version}-%{release}
Provides:       python3dist(glances[sparklines]) = %{version}-%{release}

%description -n python3-glances+sparklines
Metapackage for python3-glances sparklines extras.

%package -n       python3-glances+web
Summary:        Metapackage for python3-glances web extras
Requires:       python3-glances = %{version}-%{release}
Requires:       python3dist(fastapi) >= 0.82.0
Requires:       python3dist(python-jose[cryptography]) >= 3.3.0
Provides:       python3dist(glances[web]) = %{version}-%{release}

%description -n python3-glances+web
Metapackage for python3-glances web extras.

%package -n       python3-glances+wifi
Summary:        Metapackage for python3-glances wifi extras
Requires:       python3-glances = %{version}-%{release}
Provides:       python3dist(glances[wifi]) = %{version}-%{release}

%description -n python3-glances+wifi
Metapackage for python3-glances wifi extras.

%description
%{desc}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

# disable PyPI update check + no need to have packaging dep
sed -i -e 's/check_update=true/check_update=false/' conf/glances.conf
sed -i '/packaging/d' requirements.txt

%build

%pyproject_wheel
%install
%pyproject_install
mkdir -p %{buildroot}%{_unitdir}
install -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -D -p -m 644 conf/glances.conf $RPM_BUILD_ROOT/etc/glances/glances.conf
%oreon_autofiles main

%check

%tox
%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files

%changelog

%autochangelog
