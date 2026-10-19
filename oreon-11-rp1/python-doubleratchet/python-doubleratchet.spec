%global source0_hash 1368d7bbd71f4b94999d72301be3637ff244105cb015cc090423afe0fdaad0d0
Name:           python-doubleratchet
Version:        1.3.0
Release:        1%{?dist}
Summary:        Python implementation of the Double Ratchet algorithm
License:        MIT
URL:            https://github.com/Syndace/%{name}
Source0:        https://github.com/Syndace/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-doubleratchet = %{version}-%{release}
# /oreon:deps
%package -n       python3-doubleratchet+docs
Summary:        Metapackage for python3-doubleratchet docs extras
Requires:       python3-doubleratchet = %{version}-%{release}
Provides:       python3dist(doubleratchet[docs]) = %{version}-%{release}

%description -n python3-doubleratchet+docs
Metapackage for python3-doubleratchet docs extras.

%package -n       python3-doubleratchet+test
Summary:        Metapackage for python3-doubleratchet test extras
Requires:       python3-doubleratchet = %{version}-%{release}
Provides:       python3dist(doubleratchet[test]) = %{version}-%{release}

%description -n python3-doubleratchet+test
Metapackage for python3-doubleratchet test extras.

%package -n       python3-doubleratchet+lint
Summary:        Metapackage for python3-doubleratchet lint extras
Requires:       python3-doubleratchet = %{version}-%{release}
Provides:       python3dist(doubleratchet[lint]) = %{version}-%{release}

%description -n python3-doubleratchet+lint
Metapackage for python3-doubleratchet lint extras.

%package -n       python3-doubleratchet+dev
Summary:        Metapackage for python3-doubleratchet dev extras
Requires:       python3-doubleratchet = %{version}-%{release}
Provides:       python3dist(doubleratchet[dev]) = %{version}-%{release}

%description -n python3-doubleratchet+dev
Metapackage for python3-doubleratchet dev extras.

%description
This python library offers an implementation of the Double Ratchet
algorithm.

A double ratchet allows message encryption providing perfect forward
secrecy. A double ratchet instance synchronizes with a second instance
using Diffie-Hellman calculations, that are provided by the DHRatchet
class.

%package     -n python3-doubleratchet
Summary:        Python implementation of the Double Ratchet algorithm
# oreon:reqs
Requires:       python3dist(cryptography) >= 3.3.2
Requires:       python3dist(pydantic) >= 1.7.4
Requires:       python3dist(typing-extensions) >= 4.3.0
# /oreon:reqs
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
install -pDm0644 docs/texinfo/doubleratchet.xml \
  %{buildroot}%{_datadir}/help/en/python-doubleratchet/doubleratchet.xml
%oreon_autofiles python3-doubleratchet usr/lib/python3*/site-packages/doubleratchet* usr/lib64/python3*/site-packages/doubleratchet* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/doubleratchet* usr/lib64/python3*/site-packages/doubleratchet* usr/bin/*

%check

%pyproject_check_import
%pytest tests 
%files
%files -n python3-doubleratchet -f %{oreon_filedir}/python3-doubleratchet.list

%changelog

%autochangelog
