%global source0_hash becb3013fce7a27bdb84d7109fc652e13dc0a6e9325a6ab7b80014248b777c4c
Summary:        Python tool for decrypting MS Office files with passwords or other keys
Name:           msoffcrypto-tool
Version:        6.0.0
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/nolze/msoffcrypto-tool
VCS:            https://github.com/nolze/msoffcrypto-tool
Source0:        https://github.com/nolze/msoffcrypto-tool/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
%global         common_description %{expand:
The msoffcrypto-tool (formerly ms-offcrypto-tool) is a Python tool and
library for decrypting encrypted Microsoft Office files with password,
intermediate key, or private key which generated its escrow key.
}
%global modulename msoffcrypto
Requires:       python%{python3_pkgversion}-%{modulename}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-msoffcrypto-tool = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python%{python3_pkgversion}-%{modulename}
Summary:        Python library for decrypting MS Office files with passwords or other keys
Requires:       python%{python3_pkgversion}-cryptography >= 2.3
Requires:       python%{python3_pkgversion}-olefile >= 0.45
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modulename}}
%description -n python%{python3_pkgversion}-%{modulename} %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
rm -f %{buildroot}%{python3_sitelib}/NOTICE.txt
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest -sv
%files
%files -n python3-msoffcrypto -f %{oreon_filedir}/python3-msoffcrypto.list

%changelog

%autochangelog
