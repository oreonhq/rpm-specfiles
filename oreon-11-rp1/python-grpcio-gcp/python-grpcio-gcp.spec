%global source0_hash 44de25348f489920efb3b1a05134816cfbc3e880fa92e3a7b4dfcb7e772ac625

%global srcname grpcio-gcp
%global _description %{summary}.

Name:           python-%{srcname}
Version:        0.2.2
Release:        23%{?dist}
Summary:        gRPC for GCP extensions

License:        Apache-2.0
URL:            https://github.com/GoogleCloudPlatform/grpc-gcp-python/
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildArch:      noarch

%description
%{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n grpc-gcp-python-%{version}

# Remove bundled egg-info
rm -rf *.egg-info

%generate_buildrequires
cd src
ln -sf ../template/version.py .
%pyproject_buildrequires

%build
cd src
%pyproject_wheel

%install
cd src
%pyproject_install

%files -n python3-%{srcname}
%doc src/{CHANGELOG.rst,README.md}
%license src/LICENSE
%{python3_sitelib}/grpc_gcp/
%{python3_sitelib}/grpcio_gcp-%{version}.dist-info/

%changelog
%autochangelog
