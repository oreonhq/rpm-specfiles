%global source0_hash f94dee171643798b4d7b2b1d649a35c187dcb52e2fb3e3242083a0fd3d171daf

# set upstream name variable
%global srcname slixmpp

Name:           python-slixmpp
Version:        1.12.0
Release:        2%{?dist}
Summary:        Slixmpp is an XMPP library for Python 3.5+

License:        MIT
URL:            https://codeberg.org/poezio/%{srcname}
Source0:        https://codeberg.org/poezio/%{srcname}/archive/slix-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  python3-devel
# Optional dependencies
BuildRequires:  python3-aiohttp
BuildRequires:  python3-cryptography
BuildRequires:  python3-defusedxml
BuildRequires:  python3-emoji
# for docs
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-autodoc-typehints
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  texinfo
# for tests
BuildRequires:  python3-pytest
# Rust jid
BuildRequires:  cargo-rpm-macros

%description
Slixmpp is an MIT licensed XMPP library for Python 3.5+. It is a fork
of SleekXMPP. Goals is to only rewrite the core of the library (the low
level socket handling, the timers, the events dispatching) in order to
remove all threads.

%package -n python3-%{srcname}
Summary:        Slixmpp is an XMPP library for Python 3.5+

%description -n python3-%{srcname}
Slixmpp is an MIT licensed XMPP library for Python 3.5+. It is a fork
of SleekXMPP. Goals is to only rewrite the core of the library (the low
level socket handling, the timers, the events dispatching) in order to
remove all threads.

%package -n python-%{srcname}-doc
Summary:        Documentation for Slixmpp
BuildArch:      noarch
Requires:       python3-%{srcname} = %{version}-%{release}

%description -n python-%{srcname}-doc
Slixmpp is an MIT licensed XMPP library for Python 3.4+. It is a fork
of SleekXMPP. Goals is to only rewrite the core of the library (the low
level socket handling, the timers, the events dispatching) in order to
remove all threads.

This package contains documentation in docbook format.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}
%cargo_prep
sed -i '18d' slixmpp/plugins/xep_0055/search.py
sed -i '17d' slixmpp/plugins/xep_0055/search.py

%generate_buildrequires
%cargo_generate_buildrequires -a -t
%pyproject_buildrequires

%build
%pyproject_wheel
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

# Build sphinx documentation
pushd docs/
sphinx-build -b texinfo . texinfo
pushd texinfo
makeinfo --docbook slixmpp.texi
popd # texinfo
popd # docs

%install
%pyproject_install
%pyproject_save_files -l slixmpp

# Install docbook docs
install -pDm0644 docs/texinfo/slixmpp.xml \
 %{buildroot}%{_datadir}/help/en/python-slixmpp/slixmpp.xml

%check
%pyproject_check_import -t
%python3 run_tests.py

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%license LICENSE.dependencies
%doc CONTRIBUTING.rst README.rst

%files -n python-%{srcname}-doc
%doc examples/
%dir  %{_datadir}/help/en/
%lang(en) %{_datadir}/help/en/python-slixmpp/

%changelog
%autochangelog
