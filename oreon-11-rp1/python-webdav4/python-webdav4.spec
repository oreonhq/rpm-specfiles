%global source0_hash 7062c6640e0520bfbd49862bdd335db839e519bf2ca02cd4f89957069ed600ea
Name:           python-webdav4
Version:        0.11.0
Release:        1%{?dist}
Summary:        WebDAV client library with an fsspec-based filesystem and a CLI
License:        MIT
URL:            https://github.com/skshetry/webdav4
Source0:        https://files.pythonhosted.org/packages/source/w/webdav4/webdav4-%{version}.tar.gz
Source10:       dav.1
Source11:       dav-cat.1
Source12:       dav-cp.1
Source13:       dav-du.1
Source14:       dav-ls.1
Source15:       dav-mkdir.1
Source16:       dav-mv.1
Source17:       dav-rm.1
Source18:       dav-run.1
Source19:       dav-sync.1
BuildArch:      noarch
%global common_description %{expand:
Webdav API with an (optional) fsspec implementation and a CLI.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-webdav4 = %{version}-%{release}
# /oreon:deps
%package -n       python3-webdav4+all
Summary:        Metapackage for python3-webdav4 all extras
Requires:       python3-webdav4 = %{version}-%{release}
Provides:       python3dist(webdav4[all]) = %{version}-%{release}

%description -n python3-webdav4+all
Metapackage for python3-webdav4 all extras.

%package -n       python3-webdav4+dev
Summary:        Metapackage for python3-webdav4 dev extras
Requires:       python3-webdav4 = %{version}-%{release}
Provides:       python3dist(webdav4[dev]) = %{version}-%{release}

%description -n python3-webdav4+dev
Metapackage for python3-webdav4 dev extras.

%package -n       python3-webdav4+docs
Summary:        Metapackage for python3-webdav4 docs extras
Requires:       python3-webdav4 = %{version}-%{release}
Requires:       python3dist(furo) == 2024.8.6
Requires:       python3dist(furo) == 2025.12.19
Requires:       python3dist(myst-parser) >= 3
Requires:       python3dist(myst-parser) < 6
Requires:       python3dist(sphinx) >= 7
Requires:       python3dist(sphinx) < 10
Requires:       python3dist(sphinx-copybutton) == 0.5.2
Provides:       python3dist(webdav4[docs]) = %{version}-%{release}

%description -n python3-webdav4+docs
Metapackage for python3-webdav4 docs extras.

%package -n       python3-webdav4+fsspec
Summary:        Metapackage for python3-webdav4 fsspec extras
Requires:       python3-webdav4 = %{version}-%{release}
Requires:       python3dist(fsspec) >= 2021.7
Provides:       python3dist(webdav4[fsspec]) = %{version}-%{release}

%description -n python3-webdav4+fsspec
Metapackage for python3-webdav4 fsspec extras.

%package -n       python3-webdav4+http2
Summary:        Metapackage for python3-webdav4 http2 extras
Requires:       python3-webdav4 = %{version}-%{release}
Requires:       python3dist(httpx[http2]) < 1
Requires:       python3dist(httpx[http2]) >= 0.20
Provides:       python3dist(webdav4[http2]) = %{version}-%{release}

%description -n python3-webdav4+http2
Metapackage for python3-webdav4 http2 extras.

%package -n       python3-webdav4+qa
Summary:        Metapackage for python3-webdav4 qa extras
Requires:       python3-webdav4 = %{version}-%{release}
Requires:       python3dist(mypy) == 1.14
Requires:       python3dist(mypy) == 1.19.1
Provides:       python3dist(webdav4[qa]) = %{version}-%{release}

%description -n python3-webdav4+qa
Metapackage for python3-webdav4 qa extras.

%package -n       python3-webdav4+tests
Summary:        Metapackage for python3-webdav4 tests extras
Requires:       python3-webdav4 = %{version}-%{release}
Provides:       python3dist(webdav4[tests]) = %{version}-%{release}

%description -n python3-webdav4+tests
Metapackage for python3-webdav4 tests extras.

%description %{common_description}

%package -n python3-webdav4
Summary:        WebDAV client library with an fsspec-based filesystem and a CLI
Recommends:     %{py3_dist colorama}
# oreon:reqs
Requires:       python3dist(httpx) < 1
Requires:       python3dist(httpx) >= 0.20
Requires:       python3dist(python-dateutil) >= 2.8.1
# /oreon:reqs
%description -n python3-webdav4 %{common_description}

%prep

%autosetup -p1
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
tomcli set pyproject.toml lists delitem \
    project.optional-dependencies.tests 'pytest-cov*'
tomcli set pyproject.toml str tool.pytest.ini_options.addopts -- "$(
  tomcli get pyproject.toml tool.pytest.ini_options.addopts |
  sed -r 's/--cov[^[:blank:]]*//g')"

%install
%pyproject_install
install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 -D \
    '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}' '%{SOURCE13}' '%{SOURCE14}' \
    '%{SOURCE15}' '%{SOURCE16}' '%{SOURCE17}' '%{SOURCE18}' '%{SOURCE19}'
%oreon_autofiles python3-webdav4 usr/lib/python3*/site-packages/webdav4* usr/lib64/python3*/site-packages/webdav4* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/webdav4* usr/lib64/python3*/site-packages/webdav4* usr/bin/*

%build

%pyproject_wheel
%check

%pytest ${ignore-} -rs -vv
%files
%files -n python3-webdav4 -f %{oreon_filedir}/python3-webdav4.list

%changelog

%autochangelog
