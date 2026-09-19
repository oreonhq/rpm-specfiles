%global source0_hash 91efa50e4990649da97408a384782d6ccf58342fc59cdfe21ed7a42911569975

Name:           python-pigpio
Version:        1.78
Release:        %autorelease
Summary:        Raspberry Pi GPIO module

License:        Unlicense
URL:            http://abyz.co.uk/rpi/pigpio/python.html
Source0:        %{pypi_source pigpio}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
Raspberry Pi Python module to access the pigpio daemon.

%package -n     python3-pigpio
Summary:        %{summary}

%description -n python3-pigpio
Raspberry Pi Python module to access the pigpio daemon.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pigpio-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pigpio

%check
%pyproject_check_import

%files -n python3-pigpio -f %{pyproject_files}

%changelog
%autochangelog
