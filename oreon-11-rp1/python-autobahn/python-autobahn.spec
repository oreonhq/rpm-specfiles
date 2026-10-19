%global source0_hash c6949a2c6eb95fb1c218837dbda0a59abbbebafb8b11098551c01a7061dfd245
Name:           python-autobahn
Version:        26.7.1
Release:        1%{?dist}
Summary:        WebSocket client _ server library, WAMP real-time framework
License:        MIT
URL:            https://autobahn.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/a/autobahn/autobahn-%{version}.tar.gz
Patch0:         remove-ubjson.patch
Patch1:         remove-unpackaged-sphinx-ext.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cffi) >= 2.0.0
BuildRequires:  python3dist(setuptools) >= 70.0.0
Requires:       python3-autobahn = %{version}-%{release}
# /oreon:deps
%package -n       python3-autobahn+twisted
Summary:        Metapackage for python3-autobahn twisted extras
Requires:       python3-autobahn = %{version}-%{release}
Requires:       python3dist(zope.interface) >= 5.2.0
Requires:       python3dist(twisted) >= 22.10.0
Requires:       python3dist(attrs) >= 20.3.0
Provides:       python3dist(autobahn[twisted]) = %{version}-%{release}

%description -n python3-autobahn+twisted
Metapackage for python3-autobahn twisted extras.

%package -n       python3-autobahn+accelerate
Summary:        Metapackage for python3-autobahn accelerate extras
Requires:       python3-autobahn = %{version}-%{release}
Provides:       python3dist(autobahn[accelerate]) = %{version}-%{release}

%description -n python3-autobahn+accelerate
Metapackage for python3-autobahn accelerate extras.

%package -n       python3-autobahn+compress
Summary:        Metapackage for python3-autobahn compress extras
Requires:       python3-autobahn = %{version}-%{release}
Requires:       python3dist(brotli) >= 1.0.0
Requires:       python3dist(brotlicffi) >= 1.0.0
Provides:       python3dist(autobahn[compress]) = %{version}-%{release}

%description -n python3-autobahn+compress
Metapackage for python3-autobahn compress extras.

%package -n       python3-autobahn+serialization
Summary:        Metapackage for python3-autobahn serialization extras
Requires:       python3-autobahn = %{version}-%{release}
Requires:       python3dist(bjdata) >= 0.6.0
Provides:       python3dist(autobahn[serialization]) = %{version}-%{release}

%description -n python3-autobahn+serialization
Metapackage for python3-autobahn serialization extras.

%package -n       python3-autobahn+encryption
Summary:        Metapackage for python3-autobahn encryption extras
Requires:       python3-autobahn = %{version}-%{release}
Requires:       python3dist(pyopenssl) >= 20.0.1
Requires:       python3dist(service-identity) >= 18.1.0
Requires:       python3dist(pynacl) >= 1.4.0
Requires:       python3dist(pytrie) >= 0.4.0
Requires:       python3dist(qrcode) >= 7.3.1
Requires:       python3dist(base58) >= 2.1.1
Requires:       python3dist(ecdsa) >= 0.19.1
Provides:       python3dist(autobahn[encryption]) = %{version}-%{release}

%description -n python3-autobahn+encryption
Metapackage for python3-autobahn encryption extras.

%package -n       python3-autobahn+scram
Summary:        Metapackage for python3-autobahn scram extras
Requires:       python3-autobahn = %{version}-%{release}
Requires:       python3dist(argon2-cffi) >= 20.1.0
Requires:       python3dist(passlib) >= 1.7.4
Provides:       python3dist(autobahn[scram]) = %{version}-%{release}

%description -n python3-autobahn+scram
Metapackage for python3-autobahn scram extras.

%package -n       python3-autobahn+nvx
Summary:        Metapackage for python3-autobahn nvx extras
Requires:       python3-autobahn = %{version}-%{release}
Provides:       python3dist(autobahn[nvx]) = %{version}-%{release}

%description -n python3-autobahn+nvx
Metapackage for python3-autobahn nvx extras.

%package -n       python3-autobahn+benchmark
Summary:        Metapackage for python3-autobahn benchmark extras
Requires:       python3-autobahn = %{version}-%{release}
Requires:       python3dist(vmprof) >= 0.4.15
Requires:       python3dist(vmprof-flamegraph) >= 0.0.1
Requires:       python3dist(jinja2) >= 3.0.0
Requires:       python3dist(humanize) >= 4.0.0
Provides:       python3dist(autobahn[benchmark]) = %{version}-%{release}

%description -n python3-autobahn+benchmark
Metapackage for python3-autobahn benchmark extras.

%package -n       python3-autobahn+build-tools
Summary:        Metapackage for python3-autobahn build-tools extras
Requires:       python3-autobahn = %{version}-%{release}
Requires:       python3dist(build) >= 1.0.0
Requires:       python3dist(wheel) >= 0.36.2
Requires:       python3dist(auditwheel) >= 5.0.0
Provides:       python3dist(autobahn[build-tools]) = %{version}-%{release}

%description -n python3-autobahn+build-tools
Metapackage for python3-autobahn build-tools extras.

