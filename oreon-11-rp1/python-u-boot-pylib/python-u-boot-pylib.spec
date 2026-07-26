%global source0_hash 9b06f0df7f4ee75a8d39bbba327e05bcb01123b63acd291d2f1782c78f6d35dd

Name:           python-u-boot-pylib
Version:        0.0.6
Release:        %autorelease
Summary:        U-Boot Python library

License:        GPL-2.0-or-later
URL:            https://docs.u-boot.org
Source:         %{pypi_source u_boot_pylib}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This is a Python library used by various U-Boot tools, including patman,
buildman and binman.}

%description %_description

%package -n     python3-u-boot-pylib
Summary:        %{summary}

%description -n python3-u-boot-pylib %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n u_boot_pylib-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files u_boot_pylib

%check
%pyproject_check_import

%files -n python3-u-boot-pylib -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
