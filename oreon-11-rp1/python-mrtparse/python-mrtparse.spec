%global source0_hash 8806e20f57dfbbcdc107a9838af9d5386dacdc6d43474bfedeeacd80eb3945d4

%global pypi_name mrtparse
%global srcname mrtparse

Name:           python-%{pypi_name}
Version:        2.2.0
Release:        6%{?dist}
Summary:        MRT format data parser

License:        Apache-2.0
URL:            https://github.com/t2mune/mrtparse/
Source0:        %{pypi_source %{srcname}}
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
mrtparse is a module to read and analyze the MRT format data.
The MRT format can be used to export routing protocol messages, state changes,
and routing information base contents, and is defined in RFC6396.
Programs like FRRouting, Quagga, Zebra, BIRD, OpenBGPD and PyRT can dump the
MRT format data.
You can also download archives from the Route Views Projects, RIPE NCC.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%pyproject_check_import
# Test the example scripts
for bgp in samples/*_bgp; do
    PYTHONPATH=. %{__python3} examples/mrt2bgpdump.py $bgp > /dev/null
done
for rib in samples/*_rib*; do
    PYTHONPATH=. %{__python3} examples/mrt2exabgp.py $rib > /dev/null
done
for file in samples/*_bgp samples/*_rib*; do
    PYTHONPATH=. %{__python3} examples/mrt2json.py $file > /dev/null
done

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst examples samples

%changelog
%autochangelog
