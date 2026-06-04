%global source0_hash d143da7c0f155a67590983c7ff7f7c181c0ebaf350b37a28b34198c6b4b9a5d2

%global sepol_ver 3.9
%global selinux_ver 3.9

Name:           setools
Version:        4.6.0
Release:        5%{?dist}
Summary:        Policy analysis tools for SELinux

License:        GPL-2.0-only AND LGPL-2.1-only
URL:            https://github.com/SELinuxProject/setools/wiki
Source0:        https://github.com/SELinuxProject/setools/archive/refs/tags/%{version}.tar.gz

Source1:        setools.pam
Source2:        apol.desktop

# Remove redundant runtime requirement on setuptools
Patch:          https://github.com/SELinuxProject/setools/pull/156.patch
# Fix seinfo argument parsing when policy path follows query
Patch:          https://github.com/SELinuxProject/setools/pull/157.patch

Obsoletes:      setools < 4.0.0, setools-devel < 4.0.0
BuildRequires:  flex,  bison
BuildRequires:  glibc-devel, gcc, git-core
BuildRequires:  libsepol-devel >= %{sepol_ver}, libsepol-static >= %{sepol_ver}
BuildRequires:  swig
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  libselinux-devel

Requires:       %{name}-console = %{version}-%{release}
Requires:       %{name}-console-analyses = %{version}-%{release}
Requires:       %{name}-gui = %{version}-%{release}

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
%autosetup -p 1 -S git -n setools-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%check
%if %{?_with_check:1}%{!?_with_check:0}
# dnf install python3-pytest python3-pytest-qt
%pytest
%endif


%files

%files console
%license COPYING.GPL
%{_bindir}/sechecker
%{_bindir}/sediff
%{_bindir}/seinfo
%{_bindir}/sesearch
%{_mandir}/man1/sechecker*
%{_mandir}/man1/sediff*
%{_mandir}/man1/seinfo*
%{_mandir}/man1/sesearch*
%{_mandir}/ru/man1/sediff*
%{_mandir}/ru/man1/seinfo*
%{_mandir}/ru/man1/sesearch*

%files console-analyses
%license COPYING.GPL
%{_bindir}/sedta
%{_bindir}/seinfoflow
%{_mandir}/man1/sedta*
%{_mandir}/man1/seinfoflow*
%{_mandir}/ru/man1/sedta*
%{_mandir}/ru/man1/seinfoflow*

%files -n python3-setools
%license COPYING COPYING.LGPL
%{python3_sitearch}/setools
%{python3_sitearch}/setools-*

%files gui
%license COPYING.GPL
%{_bindir}/apol
%{python3_sitearch}/setoolsgui
%{_mandir}/man1/apol*
%{_mandir}/ru/man1/apol*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.6.0-5
- Prepare for Oreon 11 (RP1)
