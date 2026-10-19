%global source0_hash 6d218cb3d836b38574bab632a543e0bd8cc0355fa0dee66ed90b016e255ce22f
Name:           opensuse-distro-aliases
Version:        0.2.4
Release:        1%{?dist}
Summary:        Aliases for active openSUSE releases
License:        MIT
URL:            https://github.com/rpm-software-management/opensuse-distro-aliases
Source0:        https://files.pythonhosted.org/packages/source/o/opensuse_distro_aliases/opensuse_distro_aliases-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-opensuse-distro-aliases = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-opensuse-distro-aliases
Summary:        Aliases for active openSUSE releases
%description -n python3-opensuse-distro-aliases

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir opensuse_distro_aliases-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-opensuse-distro-aliases usr/lib/python3*/site-packages/opensuse_distro_aliases* usr/lib64/python3*/site-packages/opensuse_distro_aliases* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/opensuse_distro_aliases* usr/lib64/python3*/site-packages/opensuse_distro_aliases* usr/bin/*

%check

%pyproject_check_import -t
%files
%files -n python3-opensuse-distro-aliases -f %{oreon_filedir}/python3-opensuse-distro-aliases.list

%changelog

%autochangelog
