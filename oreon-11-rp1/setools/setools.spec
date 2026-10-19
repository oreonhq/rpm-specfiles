%global source0_hash 13a39cdccae7fc8454c41e5bf619514d84d7113ffcdcd0cf6ea7ef867a74937e
%global sepol_ver 3.9
%global selinux_ver 3.9
Name:           setools
Version:        4.7.1
Release:        1%{?dist}
Summary:        Policy analysis tools for SELinux
License:        GPL-2.0-only AND LGPL-2.1-only
URL:            https://github.com/SELinuxProject/setools/wiki
Source0:        https://github.com/SELinuxProject/setools/archive/refs/tags/%{version}.tar.gz#/setools-%{version}.tar.gz
Source1:        setools.pam
Source2:        apol.desktop
Obsoletes:      setools < 4.0.0, setools-devel < 4.0.0
Requires:       %{name}-console = %{version}-%{release}
Requires:       %{name}-console-analyses = %{version}-%{release}
Requires:       %{name}-gui = %{version}-%{release}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 0.29.14
Requires:       python3-setools = %{version}-%{release}
# /oreon:deps
%package -n       python3-setools+analysis
Summary:        Metapackage for python3-setools analysis extras
Requires:       python3-setools = %{version}-%{release}
Requires:       python3dist(networkx) >= 2.6
Provides:       python3dist(setools[analysis]) = %{version}-%{release}

%description -n python3-setools+analysis
Metapackage for python3-setools analysis extras.

%package -n       python3-setools+gui
Summary:        Metapackage for python3-setools gui extras
Requires:       python3-setools = %{version}-%{release}
Provides:       python3dist(setools[gui]) = %{version}-%{release}

%description -n python3-setools+gui
Metapackage for python3-setools gui extras.

%package -n       python3-setools+mcp
Summary:        Metapackage for python3-setools mcp extras
Requires:       python3-setools = %{version}-%{release}
Requires:       python3dist(fastmcp) >= 2.0
Provides:       python3dist(setools[mcp]) = %{version}-%{release}

%description -n python3-setools+mcp
Metapackage for python3-setools mcp extras.

%package -n       python3-setools+test
Summary:        Metapackage for python3-setools test extras
Requires:       python3-setools = %{version}-%{release}
Provides:       python3dist(setools[test]) = %{version}-%{release}

%description -n python3-setools+test
Metapackage for python3-setools test extras.

%description
SETools is a collection of graphical tools, command-line tools, and
Python modules designed to facilitate SELinux policy analysis.

%package     console
Summary:     Policy analysis command-line tools for SELinux
License:     GPL-2.0-only
Requires:    python3-setools = %{version}-%{release}
Requires:    libselinux >= %{selinux_ver}
%description console
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes the following console tools:

  sediff       Compare two policies to find differences.
  seinfo       List policy components.
  sesearch     Search rules (allow, type_transition, etc.)

%package     console-analyses
Summary:     Policy analysis command-line tools for SELinux
License:     GPL-2.0-only
Requires:    python3-setools = %{version}-%{release}
Requires:    libselinux >= %{selinux_ver}
Requires:    python3-networkx
%description console-analyses
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes the following console tools:

  sedta        Perform domain transition analyses.
  seinfoflow   Perform information flow analyses.

%package     -n python3-setools
Summary:     Policy analysis tools for SELinux
License:     LGPL-2.1-only
Obsoletes:   setools-libs < 4.0.0
%description -n python3-setools
SETools is a collection of graphical tools, command-line tools, and
Python 3 modules designed to facilitate SELinux policy analysis.

%package     gui
Summary:     Policy analysis graphical tools for SELinux
License:     GPL-2.0-only
Requires:    python3-setools = %{version}-%{release}
Requires:    python3-pyqt6 python3-pyqt6-sip
Requires:    python3-networkx
%description gui
SETools is a collection of graphical tools, command-line tools, and
Python modules designed to facilitate SELinux policy analysis.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir setools-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-setools usr/lib/python3*/site-packages/setools* usr/lib64/python3*/site-packages/setools* usr/bin/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/lib/python3*/site-packages/setools* usr/lib64/python3*/site-packages/setools* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{?_with_check:1}%{!?_with_check:0}
%pytest
%endif
%files
%files -n setools-console -f %{oreon_filedir}/setools-console.list
%files -n setools-console-analyses -f %{oreon_filedir}/setools-console-analyses.list
%files -n python3-setools -f %{oreon_filedir}/python3-setools.list
%files -n setools-gui -f %{oreon_filedir}/setools-gui.list

%changelog

%autochangelog
