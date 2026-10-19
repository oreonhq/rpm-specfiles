%global source8_hash 125e84db872eeba443d270c70315c256b0af43a502fcfe51f50621166ad035d7
%global source7_hash 2f48a5a434613cafff0639fc636b95360ba19b4bfdacdca5d2e3a6089db0a327
%global source6_hash ced02f86e612c0b16f0cb671e0c2729717586f13f01db51ada6be8d84b757b46
%global source5_hash 972355bd24e82cea62911e0f3081f58e83c49ffde686fe3a3b156e05e70d142f
%global source4_hash 194ae6ac0b964417c7af69acedb5b3361ac79ccd42e376a4bac74599f91e9be9
%global source3_hash 892a718c58cb33ce4a716ac06bd6d80c2c4c184c795159feb68213a57acb7840
%global source2_hash 1f9b5ee2fcdc39a726003084cdda9f10c7c54c47e01a4ad2ffa57502dec79b82
%global source1_hash 8eaf3e816a21bad7dc177eb881a1a3a2f61b276b2dd4ecc25d1c192dfab294cd
%global source0_hash e12df70fc51003f7d19e93220ff9ab919033056e658a38d1520532ece7af6fda
%global source9_hash 147081ba047c919782896b26852f812e65880a9e52f69070069f950eea90c396
%bcond bootstrap 0
%bcond extras  %[%{without bootstrap} && !0%{?rhel}]
%if 0%{?fedora} >= 44 || 0%{?oreon} >= 11
%bcond doctest 0
%else
%bcond doctest  %[%{with extras} && "%(uname -m)" != "i686"]
%endif
%global giturl  https://github.com/networkx/networkx
Name:           python-networkx
Version:        3.6.1
Release:        1%{?dist}
Summary:        Creates and Manipulates Graphs and Networks
License:        BSD-3-Clause
URL:            https://networkx.org/
VCS:            git:%{giturl}.git
Source0:        https://github.com/networkx/networkx/archive/networkx-3.6.1.tar.gz#/python-networkx-3.6.1.tar.gz
Source1:        https://numpy.org/neps/objects.inv#/objects-neps.inv
Source2:        https://matplotlib.org/stable/objects.inv#/objects-matplotlib.inv
Source3:        https://docs.scipy.org/doc/scipy/objects.inv#/objects-scipy.inv
Source4:        https://pandas.pydata.org/pandas-docs/stable/objects.inv#/objects-pandas.inv
Source5:        https://geopandas.org/en/stable/objects.inv#/objects-geopandas.inv
Source6:        https://sphinx-gallery.github.io/stable/objects.inv#/objects-sphinx-gallery.inv
Source7:        https://networkx.org/nx-guides/objects.inv#/objects-nx-guides.inv
Source8:        https://snap.stanford.edu/data/facebook_combined.txt.gz
Source9:        https://www-personal.umich.edu/~mejn/netdata/football.zip
BuildArch:      noarch
%if %{with doctest}
%endif
%if %{with doctest}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-networkx = %{version}-%{release}
# /oreon:deps
%package -n       python3-networkx+benchmarking
Summary:        Metapackage for python3-networkx benchmarking extras
Requires:       python3-networkx = %{version}-%{release}
Provides:       python3dist(networkx[benchmarking]) = %{version}-%{release}

%description -n python3-networkx+benchmarking
Metapackage for python3-networkx benchmarking extras.

%package -n       python3-networkx+default
Summary:        Metapackage for python3-networkx default extras
Requires:       python3-networkx = %{version}-%{release}
Requires:       python3dist(numpy) >= 1.25
Requires:       python3dist(scipy) >= 1.11.2
Requires:       python3dist(matplotlib) >= 3.8
Requires:       python3dist(pandas) >= 2.0
Provides:       python3dist(networkx[default]) = %{version}-%{release}

%description -n python3-networkx+default
Metapackage for python3-networkx default extras.

%package -n       python3-networkx+developer
Summary:        Metapackage for python3-networkx developer extras
Requires:       python3-networkx = %{version}-%{release}
Requires:       python3dist(pre-commit) >= 4.1
Requires:       python3dist(mypy) >= 1.15
Provides:       python3dist(networkx[developer]) = %{version}-%{release}

%description -n python3-networkx+developer
Metapackage for python3-networkx developer extras.

%package -n       python3-networkx+doc
Summary:        Metapackage for python3-networkx doc extras
Requires:       python3-networkx = %{version}-%{release}
Requires:       python3dist(sphinx) >= 8.0
Requires:       python3dist(pydata-sphinx-theme) >= 0.16
Requires:       python3dist(sphinx-gallery) >= 0.18
Requires:       python3dist(numpydoc) >= 1.8.0
Requires:       python3dist(pillow) >= 10
Requires:       python3dist(texext) >= 0.6.7
Requires:       python3dist(myst-nb) >= 1.1
Provides:       python3dist(networkx[doc]) = %{version}-%{release}

%description -n python3-networkx+doc
Metapackage for python3-networkx doc extras.

%package -n       python3-networkx+example
Summary:        Metapackage for python3-networkx example extras
Requires:       python3-networkx = %{version}-%{release}
Requires:       python3dist(osmnx) >= 2.0.0
Requires:       python3dist(momepy) >= 0.7.2
Requires:       python3dist(contextily) >= 1.6
Requires:       python3dist(seaborn) >= 0.13
Requires:       python3dist(cairocffi) >= 1.7
Requires:       python3dist(igraph) >= 0.11
Requires:       python3dist(scikit-learn) >= 1.5
Requires:       python3dist(iplotx) >= 0.9.0
Provides:       python3dist(networkx[example]) = %{version}-%{release}

