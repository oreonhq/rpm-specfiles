%global source0_hash 7e9b232fcb6fa86582bd29870e8aa8cd27d350d684d6132b402bf2476490f981

Name:           python-sounddevice
Version:        0.5.3
Release:        %autorelease
Summary:        Play and record sound with Python

License:        MIT
URL:            https://github.com/spatialaudio/python-sounddevice
Source:         %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  portaudio

%global _description %{expand:
Play and record sound with Python.}

%description %_description

%package -n python3-sounddevice
Summary:        %{summary}

%description -n python3-sounddevice %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l sounddevice _sounddevice

%check
%pyproject_check_import

%files -n python3-sounddevice -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
