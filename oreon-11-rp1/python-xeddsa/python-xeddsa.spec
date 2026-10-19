%global source0_hash 1880e0432953cb5580cd32fcde8be221f61c6d5d5d821992cb69f82a4cb509fd
Name:           python-xeddsa
Version:        1.2.0
Release:        1%{?dist}
Summary:        Python implementation of the XEdDSA signature scheme
License:        MIT
URL:            https://github.com/Syndace/%{name}
Source0:        https://github.com/Syndace/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cffi) >= 1.14.5
Requires:       python3-xeddsa = %{version}-%{release}
# /oreon:deps
%package -n       python3-xeddsa+docs
Summary:        Metapackage for python3-xeddsa docs extras
Requires:       python3-xeddsa = %{version}-%{release}
Provides:       python3dist(xeddsa[docs]) = %{version}-%{release}

%description -n python3-xeddsa+docs
Metapackage for python3-xeddsa docs extras.

%package -n       python3-xeddsa+test
Summary:        Metapackage for python3-xeddsa test extras
Requires:       python3-xeddsa = %{version}-%{release}
Provides:       python3dist(xeddsa[test]) = %{version}-%{release}

%description -n python3-xeddsa+test
Metapackage for python3-xeddsa test extras.

%package -n       python3-xeddsa+lint
Summary:        Metapackage for python3-xeddsa lint extras
Requires:       python3-xeddsa = %{version}-%{release}
Provides:       python3dist(xeddsa[lint]) = %{version}-%{release}

%description -n python3-xeddsa+lint
Metapackage for python3-xeddsa lint extras.

%package -n       python3-xeddsa+dev
Summary:        Metapackage for python3-xeddsa dev extras
Requires:       python3-xeddsa = %{version}-%{release}
Provides:       python3dist(xeddsa[dev]) = %{version}-%{release}

%description -n python3-xeddsa+dev
Metapackage for python3-xeddsa dev extras.

%description
This python library offers an open implementation of the XEdDSA
signature scheme.

It allows to create and verify EdDSA-compatible signatures using
public key and private key formats initially defined for the X25519
and X448 elliptic curve Diffie-Hellman functions.

%package     -n python3-xeddsa
Summary:        Python implementation of the XEdDSA signature scheme
# oreon:reqs
Requires:       python3dist(cffi) >= 1.14.5
# /oreon:reqs
%description -n python3-xeddsa
This python library offers an open implementation of the XEdDSA
signature scheme.

It allows to create and verify EdDSA-compatible signatures using
public key and private key formats initially defined for the X25519
and X448 elliptic curve Diffie-Hellman functions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%pyproject_wheel
pushd docs/
sphinx-build -b texinfo . texinfo
pushd texinfo
makeinfo --docbook xeddsa.texi
popd # texinfo
popd # docs
%install
%pyproject_install
install -pDm0644 docs/texinfo/xeddsa.xml \
 %{buildroot}%{_datadir}/help/en/python-xeddsa/xeddsa.xml
%oreon_autofiles python3-xeddsa usr/lib/python3*/site-packages/xeddsa* usr/lib64/python3*/site-packages/xeddsa* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/xeddsa* usr/lib64/python3*/site-packages/xeddsa* usr/bin/*

%files
%files -n python3-xeddsa -f %{oreon_filedir}/python3-xeddsa.list

%changelog

%autochangelog
