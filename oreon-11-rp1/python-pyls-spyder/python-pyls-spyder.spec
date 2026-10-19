%global source0_hash 45a321c83f64267d82907492c55199fccabda45bc872dd23bf1efd08edac1b0b
Name:           python-pyls-spyder
Version:        0.4.0
Release:        1%{?dist}
Summary:        Spyder extensions for the python-language-server (pyls)
License:        MIT
URL:            https://github.com/spyder-ide/pyls-spyder
Source0:        https://files.pythonhosted.org/packages/source/p/pyls-spyder/pyls-spyder-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyls-spyder = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyls-spyder
Summary:        Spyder extensions for the python-language-server (pyls)
%description -n python3-pyls-spyder

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pyls-spyder-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyls-spyder usr/lib/python3*/site-packages/pyls_spyder* usr/lib64/python3*/site-packages/pyls_spyder* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyls_spyder* usr/lib64/python3*/site-packages/pyls_spyder* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-pyls-spyder -f %{oreon_filedir}/python3-pyls-spyder.list

%changelog

%autochangelog
