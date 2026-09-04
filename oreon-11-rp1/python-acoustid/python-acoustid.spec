%global source0_hash bb0ecae40109c0aa80f709e33c66c83ec36b2fd84658f9fad056a34538f79e8a

%global oname   pyacoustid

Summary:        Python bindings for Chromaprint acoustic fingerprinting and the Acoustid API
Name:           python-acoustid
Version:        1.3.1
Release:        1%{?dist}
License:        MIT
URL:            http://pypi.python.org/pypi/pyacoustid
Source0:        https://files.pythonhosted.org/packages/source/p/%{oname}/%{oname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel

%description
Chromaprint and its associated Acoustid Web service make up a
high-quality, open-source acoustic fingerprinting system. This package
provides Python bindings for both the fingerprinting algorithm
library, which is written in C but portable, and the Web service,
which provides fingerprint look ups.

%package -n    python3-acoustid
Summary:       Python bindings for Chromaprint acoustic fingerprinting and the Acoustid API
Requires:      libchromaprint
Requires:      python3-audioread
%description -n python3-acoustid
Chromaprint and its associated Acoustid Web service make up a
high-quality, open-source acoustic fingerprinting system. This package
provides Python bindings for both the fingerprinting algorithm
library, which is written in C but portable, and the Web service,
which provides fingerprint look ups.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{oname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%{pyproject_wheel}

%install
%{pyproject_install}
%pyproject_save_files acoustid chromaprint

%check
%pyproject_check_import

%files -n python3-acoustid -f %{pyproject_files}
%doc README.rst aidmatch.py fpcalc.py

%changelog
%autochangelog
