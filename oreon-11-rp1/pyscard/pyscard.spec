%global source0_hash 6b84eea9f2fd19a0a54e213b3d76870b21a7792f823755a824f49de822c964c7
Name:           pyscard
Version:        2.3.1
Release:        1%{?dist}
Summary:        A framework for building smart card aware applications in Python
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/LudovicRousseau/pyscard
Source0:        https://github.com/LudovicRousseau/pyscard/archive/%{version}/%{name}-%{version}.tar.gz
Patch:          https://github.com/LudovicRousseau/pyscard/commit/54ef7f2ca636b83657506030e6bfbdc335f65bb5.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyscard = %{version}-%{release}
# /oreon:deps
%description
The pyscard smartcard library is a framework for building smart card aware
applications in Python. The smartcard module is built on top of the PCSC API
Python wrapper module.

%package -n python%{python3_pkgversion}-%{name}
Summary:        A framework for building smart card aware applications in Python
BuildRequires:  python%{python3_pkgversion}-devel
Requires:       pcsc-lite
%description -n python%{python3_pkgversion}-%{name}
The pyscard smartcard library is a framework for building smart card aware
applications in Python. The smartcard module is built on top of the PCSC API
Python wrapper module.

This is the python3 package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i 's/,"swig"//' pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
ls -l %{buildroot}%{python3_sitearch}/smartcard/scard/*.so
chmod 755 %{buildroot}%{python3_sitearch}/smartcard/scard/*.so
%oreon_autofiles main usr/lib/python3*/site-packages/pyscard* usr/lib64/python3*/site-packages/pyscard* usr/bin/*

%files
%files -n python3-pyscard -f %{oreon_filedir}/python3-pyscard.list

%changelog

%autochangelog
