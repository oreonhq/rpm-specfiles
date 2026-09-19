%global source0_hash da2def484310e28162c66a2fc6b5e8131e944c3fa158a6ab554f0a469464c089

%global pypi_name pyCEC
%global mod_name pycec

Name:           python-%{mod_name}
Version:        0.6.0
Release:        %autorelease
Summary:        Provide HDMI CEC devices as objects

License:        MIT
URL:            https://github.com/konikvranik/pycec/
Source0:        %{url}/archive/v%{version}/%{mod_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  libcec-devel
BuildRequires:	python3-devel
BuildRequires:	python3-pytest

%description
TCP <=> HDMI bridge to control HDMI devices over TCP network.

%package -n     python3-%{mod_name}
Summary:        %{summary}
Requires:	python3-libcec

%description -n python3-%{mod_name}
TCP <=> HDMI bridge to control HDMI devices over TCP network.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

# python asyncio fix
sed -i 's/asyncio.get_event_loop/asyncio.new_event_loop/' tests/test_hdmi_network.py

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{mod_name}

%check
%pytest -v

%files -n python3-%{mod_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_bindir}/pycec

%changelog
%autochangelog
