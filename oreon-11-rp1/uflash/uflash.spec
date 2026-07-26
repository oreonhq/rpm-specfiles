%global source0_hash f583d2264fcf37e3e358f1f3a4370ce43b24eb3fdf845a477202555235b52582

Name:           uflash
Version:        2.0.0
Release:        %autorelease
Summary:        A module and utility to flash Python onto the BBC micro:bit
License:        MIT
URL:            https://github.com/ntoll/uflash
Source0:        %{pypi_source uflash}

# For tests, they don't have tags
%define hash    147ea945fbe841b0ae17888ab60a60c6080b1225
Source1:        https://github.com/ntoll/uflash/archive/%{hash}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

BuildArch:      noarch

# Other tools are using this as a module, so provide also the python3- name
%py_provides    python3-%{name}

%description
A utility for flashing the BBC micro:bit with Python scripts and the
MicroPython runtime. You pronounce the name of this utility "micro-flash". ;-)
It provides two services. A library of functions to programatically create a
hex file and flash it onto a BBC micro:bit.  A command line utility called
uflash that will flash Python scripts onto a BBC micro:bit.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
tar -xf %{SOURCE1}
mv %{name}-%{hash}/tests .
rm -rf %{name}-%{hash}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l 'uflash*'

%check
%pyproject_check_import
%pytest

%files -f %{pyproject_files}
%doc README.rst CHANGES.rst
%{_bindir}/uflash
%{_bindir}/py2hex

%changelog
%autochangelog
