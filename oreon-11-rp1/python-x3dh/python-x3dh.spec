%global source0_hash 0a7b3b589fe747a20649d2b3112256cb76ce600ea5c715ea459c6c5b3b67cdcf
Name:           python-x3dh
Version:        1.3.0
Release:        1%{?dist}
Summary:        Python implementation of the X3DH key agreement protocol
License:        MIT
URL:            https://github.com/Syndace/%{name}
Source0:        https://github.com/Syndace/%{name}/archive/v%{version}/python-x3dh-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-x3dh = %{version}-%{release}
# /oreon:deps
%package -n       python3-x3dh+docs
Summary:        Metapackage for python3-x3dh docs extras
Requires:       python3-x3dh = %{version}-%{release}
Provides:       python3dist(x3dh[docs]) = %{version}-%{release}

%description -n python3-x3dh+docs
Metapackage for python3-x3dh docs extras.

%package -n       python3-x3dh+test
Summary:        Metapackage for python3-x3dh test extras
Requires:       python3-x3dh = %{version}-%{release}
Provides:       python3dist(x3dh[test]) = %{version}-%{release}

%description -n python3-x3dh+test
Metapackage for python3-x3dh test extras.

%package -n       python3-x3dh+lint
Summary:        Metapackage for python3-x3dh lint extras
Requires:       python3-x3dh = %{version}-%{release}
Provides:       python3dist(x3dh[lint]) = %{version}-%{release}

%description -n python3-x3dh+lint
Metapackage for python3-x3dh lint extras.

%package -n       python3-x3dh+dev
Summary:        Metapackage for python3-x3dh dev extras
Requires:       python3-x3dh = %{version}-%{release}
Provides:       python3dist(x3dh[dev]) = %{version}-%{release}

%description -n python3-x3dh+dev
Metapackage for python3-x3dh dev extras.

%description

%package     -n python3-x3dh
Summary:        Python implementation of the X3DH key agreement protocol
# oreon:reqs
Requires:       python3dist(cryptography) >= 3.3.2
Requires:       python3dist(pydantic) >= 1.7.4
Requires:       python3dist(typing-extensions) >= 4.3.0
Requires:       python3dist(xeddsa) < 2
Requires:       python3dist(xeddsa) >= 1.0.0
# /oreon:reqs
%description -n python3-x3dh
This python library offers an implementation of the Extended Triple
Diffie-Hellman key agreement protocol (X3DH).

X3DH establishes a shared secret key between two parties who mutually
authenticate each other based on public keys. X3DH provides forward
secrecy and cryptographic deniability.

%package docs
Summary: Documentation for python-twomemo
BuildArch: noarch
%description docs

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%pyproject_wheel
pushd docs
sphinx-build -b texinfo . texinfo
pushd texinfo
makeinfo --docbook x3dh.texi
popd # texinfo
popd # docs
%install
%pyproject_install
install -pDm0644 docs/texinfo/x3dh.xml \
 %{buildroot}%{_datadir}/help/en/python-x3dh/x3dh.xml
%oreon_autofiles python3-x3dh usr/lib/python3*/site-packages/x3dh* usr/lib64/python3*/site-packages/x3dh* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/x3dh* usr/lib64/python3*/site-packages/x3dh* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files
%files -n python3-x3dh -f %{oreon_filedir}/python3-x3dh.list
%files -n python-x3dh-docs -f %{oreon_filedir}/python-x3dh-docs.list

%changelog

%autochangelog
