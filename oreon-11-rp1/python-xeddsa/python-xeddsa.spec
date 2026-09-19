%global source0_hash 1880e0432953cb5580cd32fcde8be221f61c6d5d5d821992cb69f82a4cb509fd

Name:           python-xeddsa
Version:        1.2.0
Release:        1%{?dist}
Summary:        Python implementation of the XEdDSA signature scheme

License:        MIT
URL:            https://github.com/Syndace/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  libxeddsa-devel
BuildRequires:  libsodium-devel
# docs
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(sphinx-autodoc-typehints)
BuildRequires:  texinfo

%description
This python library offers an open implementation of the XEdDSA
signature scheme.

It allows to create and verify EdDSA-compatible signatures using
public key and private key formats initially defined for the X25519
and X448 elliptic curve Diffie-Hellman functions.

%package     -n python3-xeddsa
Summary:        Python implementation of the XEdDSA signature scheme

%description -n python3-xeddsa
This python library offers an open implementation of the XEdDSA
signature scheme.

It allows to create and verify EdDSA-compatible signatures using
public key and private key formats initially defined for the X25519
and X448 elliptic curve Diffie-Hellman functions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

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
%pyproject_save_files -l xeddsa

# Install docbook docs
install -pDm0644 docs/texinfo/xeddsa.xml \
 %{buildroot}%{_datadir}/help/en/python-xeddsa/xeddsa.xml

%files -n python3-xeddsa  -f %{pyproject_files}
%doc README.md
%{python3_sitearch}/_libxeddsa.abi3.so
%dir  %{_datadir}/help/en/
%lang(en) %{_datadir}/help/en/python-xeddsa/

%changelog
%autochangelog