%package -n       python3-autobahn+dev
Summary:        Metapackage for python3-autobahn dev extras
Requires:       python3-autobahn = %{version}-%{release}
Requires:       python3dist(auditwheel) >= 5.0.0
Requires:       python3dist(backports.tempfile) >= 1.0
Requires:       python3dist(build) >= 1.0.0
Requires:       python3dist(bumpversion) >= 0.5.3
Requires:       python3dist(codecov) >= 2.0.15
Requires:       python3dist(humanize) >= 4.0.0
Requires:       python3dist(pep8-naming) >= 0.3.3
Requires:       python3dist(pyflakes) >= 1.0.0
Requires:       python3dist(pylint) >= 1.9.2
Requires:       python3dist(pytest-asyncio) >= 0.14.0
Requires:       python3dist(pytest-runner) >= 2.11.1
Requires:       python3dist(pytest) >= 3.4.2
Requires:       python3dist(pyyaml) >= 4.2b4
Requires:       python3dist(qualname) >= 0.1.0
Requires:       python3dist(ruff) >= 0.12.1
Requires:       python3dist(setuptools) >= 70.0.0
Requires:       python3dist(twisted) >= 22.10.0
Requires:       python3dist(txaio) >= 25.12.2
Requires:       python3dist(watchdog) >= 0.8.3
Requires:       python3dist(wheel) >= 0.36.2
Requires:       python3dist(yapf) == 0.29.0
Requires:       python3dist(sphinx) >= 8.2.3
Requires:       python3dist(myst-parser) >= 2.0
Requires:       python3dist(furo) >= 2024.7.0
Requires:       python3dist(sphinx-autoapi) >= 2.1.0
Requires:       python3dist(sphinx-copybutton) >= 0.5
Requires:       python3dist(sphinx-design) >= 0.5
Requires:       python3dist(sphinxcontrib-images) >= 0.9
Requires:       python3dist(sphinxcontrib-spelling) >= 8.0
Requires:       python3dist(pyenchant) >= 3.2
Requires:       python3dist(scour) >= 0.38
Requires:       python3dist(sphinxext-opengraph) >= 0.9
Requires:       python3dist(linkify-it-py) >= 2.0.0
Requires:       python3dist(twine) >= 3.3.0
Provides:       python3dist(autobahn[dev]) = %{version}-%{release}

%description -n python3-autobahn+dev
Metapackage for python3-autobahn dev extras.

%package -n       python3-autobahn+docs
Summary:        Metapackage for python3-autobahn docs extras
Requires:       python3-autobahn = %{version}-%{release}
Requires:       python3dist(sphinx) >= 8.2.3
Requires:       python3dist(myst-parser) >= 2.0
Requires:       python3dist(furo) >= 2024.7.0
Requires:       python3dist(sphinx-autoapi) >= 2.1.0
Requires:       python3dist(sphinx-copybutton) >= 0.5
Requires:       python3dist(sphinx-design) >= 0.5
Requires:       python3dist(sphinxcontrib-images) >= 0.9
Requires:       python3dist(sphinxcontrib-spelling) >= 8.0
Requires:       python3dist(pyenchant) >= 3.2
Requires:       python3dist(scour) >= 0.38
Requires:       python3dist(sphinxext-opengraph) >= 0.9
Requires:       python3dist(linkify-it-py) >= 2.0.0
Provides:       python3dist(autobahn[docs]) = %{version}-%{release}

%description -n python3-autobahn+docs
Metapackage for python3-autobahn docs extras.

%package -n       python3-autobahn+all
Summary:        Metapackage for python3-autobahn all extras
Requires:       python3-autobahn = %{version}-%{release}
Provides:       python3dist(autobahn[all]) = %{version}-%{release}

%description -n python3-autobahn+all
Metapackage for python3-autobahn all extras.

%package -n       python3-autobahn+asyncio
Summary:        Metapackage for python3-autobahn asyncio extras
Requires:       python3-autobahn = %{version}-%{release}
Provides:       python3dist(autobahn[asyncio]) = %{version}-%{release}

%description -n python3-autobahn+asyncio
Metapackage for python3-autobahn asyncio extras.

%description

%package -n     python3-autobahn
Summary:        WebSocket client _ server library, WAMP real-time framework
# oreon:reqs
Requires:       python3dist(cbor2) < 6
Requires:       python3dist(cbor2) >= 5.2.0
Requires:       python3dist(cffi) >= 2.0.0
Requires:       python3dist(cryptography) >= 3.4.6
Requires:       python3dist(hyperlink) >= 21.0.0
Requires:       python3dist(importlib-resources) >= 5.0.0
Requires:       python3dist(msgpack) >= 1.0.2
Requires:       python3dist(txaio) >= 25.12.2
Requires:       python3dist(u-msgpack-python) >= 2.1
Requires:       python3dist(ujson) >= 4.0.2
# /oreon:reqs
%description -n python3-autobahn

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir autobahn-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-autobahn usr/lib/python3*/site-packages/autobahn* usr/lib64/python3*/site-packages/autobahn* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/autobahn* usr/lib64/python3*/site-packages/autobahn* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-autobahn -f %{oreon_filedir}/python3-autobahn.list

%changelog

%autochangelog
