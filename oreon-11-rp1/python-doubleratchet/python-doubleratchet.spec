%global source0_hash 1368d7bbd71f4b94999d72301be3637ff244105cb015cc090423afe0fdaad0d0

Name:           python-doubleratchet
Version:        1.3.0
Release:        1%{?dist}
Summary:        Python implementation of the Double Ratchet algorithm

License:        MIT
URL:            https://github.com/Syndace/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# For tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
# For documentation
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(sphinx-autodoc-typehints)
BuildRequires:  texinfo

%description
This python library offers an implementation of the Double Ratchet
algorithm.

A double ratchet allows message encryption providing perfect forward
secrecy. A double ratchet instance synchronizes with a second instance
using Diffie-Hellman calculations, that are provided by the DHRatchet
class.

%package     -n python3-doubleratchet
Summary:        Python implementation of the Double Ratchet algorithm

%description -n python3-doubleratchet
This python library offers an implementation of the Double Ratchet
algorithm.

A double ratchet allows message encryption providing perfect forward
secrecy. A double ratchet instance synchronizes with a second instance
using Diffie-Hellman calculations, that are provided by the DHRatchet
class.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1
# Do not measure coverage in tests
sed -i '/addopts = "--cov=doubleratchet --cov-report term-missing:skip-covered"/d' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
pushd docs
sphinx-build -b texinfo . texinfo
pushd texinfo
makeinfo --docbook doubleratchet.texi
popd
popd

%install
%pyproject_install
%pyproject_save_files doubleratchet
install -pDm0644 docs/texinfo/doubleratchet.xml \
  %{buildroot}%{_datadir}/help/en/python-doubleratchet/doubleratchet.xml

%check
%pyproject_check_import
%pytest tests 

%files -n python3-doubleratchet -f %{pyproject_files}
%license LICENSE
%doc README.md
%dir  %{_datadir}/help/en
%lang(en) %{_datadir}/help/en/python-doubleratchet

%changelog
%autochangelog
