%global source0_hash 0dcedded6da049f2d1c0f6e643c8149557165fe4dd16b4952b44557e5eae8bd1
%if 0%{?el9}
%bcond_with tests
%else
%bcond_without tests
%endif
Name:           packit
Version:        1.16.3
Release:        1%{?dist}
Summary:        A tool for integrating upstream projects with Fedora operating system
License:        MIT
URL:            https://github.com/packit/packit
Source0:        https://files.pythonhosted.org/packages/source/p/packitos/packitos-%{version}.tar.gz
BuildArch:      noarch
Requires:       python3-packit = %{version}-%{release}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-packit = %{version}-%{release}
# /oreon:deps
%package -n       python3-packit+testing
Summary:        Metapackage for python3-packit testing extras
Requires:       python3-packit = %{version}-%{release}
Provides:       python3dist(packit[testing]) = %{version}-%{release}

%description -n python3-packit+testing
Metapackage for python3-packit testing extras.

%package -n       python3-packit+schema
Summary:        Metapackage for python3-packit schema extras
Requires:       python3-packit = %{version}-%{release}
Provides:       python3dist(packit[schema]) = %{version}-%{release}

%description -n python3-packit+schema
Metapackage for python3-packit schema extras.

%package -n       python3-packit+dev
Summary:        Metapackage for python3-packit dev extras
Requires:       python3-packit = %{version}-%{release}
Provides:       python3dist(packit[dev]) = %{version}-%{release}

%description -n python3-packit+dev
Metapackage for python3-packit dev extras.

%description
This project provides tooling and automation to integrate upstream open source
projects into Fedora operating system.

%package -n     python3-packit
Summary:        A tool for integrating upstream projects with Fedora operating system
Requires:       fedpkg
Requires:       git-core
Requires:       krb5-workstation
Requires:       rpm-build
Requires:       rpmdevtools
Requires:       rsync
Recommends:       osh-cli
# oreon:reqs
Requires:       python3dist(bodhi-client) >= 7.0.0
Requires:       python3dist(marshmallow) >= 3.18.0
Requires:       python3dist(osc) >= 1.6.2
# /oreon:reqs
%description -n python3-packit
Python library for Packit,
check out packit package for the executable.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir packitos-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
PYTHONPATH="%{buildroot}%{python3_sitelib}" click-man packit --target %{buildroot}%{_mandir}/man1
install -d -m 755 %{buildroot}%{bash_completions_dir}
cp files/bash-completion/packit %{buildroot}%{bash_completions_dir}/packit
%oreon_autofiles python3-packit usr/lib/python3*/site-packages/packit* usr/lib64/python3*/site-packages/packit* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/packit* usr/lib64/python3*/site-packages/packit* usr/bin/*

%files
%files -n python3-packit -f %{oreon_filedir}/python3-packit.list

%changelog

%autochangelog
