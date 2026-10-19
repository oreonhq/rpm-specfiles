%global source0_hash a43388f9067678fef6e13bdff325b6cfa6961a590498bb37f7ff31589c83bc75
Name:           python-hypothesis
Version:        6.168.3
Release:        1%{?dist}
Summary:        The property-based testing library for Python
License:        MPL-2.0
URL:            https://hypothesis.works
Source0:        https://files.pythonhosted.org/packages/source/h/hypothesis/hypothesis-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(maturin) < 2.0
BuildRequires:  python3dist(maturin) >= 1.9.4
Requires:       python3-hypothesis = %{version}-%{release}
# /oreon:deps
%package -n       python3-hypothesis+cli
Summary:        Metapackage for python3-hypothesis cli extras
Requires:       python3-hypothesis = %{version}-%{release}
Requires:       python3dist(click) >= 7.0
Requires:       python3dist(black) >= 20.8b0
Requires:       python3dist(rich) >= 9.0.0
Provides:       python3dist(hypothesis[cli]) = %{version}-%{release}

%description -n python3-hypothesis+cli
Metapackage for python3-hypothesis cli extras.

%package -n       python3-hypothesis+codemods
Summary:        Metapackage for python3-hypothesis codemods extras
Requires:       python3-hypothesis = %{version}-%{release}
Requires:       python3dist(libcst) >= 0.3.16
Provides:       python3dist(hypothesis[codemods]) = %{version}-%{release}

%description -n python3-hypothesis+codemods
Metapackage for python3-hypothesis codemods extras.

%package -n       python3-hypothesis+ghostwriter
Summary:        Metapackage for python3-hypothesis ghostwriter extras
Requires:       python3-hypothesis = %{version}-%{release}
Requires:       python3dist(black) >= 20.8b0
Provides:       python3dist(hypothesis[ghostwriter]) = %{version}-%{release}

%description -n python3-hypothesis+ghostwriter
Metapackage for python3-hypothesis ghostwriter extras.

%package -n       python3-hypothesis+pytz
Summary:        Metapackage for python3-hypothesis pytz extras
Requires:       python3-hypothesis = %{version}-%{release}
Requires:       python3dist(pytz) >= 2014.1
Provides:       python3dist(hypothesis[pytz]) = %{version}-%{release}

%description -n python3-hypothesis+pytz
Metapackage for python3-hypothesis pytz extras.

%package -n       python3-hypothesis+dateutil
Summary:        Metapackage for python3-hypothesis dateutil extras
Requires:       python3-hypothesis = %{version}-%{release}
Requires:       python3dist(python-dateutil) >= 1.4
Provides:       python3dist(hypothesis[dateutil]) = %{version}-%{release}

%description -n python3-hypothesis+dateutil
Metapackage for python3-hypothesis dateutil extras.

%package -n       python3-hypothesis+lark
Summary:        Metapackage for python3-hypothesis lark extras
Requires:       python3-hypothesis = %{version}-%{release}
Requires:       python3dist(lark) >= 0.10.1
Provides:       python3dist(hypothesis[lark]) = %{version}-%{release}

%description -n python3-hypothesis+lark
Metapackage for python3-hypothesis lark extras.

%package -n       python3-hypothesis+numpy
Summary:        Metapackage for python3-hypothesis numpy extras
Requires:       python3-hypothesis = %{version}-%{release}
Requires:       python3dist(numpy) >= 1.21.6
Provides:       python3dist(hypothesis[numpy]) = %{version}-%{release}

%description -n python3-hypothesis+numpy
Metapackage for python3-hypothesis numpy extras.

%package -n       python3-hypothesis+pandas
Summary:        Metapackage for python3-hypothesis pandas extras
Requires:       python3-hypothesis = %{version}-%{release}
Requires:       python3dist(pandas) >= 1.1
Provides:       python3dist(hypothesis[pandas]) = %{version}-%{release}

%description -n python3-hypothesis+pandas
Metapackage for python3-hypothesis pandas extras.

%package -n       python3-hypothesis+pytest
Summary:        Metapackage for python3-hypothesis pytest extras
Requires:       python3-hypothesis = %{version}-%{release}
Requires:       python3dist(pytest) >= 4.6
Provides:       python3dist(hypothesis[pytest]) = %{version}-%{release}

%description -n python3-hypothesis+pytest
Metapackage for python3-hypothesis pytest extras.

%package -n       python3-hypothesis+dpcontracts
Summary:        Metapackage for python3-hypothesis dpcontracts extras
Requires:       python3-hypothesis = %{version}-%{release}
Requires:       python3dist(dpcontracts) >= 0.4
Provides:       python3dist(hypothesis[dpcontracts]) = %{version}-%{release}

