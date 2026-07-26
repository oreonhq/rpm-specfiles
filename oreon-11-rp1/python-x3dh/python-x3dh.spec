%global source0_hash 0a7b3b589fe747a20649d2b3112256cb76ce600ea5c715ea459c6c5b3b67cdcf

Name:           python-x3dh
Version:        1.3.0
Release:        1%{?dist}
Summary:        Python implementation of the X3DH key agreement protocol

License:        MIT
URL:            https://github.com/Syndace/%{name}
Source:         https://github.com/Syndace/%{name}/archive/v%{version}/python-x3dh-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# For tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)

# for docs
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-autodoc-typehints
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  texinfo

%global _description %{expand:
This python library offers an implementation of the Extended Triple
Diffie-Hellman key agreement protocol (X3DH).

X3DH establishes a shared secret key between two parties who mutually
authenticate each other based on public keys. X3DH provides forward
secrecy and cryptographic deniability.}

%description %_description

%package     -n python3-x3dh
Summary:        Python implementation of the X3DH key agreement protocol

%description -n python3-x3dh
This python library offers an implementation of the Extended Triple
Diffie-Hellman key agreement protocol (X3DH).

X3DH establishes a shared secret key between two parties who mutually
authenticate each other based on public keys. X3DH provides forward
secrecy and cryptographic deniability.

%package docs
Summary: Documentation for python-twomemo
BuildArch: noarch

%description docs %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

 
%generate_buildrequires
%pyproject_buildrequires -x docs

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
%pyproject_save_files -l x3dh
# Install docbook docs
install -pDm0644 docs/texinfo/x3dh.xml \
 %{buildroot}%{_datadir}/help/en/python-x3dh/x3dh.xml

%files -n python3-x3dh -f %{pyproject_files}

%files docs
%license LICENSE
%dir  %{_datadir}/help/en/
%lang(en) %{_datadir}/help/en/python-x3dh/

%changelog
%autochangelog