%description -n python3-networkx+example
Metapackage for python3-networkx example extras.

%package -n       python3-networkx+extra
Summary:        Metapackage for python3-networkx extra extras
Requires:       python3-networkx = %{version}-%{release}
Requires:       python3dist(lxml) >= 4.6
Requires:       python3dist(pygraphviz) >= 1.14
Requires:       python3dist(pydot) >= 3.0.1
Requires:       python3dist(sympy) >= 1.10
Provides:       python3dist(networkx[extra]) = %{version}-%{release}

%description -n python3-networkx+extra
Metapackage for python3-networkx extra extras.

%package -n       python3-networkx+release
Summary:        Metapackage for python3-networkx release extras
Requires:       python3-networkx = %{version}-%{release}
Requires:       python3dist(build) >= 0.10
Requires:       python3dist(twine) >= 4.0
Requires:       python3dist(wheel) >= 0.40
Requires:       python3dist(changelist) == 0.5
Provides:       python3dist(networkx[release]) = %{version}-%{release}

%description -n python3-networkx+release
Metapackage for python3-networkx release extras.

%package -n       python3-networkx+test
Summary:        Metapackage for python3-networkx test extras
Requires:       python3-networkx = %{version}-%{release}
Requires:       python3dist(pytest) >= 7.2
Requires:       python3dist(pytest-cov) >= 4.0
Requires:       python3dist(pytest-xdist) >= 3.0
Provides:       python3dist(networkx[test]) = %{version}-%{release}

%description -n python3-networkx+test
Metapackage for python3-networkx test extras.

%package -n       python3-networkx+test-extras
Summary:        Metapackage for python3-networkx test-extras extras
Requires:       python3-networkx = %{version}-%{release}
Provides:       python3dist(networkx[test-extras]) = %{version}-%{release}

%description -n python3-networkx+test-extras
Metapackage for python3-networkx test-extras extras.

%description
NetworkX is a Python package for the creation, manipulation, and study of the
structure, dynamics, and functions of complex networks.

%package -n python3-networkx
Summary:        Creates and Manipulates Graphs and Networks
Recommends:     xdg-utils
%description -n python3-networkx
NetworkX is a Python 3 package for the creation, manipulation, and study of
the structure, dynamics, and functions of complex networks.

%if %{with doctest}
%package doc
License:        BSD-3-Clause AND BSD-2-Clause AND MIT AND PSF-2.0
Summary:        Documentation for networkx
Requires:       fontawesome-fonts-all
Provides:       bundled(js-bootstrap)
%description doc
Documentation for networkx
%endif

%if %{with extras}
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source9_hash}" = "none" || { f="%{SOURCE9}"; test -f "$f" || { echo "oreon: missing Source9 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source9_hash}" || { echo "oreon: Source9 hash mismatch" >&2; exit 1; }; }
%autosetup -n networkx-networkx-%{version}

# Use local objects.inv for intersphinx
sed -e 's|\("https://numpy.org/neps/", \)None|\1"%{SOURCE1}"|' \
    -e 's|\("https://matplotlib.org/stable/", \)None|\1"%{SOURCE2}"|' \
    -e 's|\("https://docs.scipy.org/doc/scipy/", \)None|\1"%{SOURCE3}"|' \
    -e 's|\("https://pandas.pydata.org/pandas-docs/stable/", \)None|\1"%{SOURCE4}"|' \
    -e 's|\("https://geopandas.org/en/stable/", \)None|\1"%{SOURCE5}"|' \
    -e 's|\("https://sphinx-gallery.github.io/stable/", \)None|\1"%{SOURCE6}"|' \
    -e 's|\("https://networkx.org/nx-guides/", \)None|\1"%{SOURCE7}"|' \
    -i doc/conf.py

# Do not try to download the SNAP database from the web during the build
sed -i 's,https:.*\.gz,%{SOURCE8},' examples/3d_drawing/plot_facebook_3d.py

# Do not try to download the football database from the web during the build
sed -i 's,http:.*\.zip,file://%{SOURCE9},' examples/graph/plot_football.py

# Point to the local switcher instead of the inaccessible one on the web
sed -i 's,https://networkx.org/documentation/latest/,,' doc/conf.py

# Use a free font instead of a proprietary font
sed -i 's/Helvetica/sans-serif/' examples/drawing/plot_chess_masters.py

# Do not run code coverage tools
sed -i '/pytest-cov/d' pyproject.toml requirements/test.txt
sed -i '/intersphinx-registry/d' pyproject.toml requirements/doc.txt

%build

%pyproject_wheel
%if %{with doctest}
PYTHONPATH=$PWD/build/lib make -C doc html
rst2html --no-datestamp README.rst README.html
%endif
%install
%pyproject_install
%if %{with doctest}
for fil in $(find doc/build -name \*.zip); do
  mkdir zip
  cd zip
  unzip ../$fil
  zip -9r ../$fil .
  cd ..
  rm -fr zip
done
%oreon_autofiles python3-networkx usr/lib/python3*/site-packages/networkx* usr/lib64/python3*/site-packages/networkx* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/networkx* usr/lib64/python3*/site-packages/networkx* usr/bin/*
%endif
%check

export FLEXIBLAS=NETLIB
%if %{with doctest}
%pytest -v
%else
%pyproject_check_import -e '*.tests.*' -e '*.conftest'
%endif
%files
%files -n python3-networkx -f %{oreon_filedir}/python3-networkx.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.6.1-1
- Prepare for Oreon 11 (RP1)