%description -n python3-hypothesis+dpcontracts
Metapackage for python3-hypothesis dpcontracts extras.

%package -n       python3-hypothesis+redis
Summary:        Metapackage for python3-hypothesis redis extras
Requires:       python3-hypothesis = %{version}-%{release}
Requires:       python3dist(redis) >= 3.0.0
Provides:       python3dist(hypothesis[redis]) = %{version}-%{release}

%description -n python3-hypothesis+redis
Metapackage for python3-hypothesis redis extras.

%package -n       python3-hypothesis+crosshair
Summary:        Metapackage for python3-hypothesis crosshair extras
Requires:       python3-hypothesis = %{version}-%{release}
Requires:       python3dist(hypothesis-crosshair) >= 0.0.30
Requires:       python3dist(crosshair-tool) >= 0.0.110
Provides:       python3dist(hypothesis[crosshair]) = %{version}-%{release}

%description -n python3-hypothesis+crosshair
Metapackage for python3-hypothesis crosshair extras.

%package -n       python3-hypothesis+zoneinfo
Summary:        Metapackage for python3-hypothesis zoneinfo extras
Requires:       python3-hypothesis = %{version}-%{release}
Requires:       python3dist(tzdata) >= 2026.4
Provides:       python3dist(hypothesis[zoneinfo]) = %{version}-%{release}

%description -n python3-hypothesis+zoneinfo
Metapackage for python3-hypothesis zoneinfo extras.

%package -n       python3-hypothesis+django
Summary:        Metapackage for python3-hypothesis django extras
Requires:       python3-hypothesis = %{version}-%{release}
Requires:       python3dist(django) >= 5.2
Provides:       python3dist(hypothesis[django]) = %{version}-%{release}

%description -n python3-hypothesis+django
Metapackage for python3-hypothesis django extras.

%package -n       python3-hypothesis+watchdog
Summary:        Metapackage for python3-hypothesis watchdog extras
Requires:       python3-hypothesis = %{version}-%{release}
Requires:       python3dist(watchdog) >= 4.0.0
Provides:       python3dist(hypothesis[watchdog]) = %{version}-%{release}

%description -n python3-hypothesis+watchdog
Metapackage for python3-hypothesis watchdog extras.

%package -n       python3-hypothesis+all
Summary:        Metapackage for python3-hypothesis all extras
Requires:       python3-hypothesis = %{version}-%{release}
Requires:       python3dist(black) >= 20.8b0
Requires:       python3dist(click) >= 7.0
Requires:       python3dist(crosshair-tool) >= 0.0.110
Requires:       python3dist(django) >= 5.2
Requires:       python3dist(dpcontracts) >= 0.4
Requires:       python3dist(hypothesis-crosshair) >= 0.0.30
Requires:       python3dist(lark) >= 0.10.1
Requires:       python3dist(libcst) >= 0.3.16
Requires:       python3dist(numpy) >= 1.21.6
Requires:       python3dist(pandas) >= 1.1
Requires:       python3dist(pytest) >= 4.6
Requires:       python3dist(python-dateutil) >= 1.4
Requires:       python3dist(pytz) >= 2014.1
Requires:       python3dist(redis) >= 3.0.0
Requires:       python3dist(rich) >= 9.0.0
Requires:       python3dist(tzdata) >= 2026.4
Requires:       python3dist(watchdog) >= 4.0.0
Provides:       python3dist(hypothesis[all]) = %{version}-%{release}

%description -n python3-hypothesis+all
Metapackage for python3-hypothesis all extras.

%description

%package -n     python3-hypothesis
Summary:        The property-based testing library for Python
# oreon:reqs
Requires:       python3dist(exceptiongroup) >= 1.0.0
Requires:       python3dist(sortedcontainers) < 3.0.0
Requires:       python3dist(sortedcontainers) >= 2.1.0
# /oreon:reqs
%description -n python3-hypothesis

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep

%autosetup -p1 -n hypothesis-%{version}
cd rust
cargo vendor --versioned-dirs
mkdir -p .cargo
cat > .cargo/config.toml << 'EOF'
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF
cd ..

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-hypothesis usr/lib/python3*/site-packages/hypothesis* usr/lib64/python3*/site-packages/hypothesis* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/hypothesis* usr/lib64/python3*/site-packages/hypothesis* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-hypothesis -f %{oreon_filedir}/python3-hypothesis.list

%changelog

%autochangelog
