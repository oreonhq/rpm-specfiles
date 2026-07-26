%global source0_hash 3f0eb87d5ff2061d07663c4b010b8e7d66c274344712b01d561a0a73447ef41d

Name:           python-playsound3
Version:        3.3.1
Release:        %autorelease
Summary:        Cross-platform library to play audio files

License:        MIT
URL:            https://github.com/sjmikler/playsound3
Source:         %{pypi_source playsound3}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Cross platform library to play sound files in Python.}

%description %_description

%package -n     python3-playsound3
Summary:        %{summary}
Recommends:     gstreamer1-plugins-base-tools

%description -n python3-playsound3 %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n playsound3-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l playsound3

%check
%pyproject_check_import
#tests play sounds and don't work reliably in an rpm build.

%files -n python3-playsound3 -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
